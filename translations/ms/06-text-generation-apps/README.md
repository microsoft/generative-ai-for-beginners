<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ce8224073b86b728ed52b19bed7932fd",
  "translation_date": "2025-07-09T12:04:18+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "ms"
}
-->
# Membangun Aplikasi Penjanaan Teks

[![Membangun Aplikasi Penjanaan Teks](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.ms.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

Sehingga kini, anda telah melihat dalam kurikulum ini bahawa terdapat konsep teras seperti prompt dan juga satu disiplin penuh yang dipanggil "prompt engineering". Banyak alat yang anda boleh berinteraksi seperti ChatGPT, Office 365, Microsoft Power Platform dan lain-lain, menyokong penggunaan prompt untuk mencapai sesuatu.

Untuk anda menambah pengalaman sebegini ke dalam aplikasi, anda perlu memahami konsep seperti prompt, completions dan memilih perpustakaan untuk digunakan. Itulah yang akan anda pelajari dalam bab ini.

## Pengenalan

Dalam bab ini, anda akan:

- Mempelajari tentang perpustakaan openai dan konsep terasnya.
- Membangun aplikasi penjanaan teks menggunakan openai.
- Memahami cara menggunakan konsep seperti prompt, temperature, dan tokens untuk membina aplikasi penjanaan teks.

## Matlamat pembelajaran

Pada akhir pelajaran ini, anda akan dapat:

- Menerangkan apa itu aplikasi penjanaan teks.
- Membangun aplikasi penjanaan teks menggunakan openai.
- Mengkonfigurasi aplikasi anda untuk menggunakan lebih atau kurang token dan juga mengubah temperature, untuk hasil yang berbeza.

## Apakah itu aplikasi penjanaan teks?

Biasanya apabila anda membina aplikasi, ia mempunyai antara muka seperti berikut:

- Berasaskan arahan. Aplikasi konsol adalah aplikasi biasa di mana anda menaip arahan dan ia melaksanakan tugas. Contohnya, `git` adalah aplikasi berasaskan arahan.
- Antara muka pengguna (UI). Sesetengah aplikasi mempunyai antara muka grafik (GUI) di mana anda klik butang, masukkan teks, pilih pilihan dan lain-lain.

### Aplikasi konsol dan UI mempunyai had

Bandingkan dengan aplikasi berasaskan arahan di mana anda menaip arahan:

- **Terhad**. Anda tidak boleh menaip sebarang arahan, hanya arahan yang disokong oleh aplikasi.
- **Spesifik bahasa**. Sesetengah aplikasi menyokong banyak bahasa, tetapi secara lalai aplikasi dibina untuk bahasa tertentu, walaupun anda boleh menambah sokongan bahasa lain.

### Kelebihan aplikasi penjanaan teks

Jadi, bagaimana aplikasi penjanaan teks berbeza?

Dalam aplikasi penjanaan teks, anda mempunyai lebih banyak fleksibiliti, anda tidak terhad kepada set arahan atau bahasa input tertentu. Sebaliknya, anda boleh menggunakan bahasa semula jadi untuk berinteraksi dengan aplikasi. Satu lagi kelebihan adalah kerana anda sudah berinteraksi dengan sumber data yang telah dilatih dengan korpus maklumat yang luas, manakala aplikasi tradisional mungkin terhad pada apa yang ada dalam pangkalan data.

### Apa yang boleh saya bina dengan aplikasi penjanaan teks?

Terdapat banyak perkara yang boleh anda bina. Contohnya:

- **Chatbot**. Chatbot yang menjawab soalan tentang topik, seperti syarikat anda dan produk-produknya boleh menjadi padanan yang baik.
- **Pembantu**. LLM sangat bagus untuk perkara seperti meringkaskan teks, mendapatkan pandangan dari teks, menghasilkan teks seperti resume dan banyak lagi.
- **Pembantu kod**. Bergantung pada model bahasa yang anda gunakan, anda boleh membina pembantu kod yang membantu anda menulis kod. Contohnya, anda boleh menggunakan produk seperti GitHub Copilot serta ChatGPT untuk membantu menulis kod.

## Bagaimana saya boleh bermula?

Anda perlu mencari cara untuk berintegrasi dengan LLM yang biasanya melibatkan dua pendekatan berikut:

- Gunakan API. Di sini anda membina permintaan web dengan prompt anda dan mendapat teks yang dijana kembali.
- Gunakan perpustakaan. Perpustakaan membantu membungkus panggilan API dan menjadikannya lebih mudah digunakan.

## Perpustakaan/SDK

Terdapat beberapa perpustakaan yang terkenal untuk bekerja dengan LLM seperti:

- **openai**, perpustakaan ini memudahkan sambungan ke model anda dan menghantar prompt.

Kemudian terdapat perpustakaan yang beroperasi pada tahap lebih tinggi seperti:

- **Langchain**. Langchain terkenal dan menyokong Python.
- **Semantic Kernel**. Semantic Kernel adalah perpustakaan oleh Microsoft yang menyokong bahasa C#, Python, dan Java.

## Aplikasi pertama menggunakan openai

Mari kita lihat bagaimana kita boleh membina aplikasi pertama kita, perpustakaan apa yang diperlukan, berapa banyak yang diperlukan dan sebagainya.

### Pasang openai

Terdapat banyak perpustakaan untuk berinteraksi dengan OpenAI atau Azure OpenAI. Anda juga boleh menggunakan pelbagai bahasa pengaturcaraan seperti C#, Python, JavaScript, Java dan lain-lain. Kami memilih untuk menggunakan perpustakaan Python `openai`, jadi kami akan menggunakan `pip` untuk memasangnya.

```bash
pip install openai
```

### Cipta sumber

Anda perlu melakukan langkah-langkah berikut:

- Cipta akaun di Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Dapatkan akses ke Azure OpenAI. Pergi ke [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) dan mohon akses.

  > [!NOTE]
  > Pada masa penulisan, anda perlu memohon akses ke Azure OpenAI.

- Pasang Python <https://www.python.org/>
- Telah mencipta sumber Azure OpenAI Service. Lihat panduan ini untuk cara [mencipta sumber](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Cari kunci API dan endpoint

Pada tahap ini, anda perlu memberitahu perpustakaan `openai` kunci API yang hendak digunakan. Untuk mencari kunci API anda, pergi ke bahagian "Keys and Endpoint" sumber Azure OpenAI anda dan salin nilai "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Sekarang anda telah menyalin maklumat ini, mari arahkan perpustakaan untuk menggunakannya.

> [!NOTE]
> Adalah baik untuk memisahkan kunci API anda dari kod. Anda boleh melakukannya dengan menggunakan pembolehubah persekitaran.
>
> - Tetapkan pembolehubah persekitaran `OPENAI_API_KEY` kepada kunci API anda.
>   `export OPENAI_API_KEY='sk-...'`

### Tetapkan konfigurasi Azure

Jika anda menggunakan Azure OpenAI, berikut cara anda menetapkan konfigurasi:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Di atas kita menetapkan perkara berikut:

- `api_type` kepada `azure`. Ini memberitahu perpustakaan untuk menggunakan Azure OpenAI dan bukan OpenAI.
- `api_key`, ini adalah kunci API anda yang ditemui dalam Azure Portal.
- `api_version`, ini adalah versi API yang anda mahu gunakan. Pada masa penulisan, versi terkini ialah `2023-05-15`.
- `api_base`, ini adalah endpoint API. Anda boleh menemuinya dalam Azure Portal bersebelahan kunci API anda.

> [!NOTE] > `os.getenv` adalah fungsi yang membaca pembolehubah persekitaran. Anda boleh menggunakannya untuk membaca pembolehubah persekitaran seperti `OPENAI_API_KEY` dan `API_BASE`. Tetapkan pembolehubah persekitaran ini dalam terminal anda atau dengan menggunakan perpustakaan seperti `dotenv`.

## Jana teks

Cara untuk menjana teks adalah dengan menggunakan kelas `Completion`. Berikut adalah contoh:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

Dalam kod di atas, kita mencipta objek completion dan memasukkan model yang ingin digunakan serta prompt. Kemudian kita cetak teks yang dijana.

### Chat completions

Sejauh ini, anda telah melihat bagaimana kami menggunakan `Completion` untuk menjana teks. Tetapi terdapat satu lagi kelas yang dipanggil `ChatCompletion` yang lebih sesuai untuk chatbot. Berikut adalah contoh penggunaannya:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Lebih lanjut mengenai fungsi ini dalam bab yang akan datang.

## Latihan - aplikasi penjanaan teks pertama anda

Sekarang kita telah belajar cara menyediakan dan mengkonfigurasi openai, tiba masanya untuk membina aplikasi penjanaan teks pertama anda. Untuk membina aplikasi anda, ikut langkah berikut:

1. Cipta persekitaran maya dan pasang openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Jika anda menggunakan Windows taip `venv\Scripts\activate` dan bukannya `source venv/bin/activate`.

   > [!NOTE]
   > Cari kunci Azure OpenAI anda dengan pergi ke [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) dan cari `Open AI` dan pilih `Open AI resource` kemudian pilih `Keys and Endpoint` dan salin nilai `Key 1`.

1. Cipta fail _app.py_ dan masukkan kod berikut:

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
   > Jika anda menggunakan Azure OpenAI, anda perlu menetapkan `api_type` kepada `azure` dan tetapkan `api_key` kepada kunci Azure OpenAI anda.

   Anda sepatutnya melihat output seperti berikut:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Jenis-jenis prompt yang berbeza, untuk perkara yang berbeza

Sekarang anda telah melihat cara menjana teks menggunakan prompt. Anda juga mempunyai program yang berjalan yang boleh anda ubah suai untuk menjana jenis teks yang berbeza.

Prompt boleh digunakan untuk pelbagai tugasan. Contohnya:

- **Jana jenis teks**. Contohnya, anda boleh menjana puisi, soalan untuk kuiz dan sebagainya.
- **Cari maklumat**. Anda boleh menggunakan prompt untuk mencari maklumat seperti contoh berikut 'Apa maksud CORS dalam pembangunan web?'.
- **Jana kod**. Anda boleh menggunakan prompt untuk menjana kod, contohnya membangunkan regular expression untuk mengesahkan emel atau mengapa tidak menjana keseluruhan program, seperti aplikasi web?

## Kes penggunaan yang lebih praktikal: penjana resipi

Bayangkan anda mempunyai bahan-bahan di rumah dan anda ingin memasak sesuatu. Untuk itu, anda memerlukan resipi. Cara untuk mencari resipi adalah menggunakan enjin carian atau anda boleh menggunakan LLM untuk berbuat demikian.

Anda boleh menulis prompt seperti berikut:

> "Tunjukkan saya 5 resipi untuk hidangan dengan bahan-bahan berikut: ayam, kentang, dan lobak merah. Untuk setiap resipi, senaraikan semua bahan yang digunakan"

Berdasarkan prompt di atas, anda mungkin mendapat respons yang serupa dengan:

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

Hasil ini bagus, saya tahu apa yang hendak dimasak. Pada tahap ini, penambahbaikan yang berguna adalah:

- Menapis bahan yang saya tidak suka atau alah kepadanya.
- Menghasilkan senarai membeli-belah, sekiranya saya tidak mempunyai semua bahan di rumah.

Untuk kes di atas, mari tambah prompt tambahan:

> "Sila keluarkan resipi yang mengandungi bawang putih kerana saya alah dan gantikan dengan bahan lain. Juga, sila hasilkan senarai membeli-belah untuk resipi tersebut, mengambil kira saya sudah mempunyai ayam, kentang dan lobak merah di rumah."

Kini anda mempunyai hasil baru, iaitu:

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

Itulah lima resipi anda, tanpa bawang putih dan anda juga mempunyai senarai membeli-belah mengambil kira apa yang sudah ada di rumah.

## Latihan - bina penjana resipi

Sekarang kita telah bermain dengan senario, mari tulis kod yang sepadan dengan senario yang ditunjukkan. Untuk berbuat demikian, ikut langkah berikut:

1. Gunakan fail _app.py_ yang sedia ada sebagai titik permulaan
1. Cari pembolehubah `prompt` dan ubah kodnya kepada yang berikut:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Jika anda jalankan kod sekarang, anda sepatutnya melihat output yang serupa dengan:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE, LLM anda tidak deterministik, jadi anda mungkin mendapat keputusan yang berbeza setiap kali menjalankan program.

   Bagus, mari lihat bagaimana kita boleh memperbaiki perkara. Untuk memperbaiki, kita mahu pastikan kod itu fleksibel, supaya bahan dan bilangan resipi boleh diubah dan ditambah baik.

1. Mari ubah kod seperti berikut:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Mengambil kod untuk ujian, ia boleh kelihatan seperti ini:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Perbaiki dengan menambah penapis dan senarai membeli-belah

Kini kita mempunyai aplikasi yang berfungsi mampu menghasilkan resipi dan ia fleksibel kerana bergantung pada input pengguna, baik dari segi bilangan resipi dan juga bahan yang digunakan.

Untuk memperbaikinya lagi, kita mahu menambah perkara berikut:

- **Tapis bahan**. Kita mahu dapat menapis bahan yang tidak disukai atau alahan. Untuk mencapai perubahan ini, kita boleh sunting prompt sedia ada dan tambah syarat penapis di hujungnya seperti berikut:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Di atas, kita tambah `{filter}` di hujung prompt dan juga menangkap nilai penapis dari pengguna.

  Contoh input menjalankan program kini boleh kelihatan seperti ini:

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

  Seperti yang anda lihat, sebarang resipi yang mengandungi susu telah ditapis keluar. Tetapi, jika anda intoleran laktosa, anda mungkin mahu menapis resipi yang mengandungi keju juga, jadi perlu jelas.

- **Hasilkan senarai membeli-belah**. Kita mahu menghasilkan senarai membeli-belah, mengambil kira apa yang sudah ada di rumah.

  Untuk fungsi ini, kita boleh cuba selesaikan semuanya dalam satu prompt atau kita boleh pecahkan kepada dua prompt. Mari cuba pendekatan kedua. Di sini kita mencadangkan menambah prompt tambahan, tetapi untuk itu berfungsi, kita perlu tambah hasil dari prompt pertama sebagai konteks kepada prompt kedua.

  Cari bahagian dalam kod yang mencetak hasil dari prompt pertama dan tambah kod berikut di bawahnya:

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

  Perhatikan perkara berikut:

  1. Kita membina prompt baru dengan menambah hasil dari prompt pertama ke prompt baru:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```
1. Kita membuat permintaan baru, tetapi juga mengambil kira bilangan token yang kita minta dalam arahan pertama, jadi kali ini kita tetapkan `max_tokens` kepada 1200.

```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

Mencuba kod ini, kita kini mendapat output berikut:

```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Perbaiki persediaan anda

Apa yang kita ada setakat ini adalah kod yang berfungsi, tetapi ada beberapa penyesuaian yang perlu dilakukan untuk memperbaikinya lagi. Beberapa perkara yang perlu kita lakukan adalah:

- **Pisahkan rahsia daripada kod**, seperti kunci API. Rahsia tidak patut disimpan dalam kod dan harus disimpan di tempat yang selamat. Untuk memisahkan rahsia daripada kod, kita boleh menggunakan pembolehubah persekitaran dan perpustakaan seperti `python-dotenv` untuk memuatkannya dari fail. Berikut adalah contoh bagaimana ia kelihatan dalam kod:

  1. Buat fail `.env` dengan kandungan berikut:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     
> Nota, untuk Azure, anda perlu tetapkan pembolehubah persekitaran berikut:

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

- **Sedikit tentang panjang token**. Kita perlu pertimbangkan berapa banyak token yang diperlukan untuk menjana teks yang diinginkan. Token memerlukan kos, jadi jika boleh, kita harus berjimat dengan jumlah token yang digunakan. Contohnya, bolehkah kita susun ayat arahan supaya menggunakan token yang lebih sedikit?

  Untuk mengubah jumlah token yang digunakan, anda boleh gunakan parameter `max_tokens`. Contohnya, jika anda mahu menggunakan 100 token, anda boleh lakukan:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Mencuba dengan suhu (temperature)**. Suhu adalah sesuatu yang belum kita sebutkan sebelum ini tetapi penting untuk konteks bagaimana program kita berfungsi. Semakin tinggi nilai suhu, semakin rawak output yang dihasilkan. Sebaliknya, semakin rendah nilai suhu, semakin boleh diramal outputnya. Fikirkan sama ada anda mahu variasi dalam output anda atau tidak.

  Untuk mengubah suhu, anda boleh gunakan parameter `temperature`. Contohnya, jika anda mahu menggunakan suhu 0.5, anda boleh lakukan:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Nota, semakin hampir kepada 1.0, semakin pelbagai output yang dihasilkan.

## Tugasan

Untuk tugasan ini, anda boleh pilih apa yang ingin dibina.

Berikut adalah beberapa cadangan:

- Sesuaikan aplikasi penjana resipi untuk memperbaikinya lagi. Cuba main dengan nilai suhu dan arahan untuk lihat apa yang anda boleh hasilkan.
- Bina "rakan belajar". Aplikasi ini harus boleh menjawab soalan tentang sesuatu topik, contohnya Python, anda boleh ada arahan seperti "Apa itu topik tertentu dalam Python?", atau anda boleh ada arahan yang berkata, tunjukkan saya kod untuk topik tertentu dan sebagainya.
- Bot sejarah, hidupkan sejarah, arahkan bot untuk memainkan watak sejarah tertentu dan tanya soalan tentang kehidupan dan zaman watak tersebut.

## Penyelesaian

### Rakan belajar

Di bawah adalah arahan permulaan, lihat bagaimana anda boleh gunakan dan sesuaikan mengikut citarasa anda.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Bot sejarah

Berikut adalah beberapa arahan yang anda boleh gunakan:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Semakan pengetahuan

Apakah fungsi konsep suhu (temperature)?

1. Ia mengawal sejauh mana output adalah rawak.
1. Ia mengawal saiz jawapan.
1. Ia mengawal berapa banyak token yang digunakan.

## 🚀 Cabaran

Semasa mengerjakan tugasan, cuba variasikan suhu, cuba tetapkan kepada 0, 0.5, dan 1. Ingat bahawa 0 adalah paling kurang variasi dan 1 adalah paling banyak. Nilai mana yang paling sesuai untuk aplikasi anda?

## Kerja Hebat! Teruskan Pembelajaran Anda

Selepas menamatkan pelajaran ini, lihat koleksi [Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif anda!

Teruskan ke Pelajaran 7 di mana kita akan lihat cara untuk [membina aplikasi sembang](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.