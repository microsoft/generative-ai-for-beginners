<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-06-25T14:39:22+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "ms"
}
-->
# Membangun Aplikasi Penjanaan Teks

[![Membangun Aplikasi Penjanaan Teks](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.ms.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(Klik imej di atas untuk menonton video pelajaran ini)_

Anda telah melihat melalui kurikulum ini bahawa terdapat konsep teras seperti prompt dan bahkan satu disiplin yang dipanggil "kejuruteraan prompt". Banyak alat yang boleh anda berinteraksi seperti ChatGPT, Office 365, Microsoft Power Platform dan banyak lagi, menyokong anda menggunakan prompt untuk mencapai sesuatu.

Untuk anda menambah pengalaman sedemikian ke dalam aplikasi, anda perlu memahami konsep seperti prompt, penyelesaian dan memilih perpustakaan untuk digunakan. Itulah yang akan anda pelajari dalam bab ini.

## Pengenalan

Dalam bab ini, anda akan:

- Mempelajari tentang perpustakaan openai dan konsep terasnya.
- Membina aplikasi penjanaan teks menggunakan openai.
- Memahami bagaimana menggunakan konsep seperti prompt, suhu, dan token untuk membina aplikasi penjanaan teks.

## Matlamat pembelajaran

Pada akhir pelajaran ini, anda akan dapat:

- Menjelaskan apa itu aplikasi penjanaan teks.
- Membina aplikasi penjanaan teks menggunakan openai.
- Mengkonfigurasi aplikasi anda untuk menggunakan lebih atau kurang token dan juga mengubah suhu, untuk output yang berbeza.

## Apakah itu aplikasi penjanaan teks?

Biasanya apabila anda membina aplikasi, ia mempunyai sejenis antara muka seperti berikut:

- Berasaskan arahan. Aplikasi konsol adalah aplikasi tipikal di mana anda menaip arahan dan ia melaksanakan tugas. Sebagai contoh, `git` adalah aplikasi berasaskan arahan.
- Antara muka pengguna (UI). Sesetengah aplikasi mempunyai antara muka pengguna grafik (GUI) di mana anda klik butang, masukkan teks, pilih pilihan dan banyak lagi.

### Aplikasi konsol dan UI terhad

Bandingkan dengan aplikasi berasaskan arahan di mana anda menaip arahan:

- **Ia terhad**. Anda tidak boleh hanya menaip sebarang arahan, hanya yang disokong oleh aplikasi.
- **Spesifik bahasa**. Sesetengah aplikasi menyokong banyak bahasa, tetapi secara lalai aplikasi dibina untuk bahasa tertentu, walaupun anda boleh menambah sokongan bahasa lain.

### Manfaat aplikasi penjanaan teks

Jadi bagaimana aplikasi penjanaan teks berbeza?

Dalam aplikasi penjanaan teks, anda mempunyai lebih banyak fleksibiliti, anda tidak terhad kepada set arahan atau bahasa input tertentu. Sebaliknya, anda boleh menggunakan bahasa semula jadi untuk berinteraksi dengan aplikasi. Satu lagi manfaat ialah kerana anda sudah berinteraksi dengan sumber data yang telah dilatih pada korpus maklumat yang luas, manakala aplikasi tradisional mungkin terhad pada apa yang ada dalam pangkalan data.

### Apa yang boleh saya bina dengan aplikasi penjanaan teks?

Terdapat banyak perkara yang boleh anda bina. Sebagai contoh:

- **Chatbot**. Chatbot menjawab soalan tentang topik, seperti syarikat anda dan produknya boleh menjadi padanan yang baik.
- **Pembantu**. LLM sangat baik dalam perkara seperti meringkaskan teks, mendapatkan wawasan daripada teks, menghasilkan teks seperti resume dan banyak lagi.
- **Pembantu kod**. Bergantung pada model bahasa yang anda gunakan, anda boleh membina pembantu kod yang membantu anda menulis kod. Sebagai contoh, anda boleh menggunakan produk seperti GitHub Copilot serta ChatGPT untuk membantu anda menulis kod.

## Bagaimana saya boleh bermula?

Baiklah, anda perlu mencari cara untuk berintegrasi dengan LLM yang biasanya memerlukan dua pendekatan berikut:

- Gunakan API. Di sini anda membina permintaan web dengan prompt anda dan mendapatkan teks yang dihasilkan kembali.
- Gunakan perpustakaan. Perpustakaan membantu merangkum panggilan API dan memudahkan penggunaannya.

## Perpustakaan/SDK

Terdapat beberapa perpustakaan terkenal untuk bekerja dengan LLM seperti:

- **openai**, perpustakaan ini memudahkan untuk menyambung ke model anda dan menghantar prompt.

Kemudian terdapat perpustakaan yang beroperasi pada tahap yang lebih tinggi seperti:

- **Langchain**. Langchain terkenal dan menyokong Python.
- **Semantic Kernel**. Semantic Kernel adalah perpustakaan oleh Microsoft yang menyokong bahasa C#, Python, dan Java.

## Aplikasi pertama menggunakan openai

Mari kita lihat bagaimana kita boleh membina aplikasi pertama kita, perpustakaan apa yang kita perlukan, berapa banyak yang diperlukan dan sebagainya.

### Pasang openai

Terdapat banyak perpustakaan di luar sana untuk berinteraksi dengan OpenAI atau Azure OpenAI. Adalah mungkin untuk menggunakan pelbagai bahasa pengaturcaraan seperti C#, Python, JavaScript, Java dan banyak lagi. Kami telah memilih untuk menggunakan perpustakaan Python `openai`, jadi kami akan menggunakan `pip` untuk memasangnya.

```bash
pip install openai
```

### Buat sumber

Anda perlu melaksanakan langkah-langkah berikut:

- Buat akaun di Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Dapatkan akses ke Azure OpenAI. Pergi ke [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) dan minta akses.

  > [!NOTE]
  > Pada masa penulisan, anda perlu memohon akses ke Azure OpenAI.

- Pasang Python <https://www.python.org/>
- Telah mencipta sumber Perkhidmatan Azure OpenAI. Lihat panduan ini untuk cara [mencipta sumber](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Cari kunci API dan titik akhir

Pada ketika ini, anda perlu memberitahu perpustakaan `openai` anda kunci API apa yang hendak digunakan. Untuk mencari kunci API anda, pergi ke bahagian "Kunci dan Titik Akhir" sumber Azure OpenAI anda dan salin nilai "Kunci 1".

![Bilah sumber Kunci dan Titik Akhir dalam Portal Azure](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Sekarang bahawa anda telah menyalin maklumat ini, mari arahkan perpustakaan untuk menggunakannya.

> [!NOTE]
> Adalah berbaloi untuk memisahkan kunci API anda dari kod anda. Anda boleh melakukannya dengan menggunakan pembolehubah persekitaran.
>
> - Tetapkan pembolehubah persekitaran `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`

### Tetapan konfigurasi Azure

Jika anda menggunakan Azure OpenAI, berikut adalah cara anda menetapkan konfigurasi:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Di atas kami menetapkan yang berikut:

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion` class. Berikut adalah contoh:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

Dalam kod di atas, kami mencipta objek penyelesaian dan memasukkan model yang ingin kami gunakan dan prompt. Kemudian kami mencetak teks yang dihasilkan.

### Penyelesaian chat

Setakat ini, anda telah melihat bagaimana kami menggunakan `Completion` to generate text. But there's another class called `ChatCompletion` yang lebih sesuai untuk chatbot. Berikut adalah contoh penggunaannya:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Lebih lanjut mengenai fungsi ini dalam bab yang akan datang.

## Latihan - aplikasi penjanaan teks pertama anda

Sekarang bahawa kami telah belajar cara menyediakan dan mengkonfigurasi openai, sudah tiba masanya untuk membina aplikasi penjanaan teks pertama anda. Untuk membina aplikasi anda, ikuti langkah-langkah berikut:

1. Buat persekitaran maya dan pasang openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Jika anda menggunakan Windows taip `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` value.

1. Buat fail _app.py_ dan beri kod berikut:

   ```python
   import openai

   openai.api_key = "<replace this value with your open ai key or Azure OpenAI key>"

   openai.api_type = 'azure'
   openai.api_version = '2023-05-15'
   openai.api_base = "<endpoint found in Azure Portal where your API key is>"
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"
   messages = [{"role": "user", "content": prompt}]

   # make completion
   completion = openai.chat.completions.create(model=deployment_name, messages=messages)

   # print response
   print(completion.choices[0].message.content)
   ```

   > [!NOTE]
   > Jika anda menggunakan Azure OpenAI, anda perlu menetapkan `api_type` to `azure` and set the `api_key` kepada kunci Azure OpenAI anda.

   Anda sepatutnya melihat output seperti berikut:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Jenis prompt yang berbeza, untuk perkara yang berbeza

Sekarang anda telah melihat bagaimana untuk menjana teks menggunakan prompt. Anda malah mempunyai program yang berfungsi yang boleh anda ubah suai dan ubah untuk menghasilkan jenis teks yang berbeza.

Prompt boleh digunakan untuk semua jenis tugas. Sebagai contoh:

- **Menjana jenis teks**. Sebagai contoh, anda boleh menjana puisi, soalan untuk kuiz dan sebagainya.
- **Cari maklumat**. Anda boleh menggunakan prompt untuk mencari maklumat seperti contoh berikut 'Apa maksud CORS dalam pembangunan web?'.
- **Menjana kod**. Anda boleh menggunakan prompt untuk menjana kod, contohnya membangunkan ungkapan biasa yang digunakan untuk mengesahkan emel atau mengapa tidak menjana keseluruhan program, seperti aplikasi web?

## Kes penggunaan yang lebih praktikal: penjana resipi

Bayangkan anda mempunyai bahan-bahan di rumah dan anda ingin memasak sesuatu. Untuk itu, anda memerlukan resipi. Satu cara untuk mencari resipi adalah menggunakan enjin carian atau anda boleh menggunakan LLM untuk melakukannya.

Anda boleh menulis prompt seperti berikut:

> "Tunjukkan kepada saya 5 resipi untuk hidangan dengan bahan-bahan berikut: ayam, kentang, dan lobak. Setiap resipi, senaraikan semua bahan yang digunakan"

Berdasarkan prompt di atas, anda mungkin mendapat jawapan seperti:

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

Hasil ini bagus, saya tahu apa yang hendak dimasak. Pada ketika ini, apa yang boleh menjadi penambahbaikan berguna adalah:

- Menapis bahan-bahan yang saya tidak suka atau alah kepada.
- Menghasilkan senarai membeli-belah, sekiranya saya tidak mempunyai semua bahan di rumah.

Untuk kes di atas, mari kita tambah prompt tambahan:

> "Sila keluarkan resipi dengan bawang putih kerana saya alah dan gantikannya dengan sesuatu yang lain. Juga, sila hasilkan senarai membeli-belah untuk resipi, memandangkan saya sudah mempunyai ayam, kentang dan lobak di rumah."

Sekarang anda mempunyai hasil baru, iaitu:

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

Itulah lima resipi anda, tanpa bawang putih disebut dan anda juga mempunyai senarai membeli-belah memandangkan apa yang sudah anda ada di rumah.

## Latihan - bina penjana resipi

Sekarang kita telah memainkan senario, mari kita tulis kod untuk memadankan senario yang ditunjukkan. Untuk melakukannya, ikuti langkah-langkah berikut:

1. Gunakan fail _app.py_ sedia ada sebagai titik permulaan
1. Cari pembolehubah `prompt` dan ubah kodnya kepada yang berikut:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Jika anda sekarang menjalankan kod, anda sepatutnya melihat output yang serupa dengan:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE, LLM anda adalah tidak deterministik, jadi anda mungkin mendapat hasil yang berbeza setiap kali anda menjalankan program.

   Hebat, mari kita lihat bagaimana kita boleh memperbaiki perkara. Untuk memperbaiki perkara, kita mahu memastikan kodnya fleksibel, jadi bahan-bahan dan bilangan resipi boleh diperbaiki dan diubah.

1. Mari kita ubah kod dengan cara berikut:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Mengambil kod untuk ujian, boleh kelihatan seperti ini:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Memperbaiki dengan menambah penapis dan senarai membeli-belah

Kami sekarang mempunyai aplikasi yang berfungsi yang mampu menghasilkan resipi dan ia fleksibel kerana ia bergantung pada input dari pengguna, kedua-duanya pada bilangan resipi tetapi juga bahan-bahan yang digunakan.

Untuk memperbaikinya, kami mahu menambah yang berikut:

- **Menapis bahan-bahan**. Kami mahu dapat menapis bahan-bahan yang kami tidak suka atau alah kepada. Untuk melaksanakan perubahan ini, kami boleh mengedit prompt sedia ada kami dan menambah syarat penapis ke penghujungnya seperti berikut:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Di atas, kami menambah `{filter}` ke penghujung prompt dan kami juga menangkap nilai penapis dari pengguna.

  Contoh input menjalankan program sekarang boleh kelihatan seperti ini:

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

  Seperti yang anda lihat, sebarang resipi dengan susu di dalamnya telah ditapis keluar. Tetapi, jika anda tidak toleran laktosa, anda mungkin mahu menapis resipi dengan keju di dalamnya juga, jadi ada keperluan untuk jelas.

- **Menghasilkan senarai membeli-belah**. Kami mahu menghasilkan senarai membeli-belah, memandangkan apa yang sudah kami ada di rumah.

  Untuk fungsi ini, kami boleh cuba menyelesaikan semuanya dalam satu prompt atau kami boleh membahagikannya kepada dua prompt. Mari cuba pendekatan kedua. Di sini kami mencadangkan menambah prompt tambahan, tetapi untuk itu berfungsi, kami perlu menambah hasil dari prompt pertama sebagai konteks kepada prompt kedua.

  Cari bahagian dalam kod yang mencetak hasil dari prompt pertama dan tambahkan kod berikut di bawah:

  ```python
  old_prompt_result = completion.choices[0].message.content
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  messages = [{"role": "user", "content": new_prompt}]
  completion = openai.Completion.create(engine=deployment_name, messages=messages, max_tokens=1200)

  # print response
  print("Shopping list:")
  print(completion.choices[0].message.content)
  ```

  Perhatikan yang berikut:

  1. Kami membina prompt baru dengan menambah hasil dari prompt pertama ke prompt baru:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Kami membuat permintaan baru, tetapi juga mempertimbangkan bilangan token yang kami minta dalam prompt pertama, jadi kali ini kami katakan `max_tokens` adalah 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     Mengambil kod ini untuk percubaan, kami sekarang tiba pada output berikut:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Memperbaiki persediaan anda

Apa yang kita ada setakat ini adalah kod yang berfungsi, tetapi terdapat beberapa perubahan yang harus kita lakukan untuk memperbaiki perkara lebih lanjut. Beberapa perkara yang harus kita lakukan adalah:

- **Pisahkan rahsia dari kod**, seperti kunci API. Rahsia tidak boleh berada dalam kod dan harus disimpan di lokasi yang selamat. Untuk memisahkan rahsia dari kod, kita boleh menggunakan pembolehubah persekitaran dan perpustakaan seperti `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env` file dengan kandungan berikut:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Nota, untuk Azure, anda perlu menetapkan pembolehubah persekitaran berikut:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     Dalam kod, anda akan memuatkan pembolehubah persekitaran seperti berikut:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Kata tentang panjang token**. Kita harus mempertimbangkan berapa banyak token yang kita perlukan untuk menjana teks yang kita mahu. Token berharga wang, jadi di mana mungkin, kita harus cuba berjimat dengan bilangan token yang kita gunakan. Sebagai contoh, bolehkah kita merumuskan prompt supaya kita boleh menggunakan kurang token?

  Untuk menukar token yang digunakan, anda boleh menggunakan parameter `max_tokens`. Sebagai contoh, jika anda mahu menggunakan 100 token, anda akan lakukan:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Bereksperimen dengan suhu**. Suhu adalah sesuatu yang belum kita sebutkan setakat ini tetapi merupakan konteks penting untuk bagaimana program kita berfungsi. Semakin tinggi nilai suhu semakin rawak outputnya. Sebaliknya semakin rendah nilai suhu semakin dapat diramalkan outputnya. Pertimbangkan sama ada anda mahu variasi dalam output anda atau tidak.

  Untuk mengubah suhu, anda boleh menggunakan parameter `temperature`. Sebagai contoh, jika anda mahu menggunakan suhu 0.5, anda akan lakukan:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Nota, semakin hampir kepada 1.0, semakin bervariasi outputnya.

## Tugasan

Untuk tugasan ini, anda boleh memilih apa yang hendak dibina.

Berikut adalah beberapa cadangan:

- Ubahsuai aplikasi penjana resipi untuk memperbaikinya lebih lanjut. Mainkan nilai suhu, dan prompt untuk melihat apa yang anda boleh hasilkan.
- Bina "rakan belajar". Aplikasi ini harus dapat menjawab soalan tentang topik contohnya Python, anda boleh mempunyai prompt seperti "Apa itu topik tertentu dalam Python?", atau anda boleh mempunyai prompt yang mengatakan, tunjukkan saya kod untuk topik tertentu dan sebagainya.
- Bot sejarah, hidupkan sejarah, arahkan bot untuk memainkan watak sejarah tertentu dan tanya soalan tentang kehidupan dan zamannya.

## Penyelesaian

### Rakan belajar

Di bawah adalah prompt permulaan, lihat bagaimana anda boleh menggunakannya dan mengubahnya mengikut keinginan anda.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Bot sejarah

Berikut adalah beberapa prompt yang boleh anda gunakan:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Semakan pengetahuan

Apa yang dilakukan oleh konsep suhu?

1. Ia mengawal seberapa rawak outputnya.
1. Ia mengawal seberapa besar responsnya.
1. Ia mengawal berapa banyak token yang digunakan.

## 🚀 Cabaran

Semasa bekerja pada tugasan, cuba variasikan suhu, cuba tetapkan kepada 0, 0.5, dan 1. Ingat bahawa 0 adalah yang paling tidak bervariasi dan 1 adalah yang paling bervariasi, nilai apa yang paling sesuai untuk aplikasi anda?

## Kerja yang Hebat! Teruskan Pembelajaran Anda

Selepas menyelesaikan pelajaran ini, lihat koleksi Pembelajaran AI Generatif kami [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk terus meningkatkan pengetahuan AI Generatif anda!

Pergi ke Pelajaran 7 di mana kita akan melihat cara [membangun aplikasi chat](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.