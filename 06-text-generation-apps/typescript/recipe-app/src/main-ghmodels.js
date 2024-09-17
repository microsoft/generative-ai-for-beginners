import ModelClient from "@azure-rest/ai-inference";
import { AzureKeyCredential } from "@azure/core-auth";

const token = process.env["GITHUB_TOKEN"];
const endpoint = "https://models.inference.ai.azure.com";

/* By using the Azure AI Inference SDK, you can easily experiment with different models
   by modifying the value of `modelName` in the code below. The following models are
   available in the GitHub Models service:

   AI21 Labs: AI21-Jamba-Instruct
   Cohere: Cohere-command-r, Cohere-command-r-plus
   Meta: Meta-Llama-3-70B-Instruct, Meta-Llama-3-8B-Instruct, Meta-Llama-3.1-405B-Instruct, Meta-Llama-3.1-70B-Instruct, Meta-Llama-3.1-8B-Instruct
   Mistral AI: Mistral-large, Mistral-large-2407, Mistral-Nemo, Mistral-small
   Azure OpenAI: gpt-4o-mini, gpt-4o
   Microsoft: Phi-3-medium-128k-instruct, Phi-3-medium-4k-instruct, Phi-3-mini-128k-instruct, Phi-3-mini-4k-instruct, Phi-3-small-128k-instruct, Phi-3-small-8k-instruct */
const modelName = "gpt-4o-mini";

export async function main() {
  const client = new ModelClient(endpoint, new AzureKeyCredential(token));

  const response = await client.path("/chat/completions").post({
    body: {
      messages: [
        { role: "system", content: "You are a helpful assistant." },
        { role: "user", content: "What is the capital of France?" },
      ],
      model: modelName,
      // Optional parameters
      temperature: 1,
      max_tokens: 1000,
      top_p: 1,
    },
  });

  if (response.status !== "200") {
    throw response.body.error;
  }
  console.log(response.body.choices[0].message.content);
}

main().catch((err) => {
  console.error("The sample encountered an error:", err);
});
