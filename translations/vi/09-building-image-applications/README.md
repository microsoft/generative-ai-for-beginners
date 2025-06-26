<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-06-25T17:27:35+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "vi"
}
-->
# Xây dựng Ứng dụng Tạo Hình ảnh

Có nhiều thứ hơn LLMs ngoài việc tạo văn bản. Cũng có thể tạo hình ảnh từ mô tả văn bản. Có hình ảnh như một phương thức có thể rất hữu ích trong nhiều lĩnh vực từ MedTech, kiến trúc, du lịch, phát triển game và nhiều hơn nữa. Trong chương này, chúng ta sẽ xem xét hai mô hình tạo hình ảnh phổ biến nhất, DALL-E và Midjourney.

## Giới thiệu

Trong bài học này, chúng ta sẽ đề cập đến:

- Tạo hình ảnh và lý do tại sao nó hữu ích.
- DALL-E và Midjourney, chúng là gì và cách chúng hoạt động.
- Cách bạn sẽ xây dựng một ứng dụng tạo hình ảnh.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Xây dựng một ứng dụng tạo hình ảnh.
- Định nghĩa ranh giới cho ứng dụng của bạn với meta prompts.
- Làm việc với DALL-E và Midjourney.

## Tại sao xây dựng một ứng dụng tạo hình ảnh?

Ứng dụng tạo hình ảnh là một cách tuyệt vời để khám phá khả năng của AI Tạo sinh. Chúng có thể được sử dụng cho, ví dụ:

- **Chỉnh sửa và tổng hợp hình ảnh**. Bạn có thể tạo hình ảnh cho nhiều trường hợp sử dụng khác nhau, chẳng hạn như chỉnh sửa hình ảnh và tổng hợp hình ảnh.

- **Áp dụng cho nhiều ngành công nghiệp**. Chúng cũng có thể được sử dụng để tạo hình ảnh cho nhiều ngành công nghiệp như Medtech, Du lịch, Phát triển game và nhiều hơn nữa.

## Tình huống: Edu4All

Là một phần của bài học này, chúng ta sẽ tiếp tục làm việc với startup của mình, Edu4All, trong bài học này. Học sinh sẽ tạo hình ảnh cho bài đánh giá của họ, chính xác những hình ảnh nào là tùy thuộc vào học sinh, nhưng chúng có thể là minh họa cho câu chuyện cổ tích của riêng họ hoặc tạo một nhân vật mới cho câu chuyện của họ hoặc giúp họ hình dung ý tưởng và khái niệm của mình.

Đây là những gì học sinh của Edu4All có thể tạo ra ví dụ nếu họ đang làm việc trong lớp về các di tích:

sử dụng một prompt như

> "Chó bên cạnh tháp Eiffel trong ánh nắng sáng sớm"

## DALL-E và Midjourney là gì?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) và [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) là hai trong số các mô hình tạo hình ảnh phổ biến nhất, chúng cho phép bạn sử dụng prompts để tạo hình ảnh.

### DALL-E

Hãy bắt đầu với DALL-E, là một mô hình AI Tạo sinh tạo ra hình ảnh từ mô tả văn bản.

- **CLIP**, là một mô hình tạo ra embeddings, là các biểu diễn số của dữ liệu, từ hình ảnh và văn bản.

- **Diffused attention**, là một mô hình tạo ra hình ảnh từ embeddings. DALL-E được huấn luyện trên một tập dữ liệu hình ảnh và văn bản và có thể được sử dụng để tạo hình ảnh từ mô tả văn bản. Ví dụ, DALL-E có thể được sử dụng để tạo ra hình ảnh của một con mèo đội mũ, hoặc một con chó có kiểu tóc mohawk.

### Midjourney

Midjourney hoạt động tương tự như DALL-E, nó tạo ra hình ảnh từ các prompt văn bản. Midjourney, cũng có thể được sử dụng để tạo hình ảnh bằng các prompt như “một con mèo đội mũ”, hoặc “một con chó có kiểu tóc mohawk”.

_Image cred Wikipedia, hình ảnh được tạo bởi Midjourney_

## DALL-E và Midjourney hoạt động như thế nào

Đầu tiên, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E là một mô hình AI Tạo sinh dựa trên kiến trúc transformer với một _transformer autoregressive_.

Một _transformer autoregressive_ định nghĩa cách một mô hình tạo ra hình ảnh từ mô tả văn bản, nó tạo ra từng pixel một, và sau đó sử dụng các pixel đã tạo để tạo ra pixel tiếp theo. Qua nhiều lớp trong một mạng nơ-ron, cho đến khi hình ảnh hoàn thành.

