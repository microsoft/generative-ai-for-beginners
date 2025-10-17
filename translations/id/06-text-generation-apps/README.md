<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df027997f1448323d6159b78a1b669bf",
  "translation_date": "2025-10-17T20:42:03+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "id"
}
-->
# Membangun Aplikasi Generasi Teks

[![Membangun Aplikasi Generasi Teks](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.id.png)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

Sejauh ini dalam kurikulum ini, Anda telah melihat konsep inti seperti prompt dan bahkan seluruh disiplin yang disebut "rekayasa prompt". Banyak alat yang dapat Anda gunakan seperti ChatGPT, Office 365, Microsoft Power Platform, dan lainnya, mendukung penggunaan prompt untuk mencapai sesuatu.

Untuk menambahkan pengalaman semacam itu ke dalam aplikasi, Anda perlu memahami konsep seperti prompt, penyelesaian, dan memilih pustaka untuk digunakan. Itulah yang akan Anda pelajari di bab ini.

## Pendahuluan

Di bab ini, Anda akan:

- Mempelajari pustaka openai dan konsep-konsep intinya.
- Membangun aplikasi generasi teks menggunakan openai.
- Memahami cara menggunakan konsep seperti prompt, suhu, dan token untuk membangun aplikasi generasi teks.

## Tujuan pembelajaran

Di akhir pelajaran ini, Anda akan dapat:

- Menjelaskan apa itu aplikasi generasi teks.
- Membangun aplikasi generasi teks menggunakan openai.
- Mengonfigurasi aplikasi Anda untuk menggunakan lebih banyak atau lebih sedikit token dan juga mengubah suhu, untuk hasil yang bervariasi.

## Apa itu aplikasi generasi teks?

Biasanya ketika Anda membangun aplikasi, aplikasi tersebut memiliki semacam antarmuka seperti berikut:

- Berbasis perintah. Aplikasi konsol adalah aplikasi khas di mana Anda mengetik perintah dan aplikasi tersebut menjalankan tugas. Misalnya, `git` adalah aplikasi berbasis perintah.
- Antarmuka pengguna (UI). Beberapa aplikasi memiliki antarmuka pengguna grafis (GUI) di mana Anda mengklik tombol, memasukkan teks, memilih opsi, dan lainnya.

### Aplikasi konsol dan UI memiliki keterbatasan

Bandingkan dengan aplikasi berbasis perintah di mana Anda mengetik perintah:

- **Terbatas**. Anda tidak bisa mengetik sembarang perintah, hanya perintah yang didukung oleh aplikasi.
- **Spesifik bahasa**. Beberapa aplikasi mendukung banyak bahasa, tetapi secara default aplikasi dibuat untuk bahasa tertentu, meskipun Anda dapat menambahkan dukungan bahasa lainnya.

### Manfaat aplikasi generasi teks

Jadi, bagaimana aplikasi generasi teks berbeda?

Dalam aplikasi generasi teks, Anda memiliki lebih banyak fleksibilitas, Anda tidak terbatas pada serangkaian perintah atau bahasa input tertentu. Sebaliknya, Anda dapat menggunakan bahasa alami untuk berinteraksi dengan aplikasi. Manfaat lainnya adalah Anda sudah berinteraksi dengan sumber data yang telah dilatih pada kumpulan informasi yang luas, sedangkan aplikasi tradisional mungkin terbatas pada apa yang ada di dalam database.

### Apa yang bisa saya bangun dengan aplikasi generasi teks?

Ada banyak hal yang bisa Anda bangun. Misalnya:

- **Chatbot**. Chatbot yang menjawab pertanyaan tentang topik, seperti perusahaan Anda dan produknya, bisa menjadi pilihan yang baik.
- **Pembantu**. LLM sangat baik dalam hal seperti meringkas teks, mendapatkan wawasan dari teks, menghasilkan teks seperti resume, dan lainnya.
- **Asisten kode**. Bergantung pada model bahasa yang Anda gunakan, Anda dapat membangun asisten kode yang membantu Anda menulis kode. Misalnya, Anda dapat menggunakan produk seperti GitHub Copilot serta ChatGPT untuk membantu Anda menulis kode.

## Bagaimana saya bisa memulai?

Nah, Anda perlu menemukan cara untuk terintegrasi dengan LLM yang biasanya melibatkan dua pendekatan berikut:

- Menggunakan API. Di sini Anda membuat permintaan web dengan prompt Anda dan mendapatkan teks yang dihasilkan kembali.
- Menggunakan pustaka. Pustaka membantu mengenkapsulasi panggilan API dan membuatnya lebih mudah digunakan.

## Pustaka/SDK

Ada beberapa pustaka terkenal untuk bekerja dengan LLM seperti:

- **openai**, pustaka ini memudahkan untuk terhubung ke model Anda dan mengirimkan prompt.

Kemudian ada pustaka yang beroperasi pada tingkat yang lebih tinggi seperti:

- **Langchain**. Langchain terkenal dan mendukung Python.
- **Semantic Kernel**. Semantic Kernel adalah pustaka dari Microsoft yang mendukung bahasa C#, Python, dan Java.

## Aplikasi pertama menggunakan openai

Mari kita lihat bagaimana kita dapat membangun aplikasi pertama kita, pustaka apa yang kita butuhkan, seberapa banyak yang diperlukan, dan sebagainya.

### Instal openai

Ada banyak pustaka di luar sana untuk berinteraksi dengan OpenAI atau Azure OpenAI. Dimungkinkan untuk menggunakan berbagai bahasa pemrograman seperti C#, Python, JavaScript, Java, dan lainnya. Kami memilih untuk menggunakan pustaka Python `openai`, jadi kami akan menggunakan `pip` untuk menginstalnya.

```bash
pip install openai
```

### Buat sumber daya

Anda perlu melakukan langkah-langkah berikut:

- Buat akun di Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Dapatkan akses ke Azure OpenAI. Kunjungi [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) dan ajukan permohonan akses.

  > [!NOTE]
  > Pada saat penulisan, Anda perlu mengajukan permohonan akses ke Azure OpenAI.

- Instal Python <https://www.python.org/>
- Buat sumber daya Azure OpenAI Service. Lihat panduan ini untuk [membuat sumber daya](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Temukan kunci API dan endpoint

Pada titik ini, Anda perlu memberi tahu pustaka `openai` Anda kunci API mana yang akan digunakan. Untuk menemukan kunci API Anda, buka bagian "Keys and Endpoint" dari sumber daya Azure OpenAI Anda dan salin nilai "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Sekarang setelah Anda memiliki informasi ini disalin, mari kita instruksikan pustaka untuk menggunakannya.

> [!NOTE]
> Sebaiknya pisahkan kunci API Anda dari kode Anda. Anda dapat melakukannya dengan menggunakan variabel lingkungan.
>
> - Atur variabel lingkungan `OPENAI_API_KEY` ke kunci API Anda.
>   `export OPENAI_API_KEY='sk-...'`

### Konfigurasi pengaturan Azure

Jika Anda menggunakan Azure OpenAI, berikut cara mengatur konfigurasi:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Di atas, kami mengatur hal-hal berikut:

- `api_type` ke `azure`. Ini memberi tahu pustaka untuk menggunakan Azure OpenAI dan bukan OpenAI.
- `api_key`, ini adalah kunci API Anda yang ditemukan di Azure Portal.
- `api_version`, ini adalah versi API yang ingin Anda gunakan. Pada saat penulisan, versi terbaru adalah `2023-05-15`.
- `api_base`, ini adalah endpoint API. Anda dapat menemukannya di Azure Portal di sebelah kunci API Anda.

> [!NOTE] > `os.getenv` adalah fungsi yang membaca variabel lingkungan. Anda dapat menggunakannya untuk membaca variabel lingkungan seperti `OPENAI_API_KEY` dan `API_BASE`. Atur variabel lingkungan ini di terminal Anda atau dengan menggunakan pustaka seperti `dotenv`.

## Menghasilkan teks

Cara untuk menghasilkan teks adalah dengan menggunakan kelas `Completion`. Berikut contohnya:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

Dalam kode di atas, kami membuat objek penyelesaian dan memasukkan model yang ingin kami gunakan serta prompt. Kemudian kami mencetak teks yang dihasilkan.

### Penyelesaian obrolan

Sejauh ini, Anda telah melihat bagaimana kami menggunakan `Completion` untuk menghasilkan teks. Tetapi ada kelas lain yang disebut `ChatCompletion` yang lebih cocok untuk chatbot. Berikut contoh penggunaannya:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Lebih lanjut tentang fungsionalitas ini akan dibahas di bab berikutnya.

## Latihan - aplikasi generasi teks pertama Anda

Sekarang setelah kita belajar cara mengatur dan mengonfigurasi openai, saatnya membangun aplikasi generasi teks pertama Anda. Untuk membangun aplikasi Anda, ikuti langkah-langkah berikut:

1. Buat lingkungan virtual dan instal openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Jika Anda menggunakan Windows, ketik `venv\Scripts\activate` alih-alih `source venv/bin/activate`.

   > [!NOTE]
   > Temukan kunci Azure OpenAI Anda dengan pergi ke [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) dan cari `Open AI`, lalu pilih `Open AI resource` dan kemudian pilih `Keys and Endpoint` dan salin nilai `Key 1`.

1. Buat file _app.py_ dan masukkan kode berikut:

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
   > Jika Anda menggunakan Azure OpenAI, Anda perlu mengatur `api_type` ke `azure` dan mengatur `api_key` ke kunci Azure OpenAI Anda.

   Anda akan melihat output seperti berikut:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Berbagai jenis prompt untuk berbagai hal

Sekarang Anda telah melihat cara menghasilkan teks menggunakan prompt. Anda bahkan memiliki program yang berjalan yang dapat Anda modifikasi dan ubah untuk menghasilkan berbagai jenis teks.

Prompt dapat digunakan untuk berbagai tugas. Misalnya:

- **Menghasilkan jenis teks tertentu**. Misalnya, Anda dapat menghasilkan puisi, pertanyaan untuk kuis, dll.
- **Mencari informasi**. Anda dapat menggunakan prompt untuk mencari informasi seperti contoh berikut 'Apa arti CORS dalam pengembangan web?'.
- **Menghasilkan kode**. Anda dapat menggunakan prompt untuk menghasilkan kode, misalnya mengembangkan ekspresi reguler yang digunakan untuk memvalidasi email atau bahkan menghasilkan seluruh program, seperti aplikasi web.

## Kasus penggunaan yang lebih praktis: generator resep

Bayangkan Anda memiliki bahan-bahan di rumah dan ingin memasak sesuatu. Untuk itu, Anda membutuhkan resep. Salah satu cara untuk menemukan resep adalah menggunakan mesin pencari atau Anda bisa menggunakan LLM untuk melakukannya.

Anda bisa menulis prompt seperti ini:

> "Tunjukkan 5 resep untuk hidangan dengan bahan-bahan berikut: ayam, kentang, dan wortel. Per resep, daftar semua bahan yang digunakan"

Dengan prompt di atas, Anda mungkin mendapatkan respons seperti:

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

Hasil ini sangat bagus, saya tahu apa yang harus dimasak. Pada titik ini, apa yang bisa menjadi perbaikan yang berguna adalah:

- Menyaring bahan-bahan yang tidak saya sukai atau alergi.
- Membuat daftar belanja, jika saya tidak memiliki semua bahan di rumah.

Untuk kasus di atas, mari tambahkan prompt tambahan:

> "Tolong hapus resep dengan bawang putih karena saya alergi dan gantikan dengan sesuatu yang lain. Juga, buat daftar belanja untuk resep-resep tersebut, dengan mempertimbangkan bahwa saya sudah memiliki ayam, kentang, dan wortel di rumah."

Sekarang Anda memiliki hasil baru, yaitu:

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

Itulah lima resep Anda, tanpa bawang putih disebutkan, dan Anda juga memiliki daftar belanja dengan mempertimbangkan apa yang sudah Anda miliki di rumah.

## Latihan - membangun generator resep

Sekarang setelah kita memainkan sebuah skenario, mari kita tulis kode untuk mencocokkan skenario yang telah ditunjukkan. Untuk melakukannya, ikuti langkah-langkah berikut:

1. Gunakan file _app.py_ yang ada sebagai titik awal
1. Temukan variabel `prompt` dan ubah kodenya menjadi berikut:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Jika Anda sekarang menjalankan kode, Anda akan melihat output yang mirip dengan:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE, LLM Anda bersifat nondeterministik, jadi Anda mungkin mendapatkan hasil yang berbeda setiap kali menjalankan program.

   Bagus, mari kita lihat bagaimana kita bisa meningkatkan hal-hal. Untuk meningkatkan hal-hal, kita ingin memastikan kode fleksibel, sehingga bahan-bahan dan jumlah resep dapat ditingkatkan dan diubah.

1. Mari kita ubah kode dengan cara berikut:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Menjalankan kode untuk uji coba, bisa terlihat seperti ini:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Tingkatkan dengan menambahkan filter dan daftar belanja

Sekarang kita memiliki aplikasi yang berfungsi yang mampu menghasilkan resep dan fleksibel karena bergantung pada input dari pengguna, baik jumlah resep maupun bahan yang digunakan.

Untuk lebih meningkatkannya, kita ingin menambahkan hal-hal berikut:

- **Menyaring bahan-bahan**. Kita ingin dapat menyaring bahan-bahan yang tidak kita sukai atau alergi. Untuk mencapai perubahan ini, kita dapat mengedit prompt yang ada dan menambahkan kondisi filter di akhir seperti ini:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Di atas, kita menambahkan `{filter}` di akhir prompt dan kita juga menangkap nilai filter dari pengguna.

  Contoh input menjalankan program sekarang bisa terlihat seperti ini:

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

  Seperti yang Anda lihat, resep apa pun dengan susu di dalamnya telah disaring. Tetapi, jika Anda intoleran laktosa, Anda mungkin ingin menyaring resep dengan keju di dalamnya juga, jadi ada kebutuhan untuk lebih jelas.

- **Membuat daftar belanja**. Kita ingin membuat daftar belanja, dengan mempertimbangkan apa yang sudah kita miliki di rumah.

  Untuk fungsionalitas ini, kita bisa mencoba menyelesaikan semuanya dalam satu prompt atau kita bisa membaginya menjadi dua prompt. Mari kita coba pendekatan kedua. Di sini kita menyarankan menambahkan prompt tambahan, tetapi untuk itu berhasil, kita perlu menambahkan hasil dari prompt sebelumnya sebagai konteks ke prompt berikutnya.

  Temukan bagian dalam kode yang mencetak hasil dari prompt pertama dan tambahkan kode berikut di bawah ini:
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

  Perhatikan hal berikut:

  1. Kita membuat prompt baru dengan menambahkan hasil dari prompt pertama ke prompt yang baru:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Kita membuat permintaan baru, tetapi juga mempertimbangkan jumlah token yang kita minta pada prompt pertama, jadi kali ini kita menetapkan `max_tokens` menjadi 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     Dengan menjalankan kode ini, kita sekarang mendapatkan output berikut:

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

Apa yang kita miliki sejauh ini adalah kode yang berfungsi, tetapi ada beberapa penyesuaian yang sebaiknya kita lakukan untuk meningkatkan hasilnya lebih jauh. Beberapa hal yang sebaiknya kita lakukan adalah:

- **Pisahkan rahasia dari kode**, seperti kunci API. Rahasia tidak seharusnya ada di dalam kode dan harus disimpan di lokasi yang aman. Untuk memisahkan rahasia dari kode, kita dapat menggunakan variabel lingkungan dan pustaka seperti `python-dotenv` untuk memuatnya dari file. Berikut adalah bagaimana hal itu akan terlihat dalam kode:

  1. Buat file `.env` dengan konten berikut:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Catatan, untuk Azure, Anda perlu menetapkan variabel lingkungan berikut:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     Dalam kode, Anda akan memuat variabel lingkungan seperti ini:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Catatan tentang panjang token**. Kita harus mempertimbangkan berapa banyak token yang kita butuhkan untuk menghasilkan teks yang diinginkan. Token memiliki biaya, jadi jika memungkinkan, kita harus mencoba untuk hemat dengan jumlah token yang digunakan. Misalnya, bisakah kita merumuskan prompt sehingga kita dapat menggunakan lebih sedikit token?

  Untuk mengubah token yang digunakan, Anda dapat menggunakan parameter `max_tokens`. Misalnya, jika Anda ingin menggunakan 100 token, Anda akan melakukan:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Bereksperimen dengan suhu**. Suhu adalah sesuatu yang belum kita bahas sejauh ini tetapi merupakan konteks penting untuk bagaimana program kita bekerja. Semakin tinggi nilai suhu, semakin acak outputnya. Sebaliknya, semakin rendah nilai suhu, semakin dapat diprediksi outputnya. Pertimbangkan apakah Anda menginginkan variasi dalam output atau tidak.

  Untuk mengubah suhu, Anda dapat menggunakan parameter `temperature`. Misalnya, jika Anda ingin menggunakan suhu 0.5, Anda akan melakukan:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Catatan, semakin mendekati 1.0, semakin bervariasi outputnya.

## Tugas

Untuk tugas ini, Anda dapat memilih apa yang ingin dibangun.

Berikut beberapa saran:

- Sesuaikan aplikasi generator resep untuk meningkatkannya lebih jauh. Bereksperimenlah dengan nilai suhu, dan prompt untuk melihat apa yang dapat Anda hasilkan.
- Bangun "teman belajar". Aplikasi ini harus dapat menjawab pertanyaan tentang suatu topik, misalnya Python, Anda dapat memiliki prompt seperti "Apa itu topik tertentu dalam Python?", atau Anda dapat memiliki prompt yang mengatakan, tunjukkan kode untuk topik tertentu, dll.
- Bot sejarah, buat sejarah menjadi hidup, instruksikan bot untuk memainkan karakter sejarah tertentu dan ajukan pertanyaan tentang kehidupan dan zamannya.

## Solusi

### Teman belajar

Berikut adalah prompt awal, lihat bagaimana Anda dapat menggunakannya dan menyesuaikannya sesuai keinginan Anda.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Bot sejarah

Berikut adalah beberapa prompt yang dapat Anda gunakan:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Uji pengetahuan

Apa yang dilakukan konsep suhu?

1. Mengontrol seberapa acak outputnya.
1. Mengontrol seberapa besar responsnya.
1. Mengontrol berapa banyak token yang digunakan.

## 🚀 Tantangan

Saat mengerjakan tugas, coba variasikan suhu, coba tetapkan ke 0, 0.5, dan 1. Ingat bahwa 0 adalah yang paling tidak bervariasi dan 1 adalah yang paling bervariasi. Nilai mana yang paling cocok untuk aplikasi Anda?

## Kerja Hebat! Lanjutkan Pembelajaran Anda

Setelah menyelesaikan pelajaran ini, lihat [koleksi Pembelajaran AI Generatif kami](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk terus meningkatkan pengetahuan AI Generatif Anda!

Lanjutkan ke Pelajaran 7 di mana kita akan melihat bagaimana [membangun aplikasi chat](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.