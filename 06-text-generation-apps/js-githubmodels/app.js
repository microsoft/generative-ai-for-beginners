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
// temperature/top_p need a non-reasoning model (reasoning models like gpt-5 reject them),
// so use a Llama model via the Microsoft Foundry Models endpoint to demonstrate temperature.
const modelName = process.env["AZURE_INFERENCE_CHAT_MODEL"] || "Llama-3.3-70B-Instruct";

export async function main() {

    console.log("== Recipe Recommendation App ==");

    console.log("Number of recipes: (for example: 5): ");
    const numRecipes = "3";

    console.log("List of ingredients: (for example: chicken, potatoes, and carrots): ");
    const ingredients = "chocolate";

    console.log("Filter (for example: vegetarian, vegan, or gluten-free): ");
    const filter = "peanuts";

    const promptText = `Show me ${numRecipes} recipes for a dish with the following ingredients: ${ingredients}. Per recipe, list all the ingredients used, no ${filter}: `;


    // The OpenAI client points at the Microsoft Foundry OpenAI-compatible /openai/v1/ endpoint,
    // which serves OpenAI models as well as models like Llama, Mistral, and Phi.
    const client = new OpenAI({
        apiKey: token,
        baseURL: `${endpoint.replace(/\/$/, "")}/openai/v1/`,
    });

    // Chat Completions is used here because temperature/top_p/max_tokens are
    // supported by the Llama model (the SDK throws on non-2xx responses).
    const response = await client.chat.completions.create({
        messages: [
            { role: "system", content: "You are a helpful assistant." },
            { role: "user", content: promptText }
        ],
        model: modelName,
        temperature: 1.0,
        max_tokens: 1000,
        top_p: 1.0
    });

    console.log(response.choices[0].message.content);


    const oldPromptResult = response.choices[0].message.content;

    const promptShoppingList = 'Produce a shopping list, and please do not include the following ingredients that I already have at home: ';

    const newPrompt = `Given ingredients at home: ${ingredients} and these generated recipes: ${oldPromptResult}, ${promptShoppingList}`;

    const shoppingListMessage = await client.chat.completions.create({
        messages: [
            {
                role: 'system',
                content: 'Here is your shopping list:'
            },
            {
                role: 'user',
                content: newPrompt
            },
        ],
        model: modelName,
    });

    console.log("Shopping list:");
    console.log(shoppingListMessage.choices[0].message.content);
}


main().catch((err) => {
    console.error("The sample encountered an error:", err);
});
