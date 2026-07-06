import { AzureOpenAI } from "openai";
import * as dotenv from "dotenv";

dotenv.config();

const endpoint = process.env.AZURE_OPENAI_ENDPOINT || '';
const apiKey = process.env.AZURE_OPENAI_API_KEY || '';
// gpt-image-1 is the current generation Azure OpenAI image model (DALL-E 3 is legacy)
const deployment = process.env.AZURE_OPENAI_DEPLOYMENT || 'gpt-image-1';
const apiVersion = "2024-10-21";

const promptImage = "captain with a parrot on his shoulder";

export async function main() {
  try {
    console.log("== Image Generation App ==");

    const client = new AzureOpenAI({ endpoint, apiKey, deployment, apiVersion });

    const imageGenerations = await client.images.generate({
      model: deployment,
      prompt: promptImage,
      n: 1,
      size: "1024x1024",
    });

    for (const image of imageGenerations.data) {
      console.log(`Image generated URL...: ${image.url}`);
    }
  } catch (error) {
    console.log("The sample encountered an error: ", error);
  }
}

main();