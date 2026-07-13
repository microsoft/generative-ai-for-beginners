# စာသား ဖန်တီးခြင်း အက်ပလิเคေးရှင်းများ တည်ဆောက်ခြင်း

[![Building Text Generation Applications](../../../translated_images/my/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(ဒီသင်ခန်းစာရဲ့ ဗီဒီယိုကို ကြည့်ရန် အထက်တွင်ရှိသော ပုံကို နှိပ်ပါ)_

ဒီ သင်ခန်းစာတွင် ကြည့်ရှုခဲ့သည်မှာ prompt များလို core concepts များရှိပြီး "prompt engineering" ဟုခေါ်သော စနစ်တစ်ခုလုံးရှိကြောင်းဖြစ်သည်။ သင်၏ အချို့ tools (ChatGPT, Office 365, Microsoft Power Platform စသည်တို့) က prompt များအား အသုံးပြု၍ တစ်စုံတစ်ခုကို ပြုလုပ်ရန် အထောက်အကူပြုသည်။

သင့်အက်ပလิเคေးရှင်းတစ်ခုတွင် ဤအတွေ့အကြုံကို ထည့်သွင်းဖို့ prompt များ၊ completions များနှင့် လုပ်ကိုင်နိုင်မည့် library တစ်ခု ရွေးချယ်ခြင်းကြောင့် အများအပြားကို နားလည်ရပါမည်။ ဒီခန်းမှာ ထိုသင်ခန်းစာများကို သင် လေ့လာမည်ဖြစ်သည်။

## နိဒါန်း

ဒီခန်းစာတွင်၊ သင်သည် -

- openai library နှင့် ၎င်း၏ core concepts များကို လေ့လာမည်။
- openai ကို အသုံးပြုပြီး စာသား ဖန်တီးခြင်း အက်ပလิเคေးရှင်း တည်ဆောက်မည်။
- prompt, temperature, tokens စသည် နည်းလမ်းများကို ဘယ်လို အသုံးပြုပြီး စာသား ဖန်တီးခြင်း အက်ပလิเคေးရှင်း တည်ဆောက်မယ်ဆိုတာ နားလည်မည်။

## သင်ယူရမည့် ရည်ရွယ်ချက်များ

ဒီသင်ခန်းစာ အဆုံးတွင်၊ သင်သည် -

- စာသား ဖန်တီးခြင်း အက်ပလิเคေးရှင်း ဆိုတာဘာလဲ ဆိုတာ ရှင်းပြနိုင်မည်။
- openai ကို အသုံးပြုပြီး စာသား ဖန်တီးခြင်း အက်ပလิเคေးရှင်း တည်ဆောက်နိုင်မည်။
- Tokens အရေအတွက်၊ temperature ကို တိုးချဲ့သုံးနိုင်ပြီး output ကို အမျိုးမျိုးပြောင်းလဲနိုင်မည်။

## စာသား ဖန်တီးခြင်း အက်ပလิเคးရှင်း ဆိုတာဘာလဲ?

ပုံမှန်အားဖြင့် အက်ပလิเคေးရှင်း တည်ဆောက်သည်အခါ interface တစ်မျိုးရှိသည်၊ ဥပမာ -

- Command-based ကျ များ။ Console apps က command တစ်ခုရိုက်ထည့်ပြီး အလုပ်လုပ်သည့် အက်ပလิเคေးရှင်းများဖြစ်သည်။ ဥပမာ `git` ဆိုတာ command-based အက်ပလิเคေးရှင်းတစ်ခုဖြစ်သည်။
- User interface (UI) ပါဝင်သည့် app များ။ Button နှိပ်ခြင်း၊ စာရေးခြင်း၊ option များရွေးချယ်ခြင်း စသည် GUI ပါဝင်သည်။

### Console နှင့် UI အက်ပလิเคေးရှင်းများ ပါမာဏကန့်သတ်ချက်ရှိသည်

Command-based app တွေလို ကြည့်ရင် -

- **ကန့်သတ်ချက်များ ရှိသည်။** တိုက်ရိုက်ရိုက် command များသာအသုံးပြုပြီး app မှပံ့ပိုးပေးသော command များကိုသာ ရိုက်ထည့်နိုင်သည်။
- **ဘာသာစကား သီးခြားဖြစ်သည်။** အချို့ app များသည် ဘာသာစကားစွမ်းရည်များ ပြင်းပြင်းထန်ထန် ရှိပေမယ့် အစဉ်အလာအရ အက်ပလิเคေးရှင်းသည် တစ်စိတ်တစ်ပိုင်း ဘာသာစကားအထူး သီးခြား ချထားသည်။

### စာသား ဖန်တီးခြင်း အက်ပလิเคးရှင်းများ၏ အကျိုးကျေးဇူးများ

ဒါဆို စာသား ဖန်တီးခြင်း အက်ပလิเคေးရှင်းသည် ဘာကွဲပြားသနည်း?

စာသား ဖန်တီးအက်ပလิเคေးရှင်းတွင် ပိုမိုလွယ်ကူမှု ရှိသည်၊ command များ ကန့်သတ်ချက်ရှိခြင်းမရှိ၊ သီးခြားဘာသာစကားပေးရန်မလိုဘဲ သဘာဝဘာသာစကားဖြင့် အဓိပ္ပာယ် ပြောဆိုနိုင့်သည်။ ထို့ပြင် အချက်အလက်စုစည်းထားသော ကြီးမားသော corpus ၏ ၄င်းတွင်သင်ယူထားသည့် ဒေတာအရင်းအမြစ်နှင့် ဆက်သွယ်သော အကျိုးကျေးဇူးရှိသည်၊ ပုံမှန် app တွေက အချက်အလက် database အတွင်းရှိစာရင်းအပေါ် အကန့်အသတ်ရှိလေ့ရှိသည်။

### စာသား ဖန်တီးခြင်း အက်ပလီကေးရှင်းဖြင့် ဘာတွေ ပြုလုပ်နိုင်မလဲ?

အများကြီး လုပ်ဆောင်နိုင်ပါသည္။ ဥပမာ -

- **Chatbot**. ကုမ္ပဏီနှင့် ထုတ်ကုန်များအကြောင်း မေးခွန်းများကို ဖြေဆိုသော chatbot ဖန်တီးနိုင်ကာ မိမိလုပ်ငန်းနှင့် ကိုက်ညီသော အကောင်းဆုံး။
- **အကူအညီပေးသူ**. LLM များသည် စာမျက်နှာ တိုတောင်းအကျဉ်းချုပ်ခြင်း၊ စာသားမှ သိရှိချက်များ ရယူခြင်း၊ သင်္ခါရစာသား တင်ဆက်ခြင်းများတွင် အထူးပြုသောအရာဖြစ်သည်။
- **Code အကူအညီပေးသူ**. သင် အသုံးပြုမည့် language model အပေါ် မူတည်၍ ကုဒ်ရေးရန် အကူအညီပေးသော code assistant တစ်ခုတည်ဆောက်နိုင်သည်။ ဥပမာ GitHub Copilot, ChatGPT တို့ကို ကူညီရေးသားရန် အသုံးပြုနိုင်သည်။

## ဘယ်လို စတင်ရမလဲ?

LLM နှင့် ပေါင်းစည်းရန် လမ်းကြောင်းနှစ်ခုရှိသည် -

- API အသုံးပြုခြင်း။ Web request များ prompt ဖြင့် ဖန်တီးပြီး စာသား ထုတ်ပေးသော API ကို သုံးသည်။
- Library အသုံးပြုခြင်း။ Library များက API call များကို ညှိနှိုင်း၍ လွယ်ကူစေသည်။

## Libraries/SDKs များ

LLM များနှင့် အလုပ်လုပ်ရန် အထူးတော်သော library များအနည်းငယ်ရှိသည် -

- **openai** - မော်ဒယ်နှင့် ချိတ်ဆက်၍ prompt များ ပို့ပေးရန် အလွယ်အကူပြုသည်။

ထို့အပြင် အဆင့်မြင့် အထောက်အကူပြု library များဖြစ်သည် -

- **Langchain** - ကြားဖြတ် Library ဖြစ်ပြီး Python ကို ထောက်ပံ့သည်။
- **Semantic Kernel** - Microsoft ထုတ် library ဖြစ်ပြီး C#, Python, Java အသုံးပြုနိုင်သည်။

## openai ашиглан анхны аппликейшн хийх

Анхны аппликейшн яаж хийх тухай, ямар library хэрэгтэй, хэр хэмжээтэй вэ гэдгийг үзье.

### openai суулгах

OpenAI, Azure OpenAI-тэй ажиллах зориулалттай олон library байдаг. C#, Python, JavaScript, Java зэрэг олон программчлалын хэл ашиглах боломжтой. Бид `openai` Python library-г сонгосон тул `pip` ашиглан суулгана.

```bash
pip install openai
```


### Нөөц үүсгэх

Дараах алхмуудыг гүйцэтгэнэ үү:

- Azure дээр бүртгэл үүсгэх [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)
- Azure OpenAI-д хандах эрх авах. [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) дээр хандаж хүсэлт гаргах.

  > [!NOTE]
  > Энэхүү бичвэрийг бичиж байх үед Azure OpenAI-д хандах эрхийг хүсэлтээр авах шаардлагатай байна.

- Python суулгах <https://www.python.org/>
- Azure OpenAI үйлчилгээний нөөц үүсгэх. Нөөц үүсгэх гарын авлага [зэрэг](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst) үзнэ үү.

### API түлхүүр, endpoint олох

Одоо таны `openai` library-д ямар API түлхүүр хэрэглэхийг хэлэх шаардлагатай. Таны API түлхүүрийг олохын тулд Azure OpenAI нөөцийн "Keys and Endpoint" хэсэгт орж "Key 1" утгыг хуулна уу။

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Одоогоор хуулсан мэдээллийг хэрэглэн, library-үүдийг зааж өгье။

> [!NOTE]
> API түлхүүрийг кодноос тусгаарлах нь зүйтэй. Үүнийг орчны хувьсагч ашиглан хийж болно.
>
> - `OPENAI_API_KEY` орчны хувьсагчийг API түлхүүр дээр тохируулна.
>   `export OPENAI_API_KEY='sk-...'`

### Azure тохиргоо хийх

Azure OpenAI ашиглаж байвал тохиргоо хийх заавар:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```


Дээрх нь дараах зүйлийг тохируулж байна:

- `api_type` = `azure`. Library-д Azure OpenAI ашиглахыг зааж байна.
- `api_key` = Azure порталийн түгжээг энд оруулна.
- `api_version` = ашиглах API хувилбар. Одоогийн хамгийн шинэ хувилбар `2023-05-15`.
- `api_base` = API endpoint. Azure портал дээр API түлхүүрийн хажууд байдаг.

> [!NOTE]
> `os.getenv` орчны хувьсагч унших функц юм. `OPENAI_API_KEY`, `API_BASE`  г.м орчны хувьсагчийг уншихад ашиглаж болно. Эдгээрийг терминал эсвэл `dotenv` мэт library ашиглан тохируулж болно.

## Сүлжээг үүсгэх

Сүлжээг үүсгэхэд `Completion` класс ашиглана. Үүний жишээ:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```


Дээрх кодонд completion объект үүсгэж, ашиглах модель болон prompt-ийг дамжуулсан. Дараа нь үүсгэсэн текст хэвлээд байна။

### Chat completions

Одоогоор, text үүсгэхэд `Completion` ашиглаж байгааг харлаа. Гэхдээ чатботод илүү тохиромжтой `ChatCompletion` класс бас бий. Жишээ:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```


Энэ функцын талаар дараа бүдүүвч дээр дэлгэрэнгүй үзэх болно။

## Дасгал - анхны текст үүсгэх аппликейшн

openai-г тохируулах талаар сурсан тул одоо анхны текст үүсгэх аппликейшн хийх цаг болсон. Дараах алхмуудыг дагана уу:

1. Виртуал орчин үүсгэж openai суулгана:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Windows хэрэглэгч бол `venv\Scripts\activate` гэж бичнэ үү, `source venv/bin/activate` биш.

   > [!NOTE]
   > Azure OpenAI түлхүүрийг олж авахын тулд [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) руу орж `Open AI` гэж хайж `Open AI resource` сонгож, `Keys and Endpoint` хэсэгт орж `Key 1` хуулна уу.

1. _app.py_ файл үүсгэн дараах код бичнэ:

   ```python
   import openai

   openai.api_key = "<replace this value with your open ai key or Azure OpenAI key>"

   openai.api_type = 'azure'
   openai.api_version = '2023-05-15'
   openai.api_base = "<endpoint found in Azure Portal where your API key is>"
   deployment_name = "<deployment name>"

   # သင့်ပြီးစီးမှုကုဒ်ကိုထည့်သွင်းပါ
   prompt = "Complete the following: Once upon a time there was a"
   messages = [{"role": "user", "content": prompt}]

   # ပြီးစီးမှုကိုလုပ်ဆောင်ပါ
   completion = openai.chat.completions.create(model=deployment_name, messages=messages)

   # တုံ့ပြန်ချက်ကိုပုံနှိပ်ပါ
   print(completion.choices[0].message.content)
   ```

   > [!NOTE]
   > Azure OpenAI ашиглаж байвал `api_type`-ийг `azure` болгож, `api_key`-г Azure OpenAI түлхүүр дээр тохируулна.

   Доорх шиг үр дүн гарна.

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Төрөл бүрийн prompt-ууд, төрөл бүрийн хэрэглүүрүүд

Одоо prompt ашиглан текст үүсгэх аргыг харлаа. Хэрхэн ажиллахыг харсан учир өөрийн хүссэнээр өөрчлөлт хийх боломжтой болсон.

Prompt-ууд нь олон янзын даалгавруудад ашиглаж болно. Жишээ нь -

- **Текст төрлийг үүсгэх**. Жишээ нь шүлэг, асуултууд үүсгэх гэх мэт
- **Мэдээлэл хайх**. Жишээ нь `What does CORS mean in web development?` гэх мэт асуулт асууж мэдээлэл авах.
- **Код үүсгэх**. Жишээ нь имэйлийг шалгах regular expression бүтээх, бүр web app шиг бүхэл бүтэн програм үүсгэх.

## Өмнөх шиг хэрэглээ: жор үүсгэгч

Гэрт байгаа орцуудаар хоол хийх гэж байна гэж бодоё. Жор хэрэгтэй. Жор хайх хамгийн сайн аргуудын нэг бол хайлтын систем эсвэл LLM-г ашиглах.

Prompt-г хэлбэрээр бичнэ:

> "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"

Дээрх prompt-д дараах хариу ирж магадгүй:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 2 cloves garlic, minced
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
```


Үр дүн дажгүй, юу хийхээ мэднэ. Дараагийн сайжруулалт бол -

- Миний дуртайгүй эсвэл харшилтай орцуудыг тусад нь шүүх
- Орц хүрэлцэхгүй бол худалдан авах жагсаалт үүсгэх

Дээрх асуудалд дараах prompt нэмнэ үү:

> "Please remove recipes with garlic as I'm allergic and replace it with something else. Also, please produce a shopping list for the recipes, considering I already have chicken, potatoes and carrots at home."

Одоо дараах шинэ үр дүнг авна:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano

Shopping List:
- Olive oil
- Onion
- Thyme
- Oregano
- Salt
- Pepper
```


Үүний үр дүнд сармис орцгүй, харшилтай зүйлс ороогүй 5 жортой болж, гэрт байгаа орцийн байр байдлыг харгалзан худалдан авах жагсаалт үүссэн байна.

## Дасгал - жор үүсгэгч хийх

Өмнөх жишээг дагаж код бичье. Алхамууд:

1. _app.py_ файлыг ашиглан эхэлнэ
1. `prompt` хувьсагчийн утгыг дараах байдлаар өөрчилнө:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```


   Одоо кодыг ажиллуулбал дараах үр дүнтэй төстэй гаралт гарна:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```


   >  Тэмдэглэл, таны LLM тодорхойгүй хариу гаргах тул програм бүр удирдлагаар өөр үр дүн гарч болно.

Хэн нэгэн сайжруулалт хийх гэж байна. Илүү уян хатан болж орц болон жорын тоог өөрчлөх боломжтой болно.

1. Кодоо дараах байдлаар өөрчилж үзэе:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # အချက်အလက်တစ်ခုအတွင်းချက်ပြုတ်နည်းအရေအတွက်ကို ရိုက်ထည့်ပါ။
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```


   Туршилтын код иймэрхүү харагдах болно:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```


### Шүүлтүүр ба худалдан авах жагсаалт нэмж сайжруулах

Одоо хэрэглэгчийн оролтоос хамаарч жор гаргах, орц болон жорын тоог өөрчлөх боломжтой ажиллах апптай боллоо.

Дараах сайжруулалтыг хийцгээе -

- **Шүүлтүүр орц**. Дуртайгүй орцууд, харшилтай зүйлсийг тусгаарлах шүүлтүүр нэмье. Үүний тулд анхны prompt-ын эцэст `{filter}` нэмнэ, мөн хэрэглэгчийн шүүлтүүр утгыг авч оруулах.

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```


Шүүлтүүр утгыг хэрэглэгчээс авч, prompt-ийн төгсгөлд нэмж оруулна.

Програмыг ажиллуулаад орцод сүү байгаа жор шүүх үр дүн:

  ```output
  No of recipes (for example, 5): 3
  List of ingredients (for example, chicken, potatoes, and carrots): onion,milk
  Filter (for example, vegetarian, vegan, or gluten-free): no milk

  1. French Onion Soup

  Ingredients:

  -1 large onion, sliced
  -3 cups beef broth
  -1 cup milk
  -6 slices french bread
  -1/4 cup shredded Parmesan cheese
  -1 tablespoon butter
  -1 teaspoon dried thyme
  -1/4 teaspoon salt
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add beef broth, milk, thyme, salt, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Place french bread slices on soup bowls.
  5. Ladle soup over bread.
  6. Sprinkle with Parmesan cheese.

  2. Onion and Potato Soup

  Ingredients:

  -1 large onion, chopped
  -2 cups potatoes, diced
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add potatoes, vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Serve hot.

  3. Creamy Onion Soup

  Ingredients:

  -1 large onion, chopped
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper
  -1/4 cup all-purpose flour
  -1/2 cup shredded Parmesan cheese

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. In a small bowl, whisk together flour and Parmesan cheese until smooth.
  5. Add to soup and simmer for an additional 5 minutes, or until soup has thickened.
  ```


Хэрэв та сүүний уураг тэсвэргүй бол бяслаг орсон жорыг бас шүүх хэрэгтэй болно. Иймд ойлгомжтой байх шаардлагатай.

- **Худалдан авах жагсаалт үүсгэх**. Гэрт байгаа орцыг харгалзан худалдан авах зүйлсийн жагсаалт гаргах.

Энэ функцийг ганц prompt-д хамтад нь хийх эсвэл хоёр prompt болгож хуваах аргыг сонгож болно. Хоёр дахь аргыг үзье. Үүний тулд эхний prompt-ийн үр дүнг хоёр дахь prompt-д контекст болгон дамжуулна.

Эхний prompt-ийн үр дүнг хэвлэж байгаа хэсэг дээр дараах кодыг нэмнэ:

  ```python
  old_prompt_result = completion.choices[0].message.content
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  messages = [{"role": "user", "content": new_prompt}]
  completion = openai.Completion.create(engine=deployment_name, messages=messages, max_tokens=1200)

  # တုံ့ပြန်ချက်ကို ပရင့်ထုတ်သည်
  print("Shopping list:")
  print(completion.choices[0].message.content)
  ```


Үүний талаар анхаарах зүйлс:
  1. ပထမဆုံး prompt မှရလဒ်ကို အသစ်သော prompt ထဲတွင် ပေါင်းထည့်၍ prompt အသစ်တစ်ခုကို တည်ဆောက်နေပါသည်-

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. အသစ်သော request ကို လုပ်ဆောင်သော်လည်း ပထမ prompt တွင် မေးမြန်းခဲ့သည့် token အရေအတွက်ကိုလည်း စဉ်းစားမည်ဖြစ်ပြီး၊ ဒီတစ်ကြိမ် `max_tokens` ကို 1200 ဟု သတ်မှတ်သွားမည်။

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     ဤကုဒ်ကို စမ်းသပ်ကြည့်ရာတွင် မည်သည့် အထွက်အနေနဲ့ရရှိ သနည်းမှာ အောက်ပါအတိုင်းဖြစ်လာပါသည်-

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## သင့်စနစ်ကို တိုးတက်အောင်လုပ်ခြင်း

ယခုအထိ ရရှိထားသော ကုဒ်မှာ အလုပ်လုပ်သော်လည်း ပိုမိုတိုးတက်စေဖို့ အချို့ ညှိနှိုင်းမှုများ လုပ်သင့်သည်။ ပြုလုပ်သင့်သော အချက်အချို့မှာ:

- **လျှိုဝှက်ချက်များကို ကုဒ်ထဲကနေ ခွဲခြားပါ၊** ဥပမာ API key ကဲ့သို့။ လျှိုဝှက်ချက်များသည် ကုဒ်ထဲရှိသင့်ခြင်း မဟုတ်ဘဲ လုံခြုံသောနေရာတစ်ခုတွင် သိုလှောင်ထားသင့်သည်။ လျှိုဝှက်ချက်များကို ကုဒ်ထဲကနေ ခွဲထုတ်ရန် environment variable များနှင့် `python-dotenv` ကဲ့သို့သော library များ ဖြင့် ဖိုင်မှ ဖတ်ရှုနိုင်သည်။ အောက်ပါနည်းဖြင့် ကုဒ်တွင် ပြသထားပါသည်-

  1. အောက်ပါအကြောင်းအရာ ဖြင့် `.env` ဖိုင် တစ်ဖိုင် ပြုလုပ်ပါ-

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > မှတ်ချက်၊ Azure အတွက် သင်သည် အောက်ပါ environment variable များကို သတ်မှတ်ရန် လိုအပ်ပါသည်-

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     ကုဒ်တွင် environment variable များကို အောက်ပါနည်းဖြင့် ဖတ်ရှုသွားမည်-

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Token အရှည်အကြောင်း**။ ထုတ်လုပ်လိုသောစာသားအတွက် ဘယ်နှစ် token လိုအပ်သည်ကို စဉ်းစားသင့်သည်။ Token များသည် ငွေသက်သာမှုရှိသောအရာဖြစ်သလို၊ အသုံးပြု token အရေအတွက်ကို လျော့နည်းစေရန်ကြိုးစားသင့်သည်။ ဥပမာအားဖြင့် prompt ကို ပိုမိုတိုတောင်းစေရန် စဉ်းစားနိုင်ပါသလား?

  tokens များကို သတ်မှတ်ရန် `max_tokens` ပါရာမီတာကို အသုံးပြုနိုင်သည်။ ဥပမာ၊ token 100 အသုံးပြုလိုပါက အောက်ပါအတိုင်းလုပ်ပါ-

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Temperature အား စမ်းသပ်ခြင်း**။ Temperature သည် ယခုထိ ပြောဆိုမထားသေးပေမယ့် ဤကဲ့သို့သော value သည် လှိမ့်လည်ဆိုးကျိုးကို ထိန်းချုပ်ပေးသောအရာဖြစ်သည်။ Temperature တန်ဖိုးမြင့်တက်လျှင် အထွက်သည် ပိုမိုမတိကျဘဲ ဖြစ်လာမည်။ Temperature တန်ဖိုးနိမ့်လျှင် အထွက်သည် ပိုမိုခန့်မှန်းနိုင်ပါသည်။ ထုတ်လွှင့်မှုတွင် မတူကွဲပြားမှုလားဆိုတာ ကိုစဉ်းစားပါ။

  temperature ကို ပြောင်းလဲချိန်ညှိရန် `temperature` ပါရာမီတာကို အသုံးပြုနိုင်သည်။ ဥပမာ အပူချိန် 0.5 သတ်မှတ်လိုပါက အောက်ပါအတိုင်းလုပ်ပါ-

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > မှတ်ချက်၊ 1.0 နီးစပ်သလောက် တတ်နိုင်သမျှ မတူကွဲပြားမှု ပိုများပါသည်။

## အလုပ်အပ်

ဤအလုပ်အပ်အတွက် သင် သင်လိုချင်သည့် အရာကို ရွေးချယ်နိုင်သည်။

အောက်ပါ အကြံပြုချက်များရှိသည်-

- တဆင့်တွဲမှုမူကြမ်း app ကို ပိုတိုးတက်အောင် ပြုပြင်ပါ။ temperature တန်ဖိုးများနှင့် prompt များဖြင့် ကစားကြည့်ကောင်းမလား စမ်းသပ်ပါ။
- "လေ့လာသူ သူငယ်ချင်း" app တစ်ခု တည်ဆောက်ပါ။ ဤ app သည် Python ကဲ့သို့သော အကြောင်းအရာများအတွက် မေးခွန်းများကို ဖြေတတ်ရမည်။ ဥပမာ "Python တွင် အဆိုပါအကြောင်းအရာဆိုတာဘာလဲ?" ဟု စတိုင်ပုံများပေးနိုင်ပြီး ပိုမိုကောင်းမွန်စေသည်။ ဒါမှမဟုတ် အဆိုပါအကြောင်းအရာအတွက် ကုဒ်ပြပါဟု prompt တစ်ခုရှိနိုင်ပါသည်။
- သမိုင်း bot တစ်ခု၊ သမိုင်းကို အသက်ဝင်စေ၍ bot ကို သမိုင်းဇာတ်ကောင်တစ်ဦးအဖြစ် လှမ်းပြီး အဲဒီဇာတ်ကောင်၏ ဘဝနှင့်အချိန် မေးခွန်းများကို မေးပါစေ။

## ဖြေရှင်းချက်

### လေ့လာသူသူငယ်ချင်း

အောက်တွင် စစဉ် prompt နှင့် မည်သို့ အသုံးပြုရမည်၊ သင်လိုသလို ပြုပြင်ရန် နမူနာတစ်ခု ပြထားသည်-

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### သမိုင်း bot

အသုံးပြုနိုင်သော prompt များအောက်ပါအတိုင်းရှိသည်-

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## သိမှတ်ချက်စစ်ဆေးခြင်း

Temperature ဆိုသည်မှာ ဘာလုပ်ဆောင်သလဲ?

1. အထွက်သည် မတိကျမှု ဘယ်လောက်ရှိသည်ကို ထိန်းချုပ်သည်။
1. ဖြေကြားချိန်အရွယ်အစားကို ထိန်းချုပ်သည်။
1. အသုံးပြု token အရေအတွက်ကို ထိန်းချုပ်သည်။

## 🚀 စိန်ခေါ်မှု

အလုပ်အပ်အတွက် လုပ်ဆောင်စဉ် temperature ကို အမျိုးမျိုးပြောင်းလဲကြည့်ပါ၊ 0, 0.5 နှင့် 1 အဖြစ် သတ်မှတ်ကြည့်ပါ။ 0 သည် အနည်းဆုံး မတူကွဲပြားမှု ဖြစ်ပြီး 1 သည် အများဆုံးဖြစ်သည်။ သင့် app အတွက် ဘယ်တန်ဖိုးအဆင်ပြေသနည်း?

## အလွန်ကောင်းမွန်သည်! သင်၏သင်ယူမှု ဆက်လက်ပါ။

ဤသင်ခန်းစာပြီးဆုံးပြီးနောက်၊ ကျွန်ုပ်တို့၏ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) တွင် တက်တူးမြှင့်တင်မှု ဆက်လက်လေ့လာနိုင်ပါသည်။

Lesson 7 သို့ သွားပါက အောက်ပါအတိုင်း [chat application များကို တည်ဆောက်နည်း](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)ကို ကြည့်ရှုနိုင်ပါပြီ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->