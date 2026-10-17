# Membina Aplikasi Penjanaan Teks

[![Membina Aplikasi Penjanaan Teks](../../../translated_images/ms/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Klik imej di atas untuk melihat video pelajaran ini)_

Anda telah melihat setakat ini melalui kurikulum ini bahawa terdapat konsep teras seperti prompt dan juga satu disiplin yang dikenali sebagai "prompt engineering". Banyak alat yang anda boleh berinteraksi seperti ChatGPT, Office 365, Microsoft Power Platform dan lain-lain, menyokong anda menggunakan prompt untuk mencapai sesuatu.

Untuk anda menambah pengalaman sedemikian kepada sebuah aplikasi, anda perlu memahami konsep seperti prompt, pelengkap dan memilih perpustakaan untuk digunakan. Itulah tepat apa yang akan anda pelajari dalam bab ini.

## Pengenalan

Dalam bab ini, anda akan:

- Belajar tentang perpustakaan openai dan konsep terasnya.
- Membina aplikasi penjanaan teks menggunakan openai.
- Memahami cara menggunakan konsep seperti prompt, suhu, dan token untuk membina aplikasi penjanaan teks.

## Matlamat pembelajaran

Di akhir pelajaran ini, anda akan dapat:

- Terangkan apa itu aplikasi penjanaan teks.
- Membina aplikasi penjanaan teks menggunakan openai.
- Konfigurasikan aplikasi anda untuk menggunakan lebih atau kurang token dan juga mengubah suhu, untuk output yang pelbagai.

## Apa itu aplikasi penjanaan teks?

Biasanya apabila anda membina sebuah aplikasi ia mempunyai satu jenis antara muka seperti berikut:

- Berasaskan arahan. Aplikasi konsol adalah aplikasi biasa di mana anda menaip arahan dan ia melaksanakan tugasan. Sebagai contoh, `git` adalah aplikasi berasaskan arahan.
- Antara muka pengguna (UI). Sesetengah aplikasi mempunyai antara muka grafik pengguna (GUI) di mana anda klik butang, masukkan teks, pilih pilihan dan banyak lagi.

### Aplikasi Konsol dan UI adalah Terhad

Bandingkan dengan aplikasi berasaskan arahan di mana anda menaip arahan:

- **Ia terhad**. Anda tidak boleh menaip sebarang arahan, hanya arahan yang disokong oleh aplikasi.
- **Spesifik bahasa**. Sesetengah aplikasi menyokong banyak bahasa, tetapi secara lalai aplikasi dibina untuk bahasa tertentu, walaupun anda boleh menambah sokongan bahasa.

### Manfaat aplikasi penjanaan teks

Jadi bagaimana aplikasi penjanaan teks berbeza?

Dalam aplikasi penjanaan teks, anda mempunyai lebih kebebasan, anda tidak terhad kepada set arahan atau bahasa input tertentu. Sebaliknya, anda boleh menggunakan bahasa semula jadi untuk berinteraksi dengan aplikasi. Satu lagi manfaat ialah anda sudah berinteraksi dengan sumber data yang telah dilatih pada korpus maklumat yang luas, manakala aplikasi tradisional mungkin terhad pada apa yang ada dalam pangkalan data.

### Apa yang boleh saya bina dengan aplikasi penjanaan teks?

Terdapat banyak perkara yang anda boleh bina. Sebagai contoh:

- **Sembang bot**. Sembang bot yang menjawab soalan tentang topik, seperti syarikat anda dan produk-produknya boleh menjadi padanan yang baik.
- **Pembantu**. LLM sangat bagus dalam perkara seperti meringkaskan teks, mendapatkan pandangan daripada teks, menghasilkan teks seperti resume dan banyak lagi.
- **Pembantu kod**. Bergantung pada model bahasa yang anda gunakan, anda boleh membina pembantu kod yang membantu anda menulis kod. Sebagai contoh, anda boleh menggunakan produk seperti GitHub Copilot serta ChatGPT untuk membantu anda menulis kod.

## Bagaimana saya boleh bermula?

Baik, anda perlu mencari cara untuk mengintegrasikan dengan LLM yang biasanya melibatkan dua pendekatan berikut:

- Gunakan API. Di sini anda membina permintaan web dengan prompt anda dan mendapatkan teks yang dijana kembali.
- Gunakan perpustakaan. Perpustakaan membantu mengabsahkan panggilan API dan memudahkan penggunaannya.

## Perpustakaan/SDK

Terdapat beberapa perpustakaan terkenal untuk bekerja dengan LLM seperti:

- **openai**, perpustakaan ini memudahkan untuk berhubung dengan model anda dan menghantar prompt.

Kemudian ada perpustakaan yang beroperasi pada tahap lebih tinggi seperti:

- **Langchain**. Langchain terkenal dan menyokong Python.
- **Semantic Kernel**. Semantic Kernel adalah perpustakaan oleh Microsoft yang menyokong bahasa C#, Python, dan Java.

## Aplikasi pertama menggunakan openai

Mari kita lihat bagaimana kita boleh membina aplikasi pertama kita, perpustakaan apa yang kita perlukan, berapa banyak yang diperlukan dan sebagainya.

### Pasang openai

Terdapat banyak perpustakaan di luar sana untuk berinteraksi dengan OpenAI atau Azure OpenAI. Adalah mungkin untuk menggunakan pelbagai bahasa pengaturcaraan juga seperti C#, Python, JavaScript, Java dan banyak lagi. Kami memilih untuk menggunakan perpustakaan Python `openai`, jadi kami akan menggunakan `pip` untuk memasangnya.

```bash
pip install openai
```

### Cipta sumber

Anda perlu menjalankan langkah-langkah berikut:

- Cipta akaun pada Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Dapatkan akses ke Azure OpenAI. Pergi ke [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) dan mohon akses.

  > [!NOTE]
  > Pada masa penulisan, anda perlu memohon akses ke Azure OpenAI.

- Pasang Python <https://www.python.org/>
- Telah mencipta sumber Perkhidmatan Azure OpenAI. Lihat panduan ini untuk cara [mencipta sumber](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Cari kunci API dan titik akhir

Pada ketika ini, anda perlu memberitahu perpustakaan `openai` anda kunci API apa yang hendak digunakan. Untuk mencari kunci API anda, pergi ke bahagian "Kunci dan Titik Akhir" sumber Azure OpenAI anda dan salin nilai "Key 1".

![Kunci dan Titik Akhir di portal Azure](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Sekarang anda telah menyalin maklumat ini, mari kita arahkan perpustakaan untuk menggunakannya.

> [!NOTE]
> Adalah baik untuk memisahkan kunci API anda daripada kod anda. Anda boleh melakukannya dengan menggunakan pembolehubah persekitaran.
>
> - Tetapkan pembolehubah persekitaran `OPENAI_API_KEY` kepada kunci API anda.
>   `export OPENAI_API_KEY='sk-...'`

### Tetapkan konfigurasi Azure

Jika anda menggunakan Azure OpenAI (sekarang sebahagian daripada Microsoft Foundry), berikut ialah cara anda menetapkan konfigurasi. Kami menggunakan klien standard `OpenAI` yang diarahkan ke titik akhir Azure OpenAI `/openai/v1/`, yang berfungsi dengan Responses API dan tidak memerlukan `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Di atas kami menetapkan perkara berikut:

- `api_key`, ini adalah kunci API anda yang ditemui di Portal Azure atau portal Microsoft Foundry.
- `base_url`, ini adalah titik akhir sumber Foundry anda dengan `/openai/v1/` yang dilampirkan. Titik akhir stabil v1 berfungsi merentasi OpenAI dan Azure OpenAI tanpa pengurusan `api_version`.

> [!NOTE] > `os.environ` membaca pembolehubah persekitaran. Anda boleh menggunakannya untuk membaca pembolehubah persekitaran seperti `AZURE_OPENAI_API_KEY` dan `AZURE_OPENAI_ENDPOINT`. Tetapkan pembolehubah persekitaran ini dalam terminal anda atau dengan menggunakan perpustakaan seperti `dotenv`.

## Jana teks

Cara untuk menjana teks adalah menggunakan Responses API melalui kaedah `responses.create`. Berikut adalah contoh:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

Dalam kod di atas, kami membuat respons dan memasukkan model yang kami mahu gunakan serta prompt. Kemudian kami cetak teks yang dijana melalui `response.output_text`.

### Perbualan multi-pusingan

API Respons sesuai untuk penjanaan teks satu pusingan ataupun chatbot multi-pusingan - anda menyediakan senarai mesej dalam `input` untuk membina perbualan:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Lebih lanjut mengenai fungsi ini dalam bab yang akan datang.

## Latihan - aplikasi penjanaan teks pertama anda

Sekarang kita telah belajar bagaimana untuk memasang dan mengkonfigurasi openai, tiba masa untuk membina aplikasi penjanaan teks pertama anda. Untuk membina aplikasi anda, ikut langkah berikut:

1. Cipta persekitaran maya dan pasang openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Jika anda menggunakan Windows taip `venv\Scripts\activate` bukannya `source venv/bin/activate`.

   > [!NOTE]
   > Cari kunci Azure OpenAI anda dengan pergi ke [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) dan cari `Open AI` dan pilih `Open AI resource` kemudian pilih `Keys and Endpoint` dan salin nilai `Key 1`.

1. Cipta fail _app.py_ dan masukkan kod berikut:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"

   # make a request using the Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # print response
   print(response.output_text)
   ```

   > [!NOTE]
   > Jika anda menggunakan OpenAI biasa (bukan Azure), gunakan `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (tanpa `base_url`) dan berikan nama model seperti `gpt-5-mini` bukannya nama pelaksanaan.

   Anda akan melihat output seperti berikut:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Jenis prompt yang berbeza, untuk perkara yang berbeza

Sekarang anda telah lihat bagaimana menjana teks menggunakan prompt. Anda juga sudah punyai program yang sedang berjalan yang boleh anda ubah suai untuk menjana jenis teks yang berlainan.

Prompt boleh digunakan untuk pelbagai tugasan. Contohnya:

- **Jana jenis teks**. Contohnya, anda boleh menjana sajak, soalan untuk kuiz dan sebagainya.
- **Cari maklumat**. Anda boleh guna prompt untuk cari maklumat seperti contoh 'Apa maksud CORS dalam pembangunan web?'.
- **Jana kod**. Anda boleh gunakan prompt untuk menjana kod, contohnya membangunkan ungkapan biasa untuk sahkan emel atau mengapa tidak menjana keseluruhan program seperti aplikasi web?

## Kes penggunaan yang lebih praktikal: penjana resipi

Bayangkan anda ada bahan di rumah dan mahu memasak sesuatu. Untuk itu, anda perlukan resipi. Cara untuk cari resipi adalah menggunakan enjin carian atau anda boleh gunakan LLM untuk itu.

Anda boleh tulis prompt seperti berikut:

> "Tunjukkan saya 5 resipi untuk hidangan dengan bahan berikut: ayam, kentang, dan lobak merah. Untuk setiap resipi, senaraikan semua bahan yang digunakan"

Berdasarkan prompt di atas, anda mungkin dapat respons seperti:

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

Hasil ini bagus, saya tahu apa nak masak. Pada masa ini, penambahbaikan yang berguna adalah:

- Menapis bahan yang saya tak suka atau alah.
- Menghasilkan senarai beli-belah, sekiranya saya belum ada semua bahan di rumah.

Untuk kes di atas, mari tambah prompt tambahan:

> "Sila keluarkan resipi dengan bawang putih kerana saya alah dan gantikan dengan bahan lain. Juga, sila hasilkan senarai beli-belah untuk resipi tersebut, mengambil kira saya sudah ada ayam, kentang dan lobak merah di rumah."

Kini anda ada keputusan baru, iaitu:

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

Itu adalah lima resipi anda, tanpa sebut bawang putih dan anda juga ada senarai beli-belah berdasarkan apa yang anda sudah ada di rumah.

## Latihan - bina penjana resipi

Sekarang setelah kita bermain dengan senario, mari tulis kod yang sepadan dengan senario yang telah ditunjukkan. Ikut langkah berikut:

1. Gunakan fail _app.py_ yang sedia ada sebagai titik permulaan
1. Cari pembolehubah `prompt` dan ubah kodnya kepada:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Jika anda jalankan kod sekarang, anda akan lihat output seperti:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTA, LLM anda tidak deterministik, jadi anda mungkin dapat hasil berbeza setiap kali jalankan program.

   Bagus, mari kita lihat bagaimana nak baiki keadaan. Untuk memperbaiki, kita mahu kod menjadi fleksibel supaya bahan dan bilangan resipi boleh diperbaiki dan diubah.

1. Mari ubah kod seperti berikut:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Menggunakan kod untuk ujian boleh jadi seperti ini:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Memperbaiki dengan menambah penapis dan senarai beli-belah

Kita kini ada app yang berfungsi yang boleh hasilkan resipi dan ia fleksibel kerana bergantung kepada input pengguna, baik pada bilangan resipi dan juga bahan yang digunakan.

Untuk lebih memperbaikinya, kita mahu tambah perkara berikut:

- **Tapis bahan**. Kita mahu boleh tapis bahan yang kita tak suka atau alah. Untuk buat ini, kita boleh edit prompt sedia ada dan tambah syarat tapis pada akhir seperti berikut:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Di atas, kita tambah `{filter}` pada akhir prompt dan kita juga tangkap nilai tapis dari pengguna.

  Contoh input menjalankan program kini boleh jadi seperti:

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

  Seperti yang anda lihat, resipi dengan susu telah ditapis keluar. Tetapi, jika anda intoleransi laktosa, mungkin juga mahu tapis resipi yang ada keju, jadi perlu jelas.

- **Hasilkan senarai beli-belah**. Kita mahu hasilkan senarai beli-belah, mengambil kira apa yang kita sudah ada di rumah.

  Untuk fungsi ini, kita boleh cuba selesaikan semuanya dalam satu prompt atau pisahkan kepada dua prompt. Mari cuba cara kedua. Di sini kita cadang tambah prompt tambahan, tetapi untuk itu berfungsi, kita perlu tambahkan hasil prompt pertama sebagai konteks kepada prompt kedua.

  Cari bahagian dalam kod yang cetak hasil dari prompt pertama dan tambah kod berikut di bawah:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Perhatikan perkara berikut:

  1. Kita bina prompt baru dengan tambah hasil dari prompt pertama ke prompt baru:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Kita buat permintaan baru, juga mengambil kira bilangan token yang diminta dalam prompt pertama, jadi kali ini kita set `max_output_tokens` kepada 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Menggunakan kod ini, kita dapat output berikut:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Perbaiki pemasangan anda

Apa yang kita ada setakat ini adalah kod yang berfungsi, tetapi terdapat beberapa penyesuaian yang harus kita lakukan untuk memperbaiki lagi. Beberapa perkara yang harus kita lakukan adalah:

- **Pisahkan rahsia daripada kod**, seperti kunci API. Rahsia tidak patut dimasukkan dalam kod dan harus disimpan di lokasi yang selamat. Untuk memisahkan rahsia daripada kod, kita boleh menggunakan pemboleh ubah persekitaran dan perpustakaan seperti `python-dotenv` untuk memuatkannya daripada fail. Berikut adalah bagaimana ia akan kelihatan dalam kod:

  1. Buat fail `.env` dengan kandungan berikut:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Nota, untuk Azure OpenAI dalam Microsoft Foundry, anda perlu menetapkan pemboleh ubah persekitaran berikut sebagai ganti:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Dalam kod, anda akan memuatkan pemboleh ubah persekitaran seperti berikut:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Satu kata tentang panjang token**. Kita harus mempertimbangkan berapa banyak token yang diperlukan untuk menjana teks yang kita mahu. Token memerlukan kos, jadi sebaiknya, kita cuba berjimat dalam penggunaan token. Sebagai contoh, bolehkah kita merangka arahan supaya kita dapat menggunakan token yang lebih sedikit?

  Untuk menukar bilangan token yang digunakan, anda boleh menggunakan parameter `max_output_tokens`. Contohnya, jika anda mahu menggunakan 100 token, anda boleh lakukan seperti berikut:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Bersperimen dengan suhu (temperature)**. Suhu adalah sesuatu yang belum kami sebutkan setakat ini tetapi ia adalah konteks penting bagi cara program kita berfungsi. Nilai suhu yang lebih tinggi menghasilkan output yang lebih rawak. Sebaliknya, nilai suhu yang lebih rendah menghasilkan output yang lebih boleh diramal. Pertimbangkan sama ada anda mahu variasi dalam output anda atau tidak.

  Untuk mengubah suhu, anda boleh gunakan parameter `temperature`. Sebagai contoh, jika anda mahu menggunakan suhu 0.5, anda boleh lakukan:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Nota, semakin hampir kepada 1.0, output akan lebih bervariasi.

- **Model penalaran tidak menggunakan `temperature`**. Ini adalah peralihan penting pada tahun 2026. Model semasa yang tidak dihentikan di Microsoft Foundry adalah **model penalaran** (keluarga GPT-5, siri o) - dan mereka **tidak menyokong `temperature` atau `top_p`** (dan juga tidak `max_tokens`; gunakan `max_output_tokens`). Jika anda menghantar `temperature` kepada `gpt-5-mini`, anda akan mendapat ralat "parameter tidak disokong". Jadi untuk mencuba contoh suhu di atas, gunakan model yang masih menyokong kawalan penapisan - contohnya model **Llama** terbuka seperti `Llama-3.3-70B-Instruct` dari [katalog model Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), dipanggil melalui endpoint Foundry Models / Azure AI Inference (cara yang sama seperti contoh `githubmodels-*`). Untuk model penalaran seperti GPT-5, anda mengawal output secara berbeza:
  - **Kejuruteraan prompt** - arahan yang jelas, contoh dan output yang berstruktur (lihat pelajaran [04 - Kejuruteraan Prompt](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) menggantikan fungsi kawalan penapisan.
  - **Kawalan penalaran** - parameter seperti usaha penalaran/keluasan bertukar antara kedalaman penalaran dengan kelewatan dan kos.

  Pendek kata: `temperature`/`top_p` masih sah pada banyak model (Llama, Mistral, Phi, dan keluarga GPT-4.x - walaupun GPT-4.x sedang dihentikan), tetapi hala tuju adalah kejuruteraan prompt + kawalan penalaran pada model penalaran seperti GPT-5.

## Tugasan

Untuk tugasan ini, anda boleh memilih apa yang ingin dibina.

Berikut beberapa cadangan:

- Sesuaikan aplikasi penjana resipi untuk memperbaikinya lagi. Cubalah bermain dengan nilai suhu, dan prompt untuk melihat apa yang anda boleh hasilkan.
- Bina "rakan belajar". Aplikasi ini harus boleh menjawab soalan tentang sesuatu topik contohnya Python, anda boleh buat prompt seperti "Apakah sesuatu topik dalam Python?", atau anda boleh buat prompt yang meminta kod untuk sesuatu topik itu dan sebagainya.
- Bot sejarah, jadikan sejarah hidup, arahkan bot untuk berperanan sebagai watak sejarah tertentu dan tanya tentang hidup dan zaman watak itu.

## Penyelesaian

### Rakan belajar

Di bawah adalah prompt permulaan, lihat bagaimana anda boleh menggunakannya dan mengubah suai mengikut kesukaan anda.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Bot sejarah

Berikut beberapa prompt yang anda boleh gunakan:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Semakan Pengetahuan

Apakah fungsi konsep suhu (temperature)?

1. Ia mengawal betapa rawaknya output.
1. Ia mengawal saiz respon.
1. Ia mengawal berapa banyak token digunakan.

## 🚀 Cabaran

Semasa mengerjakan tugasan, cuba ubah suhu, tetapkan kepada 0, 0.5, dan 1. Ingat bahawa 0 adalah paling kurang bervariasi dan 1 adalah paling banyak. Apakah nilai yang paling sesuai untuk aplikasi anda?

## Kerja Hebat! Teruskan Pembelajaran Anda

Selepas selesai pelajaran ini, lihat koleksi [Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif anda!

Pergi ke Pelajaran 7 di mana kita akan lihat cara untuk [membina aplikasi sembang](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->