Với quy trình này, DALL-E, kiểm soát các thuộc tính, đối tượng, đặc điểm, và nhiều hơn nữa trong hình ảnh mà nó tạo ra. Tuy nhiên, DALL-E 2 và 3 có nhiều kiểm soát hơn đối với hình ảnh được tạo ra.

## Xây dựng ứng dụng tạo hình ảnh đầu tiên của bạn

Vậy để xây dựng một ứng dụng tạo hình ảnh cần những gì? Bạn cần các thư viện sau:

- **python-dotenv**, bạn được khuyến nghị sử dụng thư viện này để giữ bí mật của bạn trong một tệp _.env_ tránh xa mã nguồn.
- **openai**, thư viện này là thứ bạn sẽ sử dụng để tương tác với OpenAI API.
- **pillow**, để làm việc với hình ảnh trong Python.
- **requests**, để giúp bạn thực hiện các yêu cầu HTTP.

1. Tạo một tệp _.env_ với nội dung sau:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Tìm thông tin này trong Azure Portal cho tài nguyên của bạn trong phần "Keys and Endpoint".

1. Thu thập các thư viện trên vào một tệp gọi là _requirements.txt_ như sau:

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

   Đối với Windows, sử dụng các lệnh sau để tạo và kích hoạt môi trường ảo của bạn:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Thêm mã sau vào tệp gọi là _app.py_:

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

Hãy giải thích mã này:

- Đầu tiên, chúng ta nhập các thư viện cần thiết, bao gồm thư viện OpenAI, thư viện dotenv, thư viện requests, và thư viện Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Tiếp theo, chúng ta tải các biến môi trường từ tệp _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Sau đó, chúng ta đặt endpoint, key cho OpenAI API, version và type.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Tiếp theo, chúng ta tạo hình ảnh:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Mã trên phản hồi bằng một đối tượng JSON chứa URL của hình ảnh được tạo. Chúng ta có thể sử dụng URL để tải xuống hình ảnh và lưu vào tệp.

- Cuối cùng, chúng ta mở hình ảnh và sử dụng trình xem hình ảnh tiêu chuẩn để hiển thị nó:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Chi tiết hơn về việc tạo hình ảnh

Hãy xem xét mã tạo hình ảnh chi tiết hơn:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, là prompt văn bản được sử dụng để tạo hình ảnh. Trong trường hợp này, chúng ta đang sử dụng prompt "Thỏ trên ngựa, cầm kẹo mút, trên đồng cỏ sương mù nơi trồng hoa thủy tiên".
- **size**, là kích thước của hình ảnh được tạo ra. Trong trường hợp này, chúng ta đang tạo ra một hình ảnh có kích thước 1024x1024 pixel.
- **n**, là số lượng hình ảnh được tạo ra. Trong trường hợp này, chúng ta đang tạo ra hai hình ảnh.
- **temperature**, là một tham số kiểm soát tính ngẫu nhiên của đầu ra của một mô hình AI Tạo sinh. Nhiệt độ là một giá trị giữa 0 và 1, nơi 0 có nghĩa là đầu ra là xác định và 1 có nghĩa là đầu ra là ngẫu nhiên. Giá trị mặc định là 0.7.

Có nhiều điều bạn có thể làm với hình ảnh mà chúng ta sẽ đề cập trong phần tiếp theo.

## Khả năng bổ sung của việc tạo hình ảnh

Bạn đã thấy cho đến nay cách chúng ta có thể tạo ra một hình ảnh bằng vài dòng mã trong Python. Tuy nhiên, có nhiều điều bạn có thể làm với hình ảnh.

Bạn cũng có thể làm như sau:

- **Thực hiện chỉnh sửa**. Bằng cách cung cấp một hình ảnh hiện có một mặt nạ và một prompt, bạn có thể thay đổi một hình ảnh. Ví dụ, bạn có thể thêm một cái gì đó vào một phần của hình ảnh. Hãy tưởng tượng hình ảnh thỏ của chúng ta, bạn có thể thêm một chiếc mũ cho thỏ. Cách bạn sẽ làm điều đó là bằng cách cung cấp hình ảnh, một mặt nạ (xác định phần của khu vực để thay đổi) và một prompt văn bản để nói những gì cần làm.

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

  Hình ảnh cơ bản chỉ chứa con thỏ nhưng hình ảnh cuối cùng sẽ có chiếc mũ trên con thỏ.

