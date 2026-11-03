import OpenAI from "openai";

// Get these from your Microsoft Foundry project's "Overview" page
// (GitHub Models is retiring end of July 2026 - see https://ai.azure.com/catalog/models)
const token = process.env["AZURE_INFERENCE_CREDENTIAL"];
if (!token) {
    throw new Error("AZURE_INFERENCE_CREDENTIAL environment variable is required. Please set it before running this application.");
}
const endpoint = process.env["AZURE_INFERENCE_ENDPOINT"];
if (!endpoint) {
    throw new Error("AZURE_INFERENCE_ENDPOINT environment variable is required. Please set it before running this application.");
}

/* Because Microsoft Foundry serves many models through the same OpenAI-compatible
   /openai/v1/ endpoint, you can easily experiment with different models
   by modifying the value of `modelName` in the code below. For this code sample
   you need a model supporting tools. The following compatible models are
   available in the Microsoft Foundry Models catalog:

   OpenAI: gpt-5, gpt-5-mini
   Mistral AI: Mistral-Large-3, mistral-small-2503 (see lesson 20)

   This sample uses the Responses API, which is the recommended API for OpenAI models.
   For non-OpenAI models, use `client.chat.completions.create(...)` with
   `{ type: "function", function: { name, description, parameters } }` tools instead. */
const modelName = "gpt-5-mini";

function getFlightInfo({ originCity, destinationCity }) {
    if (originCity === "Seattle" && destinationCity === "Miami") {
        return JSON.stringify({
            airline: "Delta",
            flight_number: "DL123",
            flight_date: "May 7th, 2024",
            flight_time: "10:00AM"
        });
    }
    return JSON.stringify({ error: "No flights found between the cities" });
}

function getHotelInfo({ destination }) {
    if ( destination === "Miami") {
        return JSON.stringify({
            hotelName: "Contoso Suites"
        });
    }
    return JSON.stringify({ error: "No available hotels found in this city" });
}

const namesToFunctions = {
    getFlightInfo: (data) =>
        getFlightInfo(data),
    getHotelInfo: (data) =>
        getHotelInfo(data)
};

export async function main() {

    // Responses API tools use a flat schema: { type, name, description, parameters }
    const tool = {
        type: "function",
        name: "getFlightInfo",
        description: "Returns information about the next flight between two cities." +
            "This includes the name of the airline, flight number and the date and time" +
            "of the next flight",
        parameters: {
            "type": "object",
            "properties": {
                "originCity": {
                    "type": "string",
                    "description": "The name of the city where the flight originates",
                },
                "destinationCity": {
                    "type": "string",
                    "description": "The flight destination city",
                },
            },
            "required": [
                "originCity",
                "destinationCity"
            ],
        },
    };

    const hotels = {
        type: "function",
        name: "getHotelInfo",
        description: "Returns information about the hotel of the destination city.",
        parameters: {
            "type": "object",
            "properties": {
                "destination": {
                    "type": "string",
                    "description": "The city that the traveller would like to stay",
                },
            },
            "required": [
                "destination"
            ],
        },
    };

    // The OpenAI client points at the Microsoft Foundry OpenAI-compatible /openai/v1/ endpoint.
    const client = new OpenAI({
        apiKey: token,
        baseURL: `${endpoint.replace(/\/$/, "")}/openai/v1/`,
    });

    let input = [
        { role: "system", content: "You an assistant that helps users find flight and hotel information." },
        { role: "user", content: "I'm interested in going to Miami and staying in a hotel." },
        // { role: "user", content: "I'm interested in going to Seattle. Are there flights to Denver?" },
    ];

    // The SDK throws on non-2xx responses, so no manual status check is needed.
    let response = await client.responses.create({
        input: input,
        tools: [tool, hotels],
        model: modelName,
        store: false,
    });

    // We expect the model to ask for a tool call: look for `function_call` items in the output
    const toolCalls = response.output.filter((item) => item.type === "function_call");

    // We expect a single tool call
    if (toolCalls.length === 1) {

        const toolCall = toolCalls[0];

        // SECURITY: Validate function name exists in allowed functions map
        const functionName = toolCall.name;
        if (!Object.prototype.hasOwnProperty.call(namesToFunctions, functionName)) {
            throw new Error(`Unknown function requested: ${functionName}. Only allowed functions are: ${Object.keys(namesToFunctions).join(', ')}`);
        }

        // SECURITY: Safely parse JSON with error handling
        let functionArgs;
        try {
            functionArgs = JSON.parse(toolCall.arguments);
        } catch (parseError) {
            throw new Error(`Failed to parse function arguments: ${parseError.message}`);
        }

        // Log function call (avoid logging sensitive data in production)
        console.log(`Calling function \`${functionName}\` with arguments ${toolCall.arguments}`);

        const callableFunc = namesToFunctions[functionName];
        const functionReturn = callableFunc(functionArgs);
        console.log(`Function returned = ${functionReturn}`);

        // Append the model's function call, then the function result, to the conversation
        // (matched by call_id; we use store: false, so nothing is kept server-side)
        input.push(
            {
                "type": "function_call",
                "call_id": toolCall.call_id,
                "name": toolCall.name,
                "arguments": toolCall.arguments,
            }
        );
        input.push(
            {
                "type": "function_call_output",
                "call_id": toolCall.call_id,
                "output": functionReturn,
            }
        );

        response = await client.responses.create({
            input: input,
            tools: [tool, hotels],
            model: modelName,
            store: false,
        });
        console.log(`Model response = ${response.output_text}`);
    }
}

main().catch((err) => {
    console.error("The sample encountered an error:", err);
});
