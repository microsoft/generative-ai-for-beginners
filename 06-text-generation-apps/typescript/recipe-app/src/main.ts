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
    console.log("== Recipe Recommendation App ==");

    // Use the deployment name configured in your .env file
    const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT || 'gpt-4o-mini';

    console.log("Number of recipes: (for example: 5): ");
    const numRecipes = "2";

    console.log("List of ingredients: (for example: chicken, potatoes, and carrots): ");
    const ingredients = "chocolate";

    console.log("Filter (for example: vegetarian, vegan, or gluten-free): ");
    const filter = "peanuts";

    const promptText = `Show me ${numRecipes} recipes for a dish with the following ingredients: ${ingredients}. Per recipe, list all the ingredients used, no ${filter}: `;

    try {
        const completionResponse = await client.responses.create({
            model: deploymentName,
            input: [
                {
                    role: 'system',
                    content: 'Hello, I am a recipe recommendation bot. I will recommend recipes based on the ingredients you provide me.'
                },
                {
                    role: 'user',
                    content: promptText
                },
            ],
            max_output_tokens: 700,
            temperature: 0.1,
            store: false,
        });

        console.log("Recipe Recommendations: ");
        console.log(completionResponse.output_text);

        const oldPromptResult = completionResponse.output_text;
        const promptShoppingList = 'Produce a shopping list, and please do not include the following ingredients that I already have at home: ';

        const newPrompt = `Given ingredients at home: ${ingredients} and these generated recipes: ${oldPromptResult}, ${promptShoppingList}`;

        const shoppingListResponse = await client.responses.create({
            model: deploymentName,
            input: [
                {
                    role: 'system',
                    content: 'Here is your shopping list:'
                },
                {
                    role: 'user',
                    content: newPrompt
                },
            ],
            max_output_tokens: 700,
            temperature: 0.1,
            store: false,
        });

        console.log("\n ===== Shopping List ===== \n");
        console.log(shoppingListResponse.output_text);
    } catch (error) {
        console.log('The sample encountered an error: ', error);
    }
}

main();