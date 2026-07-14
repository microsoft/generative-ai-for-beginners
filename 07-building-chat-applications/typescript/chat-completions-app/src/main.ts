import OpenAI from "openai";
import * as dotenv from "dotenv";

dotenv.config();

const endpoint = process.env.AZURE_OPENAI_ENDPOINT || '';
const azureApiKey = process.env.AZURE_OPENAI_API_KEY || '';

// The Responses API is served from the Azure OpenAI (Microsoft Foundry) v1 endpoint,
// so we point the OpenAI client at <your-endpoint>/openai/v1/.
const client = new OpenAI({
    apiKey: azureApiKey,
    baseURL: `${endpoint.replace(/\/$/, '')}/openai/v1/`,
});

export async function main() {
    try {
        console.log("== Chat Completions App ==");

        // Use the deployment name configured in your .env file
        const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT || 'gpt-5-mini';

        const result = await client.responses.create({
            model: deploymentName,
            input: [
                { role: "system", content: "You're the president of France" },
                { role: "system", content: "You have just resigned" },
                { role: "user", content: "What tasks needs doing?" }
            ],
            max_output_tokens: 100,
            store: false,
        });

        console.log(result.output_text);
    } catch (error) {
        console.log("The sample encountered an error: ", error);
    }
}

main();