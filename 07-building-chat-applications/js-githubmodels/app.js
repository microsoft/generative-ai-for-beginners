import OpenAI from "openai";

// SECURITY: Validate required environment variables
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
   by modifying the value of `modelName` in the code below. The following models are
   available in the Microsoft Foundry Models catalog:

   OpenAI: gpt-5, gpt-5-mini
   Meta: Llama-3.3-70B-Instruct, Llama-4-Scout-17B-16E-Instruct
   Mistral AI: mistral-medium-3-5, mistral-small-4-119b-2603, Codestral-2501, ministral-ministral-4b-instruct
   Microsoft: Phi-4, Phi-4-mini-instruct, Phi-4-multimodal-instruct, Phi-4-reasoning

   This sample uses the Responses API, which is the recommended API for OpenAI models.
   For the other models, call `client.chat.completions.create({ model, messages })`
   instead and read `response.choices[0].message.content`. */
const modelName = "gpt-5-mini";

export async function main() {

    // The OpenAI client points at the Microsoft Foundry OpenAI-compatible /openai/v1/ endpoint.
    const client = new OpenAI({
        apiKey: token,
        baseURL: `${endpoint.replace(/\/$/, "")}/openai/v1/`,
    });

    // The SDK throws on non-2xx responses, so no manual status check is needed.
    const response = await client.responses.create({
        input: [
            { role: "system", content: "You're the president of France"},
            { role: "system", content: "You have just resigned" },
            { role: "user", content: "What tasks needs doing?"  },
        ],
        model: modelName,
        store: false,
    });

    console.log(response.output_text);
}

main().catch((err) => {
    console.error("The sample encountered an error:", err);
});
