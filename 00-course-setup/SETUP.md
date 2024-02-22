# Setup Your Dev Environment

We have setup this repository and course with a _dev container_ that comes with a Python 3 runtime. Open the repo in GitHub Codespaces or on your local Docker Desktop, to activate the runtime automatically. Then open th Jupyter notebook and select the Python 3.x kernel to prepare the Notebook for execution.

## 1. Create `.env` file

The default notebook (identified by the 'aoai-' suffix) is set up for use with an [Azure OpenAI service resource](https://learn.microsoft.com/azure/ai-services/openai?WT.mc_id=academic-105485-koreyst). However, you have the option to run your assignments by using non-Azure openAI endpoints (choose the 'oai-' prefixed notebooks in this case).

To configure this, we need to setup local environment variables for Azure as follows:

1. Look in the root folder for a `.env.copy` file. It should contain a list of name-value pairs like this:

   ```bash
   AZURE_OPENAI_ENDPOINT='<add your endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your deployment name here>'
   AZURE_OPENAI_KEY='<add your key here>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your deployment name here>'
   ```

2. Make a copy of that file called `.env` using a command like this at the terminal:

   ```bash
   cp .env.copy .env
   ```

   This should create an identical copy _except that this file is .gitignore-d and will never get checked into source control_. We can now populate **this .env file** with the environment variable values (secrets) without fear of them being checked in accidentally. You can now move to the next section to start populating these variables.

3. (Option) If you use GitHub Codespaces, you have the option to save environment variables as _Codespaces secrets_ associated with this repository. In that case, you won't need to setup a local .env file. **However, note that this option works only if you use GitHub Codespaces.** You will still need to setup the .env file if you use Docker Desktop instead.

The above steps should be executed also if you are using the non-Azure OpenAI endpoints. In that case, you will need to populate the .env file with the appropriate values for the OpenAI service.

```bash
OPENAI_API_KEY='<add your OpenAI key here>'
```

## 2. Populate `.env` file

Let's take a quick look at the variable names to understand what they represent:

| Variable                           | Description                                                                        |
| :--------------------------------- | :--------------------------------------------------------------------------------- |
| AZURE_OPENAI_ENDPOINT              | This is the deployed endpoint for an Azure OpenAI resource                         |
| AZURE_OPENAI_KEY                   | This is the authorization key for using that service                               |
| OPENAI_API_KEY                     | This is the authorization key for using the service for non-Azure OpenAI endpoints |
| AZURE_OPENAI_DEPLOYMENT            | This is the _text generation_ model deployment endpoint                            |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | This is the _text embeddings_ model deployment endpoint                            |
|                                    |                                                                                    |

For context, the last two variables refer to specific models that are used in chat completion (text generation model) and vector search (embeddings model) activities that are frequently used in generative AI applications. In the following sections, we'll locate the _values_ for these variables and set them in `.env` (replacing the content within the `' '`, but preserving the quotes).

### 2.1 Use Azure Portal

The Azure OpenAI endpoint and key values will be found in the [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) so let's start there.

1. Go to the [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Click the **Keys and Endpoint** option in the sidebar (menu at left).
1. Click **Show Keys** - you should see the following: KEY 1, KEY 2 and Endpoint.
1. Use the KEY 1 value for AZURE_OPENAI_KEY
1. Use the Endpoint value for AZURE_OPENAI_ENDPOINT

Next, we need the endpoints for the specific models we've deployed.

1. Click the **Model deployments** option in the sidebar (left menu) for Azure OpenAI resource.
1. In the destination page, click **Manage Deployments**

This will take you to the Azure OpenAI Studio website, where we'll find the other values as described below.

### 2.2 Use Azure OpenAI Studio

1. Navigate to [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **from your resource** as described above.
1. Click the **Deployments** tab (sidebar, left) to view currently deployed models.
1. If your desired model is not deployed, use **Create new deployment** to deploy it.
1. You will need a _text-generation_ model - we recommend: **gpt-35-turbo**
1. You will need a _text-embedding_ model - we recommend **text-embedding-ada-002**

Now update the environment variables to reflect the _Deployment name_ used. This will typically be the same as the model name unless you changed it explcitly. So, as an example, you might have:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Don't forget to save the .env file when done**. You can now exit the file and return to the instructions for running the notebook.

### 2.3 Use OpenAI Public API

Your OpenAI API key can be found in your [OpenAI account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). If you don't have one, you can sign up for an account and create an API key. Once you have the key, you can use it to populate the `OPENAI_API_KEY` variable in the `.env` file.
