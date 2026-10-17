# Membangun Aplikasi Generasi Teks

[![Membangun Aplikasi Generasi Teks](../../../translated_images/id/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Klik gambar di atas untuk melihat video pelajaran ini)_

Sejauh ini Anda telah melihat dalam kurikulum ini bahwa ada konsep inti seperti prompt dan bahkan sebuah disiplin khusus bernama "rekayasa prompt". Banyak alat yang dapat Anda gunakan seperti ChatGPT, Office 365, Microsoft Power Platform dan lainnya, mendukung Anda menggunakan prompt untuk menyelesaikan sesuatu.

Agar Anda dapat menambahkan pengalaman seperti itu ke sebuah aplikasi, Anda perlu memahami konsep seperti prompt, completion dan memilih pustaka untuk digunakan. Itulah tepatnya yang akan Anda pelajari di bab ini.

## Pendahuluan

Dalam bab ini, Anda akan:

- Mempelajari tentang pustaka openai dan konsep-konsep inti nya.
- Membangun aplikasi generasi teks menggunakan openai.
- Memahami cara menggunakan konsep seperti prompt, temperature, dan token untuk membangun aplikasi generasi teks.

## Tujuan pembelajaran

Pada akhir pelajaran ini, Anda akan mampu:

- Menjelaskan apa itu aplikasi generasi teks.
- Membangun aplikasi generasi teks menggunakan openai.
- Mengonfigurasi aplikasi Anda untuk menggunakan lebih banyak atau lebih sedikit token dan juga mengubah temperature, untuk hasil yang bervariasi.

## Apa itu aplikasi generasi teks?

Biasanya ketika Anda membangun sebuah aplikasi, ia memiliki semacam antarmuka seperti berikut:

- Berbasis perintah. Aplikasi konsol adalah aplikasi khas di mana Anda mengetik perintah dan aplikasi melaksanakan tugas. Misalnya, `git` adalah aplikasi berbasis perintah.
- Antarmuka pengguna (UI). Beberapa aplikasi memiliki antarmuka pengguna grafis (GUI) di mana Anda mengklik tombol, memasukkan teks, memilih opsi dan sebagainya.

### Aplikasi konsol dan UI terbatas

Bandingkan dengan aplikasi berbasis perintah di mana Anda mengetik perintah:

- **Ini terbatas**. Anda tidak bisa mengetik perintah sembarangan, hanya perintah yang didukung oleh aplikasi.
- **Spesifik bahasa**. Beberapa aplikasi mendukung banyak bahasa, tetapi secara default aplikasi dibangun untuk bahasa tertentu, meskipun Anda bisa menambahkan dukungan bahasa lain.

### Manfaat aplikasi generasi teks

Lalu bagaimana aplikasi generasi teks berbeda?

Dalam aplikasi generasi teks, Anda memiliki fleksibilitas lebih, Anda tidak terbatas pada seperangkat perintah atau bahasa input tertentu. Sebaliknya, Anda dapat menggunakan bahasa alami untuk berinteraksi dengan aplikasi. Manfaat lainnya adalah Anda sudah berinteraksi dengan sumber data yang telah dilatih pada korpus informasi yang sangat besar, sedangkan aplikasi tradisional mungkin terbatas pada isi database.

### Apa yang bisa saya bangun dengan aplikasi generasi teks?

Ada banyak hal yang bisa Anda bangun. Misalnya:

- **Chatbot**. Chatbot yang menjawab pertanyaan tentang topik-topik, seperti perusahaan Anda dan produk-produknya bisa menjadi pilihan yang bagus.
- **Pembantu**. LLM sangat hebat dalam hal seperti meringkas teks, mendapatkan wawasan dari teks, menghasilkan teks seperti resume dan lainnya.
- **Asisten kode**. Bergantung pada model bahasa yang Anda gunakan, Anda dapat membangun asisten kode yang membantu Anda menulis kode. Misalnya, Anda dapat menggunakan produk seperti GitHub Copilot serta ChatGPT untuk membantu menulis kode.

## Bagaimana saya bisa memulai?

Nah, Anda perlu menemukan cara untuk mengintegrasikan dengan LLM yang biasanya meliputi dua pendekatan berikut:

- Gunakan API. Di sini Anda menyusun permintaan web dengan prompt Anda dan mendapatkan teks yang dihasilkan kembali.
- Gunakan pustaka. Pustaka membantu mengenkapsulasi panggilan API dan membuatnya lebih mudah digunakan.

## Pustaka/SDK

Ada beberapa pustaka terkenal untuk bekerja dengan LLM seperti:

- **openai**, pustaka ini memudahkan menghubungkan ke model Anda dan mengirim prompt.

Kemudian ada pustaka yang bekerja pada tingkat lebih tinggi seperti:

- **Langchain**. Langchain terkenal dan mendukung Python.
- **Semantic Kernel**. Semantic Kernel adalah pustaka oleh Microsoft yang mendukung bahasa C#, Python, dan Java.

## Aplikasi pertama menggunakan openai

Mari kita lihat bagaimana kita bisa membangun aplikasi pertama kita, pustaka apa yang kita butuhkan, berapa banyak yang diperlukan dan seterusnya.

### Instal openai

Ada banyak pustaka untuk berinteraksi dengan OpenAI atau Azure OpenAI. Juga memungkinkan menggunakan berbagai bahasa pemrograman seperti C#, Python, JavaScript, Java dan lain-lain. Kami memilih menggunakan pustaka Python `openai`, jadi kita akan menggunakan `pip` untuk menginstalnya.

```bash
pip install openai
```

### Buat sumber daya

Anda perlu melaksanakan langkah-langkah berikut:

- Buat akun di Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Dapatkan akses ke Azure OpenAI. Pergi ke [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) dan ajukan permohonan akses.

  > [!NOTE]
  > Pada saat penulisan, Anda perlu mengajukan permohonan akses ke Azure OpenAI.

- Instal Python <https://www.python.org/>
- Sudah membuat sumber daya Layanan Azure OpenAI. Lihat panduan ini tentang cara [membuat sumber daya](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Temukan kunci API dan endpoint

Saat ini, Anda perlu memberi tahu pustaka `openai` Anda kunci API yang akan digunakan. Untuk menemukan kunci API Anda, pergi ke bagian "Keys and Endpoint" dari sumber daya Azure OpenAI Anda dan salin nilai "Key 1".

![Bilah sumber daya Keys and Endpoint di Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Sekarang setelah Anda menyalin informasi ini, mari instruksikan pustaka untuk menggunakannya.

> [!NOTE]
> Ada baiknya memisahkan kunci API Anda dari kode Anda. Anda dapat melakukannya dengan menggunakan variabel lingkungan.
>
> - Atur variabel lingkungan `OPENAI_API_KEY` ke kunci API Anda.
>   `export OPENAI_API_KEY='sk-...'`

### Setup konfigurasi Azure

Jika Anda menggunakan Azure OpenAI (sekarang bagian dari Microsoft Foundry), berikut cara mengatur konfigurasi. Kami menggunakan klien standar `OpenAI` yang diarahkan ke endpoint Azure OpenAI `/openai/v1/`, yang bekerja dengan API Responses dan tidak memerlukan `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Di atas kita mengatur hal-hal berikut:

- `api_key`, ini adalah kunci API Anda yang ditemukan di Portal Azure atau portal Microsoft Foundry.
- `base_url`, ini adalah endpoint sumber daya Foundry Anda dengan appended `/openai/v1/`. Endpoint stabil v1 bekerja di OpenAI dan Azure OpenAI tanpa pengelolaan `api_version`.

> [!NOTE] > `os.environ` membaca variabel lingkungan. Anda dapat menggunakannya untuk membaca variabel lingkungan seperti `AZURE_OPENAI_API_KEY` dan `AZURE_OPENAI_ENDPOINT`. Atur variabel lingkungan ini di terminal Anda atau menggunakan pustaka seperti `dotenv`.

## Menghasilkan teks

Cara untuk menghasilkan teks adalah menggunakan API Responses melalui metode `responses.create`. Berikut contohnya:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

Dalam kode di atas, kita membuat response dan memasukkan model yang ingin kita gunakan serta promptnya. Kemudian kita cetak teks yang dihasilkan melalui `response.output_text`.

### Percakapan multi-giliran

Responses API sangat cocok untuk pembuatan teks satu giliran maupun chatbot multi-giliran - Anda menyediakan daftar pesan dalam `input` untuk membangun sebuah percakapan:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Lebih lanjut tentang fungsi ini di bab berikutnya.

## Latihan - aplikasi generasi teks pertama Anda

Sekarang kita sudah belajar cara mengatur dan mengonfigurasi openai, saatnya membangun aplikasi generasi teks pertama Anda. Untuk membangun aplikasi Anda, ikuti langkah-langkah berikut:

1. Buat lingkungan virtual dan instal openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Jika Anda menggunakan Windows ketik `venv\Scripts\activate` alih-alih `source venv/bin/activate`.

   > [!NOTE]
   > Temukan kunci Azure OpenAI Anda dengan pergi ke [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) dan cari `Open AI` lalu pilih `Open AI resource` dan kemudian pilih `Keys and Endpoint` dan salin nilai `Key 1`.

1. Buat file _app.py_ dan berikan kode berikut:

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
   > Jika Anda menggunakan OpenAI biasa (bukan Azure), gunakan `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (tanpa `base_url`) dan berikan nama model seperti `gpt-5-mini` bukan nama deployment.

   Anda akan melihat output seperti berikut:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Jenis prompt yang berbeda, untuk hal yang berbeda

Sekarang Anda sudah melihat cara menghasilkan teks menggunakan prompt. Bahkan Anda sudah memiliki program yang berjalan yang dapat Anda modifikasi untuk menghasilkan berbagai jenis teks.

Prompt dapat digunakan untuk berbagai tugas. Misalnya:

- **Menghasilkan jenis teks**. Misalnya, Anda dapat menghasilkan puisi, pertanyaan kuis, dll.
- **Mencari informasi**. Anda dapat menggunakan prompt untuk mencari informasi seperti contoh berikut 'Apa arti CORS dalam pengembangan web?'.
- **Menghasilkan kode**. Anda dapat menggunakan prompt untuk menghasilkan kode, misalnya membuat regular expression untuk validasi email atau bahkan menghasilkan seluruh program seperti aplikasi web?

## Kasus penggunaan yang lebih praktis: pembuat resep

Bayangkan Anda memiliki bahan di rumah dan ingin memasak sesuatu. Untuk itu, Anda butuh resep. Cara mendapat resep adalah menggunakan mesin pencari atau Anda bisa menggunakan LLM untuk itu.

Anda bisa menulis prompt seperti ini:

> "Tunjukkan 5 resep untuk hidangan dengan bahan berikut: ayam, kentang, dan wortel. Per resep, cantumkan semua bahan yang digunakan"

Berdasarkan prompt di atas, Anda mungkin mendapat respons serupa:

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

Hasil ini bagus, saya tahu apa yang harus dimasak. Pada titik ini, perbaikan yang berguna adalah:

- Menyaring bahan yang saya tidak suka atau alergi.
- Membuat daftar belanja, jika saya tidak punya semua bahan di rumah.

Untuk kasus di atas, mari tambah prompt tambahan:

> "Tolong hilangkan resep dengan bawang putih karena saya alergi dan ganti dengan bahan lain. Juga, buat daftar belanja untuk resep-resep tersebut, mempertimbangkan bahwa saya sudah punya ayam, kentang, dan wortel di rumah."

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

Itu lima resep Anda, tanpa bawang putih dan juga dengan daftar belanja mempertimbangkan apa yang sudah Anda punya di rumah.

## Latihan - buat pembuat resep

Setelah kita memainkan skenario, mari tulis kode sesuai skenario yang telah didemokan. Untuk itu, ikuti langkah-langkah berikut:

1. Gunakan file _app.py_ yang sudah ada sebagai titik awal
1. Temukan variabel `prompt` dan ganti kode di dalamnya dengan yang berikut:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Jika Anda jalankan kode sekarang, Anda akan melihat output seperti ini:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > CATATAN, LLM Anda nondeterministik, jadi hasil bisa berbeda setiap kali program dijalankan.

   Bagus, mari kita lihat bagaimana cara memperbaiki. Untuk memperbaiki, kita ingin agar kode fleksibel, sehingga bahan dan jumlah resep dapat diubah.

1. Mari ubah kode seperti berikut:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Mengambil kode untuk test run, bisa seperti ini:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Perbaikan dengan menambahkan filter dan daftar belanja

Sekarang kita memiliki aplikasi yang mampu membuat resep dan fleksibel karena mengandalkan input dari pengguna, baik jumlah resep maupun bahan yang digunakan.

Untuk memperbaikinya lebih lanjut, kita ingin menambahkan berikut ini:

- **Menapis bahan yang tidak diinginkan**. Kita ingin dapat menapis bahan yang tidak disukai atau alergi. Untuk melakukan ini, kita bisa edit prompt yang sudah ada dan menambahkan kondisi filter di akhir seperti berikut:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Di atas, kita menambahkan `{filter}` ke akhir prompt dan juga menangkap nilai filter dari pengguna.

  Contoh input menjalankan program sekarang bisa seperti ini:

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

  Seperti yang Anda lihat, resep dengan susu sudah difilter. Namun, jika Anda intoleran laktosa, Anda mungkin ingin menapis resep dengan keju juga, jadi kebutuhan untuk jelas.

- **Membuat daftar belanja**. Kita ingin membuat daftar belanja, mempertimbangkan apa yang sudah kita miliki di rumah.

  Untuk fitur ini, kita bisa mencoba menyelesaikan semuanya dalam satu prompt atau memecahnya menjadi dua prompt. Mari coba pendekatan kedua. Di sini kita menambahkan prompt tambahan, tapi agar berhasil, kita harus menambahkan hasil prompt pertama sebagai konteks prompt kedua.

  Cari bagian kode yang mencetak hasil dari prompt pertama dan tambahkan kode berikut di bawahnya:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Perhatikan yang berikut:

  1. Kita membangun prompt baru dengan menambahkan hasil prompt pertama ke prompt baru:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Kita buat permintaan baru, juga memperhitungkan jumlah token yang diminta di prompt pertama, jadi kali ini kita set `max_output_tokens` ke 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Mencoba kode ini, kita dapat output sebagai berikut:

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

Apa yang kita miliki sejauh ini adalah kode yang berfungsi, tetapi ada beberapa penyesuaian yang harus kita lakukan untuk meningkatkan lebih lanjut. Beberapa hal yang harus kita lakukan adalah:

- **Pisahkan rahasia dari kode**, seperti kunci API. Rahasia tidak boleh ada di dalam kode dan harus disimpan di lokasi yang aman. Untuk memisahkan rahasia dari kode, kita dapat menggunakan variabel lingkungan dan pustaka seperti `python-dotenv` untuk memuatnya dari file. Berikut cara menulisnya dalam kode:

  1. Buat file `.env` dengan isi sebagai berikut:

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

- **Sedikit tentang panjang token**. Kita harus mempertimbangkan berapa banyak token yang dibutuhkan untuk menghasilkan teks yang kita inginkan. Token membutuhkan biaya, jadi sejauh mungkin, kita harus mencoba hemat dengan jumlah token yang digunakan. Misalnya, bisakah kita merancang prompt sehingga kita bisa menggunakan token lebih sedikit?

  Untuk mengubah jumlah token yang digunakan, Anda bisa menggunakan parameter `max_output_tokens`. Misalnya, jika Anda ingin menggunakan 100 token, Anda bisa melakukan:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Bereksperimen dengan temperature**. Temperature adalah sesuatu yang belum kita sebutkan sejauh ini tetapi merupakan konteks penting bagi bagaimana program kita bekerja. Semakin tinggi nilai temperature, keluaran akan semakin acak. Sebaliknya, semakin rendah nilai temperature, keluaran akan semakin dapat diprediksi. Pertimbangkan apakah Anda menginginkan variasi dalam keluaran Anda atau tidak.

  Untuk mengubah temperature, Anda bisa menggunakan parameter `temperature`. Misalnya, jika Anda ingin menggunakan temperature 0,5, Anda bisa melakukan:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Catatan, semakin mendekati 1.0, keluaran akan semakin bervariasi.

- **Model penalaran tidak menggunakan `temperature`**. Ini adalah perubahan penting tahun 2026. Model saat ini yang tidak kedaluwarsa di Microsoft Foundry adalah **model penalaran** (keluarga GPT-5, seri o) - dan mereka **tidak mendukung `temperature` atau `top_p`** (juga bukan `max_tokens`; gunakan `max_output_tokens`). Jika Anda mengirim `temperature` ke `gpt-5-mini` Anda akan mendapatkan kesalahan "parameter tidak didukung". Jadi, untuk mencoba contoh temperature di atas, arahkan ke model yang masih mendukung kontrol sampling - misalnya model **Llama** terbuka seperti `Llama-3.3-70B-Instruct` dari [katalog model Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), dipanggil melalui Foundry Models / Azure AI Inference endpoint (dengan cara yang sama seperti contoh `githubmodels-*`). Untuk model penalaran seperti GPT-5, Anda mengarahkan keluaran dengan cara berbeda:
  - **Rekayasa prompt** - instruksi yang jelas, contoh, dan keluaran terstruktur (lihat pelajaran [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) menggantikan fungsi knob sampling.
  - **Kontrol penalaran** - parameter seperti usaha penalaran/verbositas menukar kedalaman penalaran dengan latensi dan biaya.

  Singkatnya: `temperature`/`top_p` masih berlaku pada banyak model (Llama, Mistral, Phi, dan keluarga GPT-4.x - meskipun GPT-4.x sedang kedaluwarsa), tetapi arah perjalanan adalah rekayasa prompt + kontrol penalaran pada model penalaran seperti GPT-5.

## Tugas

Untuk tugas ini, Anda boleh memilih apa yang ingin dibuat.

Berikut beberapa saran:

- Sesuaikan aplikasi pembuat resep untuk meningkatkannya lebih jauh. Bereksperimenlah dengan nilai temperature, dan prompt untuk melihat apa yang bisa Anda buat.
- Buat "teman belajar". Aplikasi ini harus bisa menjawab pertanyaan tentang suatu topik misalnya Python, Anda bisa membuat prompt seperti "Apa itu topik tertentu di Python?", atau Anda bisa membuat prompt yang mengatakan, tunjukkan kode untuk topik tertentu, dll.
- Bot sejarah, hidupkan sejarah, instruksikan bot untuk memainkan karakter sejarah tertentu dan tanyakan tentang kehidupan dan zamannya.

## Solusi

### Teman belajar

Berikut adalah prompt awal, lihat bagaimana Anda bisa menggunakannya dan menyempurnakannya sesuai keinginan Anda.

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

## Cek pengetahuan

Apa fungsi konsep temperature?

1. Mengontrol seberapa acak keluaran.
1. Mengontrol seberapa besar respon.
1. Mengontrol berapa banyak token yang digunakan.

## 🚀 Tantangan

Saat mengerjakan tugas, coba variasikan temperature, coba atur ke 0, 0,5, dan 1. Ingat bahwa 0 adalah yang paling sedikit variasi dan 1 adalah yang paling banyak. Nilai mana yang paling cocok untuk aplikasi Anda?

## Kerja Bagus! Lanjutkan Pembelajaran Anda

Setelah menyelesaikan pelajaran ini, lihat koleksi [Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif Anda!

Lanjutkan ke Pelajaran 7 di mana kita akan melihat cara [membangun aplikasi obrolan](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->