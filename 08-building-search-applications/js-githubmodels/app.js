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

/* Because Microsoft Foundry serves models through the same OpenAI-compatible
   /openai/v1/ endpoint, you can easily experiment with different models
   by modifying the value of `modelName` in the code below. For this code sample
   you need an embedding model deployed in your Foundry resource, for example:

   OpenAI: text-embedding-3-small, text-embedding-3-large */
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

    // The OpenAI client points at the Microsoft Foundry OpenAI-compatible /openai/v1/ endpoint.
    const client = new OpenAI({
        apiKey: token,
        baseURL: `${endpoint.replace(/\/$/, "")}/openai/v1/`,
    });

    // The SDK throws on non-2xx responses, so no manual status check is needed.
    const response = await client.embeddings.create({
        input: ["Car", "Vehicle", "Bird"],
        model: modelName
    });

    for (const item of response.data) {
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

    console.log(response.usage);
    console.log(carEmbedding)
    const scoreCarWithVehicle = cosineSimilarity(carEmbedding, vehicleEmbedding);
    console.log("Comparing - Car vs Vehicle...: ", scoreCarWithVehicle.toFixed(7));


    const scoreCarWithBird = cosineSimilarity(carEmbedding, birdEmbedding);
    console.log("Comparing - Car vs Bird...: ", scoreCarWithBird.toFixed(7));
    
}

main().catch((err) => {
    console.error("The sample encountered an error:", err);
});
