import { AzureOpenAI } from "openai";
import * as dotenv from "dotenv";
import * as fs from "fs";

dotenv.config();

const endpoint = process.env.AZURE_OPENAI_ENDPOINT || '';
const apiKey = process.env.AZURE_OPENAI_API_KEY || '';
// gpt-image-2 is the latest Azure OpenAI image model (DALL-E is legacy)
const deployment = process.env.AZURE_OPENAI_DEPLOYMENT || 'gpt-image-2';
const apiVersion = "2025-04-01-preview";

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
      // gpt-image models return the image as base64 (b64_json), not a URL
      const buffer = Buffer.from(image.b64_json ?? "", "base64");
      fs.writeFileSync("generated-image.png", buffer);
      console.log("Saved generated-image.png");
    }
  } catch (error) {
    console.log("The sample encountered an error: ", error);
  }
}

main();