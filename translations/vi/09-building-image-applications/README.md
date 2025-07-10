<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a7fd0f95f9eb673b79da47c0814f4d4",
  "translation_date": "2025-07-09T13:29:28+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "vi"
}
-->
# Xây dựng Ứng dụng Tạo Hình ảnh

[![Xây dựng Ứng dụng Tạo Hình ảnh](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.vi.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM không chỉ dùng để tạo văn bản. Bạn cũng có thể tạo hình ảnh từ mô tả bằng văn bản. Việc có hình ảnh như một phương thức truyền tải có thể rất hữu ích trong nhiều lĩnh vực như MedTech, kiến trúc, du lịch, phát triển game và nhiều hơn nữa. Trong chương này, chúng ta sẽ tìm hiểu về hai mô hình tạo hình ảnh phổ biến nhất, DALL-E và Midjourney.

## Giới thiệu

Trong bài học này, chúng ta sẽ đề cập đến:

- Tạo hình ảnh và lý do tại sao nó hữu ích.
- DALL-E và Midjourney là gì, và cách chúng hoạt động.
- Cách xây dựng một ứng dụng tạo hình ảnh.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Xây dựng một ứng dụng tạo hình ảnh.
- Định nghĩa giới hạn cho ứng dụng của bạn bằng meta prompts.
- Làm việc với DALL-E và Midjourney.

## Tại sao nên xây dựng ứng dụng tạo hình ảnh?

Ứng dụng tạo hình ảnh là cách tuyệt vời để khám phá khả năng của Generative AI. Chúng có thể được sử dụng cho, ví dụ:

- **Chỉnh sửa và tổng hợp hình ảnh**. Bạn có thể tạo hình ảnh cho nhiều mục đích khác nhau, như chỉnh sửa hình ảnh và tổng hợp hình ảnh.

- **Áp dụng cho nhiều ngành công nghiệp**. Chúng cũng có thể được dùng để tạo hình ảnh cho nhiều ngành như Medtech, Du lịch, Phát triển game và nhiều hơn nữa.

## Tình huống: Edu4All

Trong bài học này, chúng ta sẽ tiếp tục làm việc với startup Edu4All. Học sinh sẽ tạo hình ảnh cho bài tập của mình, hình ảnh cụ thể do học sinh quyết định, có thể là minh họa cho câu chuyện cổ tích của riêng họ, tạo nhân vật mới cho câu chuyện hoặc giúp họ hình dung ý tưởng và khái niệm.

Dưới đây là ví dụ những gì học sinh Edu4All có thể tạo ra khi làm việc trên chủ đề các công trình kiến trúc:

![Edu4All startup, lớp học về các công trình kiến trúc, Tháp Eiffel](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.vi.png)

với prompt như

> "Chó bên cạnh Tháp Eiffel dưới ánh nắng ban mai"

## DALL-E và Midjourney là gì?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) và [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) là hai trong số các mô hình tạo hình ảnh phổ biến nhất, cho phép bạn sử dụng prompt để tạo hình ảnh.

### DALL-E

Bắt đầu với DALL-E, một mô hình Generative AI tạo hình ảnh từ mô tả bằng văn bản.

> [DALL-E là sự kết hợp của hai mô hình, CLIP và diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** là mô hình tạo embeddings, tức là các biểu diễn số của dữ liệu, từ hình ảnh và văn bản.

- **Diffused attention** là mô hình tạo hình ảnh từ embeddings. DALL-E được huấn luyện trên bộ dữ liệu gồm hình ảnh và văn bản, và có thể tạo hình ảnh từ mô tả bằng văn bản. Ví dụ, DALL-E có thể tạo hình ảnh một con mèo đội mũ, hoặc một con chó với kiểu tóc mohawk.

### Midjourney

Midjourney hoạt động tương tự DALL-E, tạo hình ảnh từ các prompt văn bản. Midjourney cũng có thể tạo hình ảnh với các prompt như “một con mèo đội mũ” hoặc “một con chó với kiểu tóc mohawk”.

![Hình ảnh do Midjourney tạo, chim bồ câu cơ khí](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Hình ảnh từ Wikipedia, do Midjourney tạo_

## DALL-E và Midjourney hoạt động như thế nào

Trước tiên, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E là mô hình Generative AI dựa trên kiến trúc transformer với _autoregressive transformer_.

Một _autoregressive transformer_ xác định cách mô hình tạo hình ảnh từ mô tả văn bản, nó tạo từng điểm ảnh một, rồi dùng các điểm ảnh đã tạo để tạo điểm ảnh tiếp theo. Quá trình này đi qua nhiều lớp trong mạng nơ-ron cho đến khi hình ảnh hoàn chỉnh.

Với quy trình này, DALL-E kiểm soát các thuộc tính, đối tượng, đặc điểm và nhiều yếu tố khác trong hình ảnh nó tạo ra. Tuy nhiên, DALL-E 2 và 3 có khả năng kiểm soát hình ảnh tạo ra tốt hơn.

## Xây dựng ứng dụng tạo hình ảnh đầu tiên của bạn

Vậy để xây dựng một ứng dụng tạo hình ảnh cần những gì? Bạn cần các thư viện sau:

- **python-dotenv**, được khuyến nghị dùng để giữ các thông tin bí mật trong file _.env_ tách biệt với mã nguồn.
- **openai**, thư viện dùng để tương tác với API OpenAI.
- **pillow**, để làm việc với hình ảnh trong Python.
- **requests**, giúp bạn thực hiện các yêu cầu HTTP.

1. Tạo file _.env_ với nội dung sau:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Thông tin này bạn có thể tìm trong Azure Portal ở phần "Keys and Endpoint" của tài nguyên.

1. Tập hợp các thư viện trên vào file _requirements.txt_ như sau:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Tiếp theo, tạo môi trường ảo và cài đặt các thư viện:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Với Windows, dùng các lệnh sau để tạo và kích hoạt môi trường ảo:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Thêm đoạn mã sau vào file _app.py_:

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

Giải thích đoạn mã này:

- Đầu tiên, chúng ta import các thư viện cần thiết, bao gồm thư viện OpenAI, dotenv, requests và Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Tiếp theo, chúng ta tải các biến môi trường từ file _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Sau đó, thiết lập endpoint, key cho API OpenAI, phiên bản và loại.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Tiếp theo, tạo hình ảnh:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Đoạn mã trên trả về một đối tượng JSON chứa URL của hình ảnh được tạo. Chúng ta có thể dùng URL này để tải hình ảnh và lưu vào file.

- Cuối cùng, mở hình ảnh và dùng trình xem ảnh mặc định để hiển thị:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Chi tiết hơn về việc tạo hình ảnh

Hãy xem kỹ đoạn mã tạo hình ảnh:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt** là đoạn văn bản dùng để tạo hình ảnh. Ở đây, chúng ta dùng prompt "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils".
- **size** là kích thước hình ảnh được tạo. Ở đây, hình ảnh có kích thước 1024x1024 pixel.
- **n** là số lượng hình ảnh được tạo. Ở đây, chúng ta tạo hai hình ảnh.
- **temperature** là tham số điều khiển độ ngẫu nhiên của kết quả từ mô hình Generative AI. Giá trị nằm trong khoảng từ 0 đến 1, trong đó 0 nghĩa là kết quả xác định, 1 nghĩa là kết quả ngẫu nhiên. Giá trị mặc định là 0.7.

Còn nhiều điều bạn có thể làm với hình ảnh mà chúng ta sẽ đề cập trong phần tiếp theo.

## Các khả năng bổ sung của tạo hình ảnh

Bạn đã thấy cách tạo hình ảnh chỉ với vài dòng Python. Tuy nhiên, còn nhiều điều khác bạn có thể làm với hình ảnh.

Bạn cũng có thể:

- **Thực hiện chỉnh sửa**. Bằng cách cung cấp một hình ảnh hiện có, một mặt nạ và một prompt, bạn có thể thay đổi hình ảnh. Ví dụ, bạn có thể thêm một vật thể vào một phần của hình ảnh. Hãy tưởng tượng hình ảnh con thỏ của chúng ta, bạn có thể thêm một chiếc mũ cho con thỏ. Cách làm là cung cấp hình ảnh, mặt nạ (xác định phần cần thay đổi) và prompt văn bản để mô tả thay đổi.

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

  Hình ảnh gốc chỉ có con thỏ, nhưng hình ảnh cuối cùng sẽ có thêm chiếc mũ trên con thỏ.

- **Tạo các biến thể**. Ý tưởng là bạn lấy một hình ảnh hiện có và yêu cầu tạo các biến thể. Để tạo biến thể, bạn cung cấp hình ảnh và prompt văn bản, cùng đoạn mã như sau:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Lưu ý, tính năng này chỉ được hỗ trợ trên OpenAI

## Temperature

Temperature là tham số điều khiển độ ngẫu nhiên của kết quả từ mô hình Generative AI. Giá trị nằm trong khoảng từ 0 đến 1, trong đó 0 nghĩa là kết quả xác định, 1 nghĩa là kết quả ngẫu nhiên. Giá trị mặc định là 0.7.

Hãy xem ví dụ về cách temperature hoạt động, bằng cách chạy prompt này hai lần:

> Prompt : "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![Bunny trên ngựa cầm kẹo mút, phiên bản 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.vi.png)

Bây giờ chạy lại prompt đó để thấy rằng chúng ta sẽ không có hai hình ảnh giống hệt nhau:

![Hình ảnh con thỏ trên ngựa được tạo](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.vi.png)

Như bạn thấy, các hình ảnh tương tự nhau nhưng không giống hệt. Hãy thử thay đổi giá trị temperature thành 0.1 và xem điều gì xảy ra:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Thay đổi temperature

Hãy thử làm cho kết quả có tính xác định hơn. Từ hai hình ảnh tạo ra, ta thấy hình ảnh đầu có con thỏ, hình ảnh thứ hai có con ngựa, nên hình ảnh khác biệt khá nhiều.

Vì vậy, hãy thay đổi mã và đặt temperature thành 0, như sau:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Khi chạy đoạn mã này, bạn sẽ có hai hình ảnh sau:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.vi.png)
- ![Temperature 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.vi.png)

Ở đây bạn có thể thấy rõ hình ảnh giống nhau hơn nhiều.

## Cách định nghĩa giới hạn cho ứng dụng của bạn với metaprompts

Với bản demo, chúng ta đã có thể tạo hình ảnh cho khách hàng. Tuy nhiên, chúng ta cần tạo ra một số giới hạn cho ứng dụng.

Ví dụ, chúng ta không muốn tạo hình ảnh không phù hợp với môi trường làm việc, hoặc không phù hợp với trẻ em.

Chúng ta có thể làm điều này với _metaprompts_. Metaprompts là các prompt văn bản dùng để kiểm soát kết quả của mô hình Generative AI. Ví dụ, chúng ta có thể dùng metaprompts để kiểm soát kết quả, đảm bảo hình ảnh tạo ra an toàn cho môi trường làm việc hoặc phù hợp với trẻ em.

### Cách hoạt động?

Vậy metaprompts hoạt động như thế nào?

Metaprompts là các prompt văn bản được đặt trước prompt chính, dùng để kiểm soát kết quả của mô hình và được nhúng trong ứng dụng để kiểm soát đầu ra. Chúng bao bọc cả prompt đầu vào và metaprompt trong một prompt duy nhất.

Một ví dụ về metaprompt như sau:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Bây giờ, hãy xem cách chúng ta có thể dùng metaprompts trong bản demo.

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

Từ prompt trên, bạn có thể thấy tất cả hình ảnh được tạo ra đều tuân theo metaprompt.

## Bài tập - kích hoạt cho học sinh

Chúng ta đã giới thiệu Edu4All từ đầu bài học. Giờ là lúc để học sinh có thể tạo hình ảnh cho bài tập của mình.

Học sinh sẽ tạo hình ảnh cho bài tập về các công trình kiến trúc, cụ thể công trình nào do học sinh quyết định. Học sinh được khuyến khích sử dụng sự sáng tạo để đặt các công trình này vào những bối cảnh khác nhau.

## Giải pháp

Dưới đây là một giải pháp có thể:

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

prompt = f"""{meta_prompt}
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

## Làm tốt lắm! Tiếp tục học tập

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) để tiếp tục nâng cao kiến thức về Generative AI!

Hãy đến với Bài học 10, nơi chúng ta sẽ tìm hiểu cách [xây dựng ứng dụng AI với low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.