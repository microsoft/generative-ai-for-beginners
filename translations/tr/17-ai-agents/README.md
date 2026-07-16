[![Open Source Models](../../../translated_images/tr/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Giriş

AI Ajanları, Büyük Dil Modellerinin (LLM'ler) asistanlardan eylem gerçekleştirebilen ajanlara dönüşmesini sağlayan Üretken Yapay Zeka'daki heyecan verici bir gelişmeyi temsil eder. AI Ajan çerçeveleri, geliştiricilere LLM'lere araçlara ve durum yönetimine erişim sağlayan uygulamalar oluşturma olanağı tanır. Bu çerçeveler ayrıca görünürlüğü artırır, böylece kullanıcılar ve geliştiriciler LLM'lerin planladığı eylemleri izleyebilir ve deneyim yönetimini geliştirebilir.

Ders aşağıdaki alanları kapsayacaktır:

- AI Agent'ın ne olduğunu anlamak - AI Agent tam olarak nedir?
- Beş farklı AI Agent Çerçevesini keşfetmek - Onları benzersiz kılan nedir?
- Bu AI Agent'ları farklı kullanım alanlarına uygulamak - AI Agent'lar ne zaman kullanılmalıdır?

## Öğrenme hedefleri

Bu dersi tamamladıktan sonra şunları yapabileceksiniz:

- AI Agent'ların ne olduğunu ve nasıl kullanılabileceğini açıklayabilmek.
- Popüler AI Agent Çerçeveleri arasındaki farkları anlamak ve aralarındaki farklılıkları kavramak.
- AI Agent'ların nasıl çalıştığını anlayarak onlarla uygulama geliştirmek.

## AI Agent'lar Nedir?

AI Agent'lar, Üretken Yapay Zeka dünyasında son derece heyecan verici bir alandır. Bu heyecan bazen terimler ve uygulamalar konusunda karışıklığa yol açabilir. Çoğu AI Agent'a atıfta bulunan araçları kapsayacak şekilde işi basit tutmak için şu tanımı kullanacağız:

AI Agent'lar, Büyük Dil Modellerinin (LLM'ler) görevleri gerçekleştirmesine izin vererek onlara **durum** ve **araçlar**a erişim sağlar.

![Agent Model](../../../translated_images/tr/what-agent.21f2893bdfd01e6a.webp)

Bu terimleri tanımlayalım:

**Büyük Dil Modelleri** - Bu dersin genelinde bahsedilen GPT-3.5, GPT-4, Llama-2 gibi modellerdir.

**Durum** - LLM'nin çalıştığı bağlamı ifade eder. LLM, geçmiş eylemlerinin ve mevcut bağlamın içeriğini kullanarak sonraki eylemlerde kararlarını yönlendirir. AI Agent Çerçeveleri, geliştiricilerin bu bağlamı daha kolay korumasını sağlar.

**Araçlar** - Kullanıcının istediği ve LLM'nin planladığı görevi tamamlamak için LLM'nin araçlara erişimi gerekir. Örnek araçlar veritabanı, API, harici uygulama ya da başka bir LLM olabilir!

Bu tanımlar, ileride nasıl uygulandıklarını incelerken size sağlam bir temel sağlayacaktır. Hadi birkaç farklı AI Agent çerçevesini keşfedelim:

## LangChain Agent'ları

[LangChain Agent'ları](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) yukarıda verdiğimiz tanımların bir uygulanışıdır.

**Durum** yönetmek için, `AgentExecutor` adlı yerleşik bir fonksiyon kullanır. Bu, tanımlanmış `agent` ve ona erişimi olan `tools`u kabul eder.

`Agent Executor` ayrıca sohbet geçmişini depolar ve sohbetin bağlamını sağlar.

![Langchain Agents](../../../translated_images/tr/langchain-agents.edcc55b5d5c43716.webp)

LangChain, uygulamanıza ithal edilebilen ve LLM'nin erişebileceği [bir araç kataloğu](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) sunar. Bunlar topluluk ve LangChain ekibi tarafından yapılmıştır.

Daha sonra bu araçları tanımlayıp `Agent Executor`a geçirebilirsiniz.

Görünürlük, AI Agent'ları konuşurken önemli bir diğer konudur. Uygulama geliştiricilerinin LLM'nin hangi aracı kullandığını ve neden kullandığını anlaması önemlidir. Bu nedenle LangChain ekibi LangSmith’i geliştirdi.

## AutoGen

Sonraki AI Agent çerçevesi [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). AutoGen'in ana odağı sohbetlerdir. Agent'lar hem **konuşabilir** hem de **özelleştirilebilir**.

**Konuşabilir -** LLM'ler, bir görevi tamamlamak için başka bir LLM ile konuşmaya başlayabilir ve devam edebilir. Bu, `AssistantAgents` oluşturularak ve onlara belirli bir sistem mesajı verilerek yapılır.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Özelleştirilebilir** - Agent'lar yalnızca LLM olarak değil, kullanıcı veya araç olarak da tanımlanabilir. Geliştirici olarak, görevin tamamlanmasında kullanıcıyla etkileşimi sağlamak için sorumlu `UserProxyAgent` oluşturabilirsiniz. Bu geri bildirim ya görevin devamını sağlar ya da durdurur.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Durum ve Araçlar

Durumu değiştirmek ve yönetmek için bir asistan Agent, görevi tamamlamak üzere Python kodu üretir.

İşte sürecin bir örneği:

![AutoGen](../../../translated_images/tr/autogen.dee9a25a45fde584.webp)

#### Sistem Mesajı ile Tanımlanmış LLM

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Bu sistem mesajı, bu belirli LLM'ye görev için hangi fonksiyonların ilgili olduğunu belirtir. Unutmayın, AutoGen ile farklı sistem mesajlarına sahip birden fazla AssistantAgents tanımlayabilirsiniz.

#### Sohbet Kullanıcı Tarafından Başlatılır

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Kullanıcı aracı (UserProxy) tarafından gelen bu mesaj, Agent'ın hangi fonksiyonları çalıştırması gerektiğini keşfetme sürecini başlatır.

#### Fonksiyon Çalıştırılır

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

İlk sohbet işlendiğinde, Agent çağrılması önerilen aracı gönderir. Bu durumda, `get_weather` adlı bir fonksiyondur. Konfigürasyonunuza bağlı olarak bu fonksiyon otomatik olarak Agent tarafından yürütülebilir veya kullanıcı girişi bazında çalıştırılabilir.

Başlamak için daha fazla keşfetmek üzere [AutoGen kod örnekleri](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) bulabilirsiniz.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst), Microsoft'un hem **Python** hem de **.NET** dillerinde AI Agent'lar ve çoklu-agent sistemleri oluşturmak için açık kaynak SDK'sıdır. Bu, iki önceki Microsoft projesinin güçlü yönlerini - **Semantic Kernel**in kurumsal özellikleri ve **AutoGen**in çoklu-agent orkestrasyonunu - tek, desteklenen bir çerçevede birleştirir. Bugün yeni bir agent projesine başlıyorsanız, AutoGen'in önerilen devamıdır.

Çerçeve, tek bir **sohbet ajanından** karmaşık **çoklu ajan iş akışlarına** kadar ölçeklenir ve doğrudan Microsoft Foundry, Azure OpenAI ve OpenAI ile entegredir. Ayrıca OpenTelemetry ile yerleşik gözlemlenebilirlik sağlar, böylece ajanlarınızın tam olarak ne yaptığını izleyebilirsiniz.

### Durum ve Araçlar

**Durum** - Çerçeve, sohbet bağlamını **iş parçacıkları (threads)** yoluyla sizin için yönetir. Bir ajan, mesaj geçmişini (kullanıcı istekleri, araç çağrıları ve sonuçları) takip eder, böylece her adım öncekilerin üzerine inşa edilir. İş parçacıkları ayrıca kaydedilebilir, böylece bir konuşma duraklatılıp daha sonra devam ettirilebilir.

**Araçlar** - Bir ajana araçları sade Python fonksiyonlarını geçerek verirsiniz. Tip açıklamalı parametreler otomatik olarak bir şemaya dönüştürülür, böylece model bunları ne zaman ve nasıl çağıracağını bilir (fonksiyon çağrısı). Çerçeve ayrıca Model Context Protocol (MCP) sunucularını ve kod yorumlayıcı gibi barındırılan araçları destekler.

İşte özel bir araç ile tek bir ajanın örneği:

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

Microsoft Foundry'de Azure OpenAI'ye bağlanmak için, uç noktayı ve kimlik bilgilerinizi client'a iletin:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Çoklu ajan iş akışları

Çerçevenin gerçekten öne çıktığı alan, birkaç ajanı birlikte orkestre etmektir. Örneğin, ajanları birbiri ardına çalıştırabilirsiniz (her biri bağlamını bir sonrakine aktarır) veya birden çok ajanı paralel olarak çalıştırıp sonuçları toplayabilirsiniz:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Konuşma bağlamını zincir boyunca geçirerek ajanları sırayla çalıştır
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Ajanlara paralel olarak dağıt ve ardından yanıtlarını birleştir
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Çerçeveyi kurmak ve başlamak için:

```bash
pip install agent-framework-core
# İsteğe bağlı entegrasyonlar
pip install agent-framework-openai       # OpenAI ve Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Daha fazlasını [Microsoft Agent Framework deposunda](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) ve [resmi belgelerde](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) keşfedebilirsiniz.

## Taskweaver

Keşfedeceğimiz sonraki ajan çerçevesi [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Buna "kod-öncelikli" ajan denir çünkü sadece `string`lerle değil, Python'da DataFrame'lerle çalışabilir. Bu, veri analizi ve üretim görevleri için çok kullanışlıdır. Örneğin grafik ve tablo oluşturmak veya rastgele sayı üretmek gibi işlevler olabilir.

### Durum ve Araçlar

Konuşma durumunu yönetmek için TaskWeaver, `Planner` kavramını kullanır. `Planner` kullanıcı isteklerini alıp bu isteği yerine getirmek için tamamlanması gereken görevleri haritalandıran bir LLM'dir.

Görevleri tamamlamak için `Planner`, `Plugins` adı verilen araç koleksiyonuna erişim sağlar. Bunlar Python sınıfları veya genel bir kod yorumlayıcısı olabilir. Bu eklentiler gömülü (embedding) olarak saklanır, böylece LLM doğru eklentiyi daha iyi arayabilir.

![Taskweaver](../../../translated_images/tr/taskweaver.da8559999267715a.webp)

İşte anomali tespiti yapan bir eklenti örneği:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Kod çalıştırılmadan önce doğrulanır. Taskweaver'da bağlamı yönetmek için bir diğer özellik `experience`dır. Experience, bir konuşmanın bağlamının uzun vadede YAML dosyasına kaydedilmesini sağlar. Bu, LLM'nin daha önceki konuşmalara maruz kalması sayesinde bazı görevlerde zamanla gelişmesini mümkün kılar.

## JARVIS

Son keşfedeceğimiz ajan çerçevesi [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). JARVIS'i benzersiz yapan, konuşma `durumunu` bir LLM'nin yönetmesi ve `araçlar` olarak diğer AI modellerinin kullanılmasıdır. Her AI modeli, nesne tespiti, yazıya dökme veya resim açıklaması gibi belirli görevler için uzmanlaşmıştır.

![JARVIS](../../../translated_images/tr/jarvis.762ddbadbd1a3a33.webp)

Genel amaçlı bir model olan LLM, kullanıcıdan isteği alır ve belirli görevi ve görevin tamamlanması için gereken argüman/verileri tanımlar.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM ardından isteği özel AI modelinin yorumlayabileceği şekilde, örneğin JSON olarak biçimlendirir. AI modeli göreve göre tahminini yaptıktan sonra LLM cevabı alır.

Görevi tamamlamak için birden çok model gerekiyorsa, önce bu modellerin yanıtlarını yorumlar, sonra bunları birleştirip kullanıcıya yanıt üretir.

Aşağıdaki örnek, bir kullanıcının bir resimdeki nesnelerin açıklamasını ve sayısını talep ettiğinde nasıl çalışacağını gösterir:

## Ödev

AI Agent'ları öğrenmeye Microsoft Agent Framework ile devam edebilirsiniz:

- Eğitim girişiminin farklı departmanlarının iş toplantısını simüle eden bir uygulama oluşturun.
- LLM'lerin farklı persona ve öncelikleri anlamasını rehberlik eden sistem mesajları oluşturun ve kullanıcının yeni bir ürün fikrini sunmasını sağlayın.
- LLM ardından her departmandan sunumu ve ürün fikrini geliştirmek için takip soruları oluşturmalıdır.

## Öğrenme burada bitmez, yolculuğa devam edin

Bu dersi tamamladıktan sonra, Üretken Yapay Zeka bilginizi artırmak için [Generative AI Learning koleksiyonumuzu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) inceleyin!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->