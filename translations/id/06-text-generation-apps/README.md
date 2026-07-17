# Membangun Aplikasi Generasi Teks

[![Membangun Aplikasi Generasi Teks](../../../translated_images/id/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Klik gambar di atas untuk melihat video pelajaran ini)_

Anda sudah melihat sejauh ini melalui kurikulum ini bahwa ada konsep inti seperti prompt dan bahkan disiplin tersendiri yang disebut "rekayasa prompt". Banyak alat yang dapat Anda interaksikan seperti ChatGPT, Office 365, Microsoft Power Platform dan lainnya, mendukung Anda menggunakan prompt untuk menyelesaikan sesuatu.

Agar Anda dapat menambahkan pengalaman seperti itu ke sebuah aplikasi, Anda perlu memahami konsep seperti prompt, penyelesaian (completion) dan memilih perpustakaan untuk digunakan. Itulah tepatnya yang akan Anda pelajari di bab ini.

## Pendahuluan

Dalam bab ini, Anda akan:

- Mempelajari tentang perpustakaan openai dan konsep intinya.
- Membangun aplikasi generasi teks menggunakan openai.
- Memahami cara menggunakan konsep seperti prompt, temperature, dan token untuk membangun aplikasi generasi teks.

## Tujuan pembelajaran

Di akhir pelajaran ini, Anda akan bisa:

- Menjelaskan apa itu aplikasi generasi teks.
- Membangun aplikasi generasi teks menggunakan openai.
- Mengonfigurasi aplikasi Anda untuk menggunakan lebih banyak atau lebih sedikit token dan juga mengubah temperature, untuk keluaran yang bervariasi.

## Apa itu aplikasi generasi teks?

Biasanya ketika Anda membangun sebuah aplikasi, aplikasi tersebut memiliki beberapa jenis antarmuka seperti berikut:

- Berbasis perintah. Aplikasi konsol adalah aplikasi tipikal dimana Anda mengetik sebuah perintah dan aplikasi melakukan tugas. Misalnya, `git` adalah aplikasi berbasis perintah.
- Antarmuka pengguna (UI). Beberapa aplikasi memiliki antarmuka pengguna grafis (GUI) dimana Anda mengklik tombol, memasukkan teks, memilih opsi dan banyak lagi.

### Aplikasi konsol dan UI terbatas

Bandingkan dengan aplikasi berbasis perintah dimana Anda mengetik perintah:

- **Ini terbatas**. Anda tidak bisa sembarang mengetik perintah, hanya perintah yang didukung aplikasi.
- **Spesifik bahasa**. Beberapa aplikasi mendukung banyak bahasa, tapi secara default aplikasi dibuat untuk bahasa tertentu, meskipun Anda bisa menambahkan dukungan bahasa lain.

### Manfaat aplikasi generasi teks

Jadi bagaimana aplikasi generasi teks berbeda?

Dalam aplikasi generasi teks, Anda memiliki lebih banyak fleksibilitas, Anda tidak dibatasi oleh sekumpulan perintah atau bahasa input tertentu. Sebagai gantinya, Anda dapat menggunakan bahasa alami untuk berinteraksi dengan aplikasi. Manfaat lainnya adalah Anda sudah berinteraksi dengan sumber data yang telah dilatih pada korpus informasi yang luas, sedangkan aplikasi tradisional mungkin terbatas pada apa yang ada di database.

### Apa yang bisa saya bangun dengan aplikasi generasi teks?

Ada banyak hal yang bisa Anda bangun. Contohnya:

- **Chatbot**. Sebuah chatbot yang menjawab pertanyaan tentang topik, seperti perusahaan Anda dan produknya bisa menjadi pilihan tepat.
- **Asisten**. LLM sangat hebat pada hal-hal seperti merangkum teks, mendapatkan wawasan dari teks, menghasilkan teks seperti resume dan banyak lagi.
- **Asisten kode**. Bergantung pada model bahasa yang Anda gunakan, Anda bisa membangun asisten kode yang membantu menulis kode. Misalnya, Anda bisa menggunakan produk seperti GitHub Copilot serta ChatGPT untuk membantu menulis kode.

## Bagaimana saya bisa memulai?

Nah, Anda perlu mencari cara untuk mengintegrasikan dengan LLM yang biasanya melibatkan dua pendekatan berikut:

- Menggunakan API. Di sini Anda membentuk permintaan web dengan prompt Anda dan mendapatkan teks yang dihasilkan sebagai respons.
- Menggunakan perpustakaan. Perpustakaan membantu membungkus panggilan API dan membuatnya lebih mudah digunakan.

## Perpustakaan/SDK

Ada beberapa perpustakaan terkenal untuk bekerja dengan LLM seperti:

- **openai**, perpustakaan ini memudahkan untuk terhubung ke model Anda dan mengirim prompt.

Kemudian ada perpustakaan yang beroperasi pada tingkat lebih tinggi seperti:

- **Langchain**. Langchain terkenal dan mendukung Python.
- **Semantic Kernel**. Semantic Kernel adalah perpustakaan dari Microsoft yang mendukung bahasa C#, Python, dan Java.

## Aplikasi pertama menggunakan openai

Mari kita lihat bagaimana kita dapat membangun aplikasi pertama kita, perpustakaan apa yang dibutuhkan, berapa banyak yang dibutuhkan, dan sebagainya.

### Pasang openai

Ada banyak perpustakaan untuk berinteraksi dengan OpenAI atau Azure OpenAI. Bisa menggunakan berbagai bahasa pemrograman seperti C#, Python, JavaScript, Java dan lainnya. Kami memilih menggunakan perpustakaan `openai` Python, jadi kami akan menggunakan `pip` untuk memasangnya.

```bash
pip install openai
```

### Buat sumber daya

Anda perlu melakukan langkah-langkah berikut:

- Buat akun di Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Mendapatkan akses ke Azure OpenAI. Pergi ke [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) dan ajukan permintaan akses.

  > [!NOTE]
  > Pada saat tulisan ini dibuat, Anda perlu mengajukan akses ke Azure OpenAI.

- Pasang Python <https://www.python.org/>
- Sudah membuat sumber daya Layanan Azure OpenAI. Lihat panduan ini tentang cara [membuat sumber daya](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Temukan kunci API dan endpoint

Pada titik ini, Anda perlu memberitahu perpustakaan `openai` kunci API mana yang akan digunakan. Untuk menemukan kunci API Anda, pergi ke bagian "Keys and Endpoint" dari sumber daya Azure OpenAI Anda dan salin nilai "Key 1".

![Keys and Endpoint resource blade di Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Sekarang setelah Anda menyalin informasi ini, mari instruksikan perpustakaan untuk menggunakannya.

> [!NOTE]
> Ada baiknya memisahkan kunci API dari kode Anda. Anda dapat melakukannya dengan menggunakan variabel lingkungan.
>
> - Atur variabel lingkungan `OPENAI_API_KEY` ke kunci API Anda.
>   `export OPENAI_API_KEY='sk-...'`

### Pengaturan konfigurasi Azure

Jika Anda menggunakan Azure OpenAI (sekarang bagian dari Microsoft Foundry), berikut cara mengatur konfigurasi. Kami menggunakan klien standar `OpenAI` yang diarahkan ke endpoint Azure OpenAI `/openai/v1/`, yang berfungsi dengan Responses API dan tidak memerlukan `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Di atas kami mengatur hal berikut:

- `api_key`, ini adalah kunci API Anda yang ditemukan di Azure Portal atau portal Microsoft Foundry.
- `base_url`, ini adalah endpoint sumber daya Foundry Anda dengan `/openai/v1/` yang ditambahkan. Endpoint v1 stabil ini berfungsi di OpenAI dan Azure OpenAI tanpa pengelolaan `api_version`.

> [!NOTE] > `os.environ` membaca variabel lingkungan. Anda dapat menggunakannya untuk membaca variabel lingkungan seperti `AZURE_OPENAI_API_KEY` dan `AZURE_OPENAI_ENDPOINT`. Atur variabel lingkungan ini di terminal Anda atau menggunakan perpustakaan seperti `dotenv`.

## Menghasilkan teks

Cara menghasilkan teks adalah dengan menggunakan Responses API melalui metode `responses.create`. Berikut contohnya:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # ini adalah nama deployment model Anda
    input=prompt,
    store=False,
)
print(response.output_text)
```

Dalam kode di atas, kami membuat respons dan memasukkan model yang ingin digunakan serta prompt-nya. Kemudian kami mencetak teks yang dihasilkan melalui `response.output_text`.

### Percakapan multi-giliran (multi-turn)

Responses API sangat cocok untuk kedua kasus generasi teks satu giliran dan chatbot multi-giliran - Anda memberikan daftar pesan di `input` untuk membangun percakapan:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Lebih lanjut tentang fungsionalitas ini di bab yang akan datang.

## Latihan - aplikasi generasi teks pertama Anda

Sekarang kita telah belajar cara mengatur dan mengonfigurasi openai, saatnya membangun aplikasi generasi teks pertama Anda. Untuk membangun aplikasi Anda, ikuti langkah-langkah ini:

1. Buat lingkungan virtual dan pasang openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Jika Anda menggunakan Windows ketik `venv\Scripts\activate` sebagai gantinya `source venv/bin/activate`.

   > [!NOTE]
   > Temukan kunci Azure OpenAI Anda dengan pergi ke [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) dan cari `Open AI` lalu pilih `Open AI resource` dan kemudian pilih `Keys and Endpoint` dan salin nilai `Key 1`.

1. Buat file _app.py_ dan masukkan kode berikut:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # tambahkan kode penyelesaian Anda
   prompt = "Complete the following: Once upon a time there was a"

   # buat permintaan menggunakan API Respons
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # cetak respons
   print(response.output_text)
   ```

   > [!NOTE]
   > Jika Anda menggunakan OpenAI biasa (bukan Azure), gunakan `client = OpenAI(api_key="<ganti nilai ini dengan kunci OpenAI Anda>")` (tanpa `base_url`) dan berikan nama model seperti `gpt-5-mini` alih-alih nama implementasi.

   Anda akan melihat keluaran seperti berikut:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Jenis prompt yang berbeda, untuk hal yang berbeda

Sekarang Anda sudah melihat bagaimana menghasilkan teks menggunakan prompt. Anda bahkan sudah memiliki program berjalan yang bisa Anda modifikasi dan ubah untuk menghasilkan berbagai jenis teks.

Prompt dapat digunakan untuk berbagai tugas. Misalnya:

- **Menghasilkan jenis teks**. Misalnya, Anda bisa menghasilkan puisi, pertanyaan untuk kuis dll.
- **Mencari informasi**. Anda dapat menggunakan prompt untuk mencari informasi seperti contoh berikut 'Apa arti CORS dalam pengembangan web?'.
- **Menghasilkan kode**. Anda bisa menggunakan prompt untuk menghasilkan kode, misalnya membuat ekspresi reguler untuk memvalidasi email atau mengapa tidak menghasilkan program lengkap, seperti aplikasi web?

## Kasus penggunaan yang lebih praktis: generator resep

Bayangkan Anda memiliki bahan di rumah dan ingin memasak sesuatu. Untuk itu, Anda membutuhkan resep. Cara menemukan resep adalah menggunakan mesin pencari atau Anda bisa menggunakan LLM untuk melakukannya.

Anda bisa menulis prompt seperti ini:

> "Tunjukkan 5 resep untuk hidangan dengan bahan berikut: ayam, kentang, dan wortel. Per resep, sebutkan semua bahan yang digunakan"

Mengingat prompt di atas, Anda mungkin mendapatkan jawaban yang mirip dengan:

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

Hasil ini bagus, saya tahu apa yang akan dimasak. Saat ini, apa yang bisa menjadi perbaikan berguna adalah:

- Memfilter bahan yang tidak saya suka atau yang saya alergi.
- Membuat daftar belanja, jika saya tidak memiliki semua bahan di rumah.

Untuk kasus di atas, mari tambahkan prompt tambahan:

> "Tolong hilangkan resep dengan bawang putih karena saya alergi dan ganti dengan bahan lain. Juga, tolong buat daftar belanja untuk resep-resep tersebut, mengingat saya sudah punya ayam, kentang, dan wortel di rumah."

Kini Anda memiliki hasil baru, yaitu:

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

Itu adalah lima resep Anda, tanpa bawang putih dan Anda juga mendapatkan daftar belanja dengan memperhitungkan apa yang sudah ada di rumah.

## Latihan - buat generator resep

Sekarang kita telah memainkan sebuah skenario, mari kita tulis kode untuk menyesuaikan skenario yang ditunjukkan. Untuk itu, ikuti langkah-langkah berikut:

1. Gunakan file _app.py_ yang ada sebagai titik awal
1. Temukan variabel `prompt` dan ubah kodenya menjadi seperti berikut:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Jika Anda menjalankan kode sekarang, Anda akan melihat keluaran seperti:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > CATATAN, LLM Anda nondeterministik, jadi Anda mungkin mendapatkan hasil berbeda setiap kali menjalankan program.

   Bagus, mari kita lihat bagaimana kita bisa memperbaiki hal ini. Untuk memperbaiki, kita ingin memastikan kode fleksibel, sehingga bahan dan jumlah resep bisa ditingkatkan dan diubah.

1. Mari kita ubah kodenya seperti berikut:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolasi jumlah resep ke dalam prompt dan bahan-bahan
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Mengambil kode untuk uji coba, bisa terlihat seperti ini:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Tingkatkan dengan menambah filter dan daftar belanja

Kita sekarang memiliki aplikasi yang bekerja mampu menghasilkan resep dan cukup fleksibel karena bergantung pada input pengguna, baik pada jumlah resep maupun bahan yang digunakan.

Untuk memperbaikinya lebih lanjut, kita ingin menambahkan hal berikut:

- **Memfilter bahan**. Kita ingin dapat memfilter bahan yang tidak kita suka atau yang kita alergi. Untuk perubahan ini, kita bisa mengedit prompt yang ada dan menambahkan kondisi filter di akhir prompt seperti ini:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Di atas, kita menambahkan `{filter}` di akhir prompt dan juga menangkap nilai filter dari pengguna.

  Contoh masukan saat menjalankan program sekarang bisa seperti ini:

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

  Seperti yang Anda lihat, resep dengan susu sudah disaring keluar. Namun, jika Anda intoleran laktosa, Anda mungkin ingin juga menyaring resep dengan keju, jadi perlu kejelasan.


- **Buat daftar belanja**. Kita ingin membuat daftar belanja, dengan mempertimbangkan apa yang sudah kita miliki di rumah.

  Untuk fungsi ini, kita bisa mencoba menyelesaikan semuanya dalam satu prompt atau kita bisa membaginya menjadi dua prompt. Mari coba pendekatan yang kedua. Di sini kami menyarankan menambahkan prompt tambahan, tapi untuk itu berhasil, kita perlu menambahkan hasil dari prompt sebelumnya sebagai konteks pada prompt berikutnya.

  Temukan bagian dalam kode yang mencetak hasil dari prompt pertama dan tambahkan kode berikut di bawahnya:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # cetak respons
  print("Shopping list:")
  print(response.output_text)
  ```

  Perhatikan hal berikut:

  1. Kami membangun prompt baru dengan menambahkan hasil dari prompt pertama ke prompt baru:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Kami membuat permintaan baru, tapi juga mempertimbangkan jumlah token yang diminta pada prompt pertama, jadi kali ini kami mengatakan `max_output_tokens` adalah 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Dengan mencoba kode ini, kita sekarang mendapatkan output sebagai berikut:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Tingkatkan pengaturan Anda

Apa yang kita miliki sejauh ini adalah kode yang berfungsi, tetapi ada beberapa penyesuaian yang harus kita lakukan untuk meningkatkan semuanya lebih lanjut. Beberapa hal yang harus kita lakukan adalah:

- **Pisahkan rahasia dari kode**, seperti kunci API. Rahasia tidak boleh ada di dalam kode dan harus disimpan di tempat yang aman. Untuk memisahkan rahasia dari kode, kita bisa menggunakan variabel lingkungan dan pustaka seperti `python-dotenv` untuk memuatnya dari file. Berikut adalah bagaimana itu terlihat dalam kode:

  1. Buat file `.env` dengan isi berikut:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Catatan, untuk Azure OpenAI di Microsoft Foundry, Anda perlu mengatur variabel lingkungan berikut sebagai gantinya:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Dalam kode, Anda akan memuat variabel lingkungan seperti ini:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Sedikit kata tentang panjang token**. Kita harus mempertimbangkan berapa banyak token yang kita butuhkan untuk menghasilkan teks yang kita inginkan. Token berbiaya uang, jadi bila memungkinkan, kita harus mencoba hemat dengan jumlah token yang digunakan. Misalnya, bisakah kita mengubah prompt sehingga kita bisa menggunakan token lebih sedikit?

  Untuk mengubah jumlah token yang digunakan, Anda dapat menggunakan parameter `max_output_tokens`. Misalnya, jika Anda ingin menggunakan 100 token, Anda akan melakukan:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Bereksperimen dengan temperature**. Temperature adalah sesuatu yang belum kami sebutkan sejauh ini tetapi merupakan konteks penting bagi bagaimana program kami bekerja. Semakin tinggi nilai temperature semakin acak outputnya. Sebaliknya semakin rendah nilai temperature semakin dapat diprediksi outputnya. Pertimbangkan apakah Anda menginginkan variasi dalam output atau tidak.

  Untuk mengubah temperature, Anda dapat menggunakan parameter `temperature`. Misalnya, jika Anda ingin menggunakan temperature 0.5, Anda lakukan:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Catatan, semakin mendekati 1.0, semakin bervariasi outputnya.

- **Model reasoning tidak menggunakan `temperature`**. Ini adalah perubahan penting tahun 2026. Model saat ini yang tidak usang di Microsoft Foundry adalah **model reasoning** (keluarga GPT-5, seri o) - dan mereka **tidak mendukung `temperature` atau `top_p`** (juga tidak `max_tokens`; gunakan `max_output_tokens`). Jika Anda mengirim `temperature` ke `gpt-5-mini` Anda akan mendapatkan error "parameter tidak didukung". Jadi untuk mencoba contoh temperature di atas, arahkan ke model yang masih mendukung kontrol sampling - misalnya model **Llama** terbuka seperti `Llama-3.3-70B-Instruct` dari [katalog model Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), dipanggil melalui endpoint Foundry Models / Azure AI Inference (cara yang sama seperti contoh `githubmodels-*`). Untuk model reasoning seperti GPT-5, Anda mengarahkan output secara berbeda:
  - **Rekayasa prompt** - instruksi yang jelas, contoh, dan output terstruktur (lihat pelajaran [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) melakukan pekerjaan yang dulu dilakukan opsi sampling.
  - **Kontrol reasoning** - parameter seperti usaha reasoning/verbosity menukar kedalaman reasoning terhadap latensi dan biaya.

  Singkatnya: `temperature`/`top_p` masih berlaku di banyak model (Llama, Mistral, Phi, dan keluarga GPT-4.x - meski GPT-4.x sedang dihentikan), tapi arah perkembangan adalah rekayasa prompt + kontrol reasoning pada model reasoning seperti GPT-5.

## Tugas

Untuk tugas ini, Anda dapat memilih apa yang ingin dibuat.

Berikut beberapa saran:

- Ubah aplikasi pembuat resep untuk meningkatkannya lebih lanjut. Bermain-main dengan nilai temperature, dan prompt untuk melihat apa yang bisa Anda hasilkan.
- Buat "teman belajar". Aplikasi ini harus bisa menjawab pertanyaan tentang suatu topik misalnya Python, Anda dapat membuat prompt seperti "Apa itu topik tertentu dalam Python?", atau Anda bisa membuat prompt yang mengatakan, tunjukkan kode untuk topik tertentu dll.
- Bot sejarah, membuat sejarah hidup kembali, perintahkan bot untuk berperan sebagai karakter sejarah tertentu dan tanyakan pertanyaan tentang kehidupan dan zamannya.

## Solusi

### Teman belajar

Berikut adalah prompt pemula, lihat bagaimana Anda dapat menggunakannya dan mengubahnya sesuai keinginan Anda.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Bot sejarah

Berikut beberapa prompt yang bisa Anda gunakan:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Pemeriksaan pengetahuan

Apa fungsi konsep temperature?

1. Mengendalikan seberapa acak outputnya.
1. Mengendalikan seberapa besar responsnya.
1. Mengendalikan berapa banyak token yang digunakan.

## 🚀 Tantangan

Saat mengerjakan tugas, coba variasikan temperature, coba set ke 0, 0.5, dan 1. Ingat bahwa 0 adalah yang paling tidak bervariasi dan 1 adalah yang paling banyak variasinya. Nilai mana yang paling cocok untuk aplikasi Anda?

## Kerja bagus! Lanjutkan Pembelajaran Anda

Setelah menyelesaikan pelajaran ini, lihat koleksi [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk terus meningkatkan pengetahuan Generative AI Anda!

Lanjut ke Pelajaran 7 di mana kita akan melihat cara [membangun aplikasi chat](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->