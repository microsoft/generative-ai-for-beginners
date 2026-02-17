import { OpenAIClient, AzureKeyCredential } from "@azure/openai";
import axios, { AxiosError } from "axios";
import * as dotenv from "dotenv";

dotenv.config();

// SECURITY: Validate required environment variables
const endpoint = process.env.AZURE_OPENAI_ENDPOINT;
const azureApiKey = process.env.AZURE_OPENAI_API_KEY;
const bingMapsBaseUrl = process.env.BING_MAPS_BASE_URL;
const bingApiKey = process.env.BING_API_KEY;

if (!endpoint || !azureApiKey) {
  throw new Error("AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY environment variables are required");
}

if (!bingMapsBaseUrl || !bingApiKey) {
  throw new Error("BING_MAPS_BASE_URL and BING_API_KEY environment variables are required");
}

// SECURITY: Validate URL format
function isValidUrl(urlString: string): boolean {
  try {
    const url = new URL(urlString);
    return url.protocol === 'https:';
  } catch {
    return false;
  }
}

if (!isValidUrl(endpoint) || !isValidUrl(bingMapsBaseUrl)) {
  throw new Error("Invalid URL format for endpoints. Must be HTTPS URLs.");
}

async function findWeather(currentLocation: string, placeType: string): Promise<unknown> {
  // SECURITY: URL-encode ALL parameters to prevent injection
  const params = new URLSearchParams({
    query: currentLocation,
    type: placeType,
    key: bingApiKey!
  });
  const url = `${bingMapsBaseUrl}?${params.toString()}`;

  try {
    // SECURITY: Add timeout to prevent hanging requests
    const response = await axios.get(url, { timeout: 10000 });
    return response.data;
  } catch (error) {
    // SECURITY: Avoid logging full error which may contain sensitive data
    if (error instanceof AxiosError) {
      console.error(`API request failed: ${error.message} (Status: ${error.response?.status || 'N/A'})`);
    } else {
      console.error('Error in findWeather: An unexpected error occurred');
    }
    return { error: 'Failed to retrieve weather data' };
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

        // SECURITY: Safely parse JSON with validation
        let parsedArgs: { location?: string; unit?: string };
        try {
          parsedArgs = JSON.parse(argumentsJson || '{}');
        } catch (parseError) {
          console.error('Failed to parse function arguments');
          continue;
        }

        const { location, unit } = parsedArgs;
        if (!location) {
          console.error('Missing required location parameter');
          continue;
        }

        let response = await findWeather(location, unit || 'C');
        console.log("Result from Bing Maps API..: ", response);
      }
    }
  } catch (error) {
    console.error("The sample encountered an error...:", error);
  }
}

main();