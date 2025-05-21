<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:09:08+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "tr"
}
-->
# Görüntü Üretme Uygulamaları Oluşturma

LLM'lerin yalnızca metin üretiminden daha fazlası vardır. Metin açıklamalarından görüntüler üretmek de mümkündür. Görüntülerin bir mod olarak bulunması, MedTech, mimarlık, turizm, oyun geliştirme ve daha birçok alanda son derece faydalı olabilir. Bu bölümde, en popüler iki görüntü üretim modeli olan DALL-E ve Midjourney'i inceleyeceğiz.

## Giriş

Bu derste ele alacağız:

- Görüntü üretimi ve neden faydalı olduğu.
- DALL-E ve Midjourney, ne oldukları ve nasıl çalıştıkları.
- Görüntü üretme uygulaması nasıl oluşturulur.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları yapabileceksiniz:

- Görüntü üretme uygulaması oluşturmak.
- Uygulamanız için meta yönlendirmelerle sınırlar belirlemek.
- DALL-E ve Midjourney ile çalışmak.

## Neden bir görüntü üretme uygulaması oluşturmalısınız?

Görüntü üretme uygulamaları, Üretken Yapay Zekanın yeteneklerini keşfetmenin harika bir yoludur. Örneğin, şu amaçlarla kullanılabilirler:

- **Görüntü düzenleme ve sentezi**. Görüntü düzenleme ve görüntü sentezi gibi çeşitli kullanım durumları için görüntüler üretebilirsiniz.

- **Çeşitli endüstrilere uygulanabilir**. Medtech, Turizm, Oyun geliştirme ve daha birçok endüstri için görüntü üretmek amacıyla kullanılabilirler.

## Senaryo: Edu4All

Bu dersin bir parçası olarak, bu derste Edu4All adlı girişimimizle çalışmaya devam edeceğiz. Öğrenciler, değerlendirmeleri için görüntüler oluşturacaklar, hangi görüntülerin oluşturulacağı tamamen öğrencilere bağlıdır, ancak kendi masallarına illüstrasyonlar veya hikayeleri için yeni bir karakter oluşturabilirler ya da fikirlerini ve kavramlarını görselleştirmelerine yardımcı olabilirler.

Edu4All öğrencileri, sınıfta anıtlar üzerinde çalışıyorlarsa örneğin şu türde bir şey üretebilirler:

![Edu4All girişimi, anıtlar dersi, Eyfel Kulesi](../../../translated_images/startup.ec211d74fef9f4175010c3334942b715514230415744b9dd0a69a19f4ad68786.tr.png)

şu türde bir yönlendirme kullanarak

> "Erken sabah güneş ışığında Eyfel Kulesi'nin yanında köpek"

## DALL-E ve Midjourney nedir?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) ve [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst), en popüler görüntü üretim modellerinden ikisidir, yönlendirmeler kullanarak görüntü oluşturmanıza olanak tanırlar.

### DALL-E

DALL-E ile başlayalım, bu metin açıklamalarından görüntüler üreten bir Üretken Yapay Zeka modelidir.

