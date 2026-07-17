[![Açık Kaynak Modeller](../../../translated_images/tr/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Giriş

Yapay Zeka Ajanları, Üretken Yapay Zeka alanındaki heyecan verici bir gelişmeyi temsil eder ve Büyük Dil Modellerinin (LLM'ler) asistanlardan eylem alabilen ajanlara dönüşmesini sağlar. Yapay Zeka Ajan çerçeveleri, geliştiricilerin LLM'lere araçlara ve durum yönetimine erişim sağlayan uygulamalar oluşturmalarına olanak tanır. Bu çerçeveler ayrıca görünürlüğü artırır; böylece kullanıcılar ve geliştiriciler LLM'lerin planladığı eylemleri izleyebilir, bu da deneyim yönetimini geliştirir.

Ders aşağıdaki alanları kapsayacaktır:

- Yapay Zeka Ajanının ne olduğunu anlama - Yapay Zeka Ajanı tam olarak nedir?
- Beş farklı Yapay Zeka Ajan Çerçevesini keşfetme - Onları benzersiz kılan nedir?
- Bu Yapay Zeka Ajanlarını farklı kullanım durumlarına uygulama - Yapay Zeka Ajanları ne zaman kullanılmalıdır?

## Öğrenme hedefleri

Bu dersi tamamladıktan sonra şunları yapabileceksiniz:

- Yapay Zeka Ajanlarının ne olduğunu ve nasıl kullanılabileceğini açıklayabilmek.
- Popüler Yapay Zeka Ajan Çerçeveleri arasındaki farkları ve nasıl farklı olduklarını anlamak.
- Uygulama geliştirmek için Yapay Zeka Ajanlarının nasıl çalıştığını kavramak.

## Yapay Zeka Ajanları Nedir?

Yapay Zeka Ajanları, Üretken Yapay Zeka dünyasında çok heyecan verici bir alandır. Bu heyecan bazen terimlerin ve uygulamalarının karışıklığına yol açabilir. Konuları olabildiğince basit tutmak ve Yapay Zeka Ajanlarına atıfta bulunan çoğu aracı kapsamak için şu tanımı kullanacağız:

Yapay Zeka Ajanları, Büyük Dil Modellerinin (LLM'ler) **duruma** ve **araçlara** erişim vererek görevler gerçekleştirmelerine olanak tanır.

![Ajan Modeli](../../../translated_images/tr/what-agent.21f2893bdfd01e6a.webp)

Bu terimleri tanımlayalım:

**Büyük Dil Modelleri** - Bu derste değindiğimiz GPT-5, GPT-4o ve Llama 3.3 gibi modellerdir.

**Durum** - Bu, LLM'nin çalıştığı bağlama atıfta bulunur. LLM, önceki eylemlerinin bağlamını ve mevcut durumu kullanarak sonraki eylemlerine rehberlik eder. Yapay Zeka Ajan Çerçeveleri, geliştiricilerin bu bağlamı daha kolay yönetmelerini sağlar.

**Araçlar** - Kullanıcının istediği ve LLM'nin planladığı görevleri tamamlamak için araçlara erişim gereklidir. Araçlara örnek olarak veri tabanı, API, harici bir uygulama veya başka bir LLM verilebilir!

Bu tanımlar, uygulamalarına baktığımızda ileriye yönelik sağlam bir temel oluşturmanıza yardımcı olacaktır. Şimdi birkaç farklı Yapay Zeka Ajan çerçevesini keşfedelim:

## LangChain Ajanları

[LangChain Ajanları](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) yukarıda verdiğimiz tanımların bir uygulamasıdır.

**Durumu** yönetmek için `AgentExecutor` adlı yerleşik bir fonksiyon kullanır. Bu fonksiyon tanımlanmış `ajanın` ve ona erişilebilir `araçların` kabulünü sağlar.

`AgentExecutor` ayrıca sohbet geçmişini saklayarak sohbet bağlamını sağlar.

![Langchain Ajanları](../../../translated_images/tr/langchain-agents.edcc55b5d5c43716.webp)

LangChain, LLM'nin erişebileceği araçları uygulamanıza ithal edebileceğiniz bir [araç kataloğu](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) sunar. Bu araçlar topluluk ve LangChain ekibi tarafından yapılmıştır.

Bu araçları tanımlayabilir ve `AgentExecutor`'a geçirebilirsiniz.

Görünürlük, Yapay Zeka Ajanları konuşulduğunda önemli bir diğer konudur. Uygulama geliştiricilerinin LLM'nin hangi aracı neden kullandığını anlamaları önemlidir. Bunun için LangChain ekibi LangSmith'i geliştirmiştir.

## AutoGen

Bir sonraki tartışacağımız Yapay Zeka Ajan çerçevesi [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). AutoGen'in ana odağı sohbetlerdir. Ajanlar hem **konuşabilir** hem de **özelleştirilebilir**.

**Konuşabilir -** LLM'ler, bir görevi tamamlamak için başka bir LLM ile sohbet başlatabilir ve sürdürebilir. Bu, `AssistantAgents` yaratılarak ve onlara belirli bir sistem mesajı verilerek yapılır.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Özelleştirilebilir** - Ajanlar yalnızca LLM olarak değil, kullanıcı ya da araç olarak da tanımlanabilir. Geliştirici olarak, bir görevin tamamlanması için kullanıcıdan geri bildirim alması sorumlu `UserProxyAgent` tanımlayabilirsiniz. Bu geri bildirim, görevin yürütülmesini sürdürebilir veya durdurabilir.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Durum ve Araçlar

Durumu değiştirmek ve yönetmek için bir asistan ajan, görevi tamamlamak üzere Python kodu üretir.

Süreç şu şekilde örneklenebilir:

![AutoGen](../../../translated_images/tr/autogen.dee9a25a45fde584.webp)

#### Sistem Mesajı ile Tanımlı LLM

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Bu sistem mesajı, bu özel LLM'nin görevine uygun olan fonksiyonları yönlendirir. AutoGen ile farklı sistem mesajlarına sahip birden fazla AssistantAgent tanımlayabileceğinizi unutmayın.

#### Sohbet Kullanıcı Tarafından Başlatıldı

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Bu kullanıcı_proxy (İnsan) mesajı, Ajanın hangi fonksiyonları yürütmesi gerektiğini keşfetme sürecini başlatacaktır.

#### Fonksiyon Yürütülür

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Başlangıç sohbeti işlendikten sonra Ajan çağrılması önerilen aracı gönderir. Burada `get_weather` adlı bir fonksiyon vardır. Konfigürasyonunuza bağlı olarak, bu fonksiyon otomatik olarak çalıştırılabilir ve okunabilir ya da kullanıcı girdisine bağlı olarak çalıştırılabilir.

Başlamak için nasıl bir yol izleneceğini daha fazla keşfetmek amacıyla bazı [AutoGen kod örneklerine](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) bakabilirsiniz.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst), Microsoft'un hem **Python** hem de **.NET** için Yapay Zeka Ajanları ve çok ajanlı sistemler oluşturmak için açık kaynak SDK'sıdır. Bu, Microsoft'un önceki iki projesinin — **Semantic Kernel**'in kurumsal özellikleri ve **AutoGen**'in çok-ajan orkestrasyonu — güçlü yönlerini tek, desteklenen bir çerçevede birleştirir. Bugün yeni bir ajan projesine başlıyorsanız, AutoGen'in önerilen halefidir.

Bu çerçeve, tek bir **sohbet ajanından** karmaşık **çok-ajan iş akışlarına** kadar ölçeklenir ve Microsoft Foundry, Azure OpenAI ve OpenAI ile doğrudan entegre olur. Ayrıca, ajanlarınızın tam olarak ne yaptığını izleyebilmeniz için OpenTelemetry aracılığıyla yerleşik gözlemlenebilirlik sunar.

### Durum ve Araçlar

**Durum** - Çerçeve, sizin için sohbet bağlamını **thread'ler** aracılığıyla yönetir. Bir ajan mesaj geçmişini (kullanıcı istekleri, araç çağrıları ve sonuçları) takip eder, böylece her tur öncekinin üzerine kurulur. Thread'ler ayrıca korunabilir, böylece bir sohbet duraklatılıp sonra devam ettirilebilir.

**Araçlar** - Bir ajana araçları, düz Python fonksiyonları olarak verirsiniz. Tip açıklamalı parametreler otomatik olarak bir şemaya dönüştürülür, böylece model onları nasıl ve ne zaman çağıracağını bilir (fonksiyon çağrımı). Çerçeve ayrıca Model Context Protocol (MCP) sunucularını ve kod yorumlayıcı gibi barındırılan araçları destekler.

İşte özel bir araçla tek bir ajan örneği:

```python
import asyncio
from typing import Annotated

from pydantic import Field
from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient


def get_weather(
    location: Annotated[str, Field(description="The location to get the weather for.")],
) -> str:
    """Get the weather for a given location."""
    return f"The weather in {location} is sunny with a high of 22°C."


async def main():
    agent = Agent(
        client=OpenAIChatClient(),
        instructions="You are a helpful assistant that can answer weather questions.",
        tools=[get_weather],
    )

    response = await agent.run("What's the weather in Amsterdam?")
    print(response)


asyncio.run(main())
```

Microsoft Foundry'de Azure OpenAI'ye bağlanmak için, uç noktanızı ve kimlik bilgilerinizi istemciye verin:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Çok-ajan iş akışları

Çerçevenin gerçekten öne çıktığı alan, birden fazla ajanı birlikte orkestre etmesidir. Örneğin, ajanları sırayla çalıştırabilir (her biri bağlamını diğerine aktarır) veya birkaç ajanı paralel olarak çalıştırıp sonuçlarını birleştebilirsiniz:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Ajanları sırayla çalıştırın, konuşma bağlamını zincir boyunca geçirin
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Ajanlara paralel olarak yayılın, ardından yanıtlarını toplayın
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Çerçeveyi kurmak ve başlamak için:

```bash
pip install agent-framework-core
# İsteğe bağlı entegrasyonlar
pip install agent-framework-openai       # OpenAI ve Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Daha fazla keşfetmek için [Microsoft Agent Framework deposunu](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) ve [resmi dokümantasyonu](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) inceleyebilirsiniz.

## Taskweaver

Bir sonraki keşfedeceğimiz ajan çerçevesi [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Bu, katı string yerine Python'da Veri Çerçeveleri (DataFrame) ile çalışabildiği için "kod-öncelikli" bir ajan olarak bilinir. Bu, veri analizi ve üretimi görevleri için son derece faydalıdır. Örneğin grafik/chart oluşturma veya rastgele sayı üretme gibi.

### Durum ve Araçlar

Konuşma durumunu yönetmek için TaskWeaver, `Planner` kavramını kullanır. `Planner` kullanıcı isteklerini alan ve yerine getirilmesi gereken görevlerin haritasını çıkaran bir LLM'dir.

Görevleri tamamlamak için `Planner`, `Plugins` adı verilen araç koleksiyonuna maruz bırakılır. Bu, Python sınıfları veya genel bir kod yorumlayıcı olabilir. Bu eklentiler, LLM'nin doğru eklentiyi daha iyi arayabilmesi için gömme (embedding) olarak saklanır.

![Taskweaver](../../../translated_images/tr/taskweaver.da8559999267715a.webp)

İşte anormallik tespiti için bir eklenti örneği:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Kod yürütülmeden önce doğrulanır. Taskweaver'da bağlamı yönetmek için başka bir özellik `experience`dır. Experience, bir konuşma bağlamının uzun vadede bir YAML dosyasına kaydedilmesine olanak tanır. Bu, LLM'nin önceki konuşmalardan öğrenerek belirli görevlerde zamanla gelişmesini sağlayacak şekilde yapılandırılabilir.

## JARVIS

Keşfedeceğimiz son ajan çerçevesi [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). JARVIS'i benzersiz yapan, sohbetin `durumunu` yönetmek için bir LLM kullanması ve `araçların` diğer Yapay Zeka modelleri olmasıdır. Her bir Yapay Zeka modeli, nesne tespiti, transkripsiyon veya resim alt yazısı oluşturma gibi belirli görevler için uzmanlaşmış modellerdir.

![JARVIS](../../../translated_images/tr/jarvis.762ddbadbd1a3a33.webp)

Genel amaçlı model olan LLM, kullanıcıdan isteği alır ve görevi belirler, tamamlamak için gereken argümanları/verileri tanımlar.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM, isteği, uzmanlaşmış Yapay Zeka modelinin yorumlayabileceği şekilde (örneğin JSON) formatlar. Yapay Zeka modeli tahminini döndürdüğünde, LLM yanıtı alır.

Görevi tamamlamak için birden fazla modele ihtiyaç varsa, LLM bu modellerin yanıtlarını da yorumlayacak ve bunları birleştirerek kullanıcıya cevap oluşturacaktır.

Aşağıdaki örnek, kullanıcının bir resimdeki nesnelerin açıklamasını ve sayısını istediğinde nasıl çalışacağını gösterir:

## Ödev

Yapay Zeka Ajanları öğreniminize Microsoft Agent Framework ile devam edebilirsiniz:

- Bir eğitim başlangıç şirketinin farklı departmanları ile bir iş toplantısını simüle eden bir uygulama.
- LLM'lerin farklı kişilikleri ve öncelikleri anlamasına rehberlik eden sistem mesajları oluşturun ve kullanıcıya yeni bir ürün fikrini sunma imkanı verin.
- Sonra, her departman için sunumu ve ürün fikrini geliştirmek üzere takip soruları üretsin.

## Öğrenme burada bitmiyor, yolculuğa devam edin

Bu dersi tamamladıktan sonra, Üretken Yapay Zeka bilginizi ilerletmek için [Üretken Yapay Zeka Öğrenme koleksiyonumuza](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) göz atın!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->