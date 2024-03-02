# Setup Your Dev Environment

We have instrumented this repository with a _dev container_ that comes with a Python 3 runtime. Simply open the repo in GitHub Codespaces or on your local Docker Desktop, to activate the runtime automatically. Then open th Jupyter notebook and select the Python 3.x kernel to prepare the Notebook for execution.

## 1. Create `.env` file

The default notebook is set up for use with an [Azure OpenAI service resource](https://learn.microsoft.com/azure/ai-services/openai?WT.mc_id=academic-105485-koreyst). To configure this, we need to setup local environment variables for Azure as follows:

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

3. (Option) If you use GitHub Codespaces, you can also save environment variables as [_Codespaces secrets as described here_](https://docs.github.com/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces?WT.mc_id=academic-105485-koreyst). Visit that link to learn how to add a secret, edit it, delete it, and use it in your running codespace. **If you choose this option**, your [**GitHub Settings > Codespaces Secrets**](https://github.com/settings/codespaces?WT.mc_id=academic-105485-koreyst) should look something like this. 
    ![Codespaces Secrets](./img/codespaces-secrets.png?WT.mc_id=academic-105485-koreyst)

    Note that you can create these secrets once and then make them available to multiple repositories that use those env variables. **However, note that this option works only if you use GitHub Codespaces.** You will still need to setup the .env file if you plan to use Docker Desktop for local development with that devcontainer configruation.


## 2. Populate `.env` file

Let's take a quick look at the variable names to understand what they represent:

| Variable | Description |
|:---|:---|
|AZURE_OPENAI_ENDPOINT| This is the deployed endpoint for an Azure OpenAI resource|
|AZURE_OPENAI_KEY | This is the authorization key for using that service  |
|AZURE_OPENAI_DEPLOYMENT| This is the _text generation_ model deployment endpoint |
|AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | This is the _text embeddings_ model deployment endpoint |
| | | 

For context, the last two variables refer to specific models that are used in chat completion (text generation model) and vector search (embeddings model) activities that are frequently used in generative AI applications. In the following sections, we'll locate the _values_ for these variables and set them in `.env` (replacing the content within the `' '`, but preserving the quotes).

### 2.1 Use Azure Portal

The Azure OpenAI endpoint and key values will be found in the [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) so let's start there.

1. Navigate to the [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
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