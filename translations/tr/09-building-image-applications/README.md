<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-06-25T17:20:08+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "tr"
}
-->
# Görüntü Üretim Uygulamaları Oluşturma

[![Görüntü Üretim Uygulamaları Oluşturma](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.tr.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM'lerin metin üretiminden daha fazlası var. Metin açıklamalarından görüntü oluşturmak da mümkündür. Görüntülerin bir modalite olarak kullanılması, MedTech, mimarlık, turizm, oyun geliştirme ve daha birçok alanda oldukça faydalı olabilir. Bu bölümde, en popüler iki görüntü üretim modeli olan DALL-E ve Midjourney'i inceleyeceğiz.

## Giriş

Bu derste ele alacağımız konular:

- Görüntü üretimi ve neden faydalı olduğu.
- DALL-E ve Midjourney, nedirler ve nasıl çalışırlar.
- Bir görüntü üretim uygulaması nasıl oluşturulur.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra:

- Bir görüntü üretim uygulaması oluşturabileceksiniz.
- Uygulamanız için meta istemlerle sınırlar belirleyebileceksiniz.
- DALL-E ve Midjourney ile çalışabileceksiniz.

## Neden bir görüntü üretim uygulaması oluşturmalısınız?

Görüntü üretim uygulamaları, Üretken Yapay Zekanın yeteneklerini keşfetmek için harika bir yoldur. Örneğin, şu amaçlarla kullanılabilirler:

- **Görüntü düzenleme ve sentezleme**. Görüntü düzenleme ve görüntü sentezleme gibi çeşitli kullanım senaryoları için görüntüler üretebilirsiniz.

- **Çeşitli endüstrilere uygulanabilir**. Ayrıca, Medtech, Turizm, Oyun geliştirme ve daha birçok endüstri için görüntüler üretmek amacıyla kullanılabilirler.

## Senaryo: Edu4All

Bu dersin bir parçası olarak, Edu4All adındaki girişimimizle çalışmaya devam edeceğiz. Öğrenciler, değerlendirmeleri için görüntüler oluşturacaklar, hangi görüntülerin oluşturulacağı tamamen öğrencilere bağlı, ancak kendi masallarına illüstrasyonlar ekleyebilirler veya hikayeleri için yeni bir karakter yaratabilirler ya da fikirlerini ve kavramlarını görselleştirmelerine yardımcı olabilirler.

Örneğin, Edu4All'un öğrencileri, sınıfta anıtlar üzerinde çalışırken şu tür görüntüler üretebilirler:

![Edu4All girişimi, anıtlar üzerine ders, Eyfel Kulesi](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.tr.png)

şu tür bir istem kullanarak:

> "Sabahın erken saatlerinde güneş ışığında Eyfel Kulesi'nin yanında bir köpek"

## DALL-E ve Midjourney nedir?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) ve [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst), en popüler görüntü üretim modellerinden ikisidir ve istemleri kullanarak görüntüler oluşturmanıza olanak tanır.

### DALL-E

DALL-E ile başlayalım, bu metin açıklamalarından görüntü üreten bir Üretken Yapay Zeka modelidir.

> [DALL-E, iki modelin, CLIP ve diffused attention, birleşimidir](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, görüntülerden ve metinlerden sayısal veri temsilleri olan gömüler üreten bir modeldir.

- **Diffused attention**, gömülerden görüntü üreten bir modeldir. DALL-E, görüntü ve metin verileri üzerinde eğitilmiştir ve metin açıklamalarından görüntü oluşturmak için kullanılabilir. Örneğin, DALL-E, bir şapkalı kedi veya mohawk saçlı bir köpek görüntüsü oluşturmak için kullanılabilir.

### Midjourney

Midjourney, DALL-E'ye benzer bir şekilde çalışır, metin istemlerinden görüntüler üretir. Midjourney, "şapkalı bir kedi" veya "mohawk saçlı bir köpek" gibi istemlerle görüntüler oluşturmak için de kullanılabilir.

![Midjourney tarafından üretilen görüntü, mekanik güvercin](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Wikipedia'dan görsel, Midjourney tarafından üretilen görüntü_

## DALL-E ve Midjourney Nasıl Çalışır

Öncelikle, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E, bir _oto-regresif transformer_ ile transformer mimarisi üzerine kurulu bir Üretken Yapay Zeka modelidir.

Bir _oto-regresif transformer_, bir modelin metin açıklamalarından görüntü oluşturma şeklini tanımlar, bir seferde bir piksel oluşturur ve ardından oluşturulan pikselleri bir sonraki pikseli oluşturmak için kullanır. Sinir ağında birden fazla katmandan geçerek, görüntü tamamlanana kadar devam eder.

Bu süreçle, DALL-E, oluşturduğu görüntüdeki nitelikleri, nesneleri, özellikleri ve daha fazlasını kontrol eder. Ancak, DALL-E 2 ve 3, oluşturulan görüntü üzerinde daha fazla kontrole sahiptir.

## İlk görüntü üretim uygulamanızı oluşturma

Peki, bir görüntü üretim uygulaması oluşturmak için neler gereklidir? Şu kütüphanelere ihtiyacınız var:

- **python-dotenv**, sırlarınızı koddan uzak bir _.env_ dosyasında saklamak için bu kütüphaneyi kullanmanız şiddetle tavsiye edilir.
- **openai**, OpenAI API ile etkileşimde bulunmak için kullanacağınız kütüphane budur.
- **pillow**, Python'da görüntülerle çalışmak için.
- **requests**, HTTP istekleri yapmanıza yardımcı olur.

1. Aşağıdaki içeriğe sahip bir _.env_ dosyası oluşturun:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Bu bilgileri Azure Portal'da kaynağınızın "Anahtarlar ve Uç Nokta" bölümünde bulun.

1. Yukarıdaki kütüphaneleri _requirements.txt_ adlı bir dosyada toplayın:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Ardından, sanal bir ortam oluşturun ve kütüphaneleri yükleyin:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows için, sanal ortamınızı oluşturmak ve etkinleştirmek için şu komutları kullanın:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ adlı bir dosyaya aşağıdaki kodu ekleyin:

   ```python
   import openai
   import os
   import requests
   from PIL import Image
   import dotenv

   # import dotenv
   dotenv.load_dotenv()

   # Get endpoint and key from environment variables
   openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
   openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

   # Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
   openai.api_version = '2023-06-01-preview'
   openai.api_type = 'azure'


   try:
       # Create an image by using the image generation API
       generation_response = openai.Image.create(
           prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
           size='1024x1024',
           n=2,
           temperature=0,
       )
       # Set the directory for the stored image
       image_dir = os.path.join(os.curdir, 'images')

       # If the directory doesn't exist, create it
       if not os.path.isdir(image_dir):
           os.mkdir(image_dir)

       # Initialize the image path (note the filetype should be png)
       image_path = os.path.join(image_dir, 'generated-image.png')

       # Retrieve the generated image
       image_url = generation_response["data"][0]["url"]  # extract image URL from response
       generated_image = requests.get(image_url).content  # download the image
       with open(image_path, "wb") as image_file:
           image_file.write(generated_image)

       # Display the image in the default image viewer
       image = Image.open(image_path)
       image.show()

   # catch exceptions
   except openai.InvalidRequestError as err:
       print(err)

   ```

Bu kodu açıklayalım:

- İlk olarak, ihtiyaç duyduğumuz kütüphaneleri, OpenAI kütüphanesi, dotenv kütüphanesi, requests kütüphanesi ve Pillow kütüphanesi dahil olmak üzere içe aktarıyoruz.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Sonra, _.env_ dosyasından çevresel değişkenleri yüklüyoruz.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Ardından, OpenAI API için uç noktayı, anahtarı, sürümü ve türü ayarlıyoruz.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Sonra, görüntüyü üretiyoruz:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Yukarıdaki kod, üretilen görüntünün URL'sini içeren bir JSON nesnesi ile yanıt verir. URL'yi kullanarak görüntüyü indirip bir dosyaya kaydedebiliriz.

- Son olarak, görüntüyü açıp standart görüntü görüntüleyiciyi kullanarak görüntülüyoruz:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Görüntü üretimi hakkında daha fazla detay

Görüntüyü üreten koda daha detaylı bir şekilde bakalım:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, görüntüyü üretmek için kullanılan metin istemidir. Bu durumda, "Sisli bir çayırda, nergislerin yetiştiği bir alanda, elinde lolipop tutan at üzerindeki tavşan" istemini kullanıyoruz.
- **size**, üretilen görüntünün boyutudur. Bu durumda, 1024x1024 piksel boyutunda bir görüntü üretiyoruz.
- **n**, üretilen görüntü sayısıdır. Bu durumda, iki görüntü üretiyoruz.
- **temperature**, bir Üretken Yapay Zeka modelinin çıktısının rastgeleliğini kontrol eden bir parametredir. Sıcaklık, 0 ile 1 arasında bir değerdir ve 0 çıktının deterministik olduğunu, 1 ise çıktının rastgele olduğunu belirtir. Varsayılan değer 0.7'dir.

Görüntülerle yapabileceğiniz daha fazla şey var ve bunları bir sonraki bölümde ele alacağız.

## Görüntü üretiminin ek yetenekleri

Şimdiye kadar, Python'da birkaç satır kodla bir görüntü üretebildiğimizi gördünüz. Ancak, görüntülerle yapabileceğiniz daha fazla şey var.

Ayrıca şunları da yapabilirsiniz:

- **Düzenlemeler yapın**. Mevcut bir görüntüye bir maske ve bir istem sağlayarak bir görüntüyü değiştirebilirsiniz. Örneğin, bir görüntünün bir kısmına bir şey ekleyebilirsiniz. Tavşan görüntümüzü düşünün, tavşana bir şapka ekleyebilirsiniz. Bunu yapmanın yolu, görüntüyü, değişiklik yapılacak alanı belirleyen bir maske ve yapılacak işlemi belirten bir metin istemi sağlamaktır.

  ```python
  response = openai.Image.create_edit(
    image=open("base_image.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="An image of a rabbit with a hat on its head.",
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  Temel görüntü sadece tavşanı içerir, ancak son görüntü tavşanın üzerinde bir şapka olacaktır.

- **Varyasyonlar oluşturun**. Mevcut bir görüntüyü alıp, varyasyonlar oluşturulmasını istemek fikridir. Bir varyasyon oluşturmak için, bir görüntü ve bir metin istemi sağlar ve kodu şu şekilde yazarsınız:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Not, bu yalnızca OpenAI'de desteklenir

## Sıcaklık

Sıcaklık, bir Üretken Yapay Zeka modelinin çıktısının rastgeleliğini kontrol eden bir parametredir. Sıcaklık, 0 ile 1 arasında bir değerdir ve 0 çıktının deterministik olduğunu, 1 ise çıktının rastgele olduğunu belirtir. Varsayılan değer 0.7'dir.

Sıcaklığın nasıl çalıştığını görmek için bu istemi iki kez çalıştırarak bir örneğe bakalım:

> İstem: "Sisli bir çayırda, nergislerin yetiştiği bir alanda, elinde lolipop tutan at üzerindeki tavşan"

![Elinde lolipop tutan at üzerindeki tavşan, versiyon 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.tr.png)

Şimdi aynı istemi çalıştıralım ve iki kez aynı görüntüyü elde edemeyeceğimizi görelim:

![At üzerindeki tavşanın üretilen görüntüsü](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.tr.png)

Gördüğünüz gibi, görüntüler benzer ama aynı değil. Şimdi sıcaklık değerini 0.1'e değiştirip ne olacağını görelim:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Sıcaklığı değiştirmek

Şimdi yanıtı daha deterministik hale getirmeye çalışalım. Ürettiğimiz iki görüntüden ilkinde bir tavşan olduğunu, ikincisinde ise bir at olduğunu gözlemleyebiliriz, bu yüzden görüntüler büyük ölçüde farklılık gösteriyor.

Bu nedenle kodumuzu değiştirip sıcaklığı 0 olarak ayarlayalım:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Şimdi bu kodu çalıştırdığınızda, şu iki görüntüyü elde edersiniz:

- ![Sıcaklık 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.tr.png)
- ![Sıcaklık 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.tr.png)

Burada görüntülerin birbirine daha çok benzediğini açıkça görebilirsiniz.

## Uygulamanız için metaprompts ile sınırları nasıl tanımlarsınız

Demomuzla, müşterilerimiz için zaten görüntüler üretebiliriz. Ancak, uygulamamız için bazı sınırlar oluşturmamız gerekiyor.

Örneğin, iş için uygun olmayan veya çocuklar için uygun olmayan görüntüler oluşturmak istemiyoruz.

Bunu _metaprompts_ ile yapabiliriz. Metaprompts, bir Üretken Yapay Zeka modelinin çıktısını kontrol etmek için kullanılan metin istemleridir. Örneğin, metaprompts kullanarak, çıktıyı kontrol edebilir ve üretilen görüntülerin iş için uygun veya çocuklar için uygun olmasını sağlayabiliriz.

### Nasıl çalışır?

Peki, meta istemler nasıl çalışır?

Meta istemler, bir Üretken Yapay Zeka modelinin çıktısını kontrol etmek için kullanılan metin istemleridir, metin isteminden önce konumlandırılırlar ve modelin çıktısını kontrol etmek için kullanılırlar ve modelin çıktısını kontrol etmek için uygulamalara gömülürler. İstem girişi ve meta istem girişini tek bir metin isteminde kapsüllerler.

Bir meta istem örneği aşağıdaki gibi olabilir:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Şimdi, demomuzda meta istemleri nasıl kullanabileceğimizi görelim.

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

# TODO add request to generate image
```

Yukarıdaki istemden, tüm oluşturulan görüntülerin metapromtu dikkate aldığını görebilirsiniz.

## Görev - öğrencileri yetkilendirelim

Bu dersin başında Edu4All'u tanıttık. Şimdi öğrencilerin değerlendirmeleri için görüntü oluşturmalarını sağlama zamanı.

Öğrenciler, değerlendirmeleri için anıtlar içeren görüntüler oluşturacaklar, hangi anıtların olacağı tamamen öğrencilere bağlı. Öğrencilerden bu görevde yaratıcılıklarını kullanarak bu anıtları farklı bağlamlarda yerleştirmeleri isteniyor.

## Çözüm

İşte olası bir çözüm:

```python
import openai
import os
import requests
from PIL import Image
import dotenv

# import dotenv
dotenv.load_dotenv()

# Get endpoint and key from environment variables
openai.api_base = "<replace with endpoint>"
openai.api_key = "<replace with api key>"

# Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
openai.api_version = '2023-06-01-preview'
openai.api_type = 'azure'

disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}"""

prompt = f"""{metaprompt}
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
""""

try:
    # Create an image by using the image generation API
    generation_response = openai.Image.create(
        prompt=prompt,    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response["data"][0]["url"]  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except openai.InvalidRequestError as err:
    print(err)
```

## Harika İş! Öğrenmeye Devam Edin

Bu dersi tamamladıktan sonra, Üretken Yapay Zeka bilginizi artırmak için [Üretken Yapay Zeka Öğrenme koleksiyonumuzu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) inceleyin!

Düşük kodlu AI uygulamaları [oluşturmayı inceleyeceğimiz](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) 10. Derse geçin.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba gösteriyoruz, ancak otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.