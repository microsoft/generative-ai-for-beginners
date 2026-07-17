# Construindo Aplicações de Geração de Imagens

[![Construindo Aplicações de Geração de Imagens](../../../translated_images/pt-BR/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Há mais em LLMs do que geração de texto. Você também pode gerar imagens a partir de descrições em texto. Imagens como uma modalidade são úteis em MedTech, arquitetura, turismo, desenvolvimento de jogos, marketing e muito mais. Nesta lição, analisamos os modelos de **GPT Image** atuais e construímos um app de geração de imagens.

## Introdução

A geração de imagens permite transformar um comando em linguagem natural em uma figura. Nesta lição, trabalhamos com a família de modelos **`gpt-image`** da OpenAI - a geração atual dos modelos de imagem disponíveis no **[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)** e na plataforma OpenAI. Esses modelos substituem os antigos modelos DALL·E (DALL·E 2/3 são legados).

Ao longo da lição usamos uma startup fictícia, **Edu4All**, que constrói ferramentas de aprendizado. A equipe quer gerar ilustrações para tarefas e materiais de estudo.

## Objetivos de aprendizado

Ao final desta lição você será capaz de:

- Explicar o que é geração de imagens e onde ela é útil.
- Entender a família de modelos `gpt-image` e como ela difere dos modelos legados DALL·E.
- Construir um app de geração de imagens em Python (e TypeScript / .NET).
- Editar imagens e aplicar salvaguardas com metaprompts.

## O que é geração de imagens?

Modelos de geração de imagem criam imagens a partir de um comando em texto. Modelos modernos como `gpt-image` são construídos com técnicas de transformador + difusão: o modelo aprende a relação entre texto e imagem durante o treinamento, então, dado um comando, ele "limpa o ruído" iterativamente a partir de ruído aleatório até formar uma imagem que corresponde à descrição.

Duas famílias bem conhecidas de modelos de imagem são:

- **`gpt-image` (OpenAI)** - a geração atual, usada nesta lição. Suporta geração texto-para-imagem e edição de imagens (pintura com máscara).
- **Midjourney** - modelo popular de terceiros com seu próprio serviço e fluxo via Discord.

> Modelos OpenAI antigos - **DALL·E 2** e **DALL·E 3** - são legados. DALL·E 3 não está mais disponível para novos deployments e recursos como `create_variation` existiam só no DALL·E 2. Use os modelos `gpt-image` para novas aplicações.

### Qual modelo `gpt-image` devo usar?

No Microsoft Foundry os seguintes modelos são **Geralmente Disponíveis**:

| Modelo | Notas |
| --- | --- |
| **`gpt-image-2`** | O modelo de imagem mais recente e capaz - padrão recomendado. |
| `gpt-image-1.5` | Geralmente disponível; boa qualidade a custo menor. |
| `gpt-image-1-mini` | Geralmente disponível; mais rápido / menor custo. |
| `gpt-image-1` | Apenas visualização. |

Sempre verifique a atual [lista de modelos de imagem Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst) para disponibilidade e regiões.

> **Importante:** modelos `gpt-image` retornam a imagem gerada como **base64** (`b64_json`), não como URL. Seu código decodifica a string base64 em bytes e salva a imagem - não há URL para baixar.

## Configuração

Você pode executar os exemplos contra o **Azure OpenAI no Microsoft Foundry** (os exemplos `aoai-*`) ou a **plataforma OpenAI** (os exemplos `oai-*`).

### 1. Crie e faça o deploy de um modelo

Siga o guia [criar um recurso](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) para criar um recurso Microsoft Foundry, depois faça o deploy de um modelo de imagem - **`gpt-image-2`** é recomendado.

### 2. Configure seu `.env`

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

Encontre esses valores na página **Deployments** do seu recurso no [portal Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst).

### 3. Instale as bibliotecas

Crie um `requirements.txt`:

```text
python-dotenv
openai
pillow
```

Então crie e ative um ambiente virtual e instale:

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Construa o app

Crie `app.py` com o código abaixo. Ele gera uma imagem e salva como PNG.

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# Aponte o cliente para seu recurso Azure OpenAI (Microsoft Foundry).
# Modelos de imagem precisam de uma versão recente da API - verifique a documentação do Foundry para saber qual sua modelo requer.
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # ex. "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # também 1536x1024 (paisagem), 1024x1536 (retrato), ou "auto"
    n=1,
)

# modelos gpt-image retornam base64 (b64_json), não uma URL - decodifique para bytes.
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

Execute com `python app.py`. Você terá um PNG salvo em `images/`.

> Cada chamada a `images.generate` produz uma imagem diferente para o mesmo comando - modelos de imagem não usam o parâmetro `temperature` (isso é para controle de geração de texto). Para variedade, chame a API novamente; para menos variedade, faça seu comando mais específico.

## Editando imagens

Modelos `gpt-image` podem **editar** uma imagem existente: forneça a imagem, uma **máscara** opcional (que indica a área a mudar) e um comando descrevendo a alteração. Como na geração, as edições são retornadas em base64.

```python
result = client.images.edit(
    model=deployment,
    image=open("sunlit_lounge.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="A sunlit indoor lounge area with a pool containing a flamingo",
)
image_bytes = base64.b64decode(result.data[0].b64_json)
with open("images/edited-image.png", "wb") as f:
    f.write(image_bytes)
```

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/pt-BR/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/pt-BR/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/pt-BR/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## Definindo limites com metaprompts

Quando você consegue gerar imagens, precisa de salvaguardas para que seu app não produza conteúdo inseguro ou fora da marca. Um **metaprompt** é um texto que você antepõe ao comando do usuário para limitar a saída do modelo.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# passe `prompt` para client.images.generate(...)
```

Cada imagem agora é gerada dentro dos limites definidos pelo metaprompt. Combine isso com os filtros de conteúdo integrados no Microsoft Foundry para defesa em profundidade.

## Tarefa - vamos ajudar os estudantes

Estudantes da Edu4All precisam de imagens para suas avaliações. Construa um app que gere imagens de **monumentos** (quais monumentos fica a seu critério) colocados em contextos diferentes e criativos - por exemplo, um ponto turístico famoso ao pôr do sol com uma criança olhando.

Experimente você mesmo, depois compare com as soluções de referência:

- Python (Azure): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python (Azure) app completo de geração: [aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

Também trabalhe com os notebooks em [python/](../../../09-building-image-applications/python) (`aoai-assignment.ipynb` para Azure, `oai-assignment.ipynb` para OpenAI).

## Ótimo trabalho! Continue seu aprendizado

Depois de completar esta lição, confira nossa [coleção de Aprendizado em IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seus conhecimentos em IA Generativa!

Vá para a lição 10 para continuar aprendendo.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->