# ഇമേജ് ജനറേഷൻ അപ്ലിക്കേഷനുകൾ നിർമ്മിക്കുക

[![ഇമേജ് ജനറേഷൻ അപ്ലിക്കേഷനുകൾ നിർമ്മിക്കുക](../../../translated_images/ml/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLMകൾ ടെക്സ്‌റ്റ് ജനറേഷനിലും മാത്രമല്ല. ടെക്സ്‌റ്റ് വിവരണങ്ങളിൽ നിന്നുമുള്ള ചിത്രങ്ങൾ സൃഷ്ടിക്കുന്നതും സാധ്യമാണ്. ഒരു മോഡാലിറ്റി ആയി ചിത്രങ്ങൾ പല മേഖലകളിലും വളരെ പ്രയോജനകരമായിരിക്കാം, മെഡടെക്, ആർക്കിടെക്ചർ, ടൂറിസം, ഗെയിം ഡെവലപ്മെന്റ് മുതലായവയിൽ നിന്ന്. ഈ അദ്ധ്യായത്തിൽ, ഏറ്റവും ജനപ്രിയമായ രണ്ട് ഇമേജ് ജനറേഷൻ മോഡലുകൾ, DALL-E ഉം Midjourney ഉം പരിശോധിക്കുന്നു.

## പരിചയം

ഈ പാഠത്തിൽ നാം ഉൾക്കൊള്ളുന്നതിൽ:

- ഇമേജ് ജനറേഷൻ എന്താണെന്ന്, അതിന്റെ പ്രയോജനം എന്തെന്ന്.
- DALL-E ഉം Midjourney ഉം എന്താണെന്ന്, എങ്ങനെ പ്രവർത്തിക്കുന്നു എന്ന്.
- ഒരു ഇമേജ് ജനറേഷൻ അപ്ലിക്കേഷൻ എങ്ങനെ നിർമ്മിക്കും.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠം പൂർത്തിയാക്കിയതിനു ശേഷം, നിങ്ങൾക്ക് സാധിക്കുമെന്ന്:

- ഒരു ഇമേജ് ജനറേഷൻ അപ്ലിക്കേഷൻ നിർമ്മിക്കാൻ.
- മെടാ പ്രംപ്റ്റുകളിലൂടെ നിങ്ങളുടെ അപ്ലിക്കേഷനുകാർ‍ക്ക് പരിധികൾ നിർവചിക്കാൻ.
- DALL-E ഉം Midjourney ഉം ഉപയോഗിച്ച് പ്രവർത്തിക്കാൻ.

## ഇമേജ് ജനറേഷൻ അപ്ലിക്കേഷൻ എങ്ങനെ നിർമ്മിക്കണം?

ഇമേജ് ജനറേഷൻ അപ്ലിക്കേഷനുകൾ ജനറേറ്റീവ് AI യുടെ ശേഷി പരീക്ഷിക്കാൻ മികച്ച മാർഗമാണ്. അവ ഉപയോഗിക്കാം, ഉദാഹരണം കൊണ്ട്:

- **ഇമേജ് എഡിറ്റിങ്ങും സിന്തസിസും**. വ്യത്യസ്ത ഉപയോക്തൃ ഉപയോഗങ്ങൾക്ക് ചിത്രങ്ങൾ സൃഷ്ടിക്കാം, എഡിറ്റിംഗ്, സിന്തസിസു തുടങ്ങിയവ.

- **വ്യത്യസ്ത വ്യവസായങ്ങൾക്ക്**. മെഡടെക്, ടൂറിസം, ഗെയിം ഡെവലപ്മെന്റ് തുടങ്ങിയ വ്യവസായങ്ങൾക്ക് ചിത്രങ്ങൾ സൃഷ്ടിക്കാൻ.

## സംഭവകഥ: Edu4All

ഈ പാഠത്തിന്റെ ഭാഗമായി, Edu4All എന്ന സ്റ്റാർട്ടപ്പുമായി തുടർന്നു ജോലി ചെയ്യും. വിദ്യാർത്ഥികൾ അവരുടെ അസൈൻമെന്റുകൾക്കായി ചിത്രങ്ങൾ സൃഷ്ടിക്കും. ചിത്രങ്ങൾ എന്താണെന്നത് വിദ്യാർത്ഥികളുടെ deciding ആണ്, പക്ഷേ അത് അവരുടെ സ്വന്തം കഥക്കായോ പുതിയ കഥാപാത്രങ്ങൾ സൃഷ്ടിക്കാനോ ആശയങ്ങൾ ദൃശ്യവത്കരിക്കാൻ സഹായിക്കാനുള്ള ഇലസ്ട്രേഷനുകളായിരിക്കും.

ഉദാഹരണത്തിന്, Edu4All ന്റെ വിദ്യാർത്ഥികൾ ക്ലാസ്സിൽ സ്മാരകങ്ങളെക്കുറിച്ച് ജോലി ചെയ്യുമ്പോൾ സൃഷ്ടിക്കാവുന്ന ചിത്രങ്ങൾ:

![Edu4All സ്റ്റാർട്ടപ്പ്, സ്മാരകങ്ങളുടെ ക്ലാസ്, ഐഫൽ ടവർ](../../../translated_images/ml/startup.94d6b79cc4bb3f5a.webp)

ഇങ്ങനെ ഒരു പ്രംപ്റ്റ് ഉപയോഗിച്ച്

> "നടുവിൽ ഐഫൽ ടവറിനോട് കിച്ചുന്ന നായ"

## DALL-E ഉം Midjourney ഉം എന്താണ്?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) ഉം [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) ഉം ഏറ്റവും ജനപ്രിയമായ രണ്ട് ഇമേജ് ജനറേഷൻ മോഡലുകളാണ്, പ്രംപ്റ്റുകൾ ഉപയോഗിച്ച് ചിത്രങ്ങൾ സൃഷ്ടിക്കാൻ സാധിക്കുന്നു.

### DALL-E

DALL-E മുതൽക്കൂട്ടായുള്ള AI മോഡലാണ്, ടെക്സ്റ്റ് വിവരണങ്ങളിൽ നിന്നു് ചിത്രങ്ങൾ സൃഷ്ടിക്കുന്നു.

> [DALL-E CLIP ഉം Diffused Attention ഉം ചേർത്ത് നിർമ്മിച്ച മോഡലാണ്](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** എന്നത് ഒരു മോഡലാണ്, അത് ചിത്രങ്ങളിലും ടെക്സ്റ്റിലും നിന്നുള്ള ഡാറ്റയുടെ സംഖ്യാനുപാത രൂപമാണ്.

- **Diffused Attention** എന്നത് embeddings-ിൽ നിന്നും ചിത്രങ്ങൾ സൃഷ്ടിക്കുന്ന മോഡലാണ്. DALL-E, ചിത്രങ്ങളും ടെക്സ്റ്റും അടങ്ങിയ ഡാറ്റാസെറ്റിൽ പരിശീലിപ്പിക്കപ്പെട്ടതാണ്, ഇതു ടെക്സ്റ്റ് വിവരണങ്ങളിൽ നിന്നു് ചിത്രങ്ങൾ സൃഷ്ടിക്കാൻ സാധിക്കുന്നു. ഉദാഹരണത്തിന്, മുടിയുള്ള പൂച്ചയുടെ ചിത്രമോ മൊഹോക്ക് കൊണ്ട് നായയുടെ ചിത്രമോ സൃഷ്ടിക്കാം.

### Midjourney

Midjourney DALL-E പോലെയാണ് പ്രവർത്തിക്കുന്നത്, ടെക്സ്റ്റ് പ്രംപ്റ്റുകൾ കൊണ്ട് ചിത്രങ്ങൾ സൃഷ്ടിക്കുന്നു. Midjourney-യും "മുടിയുള്ള പൂച്ച" അല്ലെങ്കിൽ "മോഹോക്ക് ഉള്ള നായ" പോലുള്ള പ്രംപ്റ്റുകൾ ഉപയോഗിച്ച് ചിത്രങ്ങൾ സൃഷ്ടിക്കാം.

![Midjourney-ൽ സൃഷ്ടിച്ച മെക്കാനിക്കൽ പിജൻ](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_ചിത്രം വിഖ്യാതമായ മെക്കാനിക്കൽ പിജൻ, Midjourney-ൽ നിന്ന് സൃഷ്ടിച്ചത്_

## DALL-E ഉം Midjourney ഉം എങ്ങനെ പ്രവർത്തിക്കുന്നു

ആദ്യം, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E ഒരു Generative AI മോഡലാണ്, അത് ട്രാൻസ്ഫോർമർ ആർക്കിടെക്ചർ അടിസ്ഥാനമാക്കിയുള്ള _ഓട്ടോറഗ്രസീവ് ട്രാൻസ്ഫോർമർ_ ആണ്.

_ഓട്ടോറഗ്രസീവ് ട്രാൻസ്ഫോർമർ_ ഒരു മോഡൽ ടെക്സ്റ്റ് വിവരണങ്ങളിൽ നിന്നു് ചിത്രങ്ങൾ എങ്ങനെ സൃഷ്ടിക്കുമെന്ന് നിർവചിക്കുന്നു, ഇത് ഓരോ പിക്‌സലും ഒറ്റക്കൊടുക്കി സൃഷ്ടിച്ച്, സൃഷ്ടിച്ച പിക്‌സലുകൾ അടുത്ത പിക്‌സലിനെ സൃഷ്ടിക്കാൻ ഉപയോഗിക്കുന്നു. ന്യൂറൽ നെറ്റ്‌വർക്കിലെ പല പാളികളിലൂടെ കടന്നുപോകുന്നു, ചിത്രമാകുന്നത് വരെ.

ഈ പ്രക്രിയയിലൂടെ, DALL-E സൃഷ്ടിക്കുന്ന ചിത്രത്തിലെ ഘടകങ്ങൾ, വസ്തുക്കൾ, ലക്ഷണങ്ങൾ എന്നിവ നിയന്ത്രിക്കുന്നു. എന്നാൽ, DALL-E 2 ഉം 3 ഉം സൃഷ്ടിക്കപ്പെട്ട ചിത്രം കൂടുതൽ നിയന്ത്രിക്കുന്നു.

## നിങ്ങളുടെ ആദ്യ ഇമേജ് ജനറേഷൻ അപ്ലിക്കേഷൻ നിർമ്മിക്കുന്നത്

ഇമേജ് ജനറേഷൻ അപ്ലിക്കേഷൻ നിർമ്മിക്കാൻ എന്തൊക്കെയാണ് ആവശ്യമായത്? നിങ്ങൾക്ക് താഴെപ്പറയുന്ന ലൈബ്രറികൾ ആവശ്യമാണ്:

- **python-dotenv**: രഹസ്യങ്ങൾ _.env_ ഫയലിൽ സൂക്ഷിക്കാൻ അനുയോജ്യമായ ലൈബ്രറി.
- **openai**: OpenAI API യോട് അനുബന്ധിക്കാൻ ഉപയോഗിക്കുന്ന ലൈബ്രറി.
- **pillow**: പൈത്തണിൽ ചിത്രങ്ങളുമായി പ്രവർത്തിക്കാൻ.
- **requests**: HTTP അഭ്യർത്ഥനകൾ അയയ്ക്കാൻ.

## Azure OpenAI മോഡൽ സൃഷ്ടിക്കുകയും വിന്യസിക്കുകയും ചെയ്യുക

മൈക്രോസോഫ്റ്റ് ലേണിൽ [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) പേജിലെ നിർദ്ദേശങ്ങൾ പാലിച്ച്
ഒരു Azure OpenAI വനം (Resource)യും മോഡലും സൃഷ്ടിക്കുക. മോഡലായി **gpt-image-1** തിരഞ്ഞെടുക്കുക (നിലവിലെ തലമുറ Azure OpenAI ഇമേജ് മോഡൽ; DALL-E 3 പക്കേജ് ഹ്രസ്വകാലം ആവശ്യത്തിനു വഴി പുതിയ വിന്യസനങ്ങൾക്ക് ലഭ്യമല്ല).

## അപ്ലിക്കേഷൻ സൃഷ്ടിക്കുക

1. താഴെപ്പറയുന്ന ഉള്ളടക്കത്തോടെ _.env_ എന്ന ഫയൽ സൃഷ്ടിക്കുക:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   ഈ വിവരങ്ങൾ Azure OpenAI Foundry പോർട്ടലിലെ "Deployments" വിഭാഗത്തിൽ നിങ്ങളുടെ വനം(Resource)ക്കായി കണ്ടെത്തുക.

1. മുകളില് പറഞ്ഞ ലൈബ്രറികൾ _requirements.txt_ എന്ന ഫയലിലായി ശേഖരിക്കുക:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. തുടർന്ന്, ഒരു വിർച്വൽ എന്വയറൺമെന്റ് സൃഷ്ടിച്ച് ലൈബ്രറികൾ ഇൻസ്റ്റാൾ ചെയ്യുക:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows-ന് താഴെ കൊടുക്കുന്ന കമാൻഡുകൾ ഉപയോഗിച്ച് വിർച്വൽ എന്വയർൺമെന്റ് സൃഷ്ടിക്കുകയും ആക്ടീവേറ്റ് ചെയ്യുകയും ചെയ്യാം:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ എന്നു പേരിട്ട ഫയലിൽ താഴെ കൊടുത്തിരിക്കുന്ന കോഡ് ചേർക്കുക:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # dotenv ഇംപോർട് ചെയ്യുക
    dotenv.load_dotenv()
    
    # Azure OpenAI സർവീസ് ക്ലയന്റ് കോൺഫിഗർ ചെയ്യുക
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # ഇമേജ് ജനറേഷൻ API ഉപയോഗിച്ച് ഒരു ചിത്രം സൃഷ്ടിക്കുക
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # സൂക്ഷിച്ചിരിക്കുന്ന ചിത്രത്തിനുള്ള ഡയറക്ടറി ക്രമീകരിക്കുക
        image_dir = os.path.join(os.curdir, 'images')

        # ഡയറക്ടറി ഇല്ലെങ്കിൽ, അത് സൃഷ്ടിക്കുക
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # ചിത്രം പാത ഇൻഷിയലൈസ് ചെയ്യുക (ഫയൽടൈപ്പ് png ആയിരിക്കണം എന്ന് ശ്രദ്ധിക്കുക)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # ജനറേറ്റ് ചെയ്ത ചിത്രം പ്രാപ്തമാക്കുക
        image_url = generation_response.data[0].url  # പ്രതികരണത്തിൽ നിന്ന് ചിത്രം URL എടുക്കുക
        generated_image = requests.get(image_url).content  # ചിത്രം ഡൗൺലോഡ് ചെയ്യുക
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # സDefault image viewerൽ ചിത്രം പ്രദർശിപ്പിക്കുക
        image = Image.open(image_path)
        image.show()

    # ചതവുകൾ പിടിക്കുക
    except openai.BadRequestError as err:
        print(err)
   ```

ഈ കോഡ് വിശദീകരിക്കാം:

- ആദ്യം, ആവശ്യമായ ലൈബ്രറികൾ ഇറക്കുമതി ചെയ്യുന്നു, ഇതിൽ OpenAI, dotenv, requests, Pillow എന്നിവ ഉൾപ്പെടുന്നു.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- തുടർന്ന്, _.env_ ഫയലിൽ നിന്നും പരിസരവരങ്ങൾ ലോഡ് ചെയ്യുന്നു.

  ```python
  # ഡോട്ട് എൻവി ഇംപോർട്ട് ചെയ്യുക
  dotenv.load_dotenv()
  ```

- അതിന് ശേഷം, Azure OpenAI സേവന ക്ലയന്റ് കോൺഫിഗർ ചെയ്യുന്നു

  ```python
  # എൻവയോൺമെന്റ് മാറ്റികളിൽ നിന്ന് എൻഡ്പോയിന്റും കീയും നേടുക
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- തുടർന്ന്, ചിത്രമു് സൃഷ്ടിക്കുന്നു:

  ```python
  # ഇമേജ് ജനറേഷൻ API ഉപയോഗിച്ച് ഒരു ചിത്രം സൃഷ്ടിക്കുക
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  മുകളിൽ നൽകി കോഡ് ഒരു JSON αντικείμενο ആയി പ്രതികരിക്കുന്നു, സൃഷ്ടിച്ച ചിത്രത്തിന്റെ URL അടങ്ങിയതാണ്. ഈ URL ഉപയോഗിച്ച് ചിത്രം ഡൗൺലോഡ് ചെയ്ത് ഫയലായി സേവ് ചെയ്യാം.

- അവസാനം, ചിത്രം തുറന്ന് സാധാരണ ഇമേജ് വ്യുവർ ഉപയോഗിച്ച് പ്രദർശിപ്പിക്കുന്നു:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### ചിത്രമുണ്ടാക്കുന്ന കോഡ് വിശദമായി

ചിത്രമുണ്ടാക്കുന്ന കോഡിനെ നോക്കാം കൂടുതൽ വിശദമായി:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**: ചിത്രം സൃഷ്ടിക്കാൻ ഉപയോഗിക്കുന്ന ടെക്സ്റ്റ് പ്രംപ്റ്റ്, ഇവിടെ "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils" ആണ് ഉപയോഗിക്കുന്നത്.
- **size**: സൃഷ്ടിക്കുന്ന ചിത്രത്തിന്റെ വലുപ്പം. ഇവിടെ 1024x1024 പിക്‌സൽ ആണ്.
- **n**: എത്ര ചിത്രം സൃഷ്ടിക്കണം, ഇവിടെ രണ്ട് ചിത്രങ്ങൾ സൃഷ്ടിക്കുന്നു.
- **temperature**: ജനറേറ്റീവ് AI മോഡലിന്റെ ഔട്ട്പുട്ടിന്റെ randomness നിയന്ത്രിക്കുന്ന പാരാമീറ്റർ. 0 മുതൽ 1 വരെ മൂല്യമാണ്, 0 ആണെങ്കിൽ ഔട്ട്പുട്ട് നിർണ്ണായകമാണ്, 1 ആണെങ്കിൽ കൂടുതൽ യാദൃശ്ചികമാണ്. ഡിഫാൾട്ട് 0.7 ആണ്.

ചിത്രങ്ങളുമായി ചെയ്യാൻ കഴിയുന്ന മറ്റു കാര്യങ്ങൾ അടുത്ത ഭാഗത്ത് പറയപ്പെടും.

## ചിത്രമുണ്ടാക്കാനുള്ള അധിക ശേഷികൾ

നാം പൈത്തൺ കോഡിന്റെ കുറച്ച് വരികളിലായി ഒരു ചിത്രം എങ്ങനെ സൃഷ്ടിക്കാമെന്ന് പഠിച്ചു. എന്നാൽ ചിത്രങ്ങളുമായി ചെയ്യാൻ കഴിയുന്ന മറ്റു കാര്യങ്ങളും ഉണ്ട്.

നിങ്ങൾക്ക് താഴെുപറയുന്ന പ്രവർത്തനങ്ങളും ചെയ്യാമാവും:

- **എഡിറ്റുകൾ നടപ്പിലാക്കുക**. നിലവിലുള്ള ഒരു ചിത്രത്തിന് മാസ്‌കും പ്രംപ്റ്റും കൊടുത്താലും ചിത്രം മാറ്റാം. ഉദാഹരണത്തിന്, ബണ്ണിക്കു് ഒരു കഴുത്തു ടോപ്പ് ചേർക്കാം. അതിനു് ചിത്രം, മാസ്‌ക് (മാറ്റം വരുത്തേണ്ട ഭാഗം വ്യക്തമാക്കുന്ന) കൂടാതെ ടെക്സ്റ്റ് പ്രംപ്റ്റ് നൽകണം.
> ശ്രദ്ധിക്കുക: ഇത് DALL-E 3 ൽ പിന്തുണയ്ക്കുന്നില്ല.
 
താഴെ GPT Image ഉപയോഗിച്ചുകൊണ്ടുള്ള ഒരു ഉദാഹരണം:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  അടിസ്ഥാന ചിത്രം മാത്രമേ ഒരു പാർട്ടി ഹാൾ ഉൾക്കൊള്ളൂ, എന്നാൽ അവസാന ചിത്രം ഒരു ഫ്ലാമിംഗോ അടങ്ങിയിരിക്കും:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/ml/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/ml/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/ml/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **വിവിധത്വങ്ങൾ സൃഷ്ടിക്കുക**. നിലവിലുള്ള ഒരു ചിത്രമെടുത്ത് അതിന്റെ എളുപ്പത്തിലുള്ള വേർഷനുകൾ സൃഷ്ടിക്കാൻ, ചിത്രം, ടെക്സ്റ്റ് പ്രംപ്റ്റ് നൽകുകയും, ഇങ്ങനെ കോഡ് ഉപയോഗിക്കുക:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > ശ്രദ്ധിക്കുക, ഇത് OpenAI ന്റെ DALL-E 2 മോഡലിൽ മാത്രം പിന്തുണയുള്ളതാണ്, gpt-image-1 മോഡലിൽ ഇല്ല.

## ടെംപറേച്ചർ

ജനറേറ്റീവ് AI മോഡലിന്റെ ഔട്ട്പുട്ടിലെ randomness നിയന്ത്രിക്കുന്ന പാരാമീറ്റർ ആണ് temperature. 0 മുതൽ 1 വരെയുള്ള മൂല്യമാണിത്, 0 ആണെങ്കിൽ deterministic output ഉം 1 ആണെങ്കിൽ randomness ഉം.

താഴെ ഒരു ഉദാഹരണമാണ് temperature എങ്ങനെ പ്രവർത്തിക്കുന്നത് കാണിക്കുന്നതില്‍, ഈ പ്രംപ്റ്റ് രണ്ടുപാട് ഓടിക്കുന്നുണ്ട്:

> Prompt : "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![ലോളിപ്പോപ്പ് പിടിച്ച ബണ്ണിയുടെ ചിത്രം, പതിപ്പ് 1](../../../translated_images/ml/v1-generated-image.a295cfcffa3c13c2.webp)

ഇനി അതേ പ്രംപ്റ്റ് രണ്ടാമത് ഓടിച്ചപ്പോൾ ഉണ്ടാകുന്ന ചിത്രം നോക്കാം:

![ബണ്ണി കുതിരയിൽ, സൃഷ്ടിച്ച ചിത്രം](../../../translated_images/ml/v2-generated-image.33f55a3714efe61d.webp)

കാണുന്നത് പോലെ, രണ്ടു ചിത്രങ്ങളും സമാനമാണെങ്കിലും സമാനമല്ല. temperature മൂല്യം 0.1 ആക്കി മാറ്റിയാൽ എങ്ങനെ സംഭവിക്കും എന്ന് നോക്കാം:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # നിങ്ങളുടെ പ്രോംപ്റ്റ് ടെക്‌സ്‌റ്റ് ഇവിടെ നൽകുക
        size='1024x1024',
        n=2
    )
```

### temperature മാറ്റുന്നു

ആ വിശദീകരണം, ഏറ്റവും ആദ്യ ചിത്രത്തിൽ ഒരു ബണ്ണി ഉണ്ട്, രണ്ടാം ചിത്രത്തിൽ ഒരു കുതിര ഉണ്ട്, അതിനാൽ ചിത്രങ്ങൾ വളരെ വ്യത്യാസപ്പെട്ടിരിക്കുന്നു.

അതിനാൽ temperature 0 ആക്കി മാറ്റാം, ഇങ്ങനെ:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # നിങ്ങളുടെ പ്രോംപ്റ്റ് എഴുത്ത് ഇവിടെ നൽകുക
        size='1024x1024',
        n=2,
        temperature=0
    )
```

ഇനി ഇത് ഓടിച്ചപ്പോൾ ഈ ഇരു ചിത്രങ്ങൾ ലഭിക്കും:

- ![temperature 0, പതിപ്പ് 1](../../../translated_images/ml/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![temperature 0, പതിപ്പ് 2](../../../translated_images/ml/v2-temp-generated-image.871d0c920dbfb0f1.webp)

ഇവിടെ ചിത്രങ്ങൾ പരസ്പരം കൂടുതൽ സമാനമാണ് എന്ന് വ്യക്തമാണ്.

## മെടാപ്രംപ്റ്റുകളിലൂടെ നിങ്ങളുടെ അപ്ലിക്കേഷന്ക്ക് പരിധികൾ നിർവചിക്കാനുള്ള വിധം

നമ്മുടെ ഡെമോയിൽ, നാം ഇതിനകം തന്നെ ക്ലയന്റ്സിനായി ചിത്രങ്ങൾ സൃഷടിച്ചുകൊണ്ടിരിക്കു. എന്നാൽ, അപ്ലിക്കേഷന്ക്ക് ചില പരിധികൾ രൂപപ്പെടുത്തേണ്ടതുണ്ട്.

ഉദാഹരണത്തിന്, ജോലി സ്ഥലത്ത് അനുയോജ്യമല്ലാത്ത അശ്ലീലം ചിത്രങ്ങൾ സൃഷ്ടിക്കരുത്, അല്ലെങ്കിൽ കുട്ടികള്ക്ക് അനുയോജ്യമല്ലാത്ത ചിത്രങ്ങൾ വരുത്തരുത്.

ഇത് _മെടാപ്രംപ്റ്റുകൾ_ ഉപയോഗിച്ച് സാധ്യമാക്കാം. മെടാപ്രംപ്റ്റുകൾ ജനറേറ്റീവ് AI മോഡലിന്റെ ഔട്ട്പുട്ട് നിയന്ത്രിക്കാൻ ഉപയോഗിക്കുന്ന ടെക്സ്റ്റ് പ്രംപ്റ്റുകളാണ്. ഉദാഹരണത്തിന്, ഇത് ഉപയോഗിച്ച് പ്രസ്താവനകളുടെ നിയന്ത്രണം ഉറപ്പാക്കാം, ചിത്രങ്ങൾ ജോലി സ്ഥലത്ത് സുരക്ഷിതവുമായിരിക്കുമെന്നും കുട്ടികൾക്കാവശ്യമായവിധേയമായിരിക്കുമെന്നും.

### ഇത് എങ്ങനെ പ്രവർത്തിക്കുന്നു?

മെടാപ്രംപ്റ്റുകൾ എങ്ങനെ പ്രവർത്തിക്കുന്നു?

മെടാപ്രംപ്റ്റുകൾ, ടെക്സ്റ്റ് പ്രംപ്റ്റിനുമുന്‍പായി വരുന്ന ടെക്സ്റ്റ് പ്രംപ്റ്റുകളാണ്, ഇത് മോഡലിന്റെ ഔട്ട്പുട്ട് നിയന്ത്രിക്കാൻ ഉപയോഗിക്കുന്നു, ആ പ്രംപ്റ്റുകളും ആധാരകരമായ പ്രംപ്റ്റും ഒരുമിച്ച് അപ്ലിക്കേഷനുകളിൽ ഉൾപ്പെടുത്തിയിരിക്കുന്നു. പ്രംപ്റ്റ് ഇൻപുട്ടും മെടാപ്രംപ്റ്റ് ഇൻപുട്ടും ഒരൊറ്റ ടെക്സ്റ്റ് പ്രംപ്റ്റായി ഉൾപ്പെടുത്തുന്നു.

മെടാപ്രംപ്റ്റിന്റെ ഒരു ഉദാഹരണം താഴെപ്പറയുന്നതുപോലെയാണ്:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

ഇനി, നമ്മുടെ ഡെമോയിൽ മെടാപ്രംപ്റ്റുകൾ എങ്ങനെ ഉപയോഗിക്കുന്നു എന്നു നോക്കാം.

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

# TODO ചിത്രം സൃഷ്ടിക്കുന്നതിനുള്ള അഭ്യർത്ഥന ചേർക്കുക
```

മുകളിൽ കൊടുത്ത പ്രംപ്റ്റിൽ, സൃഷ്ടിക്കപ്പെടുന്ന എല്ലാ ചിത്രങ്ങളും മെടാപ്രംപ്റ്റിനെ പ്രാധാന്യം നൽകി പരിശോധിക്കുന്നു.

## അസൈന്മെന്റ് - വിദ്യാർത്ഥികളെ സജ്ജമാക്കാം

ഈ പാഠത്തിന്റെ ആദിയിൽ പരിചയപ്പെടുത്തി തന്ന Edu4All ന്റെ വിദ്യാർത്ഥികളെ അവരുടെ അസൈൻമെന്റുകൾക്കായി ചിത്രങ്ങൾ സൃഷ്ടിക്കാൻ സാധ്യമായിരിക്കും.


വിദ്യാർത്ഥികൾ അവരുടെ അസൈൻമെന്റുകൾക്കായി സ്മാരകങ്ങളുള്ള ചിത്രങ്ങൾ സൃഷ്ടിക്കും, ആ സ്മാരകങ്ങൾ എന്തൊക്കെയാണെന്ന് തീരുമാനിക്കുന്നത് വിദ്യാർത്ഥികളെയാണ്. ഈ പ്രവൃത്തിയിൽ ഈ സ്മാരകങ്ങളെ വ്യത്യസ്ത സാഹചര്യങ്ങളിൽ സ്ഥാപിക്കാൻ അവരുടെ സൃഷ്ടിപരമായ കഴിവ് ഉപയോഗിക്കാൻ വിദ്യാർത്ഥികളെ അഭ്യർത്ഥിക്കുന്നു.

## പരിഹാരം

ഇതാ ഒരു സാധ്യതാ പരിഹാരം:

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# dotenv ഇറക്കുമതി ചെയ്യുക
dotenv.load_dotenv()

# പരിസ്ഥിതി ചാരത്തിലുള്ള എൻഡ്‌പോയിന്റ്, കീ ലഭിക്കുക
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-10-21"
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
"""

try:
    # ഇമേജ് ജനറേഷൻ API ഉപയോഗിച്ച് ചിത്രം സൃഷ്ടിക്കുക
    generation_response = client.images.generate(
        prompt=prompt,    # നിങ്ങളുടെ പ്രമ്പ്റ്റ് വാചകം ഇവിടെ നൽകുക
        size='1024x1024',
        n=1,
    )
    # സൂക്ഷിച്ചിരിക്കുന്ന ചിത്രത്തിനായി ഡയറക്ടറി സജ്ജമാക്കുക
    image_dir = os.path.join(os.curdir, 'images')

    # ഡയറക്ടറി ഇല്ലെങ്കിൽ, അത് സൃഷ്ടിക്കുക
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # ചിത്രം പാത്ത് ആരംഭിക്കുക (ഫയൽ ടൈപ്പ് png ആണെന്ന് ശ്രദ്ധിക്കുക)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # സൃഷ്ടിച്ച ചിത്രം ലഭിക്കുക
    image_url = generation_response.data[0].url  # പ്രതികരണത്തിൽനിന്ന് ചിത്രം URL എടുക്കുക
    generated_image = requests.get(image_url).content  # ചിത്രം ഡൗൺലോഡ് ചെയ്യുക
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # ഡിഫോൾട്ട് ചിത്രം കണക്കിലെടുക്കുന്നViewer-ൽ ചിത്രം കാണിക്കുക
    image = Image.open(image_path)
    image.show()

# അപവാദങ്ങൾ പിടികൂടുക
except openai.BadRequestError as err:
    print(err)
```

## മികച്ച പ്രവർത്തനം! നിങ്ങളുടെ പഠനം തുടരുക

ഈ പാഠം പൂർത്തിയാക്കിയശേഷം, നമ്മുടെ [ജനറേറ്റീവ് AI പഠന ശേഖരം](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) പരിശോധിച്ച് നിങ്ങളുടെ ജനറേറ്റീവ് AI അറിവുകൾ മെച്ചപ്പെടാൻ തുടരുമ്!

നാം എങ്ങനെ [ലോ-കോഡ് ഉപയോഗിച്ച് AI ആപ്ലിക്കേഷനുകൾ നിർമ്മിക്കാമെന്ന്](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) പഠിക്കുന്ന പാഠം 10-ൽ ചെന്നു നോക്കൂ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->