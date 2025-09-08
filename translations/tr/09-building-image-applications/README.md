<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef74ad58fc01f7ad80788f79505f9816",
  "translation_date": "2025-08-26T16:53:47+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "tr"
}
-->
# Görüntü Üretim Uygulamaları Geliştirme

[![Görüntü Üretim Uygulamaları Geliştirme](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.tr.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM'ler sadece metin üretmekle sınırlı değildir. Metin açıklamalarından da görseller üretmek mümkündür. Görsellerin bir mod olarak kullanılması, MedTech, mimari, turizm, oyun geliştirme gibi birçok alanda oldukça faydalı olabilir. Bu bölümde, en popüler iki görüntü üretim modeli olan DALL-E ve Midjourney'e göz atacağız.

## Giriş

Bu derste şunları ele alacağız:

- Görüntü üretimi ve neden faydalı olduğu.
- DALL-E ve Midjourney, nedirler ve nasıl çalışırlar.
- Bir görüntü üretim uygulamasının nasıl geliştirileceği.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları yapabileceksiniz:

- Bir görüntü üretim uygulaması geliştirmek.
- Uygulamanız için meta istemlerle sınırlar belirlemek.
- DALL-E ve Midjourney ile çalışmak.

## Neden bir görüntü üretim uygulaması geliştirmelisiniz?

Görüntü üretim uygulamaları, Üretken Yapay Zeka'nın yeteneklerini keşfetmek için harika bir yoldur. Örneğin şu amaçlarla kullanılabilirler:

- **Görüntü düzenleme ve sentezleme**. Farklı kullanım senaryoları için görseller üretebilirsiniz, örneğin görüntü düzenleme ve görüntü sentezleme.

- **Çeşitli sektörlerde uygulanabilir**. Ayrıca Medtech, Turizm, Oyun geliştirme gibi birçok sektörde görseller üretmek için de kullanılabilirler.

## Senaryo: Edu4All

Bu ders kapsamında, startup'ımız Edu4All ile çalışmaya devam edeceğiz. Öğrenciler, değerlendirmeleri için görseller oluşturacaklar; hangi görseller olacağı tamamen öğrencilere bağlı, kendi masallarına illüstrasyonlar ekleyebilir, hikayelerine yeni bir karakter yaratabilir veya fikir ve kavramlarını görselleştirmelerine yardımcı olabilirler.

Örneğin, Edu4All öğrencileri sınıfta anıtlar üzerinde çalışıyorsa şunları üretebilirler:

![Edu4All startup, anıtlar dersi, Eyfel Kulesi](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.tr.png)

şu şekilde bir istem kullanarak

> "Sabahın erken saatlerinde Eyfel Kulesi'nin yanında bir köpek"

## DALL-E ve Midjourney nedir?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) ve [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) en popüler iki görüntü üretim modelidir, istemler kullanarak görseller üretmenizi sağlarlar.

### DALL-E

DALL-E ile başlayalım; bu, metin açıklamalarından görseller üreten bir Üretken Yapay Zeka modelidir.

> [DALL-E, iki modelin birleşimidir: CLIP ve diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, görsellerden ve metinden sayısal veri temsilleri (embedding) üreten bir modeldir.

- **Diffused attention**, embedding'lerden görseller üreten bir modeldir. DALL-E, görseller ve metinlerden oluşan bir veri seti üzerinde eğitilmiştir ve metin açıklamalarından görseller üretmek için kullanılabilir. Örneğin, DALL-E bir şapka takan kedi ya da mohawk saçlı bir köpek görseli üretebilir.

### Midjourney

Midjourney de DALL-E'ye benzer şekilde çalışır, metin istemlerinden görseller üretir. Midjourney de “şapka takan bir kedi” ya da “mohawk saçlı bir köpek” gibi istemlerle görseller oluşturabilir.

![Midjourney tarafından üretilmiş görsel, mekanik güvercin](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Görsel kaynağı Wikipedia, Midjourney tarafından üretilmiştir_

## DALL-E ve Midjourney Nasıl Çalışır

Öncelikle, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E, _autoregressive transformer_ mimarisine sahip bir Üretken Yapay Zeka modelidir.

Bir _autoregressive transformer_, modelin metin açıklamalarından görsel üretme şeklini tanımlar; her seferinde bir piksel üretir ve üretilen pikselleri bir sonraki pikseli üretmek için kullanır. Sinir ağında birden fazla katmandan geçerek, görsel tamamlanana kadar bu işlem devam eder.

Bu süreçle, DALL-E, ürettiği görseldeki öznitelikleri, nesneleri, karakteristikleri ve daha fazlasını kontrol edebilir. Ancak, DALL-E 2 ve 3, üretilen görsel üzerinde daha fazla kontrol sunar.

## İlk görüntü üretim uygulamanızı geliştirmek

Peki bir görüntü üretim uygulaması geliştirmek için neler gerekir? Şu kütüphanelere ihtiyacınız olacak:

- **python-dotenv**, gizli anahtarlarınızı _.env_ dosyasında koddan ayrı tutmak için bu kütüphaneyi kullanmanız şiddetle önerilir.
- **openai**, OpenAI API ile etkileşim kurmak için bu kütüphaneyi kullanacaksınız.
- **pillow**, Python'da görsellerle çalışmak için.
- **requests**, HTTP istekleri yapmak için yardımcı olur.

## Azure OpenAI modeli oluşturma ve dağıtma

Henüz yapmadıysanız, [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) sayfasındaki talimatları izleyerek bir Azure OpenAI kaynağı ve modeli oluşturun. Model olarak DALL-E 3'ü seçin.

## Uygulamayı oluşturun

1. _.env_ adında bir dosya oluşturun ve aşağıdaki içeriği ekleyin:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Bu bilgileri Azure OpenAI Foundry Portal'da kaynağınızın "Deployments" bölümünde bulabilirsiniz.

1. Yukarıdaki kütüphaneleri _requirements.txt_ adlı bir dosyada aşağıdaki gibi toplayın:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Sonra, sanal ortam oluşturun ve kütüphaneleri yükleyin:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows için, sanal ortamı oluşturmak ve etkinleştirmek için şu komutları kullanın:

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
    
    # import dotenv
    dotenv.load_dotenv()
    
    # configure Azure OpenAI service client 
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
    try:
        # Create an image by using the image generation API
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Set the directory for the stored image
        image_dir = os.path.join(os.curdir, 'images')

        # If the directory doesn't exist, create it
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Initialize the image path (note the filetype should be png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Retrieve the generated image
        image_url = generation_response.data[0].url  # extract image URL from response
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

- Öncelikle, ihtiyacımız olan kütüphaneleri içe aktarıyoruz; OpenAI kütüphanesi, dotenv, requests ve Pillow kütüphanesi dahil.

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

- Ardından, Azure OpenAI servis istemcisini yapılandırıyoruz

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Sonra, görseli üretiyoruz:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Yukarıdaki kod, üretilen görselin URL'sini içeren bir JSON nesnesi döndürür. Bu URL'yi kullanarak görseli indirip bir dosyaya kaydedebiliriz.

- Son olarak, görseli açıp standart görsel görüntüleyici ile gösteriyoruz:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Görsel üretme hakkında daha fazla detay

Görseli üreten koda daha yakından bakalım:

    ```python
      generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                            )
    ```

- **prompt**, görseli üretmek için kullanılan metin istemidir. Bu örnekte, "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils" istemini kullanıyoruz.
- **size**, üretilen görselin boyutudur. Bu örnekte, 1024x1024 piksel boyutunda bir görsel üretiyoruz.
- **n**, üretilen görsel sayısıdır. Bu örnekte, iki görsel üretiyoruz.
- **temperature**, Üretken Yapay Zeka modelinin çıktısının rastgeleliğini kontrol eden bir parametredir. Temperature, 0 ile 1 arasında bir değerdir; 0 çıktının deterministik, 1 ise rastgele olduğu anlamına gelir. Varsayılan değer 0.7'dir.

Görsellerle ilgili daha fazla işlemi bir sonraki bölümde ele alacağız.

## Görüntü üretiminin ek yetenekleri

Şimdiye kadar, Python'da birkaç satır kodla nasıl görsel üretebildiğimizi gördünüz. Ancak, görsellerle yapabileceğiniz daha fazla şey var.

Ayrıca şunları da yapabilirsiniz:

- **Düzenleme yapma**. Var olan bir görsel, bir maske ve bir istem vererek bir görseli değiştirebilirsiniz. Örneğin, bir görselin bir bölümüne bir şey ekleyebilirsiniz. Tavşan görselimizi düşünün, tavşana bir şapka ekleyebilirsiniz. Bunu yapmak için görseli, bir maske (değişiklik yapılacak alanı belirten) ve ne yapılacağını belirten bir metin istemi verirsiniz.
> Not: Bu özellik DALL-E 3'te desteklenmemektedir.

İşte GPT Image ile yapılmış bir örnek:

    ```python
    response = client.images.edit(
        model="gpt-image-1",
        image=open("sunlit_lounge.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo"
    )
    image_url = response.data[0].url
    ```

  Temel görselde sadece havuzlu salon bulunurken, son görselde bir flamingo da olacak:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="./images/sunlit_lounge.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/mask.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/sunlit_lounge_result.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **Varyasyonlar oluşturma**. Buradaki fikir, var olan bir görseli alıp ondan varyasyonlar oluşturmasını istemektir. Bir varyasyon oluşturmak için bir görsel ve bir metin istemi verirsiniz ve kodu şu şekilde yazarsınız:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Not: Bu özellik yalnızca OpenAI'da desteklenmektedir.

## Temperature

Temperature, Üretken Yapay Zeka modelinin çıktısının rastgeleliğini kontrol eden bir parametredir. Temperature, 0 ile 1 arasında bir değerdir; 0 çıktının deterministik, 1 ise rastgele olduğu anlamına gelir. Varsayılan değer 0.7'dir.

Temperature'ın nasıl çalıştığına bir örnekle bakalım, bu istemi iki kez çalıştırarak:

> İstem : "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![Bir atın üstünde lolipop tutan tavşan, versiyon 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.tr.png)

Şimdi aynı istemi tekrar çalıştıralım ve aynı görseli iki kez alamayacağımızı görelim:

![Atın üstünde tavşan görseli](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.tr.png)

Gördüğünüz gibi, görseller benzer ama aynı değil. Şimdi temperature değerini 0.1 yapıp ne olacağını görelim:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Temperature değerini değiştirmek

Şimdi yanıtı daha deterministik hale getirmeye çalışalım. Ürettiğimiz iki görselden birinde tavşan, diğerinde at olduğunu ve görsellerin oldukça farklı olduğunu gözlemleyebiliriz.

Bu yüzden kodumuzu değiştirip temperature'ı 0 olarak ayarlayalım:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Şimdi bu kodu çalıştırdığınızda şu iki görseli elde edersiniz:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.tr.png)
- ![Temperature 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.tr.png)

Burada, görsellerin birbirine çok daha fazla benzediğini açıkça görebilirsiniz.

## Uygulamanız için metapromptlarla sınırlar nasıl belirlenir

Demo uygulamamızla, müşterilerimiz için zaten görseller üretebiliyoruz. Ancak, uygulamamız için bazı sınırlar koymamız gerekiyor.

Örneğin, iş yerinde uygun olmayan veya çocuklar için uygun olmayan görseller üretmek istemiyoruz.

Bunu _metapromptlar_ ile yapabiliriz. Metapromptlar, Üretken Yapay Zeka modelinin çıktısını kontrol etmek için kullanılan metin istemleridir. Örneğin, metapromptlar kullanarak çıktıyı kontrol edebilir ve üretilen görsellerin iş yerinde uygun veya çocuklar için uygun olmasını sağlayabiliriz.

### Nasıl çalışır?

Peki, meta istemler nasıl çalışır?

Meta istemler, Üretken Yapay Zeka modelinin çıktısını kontrol etmek için kullanılan metin istemleridir; asıl istemden önce konumlandırılırlar ve modelin çıktısını kontrol etmek için kullanılırlar, uygulamalara gömülerek modelin çıktısını kontrol ederler. İstem girdisi ve meta istem girdisi tek bir metin isteminde birleştirilir.

Bir meta istem örneği şöyle olabilir:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Şimdi, demo uygulamamızda meta istemleri nasıl kullanabileceğimize bakalım.

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

Yukarıdaki istemden, oluşturulan tüm görsellerin metapromptu dikkate aldığını görebilirsiniz.

## Görev - Haydi öğrencileri etkinleştirelim

Bu dersin başında Edu4All'dan bahsetmiştik. Şimdi öğrencilerin değerlendirmeleri için görseller üretmelerini sağlama zamanı.

Öğrenciler, değerlendirmeleri için anıtlar içeren görseller oluşturacaklar; hangi anıtlar olacağı tamamen öğrencilere bağlı. Öğrencilerden, bu görevde yaratıcılıklarını kullanarak bu anıtları farklı bağlamlarda yerleştirmeleri isteniyor.

## Çözüm

İşte olası bir çözüm:

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# import dotenv
dotenv.load_dotenv()

# Get endpoint and key from environment variables
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-02-01"
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
""""

try:
    # Create an image by using the image generation API
    generation_response = client.images.generate(
        prompt=prompt,    # Enter your prompt text here
        size='1024x1024',
        n=1,
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response.data[0].url  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except openai.BadRequestError as err:
    print(err)
```

## Harika! Öğrenmeye Devam Edin
Bu dersi tamamladıktan sonra, Generatif Yapay Zeka bilginizi geliştirmeye devam etmek için [Generatif Yapay Zeka Öğrenme koleksiyonumuza](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) göz atabilirsiniz!

Bir sonraki adımda, 10. Derse geçerek [düşük kod ile yapay zeka uygulamaları nasıl geliştirilir](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) konusuna bakacağız.

---

**Feragatname**:  
Bu belge, yapay zeka çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerde hata veya yanlışlıklar bulunabileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından doğabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.