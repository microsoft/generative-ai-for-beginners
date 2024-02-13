import { OpenAIClient, AzureKeyCredential } from "@azure/openai";
import * as dotenv from "dotenv";

dotenv.config();

const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "";
const azureApiKey = process.env.AZURE_OPENAI_KEY || "";

/**
 * Calculates the cosine similarity between two vectors.
 * @param vector1 The first vector.
 * @param vector2 The second vector.
 * @returns The cosine similarity score.
 */
function cosineSimilarity(vector1: number[], vector2: number[]): number {
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

/**
 * Main function to execute the document similarity comparison.
 */
async function main() {
    try {
        
        console.log("== Building Search Applications with Azure OpenAI ==");

        const client = new OpenAIClient(endpoint, new AzureKeyCredential(azureApiKey));
        const deploymentName = "deployment-name-embeddings"; // here should be of type ADA embedding for Azure OpenAI

        const source = "Car";
        const compareTo = "Vehicle";
        const parrot = "A bird";

        const parrotEmbedding = await client.getEmbeddings(deploymentName, [parrot]);
        const embeddings = await client.getEmbeddings(deploymentName, [source]);
        const embeddingsCompareTo = await client.getEmbeddings(deploymentName, [compareTo]);

        const carArray = embeddings.data[0].embedding;
        const vehicleArray = embeddingsCompareTo.data[0].embedding;
        const parrotArray = parrotEmbedding.data[0].embedding;

        const scoreCarWithVehicle  = cosineSimilarity(carArray, vehicleArray);
        console.log("Comparing - Car vs Vehicle...: ", scoreCarWithVehicle.toFixed(7));

        const scoreCarWithParrot  = cosineSimilarity(carArray, parrotArray);
        console.log("Comparing - Car vs Parrot...: ", scoreCarWithParrot .toFixed(7));

    } catch (error) {
        console.error("The sample encountered an error:", error);
    }
}

main();