- **Tạo biến thể**. Ý tưởng là bạn lấy một hình ảnh hiện có và yêu cầu tạo ra các biến thể. Để tạo ra một biến thể, bạn cung cấp một hình ảnh và một prompt văn bản và mã như sau:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Lưu ý, điều này chỉ được hỗ trợ trên OpenAI

## Nhiệt độ

Nhiệt độ là một tham số kiểm soát tính ngẫu nhiên của đầu ra của một mô hình AI Tạo sinh. Nhiệt độ là một giá trị giữa 0 và 1, nơi 0 có nghĩa là đầu ra là xác định và 1 có nghĩa là đầu ra là ngẫu nhiên. Giá trị mặc định là 0.7.

Hãy xem xét một ví dụ về cách nhiệt độ hoạt động, bằng cách chạy prompt này hai lần:

> Prompt: "Thỏ trên ngựa, cầm kẹo mút, trên đồng cỏ sương mù nơi trồng hoa thủy tiên"

Bây giờ hãy chạy lại prompt đó chỉ để thấy rằng chúng ta sẽ không nhận được cùng một hình ảnh hai lần:

Như bạn có thể thấy, các hình ảnh tương tự, nhưng không giống nhau. Hãy thử thay đổi giá trị nhiệt độ thành 0.1 và xem điều gì xảy ra:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Thay đổi nhiệt độ

Vì vậy, hãy thử làm cho phản hồi xác định hơn. Chúng ta có thể quan sát từ hai hình ảnh mà chúng ta đã tạo ra rằng trong hình ảnh đầu tiên, có một con thỏ và trong hình ảnh thứ hai, có một con ngựa, vì vậy các hình ảnh thay đổi rất nhiều.

Vì vậy, hãy thay đổi mã của chúng ta và đặt nhiệt độ thành 0, như sau:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Bây giờ khi bạn chạy mã này, bạn sẽ nhận được hai hình ảnh này:

Ở đây bạn có thể rõ ràng thấy cách các hình ảnh giống nhau hơn.

## Cách định nghĩa ranh giới cho ứng dụng của bạn với metaprompts

Với demo của chúng ta, chúng ta đã có thể tạo ra hình ảnh cho khách hàng của mình. Tuy nhiên, chúng ta cần tạo ra một số ranh giới cho ứng dụng của mình.

Ví dụ, chúng ta không muốn tạo ra hình ảnh không an toàn cho công việc, hoặc không phù hợp cho trẻ em.

Chúng ta có thể làm điều này với _metaprompts_. Metaprompts là các prompt văn bản được sử dụng để kiểm soát đầu ra của một mô hình AI Tạo sinh. Ví dụ, chúng ta có thể sử dụng metaprompts để kiểm soát đầu ra, và đảm bảo rằng các hình ảnh được tạo ra là an toàn cho công việc, hoặc phù hợp cho trẻ em.

### Nó hoạt động như thế nào?

Bây giờ, metaprompts hoạt động như thế nào?

Metaprompts là các prompt văn bản được sử dụng để kiểm soát đầu ra của một mô hình AI Tạo sinh, chúng được đặt trước prompt văn bản, và được sử dụng để kiểm soát đầu ra của mô hình và được nhúng trong các ứng dụng để kiểm soát đầu ra của mô hình. Đóng gói đầu vào prompt và đầu vào metaprompt trong một prompt văn bản duy nhất.

Một ví dụ về metaprompt sẽ là như sau:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Bây giờ, hãy xem cách chúng ta có thể sử dụng metaprompts trong demo của mình.

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

Từ prompt trên, bạn có thể thấy cách tất cả các hình ảnh được tạo ra xem xét metaprompt.

## Bài tập - hãy cho phép học sinh

Chúng ta đã giới thiệu Edu4All ở đầu bài học này. Bây giờ là lúc cho phép học sinh tạo ra hình ảnh cho bài đánh giá của họ.

Học sinh sẽ tạo ra hình ảnh cho bài đánh giá của họ chứa các di tích, chính xác những di tích nào là tùy thuộc vào học sinh. Học sinh được yêu cầu sử dụng sự sáng tạo của mình trong nhiệm vụ này để đặt các di tích này trong các ngữ cảnh khác nhau.

## Giải pháp

Đây là một giải pháp khả thi:

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

## Làm tốt lắm! Tiếp tục học tập của bạn

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Học AI Tạo sinh](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức về AI Tạo sinh của bạn!

Hãy đến với Bài học 10, nơi chúng ta sẽ xem cách [xây dựng ứng dụng AI với mã thấp](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sự không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin có thẩm quyền. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.