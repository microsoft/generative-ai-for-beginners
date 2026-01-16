<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "238cde5c90363d70ecc939569378da51",
  "translation_date": "2025-12-19T20:42:10+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ml"
}
-->
# ഇമേജ് ജനറേഷൻ ആപ്ലിക്കേഷനുകൾ നിർമ്മിക്കൽ

[![ഇമേജ് ജനറേഷൻ ആപ്ലിക്കേഷനുകൾ നിർമ്മിക്കൽ](../../../translated_images/ml/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLM-കൾക്ക് ടെക്സ്റ്റ് ജനറേഷനിൽ മാത്രമല്ല, ടെക്സ്റ്റ് വിവരണങ്ങളിൽ നിന്ന് ചിത്രങ്ങൾ സൃഷ്ടിക്കാനും കഴിയും. ചിത്രങ്ങൾ ഒരു മോഡാലിറ്റി ആയി ഉള്ളത് മെഡടെക്, ആർക്കിടെക്ചർ, ടൂറിസം, ഗെയിം ഡെവലപ്പ്മെന്റ് തുടങ്ങിയ പല മേഖലകളിലും വളരെ ഉപകാരപ്രദമാണ്. ഈ അധ്യായത്തിൽ, ഏറ്റവും ജനപ്രിയമായ രണ്ട് ഇമേജ് ജനറേഷൻ മോഡലുകൾ, DALL-Eയും Midjourneyയും പരിചയപ്പെടാം.

## പരിചയം

ഈ പാഠത്തിൽ, നാം ചർച്ച ചെയ്യുന്നത്:

- ഇമേജ് ജനറേഷൻ എന്താണെന്നും അത് എങ്ങനെ ഉപകാരപ്രദമാണെന്നും.
- DALL-Eയും Midjourneyയും എന്താണെന്നും അവ എങ്ങനെ പ്രവർത്തിക്കുന്നുവെന്നും.
- ഒരു ഇമേജ് ജനറേഷൻ ആപ്പ് എങ്ങനെ നിർമ്മിക്കാമെന്നും.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠം പൂർത്തിയാക്കിയ ശേഷം, നിങ്ങൾക്ക് കഴിയും:

- ഒരു ഇമേജ് ജനറേഷൻ ആപ്ലിക്കേഷൻ നിർമ്മിക്കുക.
- മെടാ പ്രോംപ്റ്റുകൾ ഉപയോഗിച്ച് നിങ്ങളുടെ ആപ്ലിക്കേഷനു പരിധികൾ നിർവചിക്കുക.
- DALL-Eയും Midjourneyയും ഉപയോഗിച്ച് പ്രവർത്തിക്കുക.

## എന്തുകൊണ്ട് ഇമേജ് ജനറേഷൻ ആപ്ലിക്കേഷൻ നിർമ്മിക്കണം?

ഇമേജ് ജനറേഷൻ ആപ്ലിക്കേഷനുകൾ ജനറേറ്റീവ് AI-യുടെ കഴിവുകൾ പരീക്ഷിക്കാൻ മികച്ച മാർഗമാണ്. ഉദാഹരണത്തിന്, ഇവ ഉപയോഗിക്കാം:

- **ഇമേജ് എഡിറ്റിംഗ്, സിന്തസിസ്**. ഇമേജ് എഡിറ്റിംഗ്, സിന്തസിസ് തുടങ്ങിയ വിവിധ ഉപയോഗങ്ങൾക്കായി ചിത്രങ്ങൾ സൃഷ്ടിക്കാം.

- **വിവിധ വ്യവസായങ്ങളിൽ പ്രയോഗം**. മെഡടെക്, ടൂറിസം, ഗെയിം ഡെവലപ്പ്മെന്റ് തുടങ്ങിയ വ്യവസായങ്ങൾക്ക് ചിത്രങ്ങൾ സൃഷ്ടിക്കാൻ ഉപയോഗിക്കാം.

## സീനാരിയോ: Edu4All

ഈ പാഠത്തിന്റെ ഭാഗമായാണ് Edu4All സ്റ്റാർട്ടപ്പുമായി നാം തുടർന്നും പ്രവർത്തിക്കുന്നത്. വിദ്യാർത്ഥികൾ അവരുടെ അസൈൻമെന്റുകൾക്കായി ചിത്രങ്ങൾ സൃഷ്ടിക്കും, ചിത്രങ്ങൾ എന്തായിരിക്കും എന്നത് വിദ്യാർത്ഥികളുടെ ഇഷ്ടാനുസരണം, അവരുടേതായ കഥകളുടെ ചിത്രീകരണങ്ങൾ ആകാം, പുതിയ കഥാപാത്രങ്ങൾ സൃഷ്ടിക്കാം, അല്ലെങ്കിൽ അവരുടെ ആശയങ്ങൾ ദൃശ്യവൽക്കരിക്കാം.

ക്ലാസിൽ സ്മാരകങ്ങളെക്കുറിച്ച് പഠിക്കുമ്പോൾ Edu4All വിദ്യാർത്ഥികൾ സൃഷ്ടിക്കാവുന്ന ഉദാഹരണം:

![Edu4All startup, class on monuments, Eiffel Tower](../../../translated_images/ml/startup.94d6b79cc4bb3f5a.webp)

പ്രോംപ്റ്റ് ഉപയോഗിച്ച്

> "Dog next to Eiffel Tower in early morning sunlight"

## DALL-Eയും Midjourneyയും എന്താണ്?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst)യും [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst)യും ഏറ്റവും ജനപ്രിയമായ രണ്ട് ഇമേജ് ജനറേഷൻ മോഡലുകളാണ്, പ്രോംപ്റ്റുകൾ ഉപയോഗിച്ച് ചിത്രങ്ങൾ സൃഷ്ടിക്കാൻ അവ അനുവദിക്കുന്നു.

### DALL-E

DALL-E-യിൽ നിന്നാണ് തുടങ്ങുന്നത്, ഇത് ടെക്സ്റ്റ് വിവരണങ്ങളിൽ നിന്ന് ചിത്രങ്ങൾ സൃഷ്ടിക്കുന്ന ഒരു ജനറേറ്റീവ് AI മോഡലാണ്.

> [DALL-E CLIP, diffused attention എന്നീ രണ്ട് മോഡലുകളുടെ സംയോജനം ആണ്](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, ചിത്രങ്ങളിലെയും ടെക്സ്റ്റിലെയും ഡാറ്റയുടെ സംഖ്യാത്മക പ്രതിനിധാനങ്ങൾ (എംബെഡിംഗുകൾ) സൃഷ്ടിക്കുന്ന മോഡലാണ്.

- **Diffused attention**, എംബെഡിംഗുകളിൽ നിന്ന് ചിത്രങ്ങൾ സൃഷ്ടിക്കുന്ന മോഡലാണ്. DALL-E ചിത്രങ്ങളും ടെക്സ്റ്റും അടങ്ങിയ ഡാറ്റാസെറ്റിൽ പരിശീലിപ്പിച്ചിരിക്കുന്നു, ടെക്സ്റ്റ് വിവരണങ്ങളിൽ നിന്ന് ചിത്രങ്ങൾ സൃഷ്ടിക്കാൻ ഉപയോഗിക്കാം. ഉദാഹരണത്തിന്, ഒരു ടോപ്പി ധരിച്ച പൂച്ചയുടെ ചിത്രം അല്ലെങ്കിൽ മോഹോക്ക് ഉള്ള നായയുടെ ചിത്രം സൃഷ്ടിക്കാൻ DALL-E ഉപയോഗിക്കാം.

### Midjourney

Midjourney DALL-E പോലെയാണ് പ്രവർത്തിക്കുന്നത്, ടെക്സ്റ്റ് പ്രോംപ്റ്റുകളിൽ നിന്ന് ചിത്രങ്ങൾ സൃഷ്ടിക്കുന്നു. Midjourney-യും “a cat in a hat” അല്ലെങ്കിൽ “dog with a mohawk” പോലുള്ള പ്രോംപ്റ്റുകൾ ഉപയോഗിച്ച് ചിത്രങ്ങൾ സൃഷ്ടിക്കാൻ കഴിയും.

![Midjourney-ൽ സൃഷ്ടിച്ച ചിത്രം, മെക്കാനിക്കൽ പിജൻ](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_ചിത്രം: വിക്കിപീഡിയ, Midjourney-ൽ സൃഷ്ടിച്ചത്_

## DALL-Eയും Midjourneyയും എങ്ങനെ പ്രവർത്തിക്കുന്നു

ആദ്യം, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E ഒരു ട്രാൻസ്ഫോർമർ ആർക്കിടെക്ചർ അടിസ്ഥാനമാക്കിയുള്ള ജനറേറ്റീവ് AI മോഡലാണ്, അതിൽ _autoregressive transformer_ ഉണ്ട്.

_autoregressive transformer_ ഒരു മോഡൽ ടെക്സ്റ്റ് വിവരണങ്ങളിൽ നിന്ന് ചിത്രങ്ങൾ എങ്ങനെ സൃഷ്ടിക്കുന്നുവെന്ന് നിർവചിക്കുന്നു, ഓരോ പിക്‌സലും ഒരിക്കൽ സൃഷ്ടിച്ച്, സൃഷ്ടിച്ച പിക്‌സലുകൾ ഉപയോഗിച്ച് അടുത്ത പിക്‌സൽ സൃഷ്ടിക്കുന്നു. ഇത് ന്യുറൽ നെറ്റ്‌വർക്കിലെ പല ലെയറുകൾ കടന്നുപോകുന്നു, ചിത്രമാകുന്നത് വരെ.

ഈ പ്രക്രിയയിലൂടെ, DALL-E സൃഷ്ടിക്കുന്ന ചിത്രത്തിലെ ഗുണങ്ങൾ, വസ്തുക്കൾ, സ്വഭാവങ്ങൾ എന്നിവ നിയന്ത്രിക്കുന്നു. എന്നാൽ, DALL-E 2, 3-ൽ സൃഷ്ടിച്ച ചിത്രത്തെ കൂടുതൽ നിയന്ത്രണം ഉണ്ട്.

## നിങ്ങളുടെ ആദ്യ ഇമേജ് ജനറേഷൻ ആപ്ലിക്കേഷൻ നിർമ്മിക്കൽ

ഇമേജ് ജനറേഷൻ ആപ്ലിക്കേഷൻ നിർമ്മിക്കാൻ എന്തൊക്കെയാണ് വേണ്ടത്? താഴെ പറയുന്ന ലൈബ്രറികൾ ആവശ്യമാണ്:

- **python-dotenv**, രഹസ്യങ്ങൾ _.env_ ഫയലിൽ സൂക്ഷിക്കാൻ ഈ ലൈബ്രറി ഉപയോഗിക്കാൻ ശക്തമായി ശുപാർശ ചെയ്യുന്നു.
- **openai**, OpenAI API-യുമായി ഇടപഴകാൻ ഈ ലൈബ്രറി ഉപയോഗിക്കും.
- **pillow**, Python-ൽ ചിത്രങ്ങൾ കൈകാര്യം ചെയ്യാൻ.
- **requests**, HTTP അഭ്യർത്ഥനകൾ നടത്താൻ സഹായിക്കും.

## Azure OpenAI മോഡൽ സൃഷ്ടിക്കുകയും വിന്യസിക്കുകയും ചെയ്യുക

ഇപ്പോൾ വരെ ചെയ്തിട്ടില്ലെങ്കിൽ, [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) പേജിലെ നിർദ്ദേശങ്ങൾ പിന്തുടർന്ന് Azure OpenAI റിസോഴ്‌സ്, മോഡൽ സൃഷ്ടിക്കുക. മോഡലായി DALL-E 3 തിരഞ്ഞെടുക്കുക.

## ആപ്പ് സൃഷ്ടിക്കുക

1. താഴെ കാണുന്ന ഉള്ളടക്കത്തോടെ _.env_ ഫയൽ സൃഷ്ടിക്കുക:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   ഈ വിവരങ്ങൾ Azure OpenAI Foundry പോർട്ടലിലെ "Deployments" വിഭാഗത്തിൽ കണ്ടെത്തുക.

1. മുകളിൽ പറഞ്ഞ ലൈബ്രറികൾ _requirements.txt_ എന്ന ഫയലിൽ ചേർക്കുക:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. തുടർന്ന്, വെർച്വൽ എൻവയോൺമെന്റ് സൃഷ്ടിച്ച് ലൈബ്രറികൾ ഇൻസ്റ്റാൾ ചെയ്യുക:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows-ൽ, വെർച്വൽ എൻവയോൺമെന്റ് സൃഷ്ടിച്ച് സജീവമാക്കാൻ താഴെ കാണുന്ന കമാൻഡുകൾ ഉപയോഗിക്കുക:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ എന്ന ഫയലിൽ താഴെ കാണുന്ന കോഡ് ചേർക്കുക:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # dotenv ഇറക്കുമതി ചെയ്യുക
    dotenv.load_dotenv()
    
    # Azure OpenAI സേവന ക്ലയന്റ് ക്രമീകരിക്കുക
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
    try:
        # ഇമേജ് ജനറേഷൻ API ഉപയോഗിച്ച് ഒരു ചിത്രം സൃഷ്ടിക്കുക
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # സൂക്ഷിച്ചിരിക്കുന്ന ചിത്രത്തിനുള്ള ഡയറക്ടറി സജ്ജമാക്കുക
        image_dir = os.path.join(os.curdir, 'images')

        # ഡയറക്ടറി ഇല്ലെങ്കിൽ, അത് സൃഷ്ടിക്കുക
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # ചിത്രം പാത ആരംഭിക്കുക (ഫയൽടൈപ്പ് png ആകണം എന്ന് ശ്രദ്ധിക്കുക)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # സൃഷ്ടിച്ച ചിത്രം ലഭിക്കുക
        image_url = generation_response.data[0].url  # പ്രതികരണത്തിൽ നിന്ന് ചിത്രം URL എടുക്കുക
        generated_image = requests.get(image_url).content  # ചിത്രം ഡൗൺലോഡ് ചെയ്യുക
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # ഡിഫോൾട്ട് ഇമേജ് വ്യൂവറിൽ ചിത്രം പ്രദർശിപ്പിക്കുക
        image = Image.open(image_path)
        image.show()

    # исключения പിടിക്കുക
    except openai.InvalidRequestError as err:
        print(err)
   ```

ഈ കോഡ് വിശദീകരിക്കാം:

- ആദ്യം, OpenAI ലൈബ്രറി, dotenv ലൈബ്രറി, requests ലൈബ്രറി, Pillow ലൈബ്രറി എന്നിവ ഉൾപ്പെടെ ആവശ്യമായ ലൈബ്രറികൾ ഇറക്കുമതി ചെയ്യുന്നു.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- തുടർന്ന്, _.env_ ഫയലിൽ നിന്നുള്ള എൻവയോൺമെന്റ് വേരിയബിളുകൾ ലോഡ് ചെയ്യുന്നു.

  ```python
  # ഡോട്ട് എൻവൈറൺമെന്റ് ഇമ്പോർട്ട് ചെയ്യുക
  dotenv.load_dotenv()
  ```

- അതിനുശേഷം, Azure OpenAI സർവീസ് ക്ലയന്റ് കോൺഫിഗർ ചെയ്യുന്നു.

  ```python
  # എൻവയോൺമെന്റ് വേരിയബിളുകളിൽ നിന്ന് എൻഡ്‌പോയിന്റും കീയും നേടുക
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- തുടർന്ന്, ചിത്രം സൃഷ്ടിക്കുന്നു:

  ```python
  # ഇമേജ് ജനറേഷൻ API ഉപയോഗിച്ച് ഒരു ചിത്രം സൃഷ്ടിക്കുക
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  മുകളിൽ കാണുന്ന കോഡ് സൃഷ്ടിച്ച ചിത്രത്തിന്റെ URL അടങ്ങിയ JSON ഒബ്ജക്റ്റ് നൽകുന്നു. ആ URL ഉപയോഗിച്ച് ചിത്രം ഡൗൺലോഡ് ചെയ്ത് ഫയലായി സൂക്ഷിക്കാം.

- അവസാനം, ചിത്രം തുറന്ന് സാധാരണ ഇമേജ് വ്യൂവറിലൂടെ പ്രദർശിപ്പിക്കുന്നു:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### ചിത്ര സൃഷ്ടിക്കുന്ന കോഡ് കൂടുതൽ വിശദമായി

ചിത്രം സൃഷ്ടിക്കുന്ന കോഡ് കൂടുതൽ വിശദമായി നോക്കാം:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, ചിത്രം സൃഷ്ടിക്കാൻ ഉപയോഗിക്കുന്ന ടെക്സ്റ്റ് പ്രോംപ്റ്റാണ്. ഈ ഉദാഹരണത്തിൽ, "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils" എന്ന പ്രോംപ്റ്റ് ഉപയോഗിക്കുന്നു.
- **size**, സൃഷ്ടിക്കുന്ന ചിത്രത്തിന്റെ വലിപ്പമാണ്. ഇവിടെ 1024x1024 പിക്‌സലുകൾ ഉള്ള ചിത്രം സൃഷ്ടിക്കുന്നു.
- **n**, സൃഷ്ടിക്കുന്ന ചിത്രങ്ങളുടെ എണ്ണം. ഇവിടെ രണ്ട് ചിത്രങ്ങൾ സൃഷ്ടിക്കുന്നു.
- **temperature**, ജനറേറ്റീവ് AI മോഡലിന്റെ ഔട്ട്പുട്ടിന്റെ അനിശ്ചിതത്വം നിയന്ത്രിക്കുന്ന പാരാമീറ്ററാണ്. 0 മുതൽ 1 വരെ മൂല്യമുള്ളതാണ്, 0 ആണെങ്കിൽ ഔട്ട്പുട്ട് നിർവചിതമാണ്, 1 ആണെങ്കിൽ ഔട്ട്പുട്ട് യാദൃച്ഛികമാണ്. ഡിഫോൾട്ട് മൂല്യം 0.7 ആണ്.

ഇമേജുകളുമായി ചെയ്യാവുന്ന കൂടുതൽ കാര്യങ്ങൾ അടുത്ത ഭാഗത്ത് ചർച്ച ചെയ്യും.

## ഇമേജ് ജനറേഷന്റെ അധിക കഴിവുകൾ

Python-ൽ കുറച്ച് വരികളിൽ ചിത്രങ്ങൾ സൃഷ്ടിക്കാൻ കഴിഞ്ഞു. എന്നാൽ, ഇമേജുകളുമായി ചെയ്യാവുന്ന കൂടുതൽ കാര്യങ്ങൾ ഉണ്ട്.

നിങ്ങൾക്ക് താഴെ പറയുന്ന കാര്യങ്ങളും ചെയ്യാം:

- **എഡിറ്റുകൾ നടത്തുക**. നിലവിലുള്ള ഒരു ചിത്രത്തിന് മാസ്കും പ്രോംപ്റ്റും നൽകി ചിത്രം മാറ്റാം. ഉദാഹരണത്തിന്, ഒരു ചിത്രത്തിന്റെ ഒരു ഭാഗത്ത് എന്തെങ്കിലും ചേർക്കാം. നമ്മുടെ ബണ്ണി ചിത്രത്തിൽ, ബണ്ണിക്ക് ടോപ്പി ചേർക്കാം. അതിന് ചിത്രം, മാസ്ക് (മാറ്റം വരുത്തേണ്ട ഭാഗം തിരിച്ചറിയുന്ന) കൂടാതെ എന്ത് ചെയ്യണമെന്ന് പറയുന്ന ടെക്സ്റ്റ് പ്രോംപ്റ്റ് നൽകണം.  
> ശ്രദ്ധിക്കുക: DALL-E 3-ൽ ഇത് പിന്തുണയ്ക്കുന്നില്ല.

ഇവിടെ GPT Image ഉപയോഗിച്ചുള്ള ഉദാഹരണം:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  അടിസ്ഥാന ചിത്രം ലൗഞ്ചും പൂലും മാത്രമാണ് ഉൾക്കൊള്ളുന്നത്, എന്നാൽ അന്തിമ ചിത്രത്തിൽ ഫ്ലാമിംഗോ ഉണ്ടാകും:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/ml/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/ml/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/ml/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **വിവിധത്വങ്ങൾ സൃഷ്ടിക്കുക**. നിലവിലുള്ള ഒരു ചിത്രം എടുത്ത് അതിന്റെ വ്യത്യസ്ത പതിപ്പുകൾ സൃഷ്ടിക്കാൻ ആവശ്യപ്പെടാം. വ്യത്യസ്തത സൃഷ്ടിക്കാൻ, ചിത്രം, ടെക്സ്റ്റ് പ്രോംപ്റ്റ് എന്നിവ നൽകുകയും താഴെ കാണുന്ന കോഡ് ഉപയോഗിക്കുകയും ചെയ്യാം:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > ശ്രദ്ധിക്കുക, ഇത് OpenAI-യിൽ മാത്രമേ പിന്തുണയ്ക്കപ്പെടൂ.

## താപനില (Temperature)

താപനില ഒരു ജനറേറ്റീവ് AI മോഡലിന്റെ ഔട്ട്പുട്ടിന്റെ അനിശ്ചിതത്വം നിയന്ത്രിക്കുന്ന പാരാമീറ്ററാണ്. 0 മുതൽ 1 വരെ മൂല്യമുള്ളതാണ്, 0 ആണെങ്കിൽ ഔട്ട്പുട്ട് നിർവചിതമാണ്, 1 ആണെങ്കിൽ യാദൃച്ഛികമാണ്. ഡിഫോൾട്ട് മൂല്യം 0.7 ആണ്.

താപനില എങ്ങനെ പ്രവർത്തിക്കുന്നുവെന്ന് കാണാൻ, ഈ പ്രോംപ്റ്റ് രണ്ട് തവണ ഓടിക്കാം:

> പ്രോംപ്റ്റ്: "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![Bunny on a horse holding a lollipop, version 1](../../../translated_images/ml/v1-generated-image.a295cfcffa3c13c2.webp)

ഇപ്പോൾ ആ പ്രോംപ്റ്റ് വീണ്ടും ഓടിച്ച് ഒരേ ചിത്രം രണ്ടുതവണ ഉണ്ടാകില്ലെന്ന് കാണാം:

![Generated image of bunny on horse](../../../translated_images/ml/v2-generated-image.33f55a3714efe61d.webp)

കാണുന്നത് പോലെ, ചിത്രങ്ങൾ സമാനമാണ്, എന്നാൽ ഒരുപോലെയല്ല. താപനില മൂല്യം 0.1 ആക്കി മാറ്റി നോക്കാം:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # നിങ്ങളുടെ പ്രോംപ്റ്റ് ടെക്സ്റ്റ് ഇവിടെ നൽകുക
        size='1024x1024',
        n=2
    )
```

### താപനില മാറ്റുന്നു

അതിനാൽ, പ്രതികരണം കൂടുതൽ നിർവചിതമാക്കാൻ ശ്രമിക്കാം. ആദ്യ രണ്ട് ചിത്രങ്ങളിൽ ഒന്നിൽ ബണ്ണി ഉണ്ടായിരുന്നു, മറ്റൊന്നിൽ കുതിര, അതിനാൽ ചിത്രങ്ങൾ വളരെ വ്യത്യസ്തമാണ്.

അതിനാൽ, കോഡ് മാറ്റി താപനില 0 ആക്കി സജ്ജമാക്കാം:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # നിങ്ങളുടെ പ്രോംപ്റ്റ് ടെക്സ്റ്റ് ഇവിടെ നൽകുക
        size='1024x1024',
        n=2,
        temperature=0
    )
```

ഇപ്പോൾ ഈ കോഡ് ഓടിച്ചാൽ, ഈ രണ്ട് ചിത്രങ്ങൾ ലഭിക്കും:

- ![Temperature 0, v1](../../../translated_images/ml/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![Temperature 0 , v2](../../../translated_images/ml/v2-temp-generated-image.871d0c920dbfb0f1.webp)

ഇവിടെ ചിത്രങ്ങൾ പരസ്പരം കൂടുതൽ സമാനമാണെന്ന് വ്യക്തമായി കാണാം.

## മെടാപ്രോംപ്റ്റുകൾ ഉപയോഗിച്ച് ആപ്ലിക്കേഷനു പരിധികൾ നിർവചിക്കുന്നത് എങ്ങനെ

നമ്മുടെ ഡെമോയിൽ, നാം ഇതിനകം ക്ലയന്റുകൾക്കായി ചിത്രങ്ങൾ സൃഷ്ടിക്കാം. എന്നാൽ, ആപ്ലിക്കേഷനു ചില പരിധികൾ സൃഷ്ടിക്കേണ്ടതുണ്ട്.

ഉദാഹരണത്തിന്, ജോലി സ്ഥലത്തിന് അനുയോജ്യമല്ലാത്ത, കുട്ടികൾക്കു അനുയോജ്യമല്ലാത്ത ചിത്രങ്ങൾ സൃഷ്ടിക്കരുത്.

ഇത് _മെടാപ്രോംപ്റ്റുകൾ_ ഉപയോഗിച്ച് ചെയ്യാം. മെടാപ്രോംപ്റ്റുകൾ ജനറേറ്റീവ് AI മോഡലിന്റെ ഔട്ട്പുട്ട് നിയന്ത്രിക്കാൻ ഉപയോഗിക്കുന്ന ടെക്സ്റ്റ് പ്രോംപ്റ്റുകളാണ്. ഉദാഹരണത്തിന്, മെടാപ്രോംപ്റ്റുകൾ ഉപയോഗിച്ച് ഔട്ട്പുട്ട് നിയന്ത്രിച്ച് സൃഷ്ടിച്ച ചിത്രങ്ങൾ ജോലി സ്ഥലത്തിന് അനുയോജ്യമാണോ, കുട്ടികൾക്കു അനുയോജ്യമാണോ എന്ന് ഉറപ്പാക്കാം.

### ഇത് എങ്ങനെ പ്രവർത്തിക്കുന്നു?

മെടാപ്രോംപ്റ്റുകൾ എങ്ങനെ പ്രവർത്തിക്കുന്നു?

മെടാപ്രോംപ്റ്റുകൾ ടെക്സ്റ്റ് പ്രോംപ്റ്റിന് മുമ്പ് വയ്ക്കുന്ന ടെക്സ്റ്റ് പ്രോംപ്റ്റുകളാണ്, മോഡലിന്റെ ഔട്ട്പുട്ട് നിയന്ത്രിക്കാൻ ഉപയോഗിക്കുന്നു, ആപ്ലിക്കേഷനുകളിൽ ഉൾപ്പെടുത്തിയിട്ടുണ്ട്. പ്രോംപ്റ്റ് ഇൻപുട്ടും മെടാപ്രോംപ്റ്റ് ഇൻപുട്ടും ഒരേ ടെക്സ്റ്റ് പ്രോംപ്റ്റിൽ ഉൾക്കൊള്ളുന്നു.

ഒരു മെടാപ്രോംപ്റ്റിന്റെ ഉദാഹരണം:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

ഇപ്പോൾ, നമ്മുടെ ഡെമോയിൽ മെടാപ്രോംപ്റ്റുകൾ എങ്ങനെ ഉപയോഗിക്കാമെന്ന് നോക്കാം.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt =f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"{meta_prompt}
Create an image of a bunny on a horse, holding a lollipop"

# TODO ചിത്രം സൃഷ്ടിക്കാൻ അഭ്യർത്ഥന ചേർക്കുക
```

മുകളിൽ കാണുന്ന പ്രോംപ്റ്റിൽ, സൃഷ്ടിക്കുന്ന എല്ലാ ചിത്രങ്ങളും മെടാപ്രോംപ്റ്റ് പരിഗണിച്ചാണ്.

## അസൈൻമെന്റ് - വിദ്യാർത്ഥികളെ സജ്ജമാക്കാം

ഈ പാഠത്തിന്റെ തുടക്കത്തിൽ Edu4All പരിചയപ്പെടുത്തി. ഇപ്പോൾ വിദ്യാർത്ഥികൾക്ക് അവരുടെ അസൈൻമെന്റുകൾക്കായി ചിത്രങ്ങൾ സൃഷ്ടിക്കാൻ സാധിക്കണം.

വിദ്യാർത്ഥികൾ അവരുടെ അസൈൻമെന്റുകൾക്കായി സ്മാരകങ്ങൾ ഉൾക്കൊള്ളുന്ന ചിത്രങ്ങൾ സൃഷ്ടിക്കും, സ്മാരകങ്ങൾ എന്തായിരിക്കും എന്നത് വിദ്യാർത്ഥികളുടെ ഇഷ്ടാനുസരണം. ഈ സ്മാരകങ്ങളെ വ്യത്യസ്ത സാഹചര്യങ്ങളിൽ സ്ഥാപിക്കാൻ വിദ്യാർത്ഥികൾക്ക് സൃഷ്ടിപരമായ സ്വാതന്ത്ര്യം നൽകുന്നു.

## പരിഹാരം

ഇവിടെ ഒരു സാധ്യതയുള്ള പരിഹാരമാണ്:
```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# dotenv ഇറക്കുമതി ചെയ്യുക
dotenv.load_dotenv()

# പരിസ്ഥിതി വ്യത്യാസങ്ങളിൽ നിന്ന് എൻഡ്‌പോയിന്റും കീയും നേടുക
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-02-01"
  )


disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"""{meta_prompt}
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
""""

try:
    # ഇമേജ് ജനറേഷൻ API ഉപയോഗിച്ച് ഒരു ചിത്രം സൃഷ്ടിക്കുക
    generation_response = client.images.generate(
        prompt=prompt,    # നിങ്ങളുടെ പ്രോംപ്റ്റ് ടെക്സ്റ്റ് ഇവിടെ നൽകുക
        size='1024x1024',
        n=1,
    )
    # സൂക്ഷിച്ചിരിക്കുന്ന ചിത്രത്തിനുള്ള ഡയറക്ടറി സജ്ജമാക്കുക
    image_dir = os.path.join(os.curdir, 'images')

    # ഡയറക്ടറി ഇല്ലെങ്കിൽ, അത് സൃഷ്ടിക്കുക
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # ചിത്രം പാത ആരംഭിക്കുക (ഫയൽടൈപ്പ് png ആകണം എന്ന് ശ്രദ്ധിക്കുക)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # സൃഷ്ടിച്ച ചിത്രം പുനഃപ്രാപ്തമാക്കുക
    image_url = generation_response.data[0].url  # പ്രതികരണത്തിൽ നിന്ന് ചിത്രം URL എടുക്കുക
    generated_image = requests.get(image_url).content  # ചിത്രം ഡൗൺലോഡ് ചെയ്യുക
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # ഡിഫോൾട്ട് ഇമേജ് വ്യൂവറിൽ ചിത്രം പ്രദർശിപ്പിക്കുക
    image = Image.open(image_path)
    image.show()

# исключения പിടിക്കുക
except openai.BadRequestError as err:
    print(err)
```

## മികച്ച ജോലി! നിങ്ങളുടെ പഠനം തുടരുക

ഈ പാഠം പൂർത്തിയാക്കിയ ശേഷം, നിങ്ങളുടെ ജനറേറ്റീവ് AI അറിവ് മെച്ചപ്പെടുത്താൻ ഞങ്ങളുടെ [ജനറേറ്റീവ് AI പഠന ശേഖരം](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) പരിശോധിക്കുക!

നാം എങ്ങനെ [ലോ-കോഡ് ഉപയോഗിച്ച് AI ആപ്ലിക്കേഷനുകൾ നിർമ്മിക്കാമെന്ന്](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) നോക്കാൻ പാഠം 10 ലേക്ക് പോകൂ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാപത്രം**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, യന്ത്രം ചെയ്ത വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കപ്പെടണം. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->