# Xây dựng các ứng dụng tạo văn bản

[![Xây dựng các ứng dụng tạo văn bản](../../../translated_images/vi/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Nhấp vào hình ảnh bên trên để xem video bài học này)_

Bạn đã thấy cho đến nay trong chương trình này rằng có các khái niệm cốt lõi như prompts và thậm chí một lĩnh vực hoàn chỉnh gọi là "kỹ thuật prompt". Nhiều công cụ mà bạn có thể tương tác như ChatGPT, Office 365, Microsoft Power Platform và nhiều hơn nữa, đều hỗ trợ bạn sử dụng prompt để hoàn thành một việc gì đó.

Để bạn thêm trải nghiệm như vậy vào một ứng dụng, bạn cần hiểu các khái niệm như prompt, completions và chọn một thư viện để làm việc cùng. Đó chính là những gì bạn sẽ học trong chương này.

## Giới thiệu

Trong chương này, bạn sẽ:

- Tìm hiểu về thư viện openai và các khái niệm cốt lõi của nó.
- Xây dựng một ứng dụng tạo văn bản sử dụng openai.
- Hiểu cách sử dụng các khái niệm như prompt, temperature và tokens để xây dựng một ứng dụng tạo văn bản.

## Mục tiêu học tập

Vào cuối bài học này, bạn sẽ có thể:

- Giải thích ứng dụng tạo văn bản là gì.
- Xây dựng một ứng dụng tạo văn bản sử dụng openai.
- Cấu hình ứng dụng của bạn để sử dụng nhiều hoặc ít tokens hơn và cũng thay đổi temperature, để có đầu ra đa dạng.

## Ứng dụng tạo văn bản là gì?

Thông thường khi bạn xây dựng một ứng dụng, nó có một giao diện nào đó như sau:

- Dựa trên lệnh. Ứng dụng console là những ứng dụng điển hình mà bạn gõ một lệnh và nó thực hiện một tác vụ. Ví dụ, `git` là một ứng dụng dựa trên lệnh.
- Giao diện người dùng (UI). Một số ứng dụng có giao diện người dùng đồ họa (GUI) nơi bạn nhấp vào các nút, nhập văn bản, chọn các tùy chọn và nhiều hơn nữa.

### Ứng dụng Console và UI có giới hạn

So sánh nó với ứng dụng dựa trên lệnh nơi bạn gõ một lệnh:

- **Có giới hạn**. Bạn không thể gõ bất kỳ lệnh nào, chỉ có những lệnh mà ứng dụng hỗ trợ.
- **Ngôn ngữ cụ thể**. Một số ứng dụng hỗ trợ nhiều ngôn ngữ, nhưng theo mặc định ứng dụng được xây dựng cho một ngôn ngữ cụ thể, ngay cả khi bạn có thể thêm hỗ trợ ngôn ngữ khác.

### Lợi ích của các ứng dụng tạo văn bản

Vậy ứng dụng tạo văn bản khác biệt thế nào?

Trong ứng dụng tạo văn bản, bạn có nhiều sự linh hoạt hơn, bạn không bị giới hạn trong một tập hợp các lệnh hay một ngôn ngữ đầu vào cụ thể. Thay vào đó, bạn có thể sử dụng ngôn ngữ tự nhiên để tương tác với ứng dụng. Một lợi ích khác là bạn đã đang tương tác với một nguồn dữ liệu được huấn luyện trên một kho tàng thông tin rộng lớn, trong khi một ứng dụng truyền thống có thể bị giới hạn trong những gì có trong cơ sở dữ liệu.

### Tôi có thể xây dựng gì với một ứng dụng tạo văn bản?

Có nhiều thứ bạn có thể xây dựng. Ví dụ:

- **Chatbot**. Một chatbot trả lời các câu hỏi về các chủ đề, như công ty bạn và sản phẩm của nó có thể là một lựa chọn tốt.
- **Trợ lý**. Các LLM rất tốt trong việc tóm tắt văn bản, lấy thông tin chi tiết từ văn bản, tạo ra văn bản như sơ yếu lý lịch và nhiều hơn nữa.
- **Trợ lý mã nguồn**. Tùy thuộc vào mô hình ngôn ngữ bạn sử dụng, bạn có thể xây dựng trợ lý mã nguồn giúp bạn viết code. Ví dụ, bạn có thể sử dụng một sản phẩm như GitHub Copilot cũng như ChatGPT để giúp bạn viết code.

## Làm thế nào để bắt đầu?

Chà, bạn cần tìm cách tích hợp với một LLM thường gồm hai phương pháp sau:

- Sử dụng API. Ở đây bạn xây dựng các yêu cầu web với prompt của bạn và nhận text tạo ra trả về.
- Sử dụng thư viện. Các thư viện giúp đóng gói các cuộc gọi API và làm cho chúng dễ sử dụng hơn.

## Thư viện/SDK

Có một vài thư viện nổi tiếng để làm việc với LLM như:

- **openai**, thư viện này giúp kết nối dễ dàng với mô hình của bạn và gửi prompt vào.

Sau đó có các thư viện hoạt động ở cấp độ cao hơn như:

- **Langchain**. Langchain rất nổi tiếng và hỗ trợ Python.
- **Semantic Kernel**. Semantic Kernel là thư viện của Microsoft hỗ trợ các ngôn ngữ C#, Python và Java.

## Ứng dụng đầu tiên sử dụng openai

Hãy xem cách chúng ta có thể xây dựng ứng dụng đầu tiên, cần những thư viện nào, yêu cầu bao nhiêu và vân vân.

### Cài đặt openai

Có nhiều thư viện trên mạng để tương tác với OpenAI hoặc Azure OpenAI. Có thể sử dụng nhiều ngôn ngữ lập trình như C#, Python, JavaScript, Java và nhiều hơn nữa. Chúng tôi đã chọn sử dụng thư viện `openai` Python, vì vậy chúng tôi sẽ dùng `pip` để cài đặt nó.

```bash
pip install openai
```

### Tạo một tài nguyên

Bạn cần thực hiện các bước sau:

- Tạo một tài khoản trên Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Được cấp quyền truy cập Azure OpenAI. Vào [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) và yêu cầu quyền truy cập.

  > [!NOTE]
  > Tại thời điểm viết bài, bạn cần nộp đơn xin quyền truy cập Azure OpenAI.

- Cài đặt Python <https://www.python.org/>
- Đã tạo tài nguyên Azure OpenAI Service. Xem hướng dẫn này để biết cách [tạo tài nguyên](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Tìm khóa API và endpoint

Ở bước này, bạn cần nói cho thư viện `openai` biết sử dụng khóa API nào. Để tìm khóa API của bạn, vào phần "Keys and Endpoint" của tài nguyên Azure OpenAI và sao chép giá trị "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Bây giờ bạn đã sao chép thông tin này, hãy hướng dẫn thư viện sử dụng nó.

> [!NOTE]
> Bạn nên tách khóa API ra khỏi mã nguồn. Bạn có thể làm điều này bằng cách sử dụng biến môi trường.
>
> - Đặt biến môi trường `OPENAI_API_KEY` bằng khóa API của bạn.
>   `export OPENAI_API_KEY='sk-...'`

### Cấu hình Azure

Nếu bạn sử dụng Azure OpenAI (hiện là một phần của Microsoft Foundry), đây là cách cấu hình. Chúng tôi sử dụng client chuẩn `OpenAI` trỏ tới endpoint Azure OpenAI `/openai/v1/`, hoạt động với Responses API và không cần `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Trên đây chúng ta thiết lập các thông số sau:

- `api_key`, đây là khóa API của bạn tìm thấy trong Azure Portal hoặc Microsoft Foundry portal.
- `base_url`, đây là endpoint tài nguyên Foundry của bạn với `/openai/v1/` được thêm vào cuối. Endpoint v1 ổn định hoạt động trên cả OpenAI và Azure OpenAI mà không cần quản lý `api_version`.

> [!NOTE] > `os.environ` đọc biến môi trường. Bạn có thể dùng nó để đọc các biến môi trường như `AZURE_OPENAI_API_KEY` và `AZURE_OPENAI_ENDPOINT`. Đặt các biến môi trường này trong terminal hoặc bằng cách sử dụng một thư viện như `dotenv`.

## Tạo văn bản

Cách tạo văn bản là sử dụng Responses API thông qua phương thức `responses.create`. Đây là một ví dụ:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

Trong đoạn mã trên, chúng ta tạo một response và truyền vào mô hình muốn sử dụng cùng prompt. Sau đó, chúng ta in văn bản tạo ra qua `response.output_text`.

### Hội thoại đa lượt

Responses API phù hợp cho cả tạo văn bản một lượt và chatbot đa lượt - bạn cung cấp danh sách tin nhắn trong `input` để xây dựng một cuộc trò chuyện:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Sẽ có thêm về chức năng này trong chương sắp tới.

## Bài tập - ứng dụng tạo văn bản đầu tiên của bạn

Bây giờ chúng ta đã học cách thiết lập và cấu hình openai, đã đến lúc xây dựng ứng dụng tạo văn bản đầu tiên của bạn. Để xây dựng ứng dụng, hãy làm theo các bước sau:

1. Tạo môi trường ảo và cài đặt openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Nếu bạn dùng Windows thì gõ `venv\Scripts\activate` thay vì `source venv/bin/activate`.

   > [!NOTE]
   > Tìm khóa Azure OpenAI của bạn bằng cách truy cập [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) và tìm `Open AI`, chọn `Open AI resource`, rồi chọn `Keys and Endpoint` và sao chép giá trị `Key 1`.

1. Tạo một file _app.py_ và thêm mã lệnh sau:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"

   # make a request using the Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # print response
   print(response.output_text)
   ```

   > [!NOTE]
   > Nếu bạn dùng OpenAI thuần túy (không phải Azure), dùng `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (không có `base_url`) và truyền tên model như `gpt-5-mini` thay vì tên deployment.

   Bạn sẽ thấy đầu ra như sau:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Các loại prompt khác nhau, cho các mục đích khác nhau

Bây giờ bạn đã biết cách tạo văn bản với prompt. Bạn thậm chí có một chương trình chạy được mà bạn có thể sửa đổi và thay đổi để tạo các loại văn bản khác nhau.

Prompts có thể dùng cho nhiều loại nhiệm vụ. Ví dụ:

- **Tạo một loại văn bản**. Ví dụ, bạn có thể tạo một bài thơ, câu hỏi cho một bài trắc nghiệm, v.v.
- **Tra cứu thông tin**. Bạn có thể dùng prompt để tìm kiếm thông tin như ví dụ: 'CORS nghĩa là gì trong phát triển web?'
- **Tạo mã nguồn**. Bạn có thể dùng prompt để tạo mã, ví dụ như phát triển biểu thức chính quy dùng để kiểm tra email hợp lệ hoặc tại sao không tạo một chương trình hoàn chỉnh, như một ứng dụng web?

## Một trường hợp sử dụng thực tế hơn: trình tạo công thức nấu ăn

Hãy tưởng tượng bạn có nguyên liệu tại nhà và muốn nấu món gì đó. Để làm điều đó, bạn cần một công thức. Một cách để tìm công thức là dùng công cụ tìm kiếm hoặc bạn có thể sử dụng LLM để làm điều đó.

Bạn có thể viết prompt như sau:

> "Cho tôi xem 5 công thức món ăn với các nguyên liệu sau: gà, khoai tây và cà rốt. Mỗi công thức liệt kê tất cả nguyên liệu được sử dụng"

Với prompt trên, bạn có thể nhận được kết quả tương tự như:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 2 cloves garlic, minced
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
```

Kết quả này rất tốt, tôi biết nấu gì. Ở điểm này, những cải thiện hữu ích có thể là:

- Lọc ra nguyên liệu tôi không thích hoặc bị dị ứng.
- Tạo danh sách mua sắm, trong trường hợp tôi không có đủ nguyên liệu tại nhà.

Với các trường hợp trên, chúng ta thêm một prompt bổ sung:

> "Vui lòng loại bỏ các công thức có tỏi vì tôi bị dị ứng và thay thế bằng thứ khác. Ngoài ra, vui lòng tạo danh sách mua sắm cho các công thức, xem xét tôi đã có gà, khoai tây và cà rốt tại nhà."

Bây giờ bạn có kết quả mới, đó là:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano

Shopping List:
- Olive oil
- Onion
- Thyme
- Oregano
- Salt
- Pepper
```

Đó là năm công thức của bạn, không có tỏi và bạn cũng có danh sách mua sắm xem xét những gì bạn đã có tại nhà.

## Bài tập - xây dựng trình tạo công thức nấu ăn

Bây giờ chúng ta đã đóng vai một kịch bản, hãy viết mã để phù hợp với kịch bản đã trình bày. Để làm điều đó, hãy làm theo các bước sau:

1. Sử dụng file _app.py_ hiện có làm điểm bắt đầu
1. Tìm biến `prompt` và thay đổi mã của nó như sau:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Nếu bạn chạy mã này, bạn sẽ thấy kết quả tương tự:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > LƯU Ý, LLM của bạn không xác định duy nhất, vì vậy bạn có thể nhận kết quả khác nhau mỗi lần chạy chương trình.

   Rất tốt, hãy xem cách chúng ta có thể cải thiện. Để cải thiện, chúng ta muốn đảm bảo mã linh hoạt, để nguyên liệu và số lượng công thức có thể dễ dàng thay đổi.

1. Hãy thay đổi mã theo cách sau:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Thử chạy đoạn mã này sẽ ra kết quả như sau:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Cải thiện bằng cách thêm bộ lọc và danh sách mua sắm

Bây giờ chúng ta có một ứng dụng hoạt động có khả năng tạo công thức và linh hoạt vì dựa vào đầu vào từ người dùng, cả về số lượng công thức và nguyên liệu sử dụng.

Để cải tiến hơn nữa, chúng ta muốn thêm:

- **Lọc nguyên liệu**. Chúng ta muốn có thể lọc ra các nguyên liệu không thích hoặc bị dị ứng. Để làm điều này, ta có thể chỉnh sửa prompt hiện tại và thêm điều kiện lọc vào cuối prompt như sau:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Ở trên, chúng ta thêm `{filter}` vào cuối prompt và cũng nhận giá trị bộ lọc từ người dùng.

  Một ví dụ đầu vào khi chạy chương trình bây giờ có thể như sau:

  ```output
  No of recipes (for example, 5): 3
  List of ingredients (for example, chicken, potatoes, and carrots): onion,milk
  Filter (for example, vegetarian, vegan, or gluten-free): no milk

  1. French Onion Soup

  Ingredients:

  -1 large onion, sliced
  -3 cups beef broth
  -1 cup milk
  -6 slices french bread
  -1/4 cup shredded Parmesan cheese
  -1 tablespoon butter
  -1 teaspoon dried thyme
  -1/4 teaspoon salt
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add beef broth, milk, thyme, salt, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Place french bread slices on soup bowls.
  5. Ladle soup over bread.
  6. Sprinkle with Parmesan cheese.

  2. Onion and Potato Soup

  Ingredients:

  -1 large onion, chopped
  -2 cups potatoes, diced
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add potatoes, vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Serve hot.

  3. Creamy Onion Soup

  Ingredients:

  -1 large onion, chopped
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper
  -1/4 cup all-purpose flour
  -1/2 cup shredded Parmesan cheese

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. In a small bowl, whisk together flour and Parmesan cheese until smooth.
  5. Add to soup and simmer for an additional 5 minutes, or until soup has thickened.
  ```

  Như bạn thấy, bất kỳ công thức nào có sữa đã bị loại bỏ. Nhưng nếu bạn không dung nạp lactose, bạn có thể muốn lọc cả các công thức có phô mai nữa, vì thế cần rõ ràng khi nhập.

- **Tạo danh sách mua sắm**. Chúng ta muốn tạo danh sách mua sắm dựa trên những gì đã có tại nhà.

  Đối với tính năng này, chúng ta có thể thử giải quyết trong một prompt hoặc chia ra làm hai prompt. Hãy thử cách thứ hai. Ở đây chúng ta thêm prompt thứ hai, nhưng để nó hoạt động, chúng ta cần thêm kết quả từ prompt đầu làm ngữ cảnh cho prompt sau.

  Tìm phần trong mã in ra kết quả từ prompt đầu tiên và thêm đoạn mã sau bên dưới:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Lưu ý các điểm sau:

  1. Chúng ta xây dựng prompt mới bằng cách thêm kết quả từ prompt trước vào prompt mới:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Chúng ta tạo yêu cầu mới, cũng cân nhắc tới số lượng token yêu cầu ở prompt đầu, lần này đặt `max_output_tokens` là 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Thử chạy đoạn mã này, chúng ta thu được kết quả sau:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Cải thiện thiết lập của bạn

Những gì chúng ta có cho đến nay là mã hoạt động, nhưng có một số điều chỉnh chúng ta nên làm để cải thiện thêm. Một số việc chúng ta nên làm là:

- **Tách bí mật ra khỏi mã**, như khóa API. Bí mật không thuộc về mã và nên được lưu trữ ở một nơi an toàn. Để tách bí mật ra khỏi mã, chúng ta có thể sử dụng biến môi trường và các thư viện như `python-dotenv` để tải chúng từ một tệp. Dưới đây là cách điều đó sẽ trông như thế nào trong mã:

  1. Tạo một tệp `.env` với nội dung sau:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Lưu ý, với Azure OpenAI trong Microsoft Foundry, bạn cần thiết lập các biến môi trường sau thay vào đó:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Trong mã, bạn sẽ tải các biến môi trường như sau:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Một lời về độ dài token**. Chúng ta nên xem xét bao nhiêu token cần để tạo ra văn bản mong muốn. Token tiêu tốn tiền, vì vậy khi có thể, chúng ta nên cố gắng tiết kiệm số token sử dụng. Ví dụ, liệu chúng ta có thể diễn đạt prompt để dùng ít token hơn không?

  Để thay đổi số token dùng, bạn có thể sử dụng tham số `max_output_tokens`. Ví dụ, nếu bạn muốn dùng 100 token, bạn làm như sau:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Thử nghiệm với nhiệt độ**. Nhiệt độ là thứ chúng ta chưa đề cập cho đến nay nhưng là ngữ cảnh quan trọng cho cách chương trình hoạt động. Giá trị nhiệt độ càng cao thì kết quả càng ngẫu nhiên. Ngược lại, giá trị nhiệt độ càng thấp thì kết quả càng dự đoán được. Hãy cân nhắc xem bạn có muốn kết quả có biến thiên hay không.

  Để thay đổi nhiệt độ, bạn có thể sử dụng tham số `temperature`. Ví dụ, nếu bạn muốn dùng nhiệt độ 0.5, bạn làm như sau:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Lưu ý, càng gần 1.0, kết quả càng đa dạng.

- **Các mô hình suy luận không sử dụng `temperature`**. Đây là sự chuyển đổi quan trọng năm 2026. Các mô hình hiện tại không bị loại bỏ trên Microsoft Foundry là **mô hình suy luận** (dòng GPT-5, o-series) - và chúng **không hỗ trợ `temperature` hoặc `top_p`** (cũng không `max_tokens`; dùng `max_output_tokens`). Nếu bạn gửi `temperature` đến `gpt-5-mini`, bạn sẽ nhận lỗi "tham số không được hỗ trợ". Vì vậy để thử ví dụ nhiệt độ bên trên, hãy chỉ định một mô hình vẫn hỗ trợ điều khiển sampling - ví dụ một mô hình **Llama** mở như `Llama-3.3-70B-Instruct` từ [danh mục mô hình Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), gọi qua điểm cuối Foundry Models / Azure AI Inference (theo cách giống các mẫu `githubmodels-*`). Đối với các mô hình suy luận như GPT-5, bạn điều hướng kết quả khác:
  - **Kỹ thuật prompt** - hướng dẫn rõ ràng, ví dụ, và đầu ra có cấu trúc (xem bài học [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) làm công việc mà các núm sampling đã từng đảm nhiệm.
  - **Điều khiển suy luận** - các tham số như nỗ lực/độ dài thuyết minh cân bằng độ sâu suy luận với độ trễ và chi phí.

  Nói ngắn gọn: `temperature`/`top_p` vẫn còn hợp lệ trên nhiều mô hình (Llama, Mistral, Phi, và dòng GPT-4.x - mặc dù GPT-4.x đang bị loại bỏ dần), nhưng xu hướng phát triển là kỹ thuật tạo lời nhắc + điều khiển suy luận trên các mô hình suy luận như GPT-5.

## Bài tập

Với bài tập này, bạn có thể chọn xây dựng gì tùy thích.

Dưới đây là một số gợi ý:

- Tinh chỉnh ứng dụng tạo công thức nấu ăn để cải thiện nó hơn nữa. Thử nghiệm với các giá trị nhiệt độ và các lời nhắc để xem bạn có thể tạo ra gì.
- Xây dựng một "bạn học". Ứng dụng này nên có khả năng trả lời các câu hỏi về một chủ đề, ví dụ như Python, bạn có thể có các lời nhắc như "Chủ đề nào đó trong Python là gì?", hoặc bạn có thể có một lời nhắc nói, cho tôi xem mã cho một chủ đề nhất định v.v.
- Bot lịch sử, làm sống lại lịch sử, hướng dẫn bot đóng vai một nhân vật lịch sử nhất định và hỏi nó các câu hỏi về cuộc đời và thời đại của nhân vật đó.

## Giải pháp

### Bạn học

Dưới đây là một lời nhắc khởi đầu, xem cách bạn có thể sử dụng nó và tùy chỉnh theo ý thích.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Bot lịch sử

Dưới đây là một số lời nhắc bạn có thể sử dụng:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Kiểm tra kiến thức

Khái niệm nhiệt độ làm gì?

1. Nó điều khiển mức độ ngẫu nhiên của đầu ra.
1. Nó điều khiển kích thước câu trả lời.
1. Nó điều khiển số lượng token được sử dụng.

## 🚀 Thử thách

Khi làm bài tập, hãy thử thay đổi nhiệt độ, thử đặt giá trị 0, 0.5 và 1. Hãy nhớ rằng 0 là độ biến thiên thấp nhất và 1 là độ biến thiên cao nhất. Giá trị nào hoạt động tốt nhất cho ứng dụng của bạn?

## Làm tốt lắm! Tiếp tục học hỏi

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Học Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức về Generative AI của bạn!

Hãy đến Bài học 7, nơi chúng ta sẽ tìm hiểu cách [xây dựng ứng dụng trò chuyện](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->