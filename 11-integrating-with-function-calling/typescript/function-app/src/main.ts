import { OpenAIClient, AzureKeyCredential } from "@azure/openai";
import axios from "axios";
import * as dotenv from "dotenv";

dotenv.config();

const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "";
const azureApiKey = process.env.AZURE_OPENAI_KEY || "";
const bingMapsBaseUrl = process.env.BING_MAPS_BASE_URL || "";
const bingApiKey = process.env.BING_API_KEY || "";

async function findWeather(currentLocation: string, placeType: string) {
  const url = `${bingMapsBaseUrl}?query=${encodeURIComponent(currentLocation)}&type=${placeType}&key=${bingApiKey}`;

  try {
    const response = await axios.get(url);
    return response.data;
  } catch (error) {
    console.log('Error in findWeather...: ', error);
  }
}

const getCurrentWeatherFunction = {
  name: "findWeather",
  description: "Get the current weather in a given location",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city and state, e.g. San Francisco, CA"
      },
      unit: {
        type: "string",
        enum: ["C", "F"], // Celsius or Fahrenheit
      },
    },
    required: ["location"],
  },
};

async function main() {
  try {
    console.log("== Chat Completions App with Functions ==");

    const client = new OpenAIClient(endpoint, new AzureKeyCredential(azureApiKey));
    const deploymentName = "gpt-4"; // if you want to use 'gpt-4' model you need to create a resource in Sweden Central region
    
    const userParams = { 
      location: "New York", 
      unit: "C" 
    };
    
    const result = await client.getChatCompletions(deploymentName, [
      { 
        role: "user", 
        content: `What's the weather in ${userParams.location}, ${userParams.unit}?`,
      },  
    ], {
      functions: [getCurrentWeatherFunction],
    });

    for (const choice of result.choices) {
      console.log(choice.message?.functionCall);

      if (choice.message?.functionCall) {
        const { arguments: argumentsJson } = choice.message.functionCall;
        const { location, unit } = JSON.parse(argumentsJson);
        let response = await findWeather(location, unit);
        console.log("Result from Bing Maps API..: ", response);
      }
    }
  } catch (error) {
    console.error("The sample encountered an error...:", error);
  }
}

main();