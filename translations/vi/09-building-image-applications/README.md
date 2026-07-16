# Xây dựng ứng dụng tạo hình ảnh

[![Xây dựng ứng dụng tạo hình ảnh](../../../translated_images/vi/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLM không chỉ tạo ra văn bản. Nó cũng có thể tạo ra hình ảnh từ mô tả văn bản. Có hình ảnh như một phương thức có thể rất hữu ích trong nhiều lĩnh vực từ công nghệ y tế, kiến trúc, du lịch, phát triển trò chơi và nhiều hơn nữa. Trong chương này, chúng ta sẽ tìm hiểu hai mô hình tạo hình ảnh phổ biến nhất, DALL-E và Midjourney.

## Giới thiệu

Trong bài học này, chúng ta sẽ đề cập đến:

- Tạo hình ảnh và lý do tại sao nó hữu ích.
- DALL-E và Midjourney là gì và cách chúng hoạt động.
- Cách bạn xây dựng một ứng dụng tạo hình ảnh.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Xây dựng một ứng dụng tạo hình ảnh.
- Định nghĩa giới hạn cho ứng dụng của bạn với các meta prompt.
- Làm việc với DALL-E và Midjourney.

## Tại sao nên xây dựng ứng dụng tạo hình ảnh?

Ứng dụng tạo hình ảnh là một cách tuyệt vời để khám phá khả năng của AI tạo sinh. Chúng có thể được dùng cho ví dụ như:

- **Chỉnh sửa và tổng hợp hình ảnh**. Bạn có thể tạo hình ảnh cho nhiều mục đích khác nhau, như chỉnh sửa hình ảnh và tổng hợp hình ảnh.

- **Áp dụng cho nhiều ngành công nghiệp**. Chúng cũng có thể được dùng để tạo hình ảnh cho nhiều ngành như công nghệ y tế, du lịch, phát triển trò chơi và hơn thế nữa.

## Tình huống: Edu4All

Trong bài học này, chúng ta sẽ tiếp tục làm việc với startup của chúng ta, Edu4All. Học sinh sẽ tạo hình ảnh cho các bài kiểm tra của họ, hình ảnh là gì tùy theo học sinh, nhưng có thể là minh họa cho câu chuyện cổ tích của họ, tạo nhân vật mới cho câu chuyện hoặc giúp họ hình dung ý tưởng và khái niệm của mình.

Đây là những gì học sinh Edu4All có thể tạo ví dụ nếu họ làm việc trong lớp về các tượng đài:

![Startup Edu4All, lớp học về các tượng đài, tháp Eiffel](../../../translated_images/vi/startup.94d6b79cc4bb3f5a.webp)

dùng một prompt như

> "Chó bên cạnh tháp Eiffel dưới ánh nắng buổi sáng sớm"

## DALL-E và Midjourney là gì?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) và [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) là hai trong số các mô hình tạo hình ảnh phổ biến nhất, cho phép bạn dùng prompt để tạo hình ảnh.

### DALL-E

Chúng ta bắt đầu với DALL-E, một mô hình AI tạo sinh tạo hình ảnh từ mô tả văn bản.

> [DALL-E là sự kết hợp của hai mô hình, CLIP và diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, là một mô hình tạo embedding, là biểu diễn số học của dữ liệu, từ hình ảnh và văn bản.

- **Diffused attention**, là mô hình tạo hình ảnh từ embedding. DALL-E được huấn luyện trên bộ dữ liệu hình ảnh và văn bản và có thể dùng để tạo hình ảnh từ mô tả văn bản. Ví dụ, DALL-E có thể tạo hình ảnh một con mèo đội mũ hoặc một con chó kiểu mohawk.

### Midjourney

Midjourney hoạt động tương tự DALL-E, tạo hình ảnh dựa trên prompt văn bản. Midjourney cũng có thể tạo hình ảnh dùng các prompt như “một con mèo đội mũ”, hoặc “con chó kiểu mohawk”.

![Hình ảnh do Midjourney tạo, chim bồ câu cơ khí](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Ảnh từ Wikipedia, hình ảnh tạo bởi Midjourney_

## DALL-E và Midjourney hoạt động thế nào

Đầu tiên, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E là mô hình AI tạo sinh dựa trên kiến trúc transformer với _autoregressive transformer_.

_Autoregressive transformer_ xác định cách mô hình tạo hình ảnh dựa trên mô tả văn bản, tạo từng điểm ảnh một, rồi dùng điểm ảnh đã tạo để tạo điểm ảnh kế tiếp. Đi qua nhiều lớp trong mạng neural, cho tới khi hoàn thành hình ảnh.

Với quá trình này, DALL-E kiểm soát thuộc tính, đối tượng, đặc điểm, và hơn thế nữa trong hình ảnh nó tạo. Tuy nhiên, DALL-E 2 và 3 kiểm soát hình ảnh tạo ra tốt hơn.

## Xây dựng ứng dụng tạo hình ảnh đầu tiên của bạn

Vậy để xây dựng ứng dụng tạo hình ảnh cần gì? Bạn cần các thư viện sau:

- **python-dotenv**, bạn nên dùng thư viện này để giữ bí mật trong file _.env_ tách biệt với code.
- **openai**, thư viện này dùng để tương tác với API của OpenAI.
- **pillow**, để làm việc với hình ảnh trong Python.
- **requests**, giúp bạn gửi yêu cầu HTTP.

## Tạo và triển khai mô hình Azure OpenAI

Nếu chưa làm, làm theo hướng dẫn trên trang [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)
để tạo tài nguyên và mô hình Azure OpenAI. Chọn **gpt-image-1** làm mô hình (mô hình tạo hình ảnh Azure OpenAI hiện tại; DALL-E 3 là phiên bản cũ không còn cho triển khai mới).

## Tạo ứng dụng

1. Tạo file _.env_ với nội dung sau:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   Dò thông tin này trong Azure OpenAI Foundry Portal cho tài nguyên của bạn ở phần "Deployments".

1. Gom các thư viện trên trong file _requirements.txt_ như sau:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Tiếp theo, tạo môi trường ảo và cài thư viện:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Với Windows, dùng lệnh sau để tạo và kích hoạt môi trường ảo:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Thêm đoạn code sau vào file _app.py_:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # import dotenv
    dotenv.load_dotenv()
    
    # cấu hình client dịch vụ Azure OpenAI
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # Tạo ảnh bằng cách sử dụng API tạo ảnh
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Đặt thư mục cho ảnh được lưu trữ
        image_dir = os.path.join(os.curdir, 'images')

        # Nếu thư mục không tồn tại, tạo nó
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Khởi tạo đường dẫn ảnh (lưu ý định dạng tệp phải là png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Lấy ảnh đã tạo
        image_url = generation_response.data[0].url  # trích xuất URL ảnh từ phản hồi
        generated_image = requests.get(image_url).content  # tải ảnh về
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # Hiển thị ảnh trong trình xem ảnh mặc định
        image = Image.open(image_path)
        image.show()

    # bắt ngoại lệ
    except openai.BadRequestError as err:
        print(err)
   ```

Giải thích đoạn code này:

- Đầu tiên, chúng ta import các thư viện cần thiết, bao gồm thư viện OpenAI, dotenv, requests và Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Tiếp theo, chúng ta load biến môi trường từ file _.env_.

  ```python
  # nhập dotenv
  dotenv.load_dotenv()
  ```

- Sau đó, cấu hình client dịch vụ Azure OpenAI 

  ```python
  # Lấy điểm cuối và khóa từ biến môi trường
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- Tiếp theo, chúng ta tạo hình ảnh:

  ```python
  # Tạo một hình ảnh bằng cách sử dụng API tạo hình ảnh
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Đoạn code trên trả về một đối tượng JSON chứa URL hình ảnh được tạo. Chúng ta có thể dùng URL để tải hình ảnh về và lưu lại.

- Cuối cùng, chúng ta mở hình ảnh và dùng trình xem ảnh tiêu chuẩn để hiển thị:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Chi tiết hơn về việc tạo hình ảnh

Hãy xem kỹ đoạn code tạo hình ảnh:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, là prompt văn bản dùng để tạo hình ảnh. Ở đây, chúng ta dùng prompt "Thỏ cưỡi ngựa, cầm kẹo que, trên đồng hoa thủy tiên trong sương mù".
- **size**, là kích thước hình ảnh tạo ra. Ở đây, hình ảnh được tạo có kích thước 1024x1024 pixel.
- **n**, là số lượng hình ảnh được tạo. Ở đây, chúng ta tạo hai hình ảnh.
- **temperature**, là tham số điều khiển mức độ ngẫu nhiên của đầu ra của mô hình AI tạo sinh. Temperature là giá trị từ 0 đến 1, 0 nghĩa là đầu ra quyết định, 1 nghĩa là đầu ra hoàn toàn ngẫu nhiên. Giá trị mặc định là 0.7.

Còn nhiều điều bạn có thể làm với hình ảnh mà chúng ta sẽ đề cập trong phần tiếp theo.

## Các khả năng mở rộng của tạo hình ảnh

Bạn đã thấy chúng ta có thể tạo hình ảnh bằng vài dòng code Python. Tuy nhiên, còn nhiều điều có thể làm với hình ảnh.

Bạn cũng có thể làm các việc sau:

- **Thực hiện chỉnh sửa**. Bằng cách cung cấp hình ảnh hiện có, mặt nạ và prompt văn bản, bạn có thể chỉnh sửa hình ảnh. Ví dụ, có thể thêm một vật gì đó vào phần hình ảnh. Lấy ví dụ hình thỏ của chúng ta, có thể thêm một cái mũ cho thỏ. Cách làm là cung cấp hình ảnh, một mặt nạ (xác định vùng cần thay đổi) và prompt văn bản nói cần làm gì.
> Lưu ý: điều này không được hỗ trợ trong DALL-E 3.
 
Đây là ví dụ dùng GPT Image:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  Hình ảnh gốc chỉ có phòng chờ với hồ bơi nhưng hình ảnh cuối cùng có một con hồng hạc:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/vi/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/vi/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/vi/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Tạo biến thể**. Ý tưởng là bạn lấy một hình ảnh có sẵn và yêu cầu tạo các biến thể. Để tạo biến thể, bạn cung cấp hình ảnh và prompt văn bản, cùng code như sau:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > Lưu ý, điều này chỉ hỗ trợ trên mô hình DALL-E 2 của OpenAI, không hỗ trợ gpt-image-1

## Temperature

Temperature là tham số điều khiển mức độ ngẫu nhiên của đầu ra từ mô hình AI tạo sinh. Giá trị từ 0 đến 1, 0 nghĩa là đầu ra quyết định, 1 nghĩa đầu ra ngẫu nhiên. Giá trị mặc định là 0.7.

Hãy xem ví dụ cách temperature hoạt động bằng cách chạy prompt này hai lần:

> Prompt: "Thỏ cưỡi ngựa, cầm kẹo que, trên đồng hoa thủy tiên trong sương mù"

![Thỏ cưỡi ngựa cầm kẹo que, phiên bản 1](../../../translated_images/vi/v1-generated-image.a295cfcffa3c13c2.webp)

Bây giờ, chạy lại prompt này chỉ để thấy chúng ta sẽ không được hình ảnh giống hệt hai lần:

![Hình ảnh tạo ra thỏ cưỡi ngựa](../../../translated_images/vi/v2-generated-image.33f55a3714efe61d.webp)

Như bạn thấy, hình ảnh tương tự nhau, nhưng không giống hệt. Hãy thử đổi giá trị temperature xuống 0.1 xem chuyện gì xảy ra:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Nhập văn bản yêu cầu của bạn ở đây
        size='1024x1024',
        n=2
    )
```

### Đổi giá trị temperature

Vậy thử làm cho phản hồi quyết định hơn. Chúng ta có thể quan sát từ hai hình ảnh tạo ra, ở hình đầu có thỏ và ở hình thứ hai có ngựa, nên hình ảnh khác biệt khá nhiều.

Vì vậy, ta đổi đoạn code và đặt temperature là 0, như sau:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Nhập văn bản nhắc của bạn tại đây
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Khi chạy code này, bạn sẽ có hai hình ảnh sau:

- ![Temperature 0, phiên bản 1](../../../translated_images/vi/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![Temperature 0, phiên bản 2](../../../translated_images/vi/v2-temp-generated-image.871d0c920dbfb0f1.webp)

Ở đây bạn có thể dễ dàng thấy hình ảnh giống nhau hơn nhiều.

## Cách định nghĩa giới hạn cho ứng dụng với metaprompts

Với bản demo của chúng ta, đã có thể tạo hình ảnh cho khách hàng. Tuy nhiên, cần tạo giới hạn cho ứng dụng.

Ví dụ, ta không muốn tạo hình ảnh không an toàn cho nơi làm việc, hoặc không phù hợp với trẻ em.

Ta có thể làm điều này bằng _metaprompts_. Metaprompts là prompt văn bản dùng để kiểm soát đầu ra của mô hình AI tạo sinh. Ví dụ, ta dùng metaprompts để kiểm soát đầu ra, đảm bảo hình ảnh tạo ra an toàn cho nơi làm việc hoặc phù hợp cho trẻ em.

### Cách nó hoạt động?

Vậy metaprompts hoạt động thế nào?

Metaprompts là prompt văn bản dùng để điều khiển đầu ra của mô hình AI tạo sinh, đặt trước prompt văn bản chính, và dùng để kiểm soát đầu ra mô hình, được tích hợp trong ứng dụng để kiểm soát đầu ra mô hình. Gói gọn input prompt và meta prompt thành một prompt văn bản duy nhất.

Một ví dụ của metaprompt như sau:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Bây giờ, hãy xem cách ta dùng metaprompt trong demo.

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

# TODO thêm yêu cầu tạo hình ảnh
```

Từ prompt trên, bạn thấy tất cả hình ảnh tạo ra đều xem xét metaprompt.

## Bài tập - hãy kích hoạt cho học sinh

Chúng ta đã giới thiệu Edu4All từ đầu bài học. Giờ là lúc hỗ trợ học sinh tạo hình ảnh cho bài kiểm tra của họ.


Các sinh viên sẽ tạo hình ảnh cho bài đánh giá của họ chứa các tượng đài, chính xác những tượng đài nào là do các sinh viên quyết định. Các sinh viên được yêu cầu sử dụng sự sáng tạo của mình trong nhiệm vụ này để đặt các tượng đài này trong các bối cảnh khác nhau.

## Giải pháp

Đây là một giải pháp có thể:

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# import dotenv
dotenv.load_dotenv()

# Lấy endpoint và khóa từ biến môi trường
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
    # Tạo hình ảnh bằng cách sử dụng API tạo hình ảnh
    generation_response = client.images.generate(
        prompt=prompt,    # Nhập đoạn văn bản gợi ý của bạn ở đây
        size='1024x1024',
        n=1,
    )
    # Đặt thư mục cho hình ảnh được lưu trữ
    image_dir = os.path.join(os.curdir, 'images')

    # Nếu thư mục không tồn tại, tạo nó
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Khởi tạo đường dẫn hình ảnh (lưu ý định dạng tệp nên là png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Lấy hình ảnh được tạo ra
    image_url = generation_response.data[0].url  # trích xuất URL hình ảnh từ phản hồi
    generated_image = requests.get(image_url).content  # tải hình ảnh về
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Hiển thị hình ảnh trong trình xem hình ảnh mặc định
    image = Image.open(image_path)
    image.show()

# bắt ngoại lệ
except openai.BadRequestError as err:
    print(err)
```

## Làm tốt lắm! Tiếp tục học tập

Sau khi hoàn thành bài học này, hãy tham khảo [Bộ sưu tập Học tập AI Sinh tạo của chúng tôi](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) để tiếp tục nâng cao kiến thức về AI Sinh tạo!

Hãy chuyển sang Bài học 10, nơi chúng ta sẽ xem cách [xây dựng ứng dụng AI với mã thấp](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->