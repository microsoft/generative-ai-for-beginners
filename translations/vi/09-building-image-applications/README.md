<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "238cde5c90363d70ecc939569378da51",
  "translation_date": "2025-10-17T20:36:03+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "vi"
}
-->
# Xây dựng ứng dụng tạo hình ảnh

[![Xây dựng ứng dụng tạo hình ảnh](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.vi.png)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLMs không chỉ dừng lại ở việc tạo văn bản. Chúng cũng có thể tạo hình ảnh từ các mô tả văn bản. Việc sử dụng hình ảnh như một phương thức có thể rất hữu ích trong nhiều lĩnh vực như công nghệ y tế, kiến trúc, du lịch, phát triển trò chơi và nhiều lĩnh vực khác. Trong chương này, chúng ta sẽ tìm hiểu về hai mô hình tạo hình ảnh phổ biến nhất, DALL-E và Midjourney.

## Giới thiệu

Trong bài học này, chúng ta sẽ đề cập đến:

- Tạo hình ảnh và lý do tại sao nó hữu ích.
- DALL-E và Midjourney, chúng là gì và cách chúng hoạt động.
- Cách bạn xây dựng một ứng dụng tạo hình ảnh.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Xây dựng một ứng dụng tạo hình ảnh.
- Đặt giới hạn cho ứng dụng của bạn bằng các meta prompt.
- Làm việc với DALL-E và Midjourney.

## Tại sao xây dựng ứng dụng tạo hình ảnh?

Ứng dụng tạo hình ảnh là một cách tuyệt vời để khám phá khả năng của Generative AI. Chúng có thể được sử dụng cho, ví dụ:

- **Chỉnh sửa và tổng hợp hình ảnh**. Bạn có thể tạo hình ảnh cho nhiều trường hợp sử dụng, chẳng hạn như chỉnh sửa hình ảnh và tổng hợp hình ảnh.

- **Áp dụng cho nhiều ngành công nghiệp**. Chúng cũng có thể được sử dụng để tạo hình ảnh cho nhiều ngành công nghiệp như công nghệ y tế, du lịch, phát triển trò chơi và nhiều hơn nữa.

## Kịch bản: Edu4All

Trong bài học này, chúng ta sẽ tiếp tục làm việc với startup của chúng ta, Edu4All. Các học sinh sẽ tạo hình ảnh cho các bài đánh giá của họ, chính xác hình ảnh nào là tùy thuộc vào học sinh, nhưng chúng có thể là minh họa cho câu chuyện cổ tích của riêng họ hoặc tạo một nhân vật mới cho câu chuyện của họ hoặc giúp họ hình dung ý tưởng và khái niệm của mình.

Đây là những gì học sinh của Edu4All có thể tạo ra, ví dụ, nếu họ đang học về các công trình kiến trúc:

![Startup Edu4All, lớp học về các công trình kiến trúc, Tháp Eiffel](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.vi.png)

sử dụng một prompt như

> "Chó bên cạnh Tháp Eiffel trong ánh sáng mặt trời buổi sáng sớm"

## DALL-E và Midjourney là gì?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) và [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) là hai trong số các mô hình tạo hình ảnh phổ biến nhất, cho phép bạn sử dụng các prompt để tạo hình ảnh.

### DALL-E

Hãy bắt đầu với DALL-E, một mô hình Generative AI tạo hình ảnh từ các mô tả văn bản.

> [DALL-E là sự kết hợp của hai mô hình, CLIP và diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, là một mô hình tạo ra các embeddings, tức là các biểu diễn số của dữ liệu, từ hình ảnh và văn bản.

- **Diffused attention**, là một mô hình tạo hình ảnh từ embeddings. DALL-E được huấn luyện trên một tập dữ liệu gồm hình ảnh và văn bản và có thể được sử dụng để tạo hình ảnh từ các mô tả văn bản. Ví dụ, DALL-E có thể được sử dụng để tạo hình ảnh của một con mèo đội mũ, hoặc một con chó với kiểu tóc mohawk.

### Midjourney

Midjourney hoạt động tương tự như DALL-E, nó tạo hình ảnh từ các prompt văn bản. Midjourney cũng có thể được sử dụng để tạo hình ảnh bằng các prompt như “một con mèo đội mũ”, hoặc “một con chó với kiểu tóc mohawk”.

![Hình ảnh được tạo bởi Midjourney, chim bồ câu cơ khí](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Hình ảnh từ Wikipedia, hình ảnh được tạo bởi Midjourney_

## DALL-E và Midjourney hoạt động như thế nào

Đầu tiên, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E là một mô hình Generative AI dựa trên kiến trúc transformer với một _autoregressive transformer_.

Một _autoregressive transformer_ định nghĩa cách một mô hình tạo hình ảnh từ các mô tả văn bản, nó tạo từng pixel một, sau đó sử dụng các pixel đã tạo để tạo pixel tiếp theo. Quá trình này đi qua nhiều lớp trong mạng neural, cho đến khi hình ảnh hoàn chỉnh.

Với quy trình này, DALL-E kiểm soát các thuộc tính, đối tượng, đặc điểm và nhiều yếu tố khác trong hình ảnh mà nó tạo ra. Tuy nhiên, DALL-E 2 và 3 có khả năng kiểm soát hình ảnh được tạo ra tốt hơn.

## Xây dựng ứng dụng tạo hình ảnh đầu tiên của bạn

Vậy cần gì để xây dựng một ứng dụng tạo hình ảnh? Bạn cần các thư viện sau:

- **python-dotenv**, bạn được khuyến nghị sử dụng thư viện này để giữ các thông tin bí mật trong tệp _.env_ tách biệt khỏi mã nguồn.
- **openai**, thư viện này sẽ được sử dụng để tương tác với API của OpenAI.
- **pillow**, để làm việc với hình ảnh trong Python.
- **requests**, để giúp bạn thực hiện các yêu cầu HTTP.

## Tạo và triển khai mô hình Azure OpenAI

Nếu chưa thực hiện, hãy làm theo hướng dẫn trên trang [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) để tạo tài nguyên và mô hình Azure OpenAI. Chọn DALL-E 3 làm mô hình.

## Tạo ứng dụng

1. Tạo một tệp _.env_ với nội dung sau:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Tìm thông tin này trong Azure OpenAI Foundry Portal cho tài nguyên của bạn trong phần "Deployments".

1. Thu thập các thư viện trên vào một tệp có tên _requirements.txt_ như sau:

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

   Đối với Windows, sử dụng các lệnh sau để tạo và kích hoạt môi trường ảo:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Thêm mã sau vào tệp có tên _app.py_:

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

Giải thích mã này:

- Đầu tiên, chúng ta nhập các thư viện cần thiết, bao gồm thư viện OpenAI, thư viện dotenv, thư viện requests và thư viện Pillow.

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

- Sau đó, chúng ta cấu hình client dịch vụ Azure OpenAI.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Tiếp theo, chúng ta tạo hình ảnh:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Mã trên trả về một đối tượng JSON chứa URL của hình ảnh được tạo. Chúng ta có thể sử dụng URL để tải hình ảnh và lưu vào tệp.

- Cuối cùng, chúng ta mở hình ảnh và sử dụng trình xem hình ảnh tiêu chuẩn để hiển thị nó:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Chi tiết hơn về việc tạo hình ảnh

Hãy xem mã tạo hình ảnh chi tiết hơn:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, là prompt văn bản được sử dụng để tạo hình ảnh. Trong trường hợp này, chúng ta sử dụng prompt "Thỏ trên lưng ngựa, cầm kẹo mút, trên đồng cỏ sương mù nơi mọc hoa thủy tiên".
- **size**, là kích thước của hình ảnh được tạo. Trong trường hợp này, chúng ta tạo hình ảnh có kích thước 1024x1024 pixel.
- **n**, là số lượng hình ảnh được tạo. Trong trường hợp này, chúng ta tạo hai hình ảnh.
- **temperature**, là tham số kiểm soát tính ngẫu nhiên của đầu ra của mô hình Generative AI. Giá trị của temperature nằm trong khoảng từ 0 đến 1, trong đó 0 nghĩa là đầu ra mang tính xác định và 1 nghĩa là đầu ra ngẫu nhiên. Giá trị mặc định là 0.7.

Có nhiều điều bạn có thể làm với hình ảnh mà chúng ta sẽ đề cập trong phần tiếp theo.

## Các khả năng bổ sung của việc tạo hình ảnh

Bạn đã thấy cách chúng ta có thể tạo hình ảnh chỉ với vài dòng mã trong Python. Tuy nhiên, còn nhiều điều bạn có thể làm với hình ảnh.

Bạn cũng có thể làm những điều sau:

- **Thực hiện chỉnh sửa**. Bằng cách cung cấp một hình ảnh hiện có, một mặt nạ và một prompt, bạn có thể thay đổi hình ảnh. Ví dụ, bạn có thể thêm một thứ gì đó vào một phần của hình ảnh. Hãy tưởng tượng hình ảnh con thỏ của chúng ta, bạn có thể thêm một chiếc mũ cho con thỏ. Cách bạn làm điều đó là cung cấp hình ảnh, một mặt nạ (xác định phần khu vực cần thay đổi) và một prompt văn bản để nói điều gì cần được thực hiện. 
> Lưu ý: điều này không được hỗ trợ trong DALL-E 3.

Dưới đây là một ví dụ sử dụng GPT Image:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  Hình ảnh gốc chỉ chứa ghế dài với hồ bơi nhưng hình ảnh cuối cùng sẽ có một con chim hồng hạc:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.vi.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.vi.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.vi.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **Tạo các biến thể**. Ý tưởng là bạn lấy một hình ảnh hiện có và yêu cầu tạo các biến thể. Để tạo một biến thể, bạn cung cấp một hình ảnh và một prompt văn bản và mã như sau:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Lưu ý, điều này chỉ được hỗ trợ trên OpenAI.

## Temperature

Temperature là một tham số kiểm soát tính ngẫu nhiên của đầu ra của mô hình Generative AI. Giá trị của temperature nằm trong khoảng từ 0 đến 1, trong đó 0 nghĩa là đầu ra mang tính xác định và 1 nghĩa là đầu ra ngẫu nhiên. Giá trị mặc định là 0.7.

Hãy xem một ví dụ về cách temperature hoạt động, bằng cách chạy prompt này hai lần:

> Prompt: "Thỏ trên lưng ngựa, cầm kẹo mút, trên đồng cỏ sương mù nơi mọc hoa thủy tiên"

![Thỏ trên lưng ngựa cầm kẹo mút, phiên bản 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.vi.png)

Bây giờ hãy chạy lại prompt đó để xem rằng chúng ta sẽ không nhận được cùng một hình ảnh hai lần:

![Hình ảnh được tạo của thỏ trên lưng ngựa](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.vi.png)

Như bạn thấy, các hình ảnh tương tự nhau, nhưng không giống hệt. Hãy thử thay đổi giá trị temperature thành 0.1 và xem điều gì xảy ra:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Thay đổi temperature

Vậy hãy thử làm cho đầu ra mang tính xác định hơn. Chúng ta có thể quan sát từ hai hình ảnh đã tạo rằng trong hình ảnh đầu tiên, có một con thỏ và trong hình ảnh thứ hai, có một con ngựa, vì vậy các hình ảnh khác nhau rất nhiều.

Do đó, hãy thay đổi mã của chúng ta và đặt temperature thành 0, như sau:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Bây giờ khi bạn chạy mã này, bạn sẽ nhận được hai hình ảnh sau:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.vi.png)
- ![Temperature 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.vi.png)

Ở đây bạn có thể thấy rõ cách các hình ảnh giống nhau hơn.

## Cách đặt giới hạn cho ứng dụng của bạn với metaprompts

Với demo của chúng ta, chúng ta đã có thể tạo hình ảnh cho khách hàng của mình. Tuy nhiên, chúng ta cần tạo một số giới hạn cho ứng dụng của mình.

Ví dụ, chúng ta không muốn tạo hình ảnh không phù hợp với công việc, hoặc không phù hợp với trẻ em.

Chúng ta có thể làm điều này với _metaprompts_. Metaprompts là các prompt văn bản được sử dụng để kiểm soát đầu ra của mô hình Generative AI. Ví dụ, chúng ta có thể sử dụng metaprompts để kiểm soát đầu ra, và đảm bảo rằng các hình ảnh được tạo ra phù hợp với công việc, hoặc phù hợp với trẻ em.

### Nó hoạt động như thế nào?

Vậy, metaprompts hoạt động như thế nào?

Metaprompts là các prompt văn bản được sử dụng để kiểm soát đầu ra của mô hình Generative AI, chúng được đặt trước prompt văn bản, và được sử dụng để kiểm soát đầu ra của mô hình và được nhúng trong các ứng dụng để kiểm soát đầu ra của mô hình. Gói gọn đầu vào của prompt và đầu vào của metaprompt trong một prompt văn bản duy nhất.

Một ví dụ về metaprompt sẽ là:

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

Từ prompt trên, bạn có thể thấy cách tất cả các hình ảnh được tạo ra đều xem xét metaprompt.

## Bài tập - hãy hỗ trợ học sinh

Chúng ta đã giới thiệu Edu4All ở đầu bài học này. Bây giờ là lúc hỗ trợ các học sinh tạo hình ảnh cho các bài đánh giá của họ.

Các học sinh sẽ tạo hình ảnh cho các bài đánh giá của họ chứa các công trình kiến trúc, chính xác công trình nào là tùy thuộc vào học sinh. Các học sinh được yêu cầu sử dụng sự sáng tạo của mình trong nhiệm vụ này để đặt các công trình kiến trúc này trong các bối cảnh khác nhau.

## Giải pháp

Dưới đây là một giải pháp khả thi:
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

## Làm tốt lắm! Tiếp tục học hỏi

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Học về AI Tạo sinh](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) để tiếp tục nâng cao kiến thức về AI Tạo sinh của bạn!

Hãy chuyển sang Bài học 10, nơi chúng ta sẽ tìm hiểu cách [xây dựng ứng dụng AI với mã thấp](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.