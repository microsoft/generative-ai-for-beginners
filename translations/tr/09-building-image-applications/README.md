# Görüntü Üretim Uygulamaları Geliştirme

[![Görüntü Üretim Uygulamaları Geliştirme](../../../translated_images/tr/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLM'lerin sadece metin üretiminden ibaret olmadığını biliyor muydunuz? Metin açıklamalarından görüntü de oluşturmak mümkündür. Görüntüleri bir modalite olarak kullanmak MedTech, mimari, turizm, oyun geliştirme ve daha birçok alanda çok faydalı olabilir. Bu bölümde, en popüler iki görüntü üretim modeli olan DALL-E ve Midjourney'i inceleyeceğiz.

## Giriş

Bu derste şunları ele alacağız:

- Görüntü üretimi ve neden faydalı olduğu.
- DALL-E ve Midjourney modellerinin ne olduğu ve nasıl çalıştığı.
- Bir görüntü üretim uygulamasını nasıl inşa edeceğiniz.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları yapabileceksiniz:

- Bir görüntü üretim uygulaması geliştirmek.
- Uygulamanız için meta komutlarla sınırlar belirlemek.
- DALL-E ve Midjourney ile çalışmak.

## Neden görüntü üretim uygulaması geliştirmeliyiz?

Görüntü üretim uygulamaları, Yaratıcı Yapay Zekanın yeteneklerini keşfetmek için harika bir yoldur. Örneğin, şu amaçlarla kullanılabilir:

- **Görüntü düzenleme ve sentezi**. Görüntü düzenleme ve sentezi gibi çeşitli kullanım durumları için görüntüler oluşturabilirsiniz.

- **Çeşitli endüstrilere uygulanabilir**. Ayrıca MedTech, Turizm, Oyun geliştirme gibi çeşitli sektörler için görüntüler oluşturmakta kullanılabilirler.

## Senaryo: Edu4All

Bu derste, girişimimiz Edu4All ile çalışmaya devam edeceğiz. Öğrenciler değerlendirmelerinde kullanmak üzere görüntüler oluşturacaklar; görüntülerin ne olduğu tamamen öğrencilere bağlıdır, kendi masalları için çizimler, hikayelerine yeni bir karakter yaratmak veya fikirlerini ve kavramlarını görselleştirmeye yardımcı olabilirler.

Örneğin, Edu4All öğrencileri sınıfta anıtlarda çalışıyorlarsa aşağıdaki gibi görüntüler oluşturabilirler:

![Edu4All girişimi, anıtlar sınıfı, Eyfel Kulesi](../../../translated_images/tr/startup.94d6b79cc4bb3f5a.webp)

şu komut kullanılarak

> "Sabah erken güneş ışığında Eyfel Kulesi yanında köpek"

## DALL-E ve Midjourney nedir?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) ve [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst), promtlar kullanarak görüntü oluşturmayı sağlayan en popüler iki görüntü üretim modelidir.

### DALL-E

Şimdi metin açıklamalarından görüntü üreten bir Yaratıcı Yapay Zeka modeli olan DALL-E ile başlayalım.

> [DALL-E, CLIP ve yayılmış dikkat olmak üzere iki modelin birleşimidir](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, görüntüler ve metinlerden veri için sayısal temsil olan embeddingler üretir.

- **Yayılmış dikkat**, embeddinglerden görüntüler üretir. DALL-E, görüntüler ve metinlerden oluşan bir veri seti üzerinde eğitilmiştir ve metin açıklamalarından görüntüler oluşturabilir. Örneğin, DALL-E şapkalı bir kedi veya mohawklı bir köpeğin görüntüsünü oluşturabilir.

### Midjourney

Midjourney, DALL-E'ye benzer şekilde çalışır ve metin komutlarından görüntüler üretir. Midjourney, “şapkalı bir kedi” veya “mohawklı bir köpek” gibi komutlarla da görüntüler oluşturabilir.

![Midjourney tarafından oluşturulan görüntü, mekanik güvercin](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Görüntü kaynağı Wikipedia, Midjourney tarafından oluşturuldu_

## DALL-E ve Midjourney nasıl çalışır

Öncelikle [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E, _autoregressive transformer_ yapısına dayalı bir Yaratıcı Yapay Zeka modelidir.

_Autoregressive transformer_, metin açıklamalarından görüntü oluşturmayı tanımlar; birer piksel üreterek ilerler ve oluşturduğu pikselleri kullanarak sonraki pikselleri üretir. Görüntü tamamlanana kadar sinir ağının birden çok katmanında işlem görür.

Bu süreçle DALL-E, ürettiği görüntüde nesneler, özellikler ve detaylar üzerinde kontrol sahibidir. Ancak DALL-E 2 ve 3, üretilen görüntü üzerinde daha fazla kontrol imkanı sunar.

## İlk görüntü üretim uygulamanızı oluşturmak

Peki bir görüntü üretim uygulaması geliştirmek için neler gerekir? Aşağıdaki kütüphanelere ihtiyacınız olacak:

- **python-dotenv**, gizli bilgilerinizi koddan uzak tutmak için _.env_ dosyasında saklamak adına kullanmanız şiddetle tavsiye edilir.
- **openai**, OpenAI API ile etkileşim için kullanacağınız kütüphane.
- **pillow**, Python'da görüntülerle çalışmak için.
- **requests**, HTTP istekleri yapmanıza yardımcı olur.

## Azure OpenAI modeli oluşturma ve dağıtma

Henüz yapmadıysanız, bir Azure OpenAI kaynağı ve modeli oluşturmak için [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) sayfasındaki talimatları takip edin.
Model olarak **gpt-image-1** seçin (mevcut nesil Azure OpenAI görüntü modeli; DALL-E 3 eskidir ve yeni dağıtımlar için artık mevcut değildir).

## Uygulamayı oluşturma

1. Aşağıdaki içerikte bir _.env_ dosyası oluşturun:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   Bu bilgileri Azure OpenAI Foundry Portalınızda "Deployments" bölümünde bulabilirsiniz.

1. Yukarıdaki kütüphaneleri _requirements.txt_ adlı bir dosyada toplayın:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Ardından, sanal ortam oluşturun ve kütüphaneleri yükleyin:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows için sanal ortam oluşturup etkinleştirmek üzere şu komutları kullanın:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ adlı dosyaya aşağıdaki kodu ekleyin:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # dotenv'i içe aktar
    dotenv.load_dotenv()
    
    # Azure OpenAI servis istemcisini yapılandır
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # Görüntü oluşturma API'si kullanarak bir resim oluştur
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Kaydedilen resim için dizini ayarla
        image_dir = os.path.join(os.curdir, 'images')

        # Dizin yoksa oluştur
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Resim yolunu başlat (dosya türünün png olması gerektiğine dikkat et)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Oluşturulan resmi al
        image_url = generation_response.data[0].url  # Yanıttan resim URL'sini çıkar
        generated_image = requests.get(image_url).content  # Resmi indir
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # Resmi varsayılan resim görüntüleyicide göster
        image = Image.open(image_path)
        image.show()

    # İstisnaları yakala
    except openai.BadRequestError as err:
        print(err)
   ```

Bu kodu açıklayalım:

- Öncelikle, OpenAI, dotenv, requests ve Pillow kütüphaneleri dahil olmak üzere gereksinim duyduğumuz kütüphaneleri içe aktarırız.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Sonra _.env_ dosyasından ortam değişkenlerini yükleriz.

  ```python
  # dotenv'i içe aktar
  dotenv.load_dotenv()
  ```

- Ardından Azure OpenAI servis istemcisini yapılandırırız

  ```python
  # Uç noktayı ve anahtarı ortam değişkenlerinden alın
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- Sonra görüntüyü oluştururuz:

  ```python
  # Görüntü oluşturma API'sini kullanarak bir görüntü oluşturun
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Yukarıdaki kod, oluşturulan görüntünün URL'sini içeren bir JSON nesnesi ile yanıt verir. Bu URL'yi kullanarak görüntüyü indirebilir ve bir dosyaya kaydedebiliriz.

- Son olarak, görüntüyü açar ve standart görüntüleyici ile görüntüleriz:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Görüntü oluşturma kodunun daha ayrıntılı açıklaması

Görüntü oluşturma kodunu daha detaylı inceleyelim:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, görüntüyü oluşturmak için kullanılan metin komutudur. Bu örnekte, "At üzerindeki tavşan, lolipop tutuyor, nergislerin yetiştiği sisli çayırda" komutunu kullanıyoruz.
- **size**, oluşturulan görüntünün boyutudur. Bu örnekte 1024x1024 piksel görüntü oluşturuluyor.
- **n**, oluşturulacak görüntü sayısıdır. Biz burada iki görüntü oluşturuyoruz.
- **temperature**, Yaratıcı Yapay Zeka modelinin çıktısının rastgeleliğini kontrol eden bir parametredir. 0 değeri çıktının deterministik olduğunu, 1 değeri ise tamamen rastgele çıktılar üreteceğini ifade eder. Varsayılan değer 0.7'dir.

Görüntülerle yapılabilecek başka şeyler de var; bunları sonraki bölümde ele alacağız.

## Görüntü üretiminin ek yetenekleri

Şimdiye kadar, Python'da birkaç satır kod ile nasıl görüntü oluşturduğumuzu gördünüz. Ancak görüntülerle yapılabilecek başka şeyler de var.

Ayrıca şunları yapabilirsiniz:

- **Düzenlemeler yapma**. Mevcut bir görüntüye maske ve komut sağlayarak görüntüyü değiştirebilirsiniz. Örneğin, bir görüntünün bir bölümüne bir şey ekleyebilirsiniz. Tavşan görüntümüzü düşünün; tavşanın üzerine şapka ekleyebilirsiniz. Bunu yapmak için görüntüyü, değişiklik yapılacak alanı belirten bir maskeyi ve ne yapılacağını belirten bir metin komutunu sağlamalısınız. 
> Not: Bu DALL-E 3'te desteklenmemektedir. 
 
İşte GPT Image kullanarak bir örnek:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  Temel görüntü sadece havuzlu salonu içerecek ancak son görüntüye bir flamingo eklenecektir:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/tr/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/tr/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/tr/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Varyasyonlar yaratma**. Var olan bir görüntü alıp varyasyonların oluşturulmasını isteyebilirsiniz. Bir varyasyon oluşturmak için görüntü ve metin komutu sağlar, şu şekilde kod yazarsınız:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > Not, bu yalnızca OpenAI'nin DALL-E 2 modelinde desteklenmektedir, gpt-image-1 modelinde değil

## Temperature (sıcaklık)

Temperature, Bir Yaratıcı Yapay Zeka modelinin çıktısının rastgeleliğini kontrol eden bir parametredir. 0 değeri çıktının deterministik olduğunu, 1 değeri ise tamamen rastgele çıktılar üreteceğini ifade eder. Varsayılan değer 0.7'dir.

Temperature'ın nasıl çalıştığına bakalım, bu komutu iki kez çalıştırarak:

> Komut : "At üzerindeki tavşan, lolipop tutuyor, nergislerin yetiştiği sisli çayırda"

![At üzerindeki tavşan lolipop tutuyor, versiyon 1](../../../translated_images/tr/v1-generated-image.a295cfcffa3c13c2.webp)

Şimdi aynı komutu tekrar çalıştırıp aynı görüntünün iki kez oluşmayacağını görelim:

![At üzerindeki tavşanın oluşturduğu görüntü](../../../translated_images/tr/v2-generated-image.33f55a3714efe61d.webp)

Görüldüğü üzere, görüntüler benzer ama aynı değil. Temperature değerini 0.1 yapalım ve ne olduğuna bakalım:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Komut metninizi buraya girin
        size='1024x1024',
        n=2
    )
```

### Temperature değerini değiştirme

Tepkiyi daha deterministik hale getirmeye çalışalım. Oluşturduğumuz iki görüntüye baktığımızda, birincisinde tavşan var, ikincisinde at var, yani görüntüler oldukça farklı.

O halde kodumuzu değiştirip temperature'ı 0 olarak ayarlayalım:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # İstek metninizi buraya girin
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Bu kodu çalıştırdığınızda şu iki görüntüyü elde edersiniz:

- ![Temperature 0, v1](../../../translated_images/tr/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![Temperature 0 , v2](../../../translated_images/tr/v2-temp-generated-image.871d0c920dbfb0f1.webp)

Burada görüntülerin birbirine daha çok benzediğini açıkça görebilirsiniz.

## Uygulamanız için sınırları nasıl belirleriz - metapromptlar

Demo uygulamamız ile müşterilerimiz için görüntüler oluşturabiliyoruz. Ancak uygulamanız için bazı sınırlar koymanız gerekir.

Örneğin, iş yerinde uygun olmayan ya da çocuklar için uygun olmayan görüntüler oluşturmak istemeyiz.

Bunu _metapromptlar_ ile yapabiliriz. Metapromptlar, bir Yaratıcı Yapay Zeka modelinin çıktısını kontrol eden metin komutlarıdır. Örneğin, metapromptlar ile çıktıyı kontrol ederek oluşturulan görüntülerin iş yeri için güvenli veya çocuklar için uygun olmasını sağlarız.

### Nasıl çalışır?

Metapromptlar nasıl çalışır?

Metapromptlar, bir Yaratıcı Yapay Zeka modelinin çıktısını kontrol etmek için metin komutlarıdır; metin komutundan önce konumlanır ve model çıktısını kontrol etmek için kullanılır. Uygulamalarda bu şekilde yerleştirilerek model çıktısı kontrol edilir. Komut girişi ve metaprompt aynı metin komutunda birleştirilir.

Bir metaprompt örneği şöyle olabilir:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Şimdi, demo uygulamamızda metapromptları nasıl kullanabileceğimize bakalım.

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

# TODO resim oluşturmak için istek ekle
```

Yukarıdaki komuttan, oluşturulan tüm görüntülerin metapromptu dikkate aldığı görülmektedir.

## Ödev - öğrencileri yetkilendirelim

Bu dersin başında Edu4All'dan bahsetmiştik. Şimdi öğrencilerin değerlendirmeleri için görüntü oluşturmalarını sağlamanın zamanı geldi.


Öğrenciler, değerlendirmeleri için anıtlar içeren görseller oluşturacaklar, hangi anıtların seçileceği öğrencilere kalmıştır. Öğrencilerden, bu görevde yaratıcılıklarını kullanarak bu anıtları farklı bağlamlarda yerleştirmeleri istenmektedir.

## Çözüm

İşte olası bir çözüm:

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# dotenv'i içe aktar
dotenv.load_dotenv()

# Uç noktayı ve anahtarı ortam değişkenlerinden al
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-10-21"
  )


disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"""{meta_prompt}
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
"""

try:
    # Görüntü oluşturma API'sini kullanarak bir resim oluştur
    generation_response = client.images.generate(
        prompt=prompt,    # İstenen metni buraya girin
        size='1024x1024',
        n=1,
    )
    # Kaydedilen resmin dizinini ayarla
    image_dir = os.path.join(os.curdir, 'images')

    # Dizin yoksa, oluştur
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Görüntü yolunu başlat (dosya türünün png olması gerektiğine dikkat et)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Oluşturulan resmi al
    image_url = generation_response.data[0].url  # yanıt içinden resim URL'sini çıkar
    generated_image = requests.get(image_url).content  # resmi indir
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Varsayılan görüntüleyicide resmi göster
    image = Image.open(image_path)
    image.show()

# istisnaları yakala
except openai.BadRequestError as err:
    print(err)
```

## Harika İş! Öğrenmeye Devam Et

Bu dersi tamamladıktan sonra, Generative AI bilginizi geliştirmeye devam etmek için [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) koleksiyonumuza göz atın!

10. Derse gidin; burada [düşük kodlu AI uygulamalarının nasıl oluşturulacağını](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) inceleyeceğiz.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->