> [DALL-E, CLIP ve diffused attention olmak üzere iki modelin birleşimidir](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, görüntüler ve metinlerden verilerin sayısal temsilini oluşturan gömme modelleri üreten bir modeldir.

- **Diffused attention**, gömmelerden görüntü üreten bir modeldir. DALL-E, görüntüler ve metinlerden oluşan bir veri kümesi üzerinde eğitilir ve metin açıklamalarından görüntü üretmek için kullanılabilir. Örneğin, DALL-E, bir şapka takmış kedi veya mohawk saçlı köpek görüntüleri oluşturmak için kullanılabilir.

### Midjourney

Midjourney, DALL-E'ye benzer şekilde çalışır, metin yönlendirmelerinden görüntüler üretir. Midjourney, "şapka takmış kedi" veya "mohawk saçlı köpek" gibi yönlendirmeler kullanarak görüntü oluşturmak için de kullanılabilir.

![Midjourney tarafından üretilen görüntü, mekanik güvercin](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Görsel kaynağı Wikipedia, Midjourney tarafından üretilen görüntü_

## DALL-E ve Midjourney Nasıl Çalışır

Öncelikle, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E, _oto-regresif transformatör_ ile transformatör mimarisine dayalı bir Üretken Yapay Zeka modelidir.

Bir _oto-regresif transformatör_, bir modelin metin açıklamalarından görüntü üretme yöntemini tanımlar, bir seferde bir piksel üretir ve ardından üretilen pikselleri kullanarak bir sonraki pikseli üretir. Bir sinir ağında birden fazla katmandan geçerek, görüntü tamamlanana kadar devam eder.

Bu süreçle, DALL-E, ürettiği görüntüdeki nitelikleri, nesneleri, özellikleri ve daha fazlasını kontrol eder. Ancak, DALL-E 2 ve 3, üretilen görüntü üzerinde daha fazla kontrol sağlar.

## İlk görüntü üretme uygulamanızı oluşturma

Peki, bir görüntü üretme uygulaması oluşturmak için neler gereklidir? Şu kütüphanelere ihtiyacınız var:

- **python-dotenv**, gizli bilgilerinizi koddan uzakta bir _.env_ dosyasında tutmanız için bu kütüphaneyi kullanmanız şiddetle tavsiye edilir.
- **openai**, OpenAI API ile etkileşimde bulunmak için kullanacağınız kütüphanedir.
- **pillow**, Python'da görüntülerle çalışmak için.
- **requests**, HTTP istekleri yapmanıza yardımcı olur.

1. Aşağıdaki içeriğe sahip bir _.env_ dosyası oluşturun:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Bu bilgileri Azure Portal'da kaynağınızın "Anahtarlar ve Uç Nokta" bölümünde bulun.

1. Yukarıdaki kütüphaneleri _requirements.txt_ adlı bir dosyada şu şekilde toplayın:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Sonra sanal ortam oluşturun ve kütüphaneleri yükleyin:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows için, sanal ortamınızı oluşturmak ve etkinleştirmek için aşağıdaki komutları kullanın:

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

- Öncelikle, OpenAI kütüphanesi, dotenv kütüphanesi, requests kütüphanesi ve Pillow kütüphanesi dahil olmak üzere ihtiyacımız olan kütüphaneleri içe aktarıyoruz.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Sonra, _.env_ dosyasından ortam değişkenlerini yüklüyoruz.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Bundan sonra, OpenAI API için uç nokta, anahtar, sürüm ve türü belirliyoruz.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Ardından, görüntüyü üretiyoruz:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Yukarıdaki kod, üretilen görüntünün URL'sini içeren bir JSON nesnesi ile yanıt verir. Görüntüyü indirmek ve bir dosyaya kaydetmek için URL'yi kullanabiliriz.

- Son olarak, görüntüyü açıyor ve standart görüntü görüntüleyiciyi kullanarak görüntülüyor:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Görüntü üretme hakkında daha fazla ayrıntı

Görüntüyü üreten kodu daha ayrıntılı inceleyelim:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, görüntüyü üretmek için kullanılan metin yönlendirmesidir. Bu durumda, "Sisli çayırda, nergislerin yetiştiği yerde, at üzerinde lolipop tutan tavşan" yönlendirmesini kullanıyoruz.
- **size**, üretilen görüntünün boyutudur. Bu durumda, 1024x1024 piksel boyutunda bir görüntü üretiyoruz.
- **n**, üretilen görüntü sayısıdır. Bu durumda, iki görüntü üretiyoruz.
- **temperature**, Üretken Yapay Zeka modelinin çıktısının rastgeleliğini kontrol eden bir parametredir. Temperature, 0 ile 1 arasında bir değerdir, burada 0, çıktının deterministik olduğunu ve 1, çıktının rastgele olduğunu ifade eder. Varsayılan değer 0.7'dir.

Görüntülerle yapabileceğiniz daha fazla şey var ve bunları sonraki bölümde ele alacağız.

## Görüntü üretiminin ek yetenekleri

Python'da birkaç satır kullanarak bir görüntü üretebildiğimizi gördünüz. Ancak, görüntülerle yapabileceğiniz daha fazla şey var.

Ayrıca şunları yapabilirsiniz:

- **Düzenlemeler yapın**. Mevcut bir görüntüye bir maske ve bir yönlendirme sağlayarak bir görüntüyü değiştirebilirsiniz. Örneğin, bir görüntünün bir bölümüne bir şey ekleyebilirsiniz. Tavşan görüntümüzü hayal edin, tavşana bir şapka ekleyebilirsiniz. Bunu yapmak için görüntüyü, değişiklik için alanı belirleyen bir maske ve ne yapılması gerektiğini belirten bir metin yönlendirmesi sağlamanız gerekmektedir.

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

  Temel görüntü yalnızca tavşanı içerir, ancak son görüntü tavşanın üzerinde şapkayı içerir.

- **Varyasyonlar oluşturun**. Fikir, mevcut bir görüntüyü alıp varyasyonların oluşturulmasını istemektir. Bir varyasyon oluşturmak için bir görüntü ve bir metin yönlendirmesi sağlarsınız ve kodu şu şekilde yazarız:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Not, bu yalnızca OpenAI tarafından desteklenir

## Temperature

Temperature, Üretken Yapay Zeka modelinin çıktısının rastgeleliğini kontrol eden bir parametredir. Temperature, 0 ile 1 arasında bir değerdir, burada 0, çıktının deterministik olduğunu ve 1, çıktının rastgele olduğunu ifade eder. Varsayılan değer 0.7'dir.

Temperature'ın nasıl çalıştığını görmek için bu yönlendirmeyi iki kez çalıştırarak bir örneğe bakalım:

> Yönlendirme : "Sisli çayırda, nergislerin yetiştiği yerde, at üzerinde lolipop tutan tavşan"

![At üzerinde lolipop tutan tavşan, versiyon 1](../../../translated_images/v1-generated-image.208ba0525ed6ae505504aa852e28d334c0440e9931b7c97f9508176a22d2dd54.tr.png)

Şimdi aynı yönlendirmeyi tekrar çalıştıralım, aynı görüntüyü iki kez almayacağımızı görmek için:

![At üzerinde tavşan görüntüsü](../../../translated_images/v2-generated-image.f0a88c05ef476e95f3682d4b21c9ba2f4807ae71cc29e9c05b42ebbf497cf61b.tr.png)

Gördüğünüz gibi, görüntüler benzer ancak aynı değil. Şimdi temperature değerini 0.1'e değiştirip ne olduğunu görelim:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Temperature'ı değiştirme

Öyleyse yanıtı daha deterministik hale getirmeye çalışalım. Ürettiğimiz iki görüntüden, ilk görüntüde bir tavşan olduğunu ve ikinci görüntüde bir at olduğunu gözlemleyebiliriz, dolayısıyla görüntüler oldukça farklıdır.

Bu nedenle kodumuzu değiştirip temperature'ı 0 olarak ayarlayalım:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Şimdi bu kodu çalıştırdığınızda, şu iki görüntüyü alırsınız:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.d8557be792b5c81c2c6d2804cb7b210fe8b340106fe4ffcadf9cf7de1cd7b991.tr.png)
- ![Temperature 0 , v2](../../../translated_images/v2-temp-generated-image.bd412fcfbd43379312b1382212a332aa311ca1a80ea692dea50a8b876a487c61.tr.png)

Burada görüntülerin birbirine daha çok benzediğini açıkça görebilirsiniz.

## Uygulamanız için metaprompts ile sınırları nasıl tanımlarsınız

Demomuzla, müşterilerimiz için zaten görüntüler üretebiliriz. Ancak, uygulamamız için bazı sınırlar oluşturmalıyız.

Örneğin, iş için uygun olmayan veya çocuklar için uygun olmayan görüntüler üretmek istemiyoruz.

Bunu _metaprompts_ ile yapabiliriz. Metaprompts, Üretken Yapay Zeka modelinin çıktısını kontrol etmek için kullanılan metin yönlendirmeleridir. Örneğin, metaprompts kullanarak çıktıyı kontrol edebilir ve üretilen görüntülerin iş için uygun veya çocuklar için uygun olmasını sağlayabiliriz.

### Nasıl çalışır?

Peki, metaprompts nasıl çalışır?

Metaprompts, Üretken Yapay Zeka modelinin çıktısını kontrol etmek için kullanılan metin yönlendirmeleridir, metin yönlendirmesinin önünde konumlandırılırlar ve modelin çıktısını kontrol etmek için kullanılırlar ve modelin çıktısını kontrol etmek için uygulamalara gömülürler. Yönlendirme girdisi ve metaprompt girdisini tek bir metin yönlendirmesinde kapsayarak.

Bir metaprompt örneği aşağıdaki gibi olabilir:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Şimdi, demomuzda metaprompts kullanmayı nasıl yapabileceğimizi görelim.

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

Yukarıdaki yönlendirmeden, oluşturulan tüm görüntülerin metapromptu dikkate aldığını görebilirsiniz.

## Ödev - öğrencileri etkinleştirelim

Bu dersin başında Edu4All'ı tanıttık. Şimdi öğrencilerin değerlendirmeleri için görüntüler oluşturmalarını sağlama zamanı.

Öğrenciler, anıtlar içeren değerlendirmeleri için görüntüler oluşturacaklar, hangi anıtların yer alacağı tamamen öğrencilere bağlıdır. Öğrencilerden bu görevde yaratıcılıklarını kullanarak bu anıtları farklı bağlamlarda yerleştirmeleri istenir.

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

Bu dersi tamamladıktan sonra, Üretken Yapay Zeka bilginizi geliştirmeye devam etmek için [Üretken Yapay Zeka Öğrenme koleksiyonumuza](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) göz atın!

Düşük kodla [AI uygulamaları oluşturmayı](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) inceleyeceğimiz 10. Derse geçin.

**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.