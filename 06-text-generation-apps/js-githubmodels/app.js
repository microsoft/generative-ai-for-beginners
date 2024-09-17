import ModelClient from "@azure-rest/ai-inference";
import { AzureKeyCredential } from "@azure/core-auth";

const token = process.env["GITHUB_TOKEN"];
const endpoint = "https://models.inference.ai.azure.com";
const modelName = "gpt-4o";

export async function main() {

    console.log("== Recipe Recommendation App ==");

    console.log("Number of recipes: (for example: 5): ");
    const numRecipes = "3";

    console.log("List of ingredients: (for example: chicken, potatoes, and carrots): ");
    const ingredients = "chocolate";
    
    console.log("Filter (for example: vegetarian, vegan, or gluten-free): ");
    const filter = "peanuts";

    const promptText = `Show me ${numRecipes} recipes for a dish with the following ingredients: ${ingredients}. Per recipe, list all the ingredients used, no ${filter}: `;


    const client = new ModelClient(endpoint, new AzureKeyCredential(token));

    const response = await client.path("/chat/completions").post({
        body: {
            messages: [
                { role: "system", content: "You are a helpful assistant." },
                { role: "user", content: promptText }
            ],
            model: modelName,
            temperature: 1.0,
            max_tokens: 1000,
            top_p: 1.0
        }
    });

try { 


    if (response.status !== "200") {
        throw response.body.error;
    }
    console.log(response.body.choices[0].message.content);


const oldPromptResult = response.body.choices[0].message.content;

const promptShoppingList = 'Produce a shopping list, and please do not include the following ingredients that I already have at home: ';

const newPrompt = `Given ingredients at home: ${ingredients} and these generated recipes: ${oldPromptResult}, ${promptShoppingList}`;

const shoppingListMessage = 
    await client.path("/chat/completions").post({
    body: {
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
}

    })

} catch (error) {
    console.log('The sample encountered an error: ', error);
}
}


main().catch((err) => {
    console.error("The sample encountered an error:", err);
});