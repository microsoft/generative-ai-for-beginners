import ModelClient from "@azure-rest/ai-inference";
import { isUnexpected } from "@azure-rest/ai-inference";
import { AzureKeyCredential } from "@azure/core-auth";
import { brotliDecompress } from "zlib";

const token = process.env["GITHUB_TOKEN"];
const endpoint = "https://models.inference.ai.azure.com";

/* By using the Azure AI Inference SDK, you can easily experiment with different models
   by modifying the value of `modelName` in the code below. For this code sample
   you need an embedding model. The following embedding models are
   available in the GitHub Models service:

   Cohere: Cohere-embed-v3-english, Cohere-embed-v3-multilingual
   Azure OpenAI: text-embedding-3-small, text-embedding-3-large */
const modelName = "text-embedding-3-small";

function cosineSimilarity(vector1, vector2) {
    if (vector1.length !== vector2.length) {
        throw new Error("Vector dimensions must match for cosine similarity calculation.");
    }

    const dotProduct = vector1.reduce((acc, val, index) => acc + val * vector2[index], 0);
    const magnitude1 = Math.sqrt(vector1.reduce((acc, val) => acc + val ** 2, 0));
    const magnitude2 = Math.sqrt(vector2.reduce((acc, val) => acc + val ** 2, 0));

    if (magnitude1 === 0 || magnitude2 === 0) {
        throw new Error("Magnitude of a vector must be non-zero for cosine similarity calculation.");
    }

    return dotProduct / (magnitude1 * magnitude2);
}



export async function main() {
    let carEmbedding, vehicleEmbedding, birdEmbedding

    const client = new ModelClient(endpoint, new AzureKeyCredential(token));

    const response = await client.path("/embeddings").post({
        body: {
            input: ["Car", "Vehicle", "Bird"],
            model: modelName
        }
    });

    if (isUnexpected(response)) {
        throw response.body.error;
    }

    for (const item of response.body.data) {
        const { embedding, index } = item;  // Destructure item for cleaner code
        const length = embedding.length;

        switch (index) {
            case 0:
                carEmbedding = embedding;
                break;
            case 1:
                vehicleEmbedding = embedding;
                break;
            case 2:
                birdEmbedding = embedding;
                break;
        }

        console.log(
            `data[${item.index}]: length=${length}, ` +
            `[${item.embedding[0]}, ${item.embedding[1]}, ` +
            `..., ${item.embedding[length - 2]}, ${item.embedding[length - 1]}]`);

        
    }

    console.log(response.body.usage);
    console.log(carEmbedding)
    const scoreCarWithVehicle = cosineSimilarity(carEmbedding, vehicleEmbedding);
    console.log("Comparing - Car vs Vehicle...: ", scoreCarWithVehicle.toFixed(7));


    const scoreCarWithBird = cosineSimilarity(carEmbedding, birdEmbedding);
    console.log("Comparing - Car vs Bird...: ", scoreCarWithBird.toFixed(7));
    
}

main().catch((err) => {
    console.error("The sample encountered an error:", err);
});
