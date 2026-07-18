# Membina Aplikasi Penjanaan Teks

[![Membina Aplikasi Penjanaan Teks](../../../translated_images/ms/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Klik imej di atas untuk menonton video pengajaran ini)_

Anda telah melihat setakat ini melalui kurikulum ini bahawa terdapat konsep teras seperti prompt dan juga satu disiplin keseluruhan yang dipanggil "kejuruteraan prompt". Banyak alat yang anda boleh berinteraksi seperti ChatGPT, Office 365, Microsoft Power Platform dan banyak lagi, menyokong anda menggunakan prompt untuk mencapai sesuatu.

Untuk anda menambah pengalaman sebegini pada aplikasi, anda perlu memahami konsep seperti prompt, penyiapan dan memilih perpustakaan untuk digunakan. Itulah tepat yang akan anda pelajari dalam bab ini.

## Pengenalan

Dalam bab ini, anda akan:

- Belajar tentang perpustakaan openai dan konsep terasnya.
- Membina aplikasi penjanaan teks menggunakan openai.
- Memahami cara menggunakan konsep seperti prompt, suhu, dan token untuk membina aplikasi penjanaan teks.

## Matlamat pembelajaran

Pada akhir pelajaran ini, anda akan dapat:

- Terangkan apa itu aplikasi penjanaan teks.
- Membina aplikasi penjanaan teks menggunakan openai.
- Konfigurasi aplikasi anda untuk menggunakan lebih atau kurang token dan juga menukar suhu, untuk output yang berbeza.

## Apa itu aplikasi penjanaan teks?

Kebiasaannya apabila anda membina aplikasi ia mempunyai sejenis antara muka seperti berikut:

- Berasaskan arahan. Aplikasi konsol adalah aplikasi tipikal di mana anda menaip arahan dan ia melaksanakan tugas. Contohnya, `git` adalah aplikasi berasaskan arahan.
- Antara muka pengguna (UI). Sesetengah aplikasi mempunyai antara muka pengguna grafik (GUI) di mana anda klik butang, masukkan teks, pilih pilihan dan banyak lagi.

### Aplikasi konsol dan UI adalah terhad

Bandingkan dengan aplikasi berasaskan arahan di mana anda menaip arahan:

- **Ia terhad**. Anda tidak boleh menaip sebarang arahan, hanya yang disokong oleh aplikasi sahaja.
- **Bersifat spesifik bahasa**. Sesetengah aplikasi menyokong banyak bahasa, tetapi secara lalai aplikasi dibina untuk satu bahasa tertentu, walaupun anda boleh menambah sokongan bahasa yang lain.

### Kelebihan aplikasi penjanaan teks

Jadi bagaimana aplikasi penjanaan teks berbeza?

Dalam aplikasi penjanaan teks, anda mempunyai lebih banyak fleksibiliti, anda tidak terhad kepada set arahan atau bahasa input tertentu. Sebaliknya, anda boleh menggunakan bahasa semula jadi untuk berinteraksi dengan aplikasi. Satu lagi kelebihan ialah anda sudah berinteraksi dengan sumber data yang telah dilatih pada korpus maklumat yang sangat besar, manakala aplikasi tradisional mungkin terhad pada apa yang ada dalam pangkalan data.

### Apa yang saya boleh bina dengan aplikasi penjanaan teks?

Terdapat banyak benda yang anda boleh bina. Contohnya:

- **Chatbot**. Chatbot yang menjawab soalan tentang topik-topik, seperti syarikat anda dan produk-produknya boleh menjadi padanan yang baik.
- **Pembantu**. LLM hebat dalam perkara seperti meringkaskan teks, mendapatkan insight dari teks, menghasilkan teks seperti resume dan banyak lagi.
- **Pembantu kod**. Bergantung pada model bahasa yang anda gunakan, anda boleh membina pembantu kod yang membantu anda menulis kod. Sebagai contoh, anda boleh menggunakan produk seperti GitHub Copilot serta ChatGPT untuk membantu anda menulis kod.

## Bagaimana saya boleh mula?

Nah, anda perlu mencari cara untuk berintegrasi dengan LLM yang biasanya melibatkan dua pendekatan berikut:

- Gunakan API. Di sini anda membina permintaan web dengan prompt anda dan mendapat teks yang dijana kembali.
- Gunakan perpustakaan. Perpustakaan membantu memuatkan panggilan API dan memudahkan penggunaannya.

## Perpustakaan/SDK

Terdapat beberapa perpustakaan terkenal untuk bekerja dengan LLM seperti:

- **openai**, perpustakaan ini memudahkan untuk berhubung dengan model anda dan menghantar prompt.

Kemudian terdapat perpustakaan yang beroperasi pada tahap lebih tinggi seperti:

- **Langchain**. Langchain terkenal dan menyokong Python.
- **Semantic Kernel**. Semantic Kernel adalah perpustakaan oleh Microsoft yang menyokong bahasa C#, Python, dan Java.

## Aplikasi pertama menggunakan openai

Mari lihat bagaimana kita membina aplikasi pertama kita, apa perpustakaan yang kita perlukan, berapa banyak diperlukan dan lain-lain.

### Pasang openai

Terdapat banyak perpustakaan di luar sana untuk berinteraksi dengan OpenAI atau Azure OpenAI. Ia mungkin digunakan dengan banyak bahasa pengaturcaraan juga seperti C#, Python, JavaScript, Java dan banyak lagi. Kami memilih untuk menggunakan perpustakaan Python `openai`, jadi kami akan menggunakan `pip` untuk memasangnya.

```bash
pip install openai
```

### Cipta sumber

Anda perlu melakukan langkah-langkah berikut:

- Daftar akaun di Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Mendapat akses ke Azure OpenAI. Pergi ke [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) dan mohon akses.

  > [!NOTE]
  > Pada masa penulisan, anda perlu memohon akses ke Azure OpenAI.

- Pasang Python <https://www.python.org/>
- Telah mencipta sumber Perkhidmatan Azure OpenAI. Lihat panduan ini tentang cara [mencipta sumber](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Cari kunci API dan titik akhir

Pada ketika ini, anda perlu memberitahu perpustakaan `openai` kunci API yang hendak digunakan. Untuk mencari kunci API anda, pergi ke bahagian "Keys and Endpoint" pada sumber Azure OpenAI anda dan salin nilai "Key 1".

![Papan kunci Keys and Endpoint pada Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Sekarang anda telah menyalin maklumat ini, mari arahkan perpustakaan untuk menggunakannya.

> [!NOTE]
> Ada baiknya memisahkan kunci API anda dari kod anda. Anda boleh melakukannya dengan menggunakan pembolehubah persekitaran.
>
> - Tetapkan pembolehubah persekitaran `OPENAI_API_KEY` kepada kunci API anda.
>   `export OPENAI_API_KEY='sk-...'`

### Sediakan konfigurasi Azure

Jika anda menggunakan Azure OpenAI (sekarang sebahagian daripada Microsoft Foundry), berikut cara anda menyediakan konfigurasi. Kami menggunakan klien `OpenAI` standard yang ditunjukkan ke titik akhir Azure OpenAI `/openai/v1/`, yang berfungsi dengan API Respons dan tidak memerlukan `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Di atas kami menetapkan perkara berikut:

- `api_key`, ini adalah kunci API anda yang dijumpai dalam Azure Portal atau portal Microsoft Foundry.
- `base_url`, ini adalah titik akhir sumber Foundry anda dengan ditambah `/openai/v1/`. Titik akhir v1 yang stabil berfungsi antara OpenAI dan Azure OpenAI tanpa pengurusan `api_version`.

> [!NOTE] > `os.environ` membaca pembolehubah persekitaran. Anda boleh menggunakannya untuk membaca pembolehubah persekitaran seperti `AZURE_OPENAI_API_KEY` dan `AZURE_OPENAI_ENDPOINT`. Tetapkan pembolehubah persekitaran ini dalam terminal anda atau dengan menggunakan perpustakaan seperti `dotenv`.

## Jana teks

Cara untuk menjana teks adalah menggunakan API Respons melalui kaedah `responses.create`. Berikut adalah contohnya:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # ini adalah nama penyebaran model anda
    input=prompt,
    store=False,
)
print(response.output_text)
```

Dalam kod di atas, kami mencipta satu respons dan menghantar model yang kami ingin gunakan dan prompt. Kemudian kami cetak teks yang dijana melalui `response.output_text`.

### Perbualan berbilang giliran

API Respons sangat sesuai untuk kedua-dua penjanaan teks satu giliran dan chatbot berbilang giliran - anda menyediakan senarai mesej dalam `input` untuk membina perbualan:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Lebih lanjut mengenai fungsi ini dalam bab yang akan datang.

## Latihan - aplikasi penjanaan teks pertama anda

Sekarang kita telah belajar bagaimana menyediakan dan mengkonfigurasi openai, tiba masanya untuk membina aplikasi penjanaan teks pertama anda. Untuk membina aplikasi anda, ikuti langkah-langkah berikut:

1. Cipta persekitaran maya dan pasang openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Jika anda menggunakan Windows taip `venv\Scripts\activate` dan bukannya `source venv/bin/activate`.

   > [!NOTE]
   > Cari kunci Azure OpenAI anda dengan pergi ke [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) dan cari `Open AI` dan pilih `Open AI resource` dan kemudian pilih `Keys and Endpoint` dan salin nilai `Key 1`.

1. Cipta fail _app.py_ dan beri kod berikut:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # tambah kod penyelesaian anda
   prompt = "Complete the following: Once upon a time there was a"

   # buat permintaan menggunakan API Responses
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # cetak respons
   print(response.output_text)
   ```

   > [!NOTE]
   > Jika anda menggunakan OpenAI biasa (bukan Azure), gunakan `client = OpenAI(api_key="<ganti nilai ini dengan kunci OpenAI anda>")` (tiada `base_url`) dan beri nama model seperti `gpt-5-mini` dan bukannya nama penyebaran.

   Anda sepatutnya melihat output seperti berikut:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Jenis-jenis prompt berbeza, untuk perkara berbeza

Kini anda telah melihat bagaimana menjana teks menggunakan prompt. Anda malah ada program berjalan yang boleh anda ubah dan tukar untuk menjana jenis teks yang berbeza.

Prompt boleh digunakan untuk pelbagai tugasan. Contohnya:

- **Jana sejenis teks**. Contohnya, anda boleh menjana puisi, soalan untuk kuiz dan sebagainya.
- **Cari maklumat**. Anda boleh menggunakan prompt untuk mencari maklumat seperti contoh berikut 'Apa maksud CORS dalam pembangunan web?'.
- **Jana kod**. Anda boleh menggunakan prompt untuk menjana kod, contohnya membangunkan ekspresi reguler untuk mengesahkan email atau kenapa tidak jana keseluruhan program, seperti aplikasi web?

## Kes penggunaan yang lebih praktikal: penjana resipi

Bayangkan anda mempunyai bahan di rumah dan anda mahu memasak sesuatu. Untuk itu, anda perlukan resipi. Cara untuk mencari resipi adalah menggunakan enjin carian atau anda boleh menggunakan LLM untuk berbuat demikian.

Anda boleh menulis prompt seperti berikut:

> "Tunjukkan saya 5 resipi hidangan dengan bahan-bahan berikut: ayam, kentang, dan lobak merah. Setiap resipi, senaraikan semua bahan yang digunakan"

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

Hasil ini hebat, saya tahu apa yang nak dimasak. Pada ketika ini, apa yang boleh menjadi penambahbaikan ialah:

- Menapis bahan yang saya tidak suka atau saya alah kepadanya.
- Hasilkan senarai beli-belah, sekiranya saya tidak mempunyai semua bahan di rumah.

Untuk kes di atas, mari tambah prompt tambahan:

> "Sila keluarkan resipi yang mengandungi bawang putih kerana saya alah dan gantikan dengan sesuatu yang lain. Juga, sila hasilkan senarai beli-belah untuk resipi, memandangkan saya sudah ada ayam, kentang dan lobak merah di rumah."

Kini anda mempunyai keputusan baru, iaitu:

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

Itulah lima resipi anda, tanpa bawang putih disebut dan anda juga mempunyai senarai beli-belah dengan mengambil kira apa yang sudah ada di rumah.

## Latihan - bina penjana resipi

Kini bahawa kita telah meluahkan satu senario, mari tulis kod untuk memadankan senario yang didemonstrasikan. Untuk berbuat demikian, ikuti langkah berikut:

1. Gunakan fail _app.py_ yang sedia ada sebagai titik permulaan
1. Cari pemboleh ubah `prompt` dan tukar kodnya kepada yang berikut:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Jika anda jalankan kod ini sekarang, anda sepatutnya melihat output yang serupa dengan:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > PERHATIAN, LLM anda bersifat nondeterministik, jadi anda mungkin mendapat keputusan berbeza setiap kali anda jalankan program.

   Hebat, mari lihat bagaimana kita boleh memperbaiki perkara. Untuk memperbaiki perkara, kita mahu pastikan kod itu fleksibel, jadi bahan dan bilangan resipi boleh diperbaiki dan diubah.

1. Mari tukar kod dengan cara berikut:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolatekan bilangan resipi ke dalam prompt dan bahan-bahan
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Menjalankan kod untuk ujian boleh nampak seperti ini:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Tingkatkan dengan menambah penapis dan senarai beli-belah

Kita kini mempunyai aplikasi berfungsi yang mampu menghasilkan resipi dan ia fleksibel kerana bergantung pada input dari pengguna, kedua-dua bilangan resipi dan juga bahan yang digunakan.

Untuk memperbaikinya lagi, kita mahu tambah perkara berikut:

- **Tapis bahan**. Kita mahu dapat menapis bahan yang kita tidak suka atau alah kepadanya. Untuk melaksanakan perubahan ini, kita boleh edit prompt sedia ada dan tambah syarat penapis di hujungnya seperti berikut:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Di atas, kita tambah `{filter}` di hujung prompt dan kita juga menangkap nilai penapis dari pengguna.

  Contoh input menjalankan program kini boleh kelihatan seperti:

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

  Seperti yang anda lihat, mana-mana resipi yang mengandungi susu telah ditapis keluar. Tetapi, jika anda intoleran laktosa, anda mungkin mahu menapis resipi yang mengandungi keju juga, jadi perlu dijelaskan.


- **Hasilkan senarai barang belian**. Kita mahu menghasilkan senarai barang belian, mengambil kira apa yang sudah kita miliki di rumah.

  Untuk fungsi ini, kita boleh cuba selesaikan semuanya dalam satu arahan atau kita boleh pecahkan kepada dua arahan. Mari cuba pendekatan yang kedua. Di sini kami mencadangkan menambah arahan tambahan, tetapi untuk itu berfungsi, kita perlu menambah hasil dari arahan pertama sebagai konteks kepada arahan yang kedua.

  Cari bahagian dalam kod yang mencetak hasil dari arahan pertama dan tambah kod berikut di bawahnya:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # cetak respons
  print("Shopping list:")
  print(response.output_text)
  ```

  Perhatikan perkara berikut:

  1. Kita sedang membina arahan baru dengan menambah hasil dari arahan pertama kepada arahan baru:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Kita membuat permintaan baru, tetapi juga mengambil kira bilangan token yang kita minta dalam arahan pertama, jadi kali ini kita tetapkan `max_output_tokens` kepada 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Dengan mencuba kod ini, kita kini mendapat output berikut:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Tingkatkan persediaan anda

Apa yang kita ada setakat ini adalah kod yang berfungsi, tetapi ada beberapa penyesuaian yang perlu kita lakukan untuk memperbaikinya lagi. Beberapa perkara yang perlu dilakukan adalah:

- **Pisahkan rahsia dari kod**, seperti kunci API. Rahsia tidak patut berada dalam kod dan harus disimpan di lokasi yang selamat. Untuk memisahkan rahsia dari kod, kita boleh menggunakan pembolehubah persekitaran dan perpustakaan seperti `python-dotenv` untuk memuatkannya dari fail. Ini adalah bagaimana ia kelihatan dalam kod:

  1. Cipta fail `.env` dengan kandungan berikut:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Nota, untuk Azure OpenAI dalam Microsoft Foundry, anda perlu tetapkan pembolehubah persekitaran berikut sebagai gantinya:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Dalam kod, anda akan memuatkan pembolehubah persekitaran seperti ini:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Perkataan tentang panjang token**. Kita harus mempertimbangkan berapa banyak token yang kita perlukan untuk menghasilkan teks yang kita mahukan. Token memerlukan bayaran, jadi seboleh mungkin, kita harus cuba berjimat dengan jumlah token yang digunakan. Contohnya, bolehkah kita menyusun arahan supaya kita boleh menggunakan token yang lebih sedikit?

  Untuk mengubah jumlah token digunakan, anda boleh guna parameter `max_output_tokens`. Contohnya, jika anda mahu gunakan 100 token, anda boleh buat:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Mencuba dengan suhu (temperature)**. Suhu adalah sesuatu yang belum kita sebut tapi penting untuk konteks bagaimana program kita berfungsi. Nilai suhu yang lebih tinggi menyebabkan output lebih rawak. Sebaliknya, nilai suhu yang lebih rendah menyebabkan output lebih boleh diramal. Fikirkan sama ada anda mahu variasi dalam output atau tidak.

  Untuk mengubah suhu, anda boleh gunakan parameter `temperature`. Contohnya, jika anda mahu gunakan suhu 0.5, anda boleh buat:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Nota, semakin dekat kepada 1.0, semakin pelbagai output yang dihasilkan.

- **Model berfikir tidak menggunakan `temperature`**. Ini adalah perubahan penting pada tahun 2026. Model terkini yang tidak ditandakan usang di Microsoft Foundry adalah **model berfikir** (keluarga GPT-5, siri o) - dan mereka **tidak menyokong `temperature` atau `top_p`** (juga tidak `max_tokens`; gunakan `max_output_tokens`). Jika anda hantar `temperature` kepada `gpt-5-mini` anda akan mendapat ralat "parameter tidak disokong". Jadi untuk cuba contoh suhu di atas, arahkan kepada model yang masih menyokong kawalan pemilihan - contohnya model **Llama** terbuka seperti `Llama-3.3-70B-Instruct` dari [katalog model Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), dipanggil melalui Titik Akhir Foundry Models / Azure AI Inference (cara yang sama seperti sampel `githubmodels-*`). Untuk model berfikir seperti GPT-5, anda mengarah output secara berbeza:
  - **Reka bentuk prompt** - arahan jelas, contoh, dan output berstruktur (lihat pelajaran [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) melakukan kerja yang sebelumnya dilakukan oleh butang sampling.
  - **Kawalan berfikir** - parameter seperti usaha/verbosity berfikir menyeimbangkan kedalaman pemikiran dengan kelewatan dan kos.

  Secara ringkas: `temperature`/`top_p` masih sah pada banyak model (Llama, Mistral, Phi, dan keluarga GPT-4.x - walaupun GPT-4.x sedang dihentikan), tetapi arah pembangunan adalah reka bentuk prompt + kawalan berfikir pada model berfikir seperti GPT-5.

## Tugasan

Untuk tugasan ini, anda boleh memilih apa yang ingin dibina.

Berikut adalah beberapa cadangan:

- Ubah suai aplikasi penjana resipi untuk memperbaikinya lagi. Cuba nilai suhu (temperature) dan arahan untuk lihat apa yang boleh anda hasilkan.
- Bina "rakan belajar". Aplikasi ini harus mampu menjawab soalan tentang satu topik contohnya Python, anda boleh buat arahan seperti "Apa itu topik tertentu dalam Python?", atau anda boleh buat arahan yang berkata, tunjukkan saya kod untuk topik tertentu dan sebagainya.
- Bot sejarah, hidupkan sejarah, arahkan bot untuk bermain watak sejarah tertentu dan tanya soalan tentang kehidupannya dan zamannya.

## Penyelesaian

### Rakan belajar

Berikut adalah contoh arahan permulaan, lihat bagaimana anda boleh gunakan dan ubah suai mengikut kesukaan anda.

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

## Pemeriksaan pengetahuan

Apakah fungsi konsep suhu (temperature)?

1. Ia mengawal berapa rawak outputnya.
1. Ia mengawal berapa besar responsnya.
1. Ia mengawal berapa banyak token yang digunakan.

## 🚀 Cabaran

Semasa mengerjakan tugasan, cuba variasikan suhu, cuba tetapkan kepada 0, 0.5, dan 1. Ingat bahawa 0 adalah paling kurang variasi dan 1 adalah paling banyak. Apakah nilai yang paling sesuai untuk aplikasi anda?

## Kerja Bagus! Teruskan Pembelajaran Anda

Selepas menyelesaikan pelajaran ini, lihat koleksi [Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk terus meningkatkan pengetahuan AI Generatif anda!

Teruskan ke Pelajaran 7 di mana kita akan melihat bagaimana [membina aplikasi sembang](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->