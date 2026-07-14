import ModelClient from "@azure-rest/ai-inference";
import { AzureKeyCredential } from "@azure/core-auth";

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

/* By using the Azure AI Inference SDK, you can easily experiment with different models
   by modifying the value of `modelName` in the code below. The following models are
   available in the Microsoft Foundry Models catalog:

   Cohere: Cohere-command-r-08-2024, Cohere-command-r-plus-08-2024
   Meta: Meta-Llama-3.1-405B-Instruct, Meta-Llama-3.1-70B-Instruct, Meta-Llama-3.1-8B-Instruct, Llama-3.2-11B-Vision-Instruct, Llama-3.2-90B-Vision-Instruct
   Mistral AI: Mistral-large-2411, Mistral-small-2503, Codestral-2501, Ministral-3B
   OpenAI: gpt-5-mini, gpt-4o-mini, gpt-4o, gpt-4.1, gpt-4.1-mini
   Microsoft: Phi-4, Phi-4-mini-instruct, Phi-4-multimodal-instruct, Phi-4-reasoning */
const modelName = "gpt-5-mini";

export async function main() {

    const client = new ModelClient(endpoint, new AzureKeyCredential(token));

    const response = await client.path("/chat/completions").post({
        body: {
            messages: [
                { role: "system", content: "You're the president of France"},
                { role: "system", content: "You have just resigned" },
                { role: "user", content: "What tasks needs doing?"  },
            ],
            model: modelName,
        }
    });

    if (response.status !== "200") {
        throw response.body.error;
    }

    for (const choice of response.body.choices) {
        console.log(choice.message.content);
    }
}

main().catch((err) => {
    console.error("The sample encountered an error:", err);
});
