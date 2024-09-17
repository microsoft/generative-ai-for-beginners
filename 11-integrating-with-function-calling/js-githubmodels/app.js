import ModelClient from "@azure-rest/ai-inference";
import { AzureKeyCredential } from "@azure/core-auth";

const token = process.env["GITHUB_TOKEN"];
const endpoint = "https://models.inference.ai.azure.com";

/* By using the Azure AI Inference SDK, you can easily experiment with different models
   by modifying the value of `modelName` in the code below. For this code sample
   you need a model supporting tools. The following compatible models are
   available in the GitHub Models service:

   Cohere: Cohere-command-r, Cohere-command-r-plus
   Mistral AI: Mistral-large, Mistral-large-2407, Mistral-Nemo, Mistral-small
   Azure OpenAI: gpt-4o-mini, gpt-4o */
const modelName = "gpt-4o";

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

    const tool = {
        "type": "function",
        "function": {
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
            
        }
    };

    const hotels ={
    "type": "function",
        "function": {
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
        }

    }

    const client = new ModelClient(endpoint, new AzureKeyCredential(token));

    let messages = [
        { role: "system", content: "You an assistant that helps users find flight and hotel information." },
        { role: "user", content: "I'm interested in going to Miami and staying in a hotel." },
        // { role: "user", content: "I'm interested in going to Seattle. Are there flights to Denver?" },




    ];

    let response = await client.path("/chat/completions").post({
        body: {
            messages: messages,
            tools: [tool, hotels],
            model: modelName
        }
    });
    if (response.status !== "200") {
        throw response.body.error;
    }

    // We expect the model to ask for a tool call
    if (response.body.choices[0].finish_reason === "tool_calls") {

        // Append the model response to the chat history
        messages.push(response.body.choices[0].message);

        // We expect a single tool call
        if (response.body.choices[0].message && response.body.choices[0].message.tool_calls.length === 1) {

            const toolCall = response.body.choices[0].message.tool_calls[0];
            // We expect the tool to be a function call
            if (toolCall.type === "function") {
                const toolCall = response.body.choices[0].message.tool_calls[0];
                // Parse the function call arguments and call the function
                const functionArgs = JSON.parse(toolCall.function.arguments);
                console.log(`Calling function \`${toolCall.function.name}\` with arguments ${toolCall.function.arguments}`);
                const callableFunc = namesToFunctions[toolCall.function.name];
                const functionReturn = callableFunc(functionArgs);
                console.log(`Function returned = ${functionReturn}`);

                // Append the function call result fo the chat history
                messages.push(
                    {
                        "tool_call_id": toolCall.id,
                        "role": "tool",
                        "name": toolCall.function.name,
                        "content": functionReturn,
                    }
                )

                response = await client.path("/chat/completions").post({
                    body: {
                        messages: messages,
                        tools: [tool, hotels],
                        model: modelName
                    }
                });
                if (response.status !== "200") {
                    throw response.body.error;
                }
                console.log(`Model response = ${response.body.choices[0].message.content}`);
            }
        }
    }
}

main().catch((err) => {
    console.error("The sample encountered an error:", err);
});