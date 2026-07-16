# Xây dựng Ứng dụng Tạo Văn bản

[![Xây dựng Ứng dụng Tạo Văn bản](../../../translated_images/vi/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Nhấp vào hình ảnh ở trên để xem video của bài học này)_

Bạn đã thấy trong suốt chương trình học này có những khái niệm cốt lõi như prompt và thậm chí một ngành học riêng gọi là "prompt engineering". Nhiều công cụ bạn có thể tương tác như ChatGPT, Office 365, Microsoft Power Platform và nhiều hơn nữa, hỗ trợ bạn sử dụng các prompt để hoàn thành một việc gì đó.

Để bạn thêm trải nghiệm như vậy vào một ứng dụng, bạn cần hiểu các khái niệm như prompt, completions và chọn một thư viện để làm việc. Đó chính là những gì bạn sẽ học trong chương này.

## Giới thiệu

Trong chương này, bạn sẽ:

- Tìm hiểu về thư viện openai và các khái niệm cốt lõi của nó.
- Xây dựng một ứng dụng tạo văn bản sử dụng openai.
- Hiểu cách sử dụng các khái niệm như prompt, nhiệt độ (temperature), và token để xây dựng ứng dụng tạo văn bản.

## Mục tiêu học tập

Vào cuối bài học này, bạn sẽ có thể:

- Giải thích ứng dụng tạo văn bản là gì.
- Xây dựng một ứng dụng tạo văn bản sử dụng openai.
- Cấu hình ứng dụng của bạn để sử dụng nhiều hoặc ít token hơn và cũng thay đổi nhiệt độ đầu ra, để có kết quả đa dạng.

## Ứng dụng tạo văn bản là gì?

Thông thường khi bạn xây dựng một ứng dụng, nó sẽ có một giao diện kiểu như sau:

- Dựa trên lệnh. Ứng dụng console là những ứng dụng điển hình nơi bạn gõ một lệnh và nó thực hiện nhiệm vụ. Ví dụ, `git` là một ứng dụng dựa trên lệnh.
- Giao diện người dùng (UI). Một số ứng dụng có giao diện đồ họa (GUI) nơi bạn nhấn nút, nhập văn bản, chọn tùy chọn và nhiều hơn nữa.

### Ứng dụng Console và UI có giới hạn

So sánh với ứng dụng dựa trên lệnh mà bạn gõ một lệnh:

- **Nó bị giới hạn**. Bạn không thể gõ bất kỳ lệnh nào, chỉ có những lệnh mà ứng dụng hỗ trợ.
- **Ngôn ngữ cụ thể**. Một số ứng dụng hỗ trợ nhiều ngôn ngữ, nhưng theo mặc định ứng dụng được xây dựng cho một ngôn ngữ cụ thể, dù bạn có thể thêm hỗ trợ ngôn ngữ.

### Lợi ích của ứng dụng tạo văn bản

Vậy ứng dụng tạo văn bản khác gì?

Trong một ứng dụng tạo văn bản, bạn có nhiều linh hoạt hơn, bạn không bị giới hạn bởi tập lệnh lệnh hay một ngôn ngữ nhập đầu vào cụ thể. Thay vào đó, bạn có thể sử dụng ngôn ngữ tự nhiên để tương tác với ứng dụng. Một lợi ích khác là bạn đã tương tác với nguồn dữ liệu đã được đào tạo trên một kho tàng thông tin rộng lớn, trong khi một ứng dụng truyền thống có thể bị giới hạn bởi dữ liệu trong cơ sở dữ liệu.

### Tôi có thể xây dựng gì với ứng dụng tạo văn bản?

Có nhiều thứ bạn có thể xây dựng. Ví dụ:

- **Chatbot**. Một chatbot trả lời các câu hỏi về các chủ đề, như công ty của bạn và sản phẩm của nó có thể là một lựa chọn tốt.
- **Trợ lý**. Các mô hình ngôn ngữ lớn (LLM) rất giỏi trong việc tóm tắt văn bản, lấy thông tin chi tiết từ văn bản, tạo văn bản như sơ yếu lý lịch và nhiều hơn nữa.
- **Trợ lý viết code**. Tùy thuộc vào mô hình ngôn ngữ bạn sử dụng, bạn có thể xây dựng trợ lý viết code giúp bạn viết code. Ví dụ, bạn có thể sử dụng sản phẩm như GitHub Copilot cũng như ChatGPT để giúp viết code.

## Làm sao để bắt đầu?

Bạn cần tìm cách tích hợp với một LLM, thường có hai cách tiếp cận sau:

- Sử dụng API. Tại đây bạn xây dựng các yêu cầu web với prompt và nhận văn bản được tạo ra.
- Sử dụng thư viện. Các thư viện giúp đóng gói các cuộc gọi API và làm cho chúng dễ sử dụng hơn.

## Thư viện/SDK

Có vài thư viện nổi tiếng để làm việc với LLM như:

- **openai**, thư viện này giúp dễ dàng kết nối với mô hình của bạn và gửi prompt.

Sau đó có các thư viện hoạt động ở mức cao hơn như:

- **Langchain**. Langchain được biết đến rộng rãi và hỗ trợ Python.
- **Semantic Kernel**. Semantic Kernel là thư viện của Microsoft hỗ trợ các ngôn ngữ C#, Python và Java.

## Ứng dụng đầu tiên sử dụng openai

Hãy xem cách chúng ta xây dựng ứng dụng đầu tiên, những thư viện cần có, bao nhiêu là đủ và những thứ khác.

### Cài đặt openai

Có nhiều thư viện để tương tác với OpenAI hoặc Azure OpenAI. Có thể dùng nhiều ngôn ngữ lập trình như C#, Python, JavaScript, Java và nhiều hơn nữa. Chúng ta chọn sử dụng thư viện Python `openai`, vì thế sẽ dùng `pip` để cài đặt.

```bash
pip install openai
```

### Tạo tài nguyên

Bạn cần thực hiện các bước sau:

- Tạo tài khoản trên Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Truy cập Azure OpenAI. Vào [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) và yêu cầu quyền truy cập.

  > [!NOTE]
  > Thời điểm viết bài, bạn cần nộp đơn xin quyền truy cập Azure OpenAI.

- Cài đặt Python <https://www.python.org/>
- Đã tạo tài nguyên Dịch vụ Azure OpenAI. Xem hướng dẫn này để biết cách [tạo tài nguyên](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Tìm khóa API và endpoint

Lúc này, bạn cần chỉ cho thư viện `openai` biết sử dụng khóa API nào. Để tìm khóa API, vào phần "Keys and Endpoint" của tài nguyên Azure OpenAI và sao chép giá trị "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Giờ bạn đã sao chép thông tin này, hãy hướng dẫn các thư viện sử dụng nó.

> [!NOTE]
> Bạn nên tách khóa API khỏi mã nguồn. Bạn có thể làm điều này bằng cách sử dụng biến môi trường.
>
> - Đặt biến môi trường `OPENAI_API_KEY` thành khóa API của bạn.
>   `export OPENAI_API_KEY='sk-...'`

### Cấu hình Azure

Nếu bạn sử dụng Azure OpenAI (nay là một phần của Microsoft Foundry), đây là cách cấu hình. Chúng ta dùng client chuẩn `OpenAI` trỏ đến endpoint Azure OpenAI `/openai/v1/`, tương thích với Responses API và không cần `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Ở trên, ta thiết lập:

- `api_key`, đó là khóa API của bạn lấy từ Azure Portal hoặc cổng Microsoft Foundry.
- `base_url`, đó là endpoint tài nguyên Foundry của bạn có thêm `/openai/v1/` ở cuối. Endpoint ổn định v1 hoạt động trên cả OpenAI và Azure OpenAI mà không cần quản lý `api_version`.

> [!NOTE] > `os.environ` đọc biến môi trường. Bạn có thể dùng để đọc biến môi trường như `AZURE_OPENAI_API_KEY` và `AZURE_OPENAI_ENDPOINT`. Thiết lập các biến này trong terminal hoặc dùng thư viện như `dotenv`.

## Tạo văn bản

Cách tạo văn bản là sử dụng Responses API thông qua phương thức `responses.create`. Ví dụ:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # đây là tên triển khai mô hình của bạn
    input=prompt,
    store=False,
)
print(response.output_text)
```

Trong đoạn mã trên, ta tạo một phản hồi và truyền mô hình muốn dùng cùng prompt. Sau đó in văn bản được tạo qua `response.output_text`.

### Đàm thoại nhiều lượt

Responses API phù hợp cho cả việc tạo văn bản một lượt và chatbot nhiều lượt — bạn cung cấp một danh sách tin nhắn trong `input` để tạo cuộc trò chuyện:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

Sẽ có chương sau giải thích chi tiết về chức năng này.

## Bài tập - ứng dụng tạo văn bản đầu tiên của bạn

Giờ bạn đã học cách thiết lập và cấu hình openai, đã đến lúc xây dựng ứng dụng tạo văn bản đầu tiên. Để xây dựng ứng dụng, làm theo các bước:

1. Tạo môi trường ảo và cài đặt openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Nếu bạn dùng Windows, gõ `venv\Scripts\activate` thay vì `source venv/bin/activate`.

   > [!NOTE]
   > Tìm khóa Azure OpenAI của bạn bằng cách vào [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), tìm `Open AI`, chọn `Open AI resource` rồi chọn `Keys and Endpoint` và sao chép giá trị `Key 1`.

1. Tạo file _app.py_ và đặt mã sau:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # thêm mã hoàn thành của bạn
   prompt = "Complete the following: Once upon a time there was a"

   # thực hiện một yêu cầu sử dụng API Responses
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # in phản hồi
   print(response.output_text)
   ```

   > [!NOTE]
   > Nếu bạn dùng OpenAI thuần túy (không phải Azure), hãy dùng `client = OpenAI(api_key="<thay giá trị này bằng khóa OpenAI của bạn>")` (không có `base_url`) và truyền tên mô hình như `gpt-4o-mini` thay vì tên triển khai.

   Bạn sẽ thấy đầu ra như sau:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Các loại prompt khác nhau, cho các mục đích khác nhau

Giờ bạn đã biết cách tạo văn bản bằng prompt. Bạn thậm chí đã có chương trình chạy được và có thể chỉnh sửa để tạo ra các loại văn bản khác nhau.

Prompt có thể dùng cho nhiều loại nhiệm vụ. Ví dụ:

- **Tạo loại văn bản**. Ví dụ, bạn có thể tạo thơ, câu hỏi cho bài kiểm tra vv.
- **Tìm kiếm thông tin**. Bạn có thể dùng prompt để tìm thông tin như ví dụ 'CORS có nghĩa là gì trong phát triển web?'.
- **Tạo code**. Bạn có thể dùng prompt để tạo code, ví dụ phát triển biểu thức chính quy để kiểm tra email hoặc thậm chí tạo chương trình hoàn chỉnh, như ứng dụng web?

## Trường hợp sử dụng thực tế hơn: trình tạo công thức nấu ăn

Hãy tưởng tượng bạn có nguyên liệu tại nhà và muốn nấu món gì đó. Để làm điều đó, bạn cần công thức. Một cách tìm công thức là dùng công cụ tìm kiếm hoặc bạn có thể dùng một LLM.

Bạn có thể viết prompt như sau:

> "Cho tôi thấy 5 công thức món ăn với các nguyên liệu sau: gà, khoai tây và cà rốt. Với mỗi công thức, liệt kê tất cả các nguyên liệu sử dụng"

Dựa vào prompt trên, bạn có thể nhận được đáp ứng tương tự:

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

Kết quả này rất tốt, tôi biết sẽ nấu món gì. Ở bước này, những cải tiến hữu ích có thể là:

- Lọc bỏ nguyên liệu tôi không thích hoặc dị ứng.
- Tạo danh sách mua sắm, phòng trường hợp tôi không có đủ nguyên liệu ở nhà.

Với các trường hợp trên, hãy thêm prompt bổ sung:

> "Vui lòng loại bỏ các công thức có tỏi vì tôi dị ứng và thay thế bằng nguyên liệu khác. Ngoài ra, làm ơn tạo danh sách mua sắm cho các công thức, tính cả việc tôi đã có sẵn gà, khoai tây và cà rốt ở nhà."

Bây giờ bạn có kết quả mới, cụ thể là:

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

Đây là 5 công thức của bạn, không có tỏi và bạn cũng có danh sách mua sắm tính đến nguyên liệu đã có.

## Bài tập - xây dựng trình tạo công thức nấu ăn

Giờ chúng ta đã mô phỏng kịch bản, hãy viết mã để phù hợp với kịch bản đã trình bày. Để làm vậy, làm theo các bước:

1. Dùng file _app.py_ hiện có làm điểm bắt đầu
1. Tìm biến `prompt` và thay đổi mã sau:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Nếu bạn chạy mã bây giờ, sẽ có đầu ra tương tự:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > LƯU Ý, mô hình ngôn ngữ bạn dùng có tính không xác định, nên bạn có thể nhận kết quả khác nhau mỗi lần chạy chương trình.

   Tốt, hãy xem làm sao ta cải thiện. Để cải tiến, chúng ta muốn code linh hoạt, để nguyên liệu và số công thức có thể được thay đổi.

1. Chúng ta thay đổi mã như sau:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # nội suy số lượng công thức vào lời nhắc và nguyên liệu
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Đoạn mã thử nghiệm có thể trông như sau:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Cải tiến bằng cách thêm bộ lọc và danh sách mua sắm

Giờ chúng ta có ứng dụng hoạt động tạo công thức và có tính linh hoạt vì phụ thuộc vào đầu vào từ người dùng, cả số lượng công thức và nguyên liệu sử dụng.

Để cải tiến thêm, ta muốn thêm:

- **Lọc nguyên liệu**. Muốn có thể lọc những nguyên liệu không thích hoặc dị ứng. Để thay đổi này, ta sửa prompt hiện có và thêm điều kiện lọc vào cuối như sau:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Ở trên, ta thêm `{filter}` vào cuối prompt và cũng lấy giá trị lọc từ người dùng.

  Ví dụ đầu vào khi chạy chương trình bây giờ có thể là:

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

  Như bạn thấy, bất kỳ công thức nào có sữa đều bị lọc ra. Nhưng nếu bạn không dung nạp lactose, có thể muốn lọc thêm những công thức có phô mai nữa, nên cần làm rõ.


- **Tạo danh sách mua sắm**. Chúng ta muốn tạo một danh sách mua sắm, xem xét những gì chúng ta đã có ở nhà.

  Đối với chức năng này, chúng ta có thể thử giải quyết mọi thứ trong một lời nhắc hoặc chúng ta có thể chia nó thành hai lời nhắc. Hãy thử cách sau. Ở đây, chúng tôi đề xuất thêm một lời nhắc bổ sung, nhưng để điều đó hoạt động, chúng ta cần thêm kết quả của lời nhắc trước làm ngữ cảnh cho lời nhắc sau.

  Định vị phần trong mã in ra kết quả từ lời nhắc đầu tiên và thêm mã sau bên dưới:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # in phản hồi
  print("Shopping list:")
  print(response.output_text)
  ```

  Lưu ý những điều sau đây:

  1. Chúng tôi đang tạo một lời nhắc mới bằng cách thêm kết quả từ lời nhắc đầu tiên vào lời nhắc mới:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Chúng tôi thực hiện một yêu cầu mới, đồng thời xem xét số lượng token chúng tôi đã yêu cầu trong lời nhắc đầu tiên, vì vậy lần này chúng tôi đặt `max_output_tokens` là 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Thử chạy đoạn mã này, chúng ta nhận được kết quả sau:

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

Những gì chúng ta có cho đến nay là mã hoạt động, nhưng có một số điều chỉnh chúng ta nên làm để cải thiện hơn nữa. Một số việc chúng ta nên làm là:

- **Tách riêng thông tin bí mật khỏi mã**, như khóa API. Thông tin bí mật không thuộc về mã và nên được lưu trữ ở vị trí an toàn. Để tách thông tin bí mật khỏi mã, chúng ta có thể dùng biến môi trường và các thư viện như `python-dotenv` để tải từ tệp. Dưới đây là cách điều đó trong mã:

  1. Tạo tệp `.env` với nội dung sau:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Lưu ý, đối với Azure OpenAI trong Microsoft Foundry, bạn cần thiết lập các biến môi trường sau thay thế:

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

- **Lời về độ dài token**. Chúng ta nên cân nhắc bao nhiêu token cần thiết để tạo văn bản mong muốn. Token tốn tiền, vì vậy nếu có thể, hãy cố gắng tiết kiệm số token sử dụng. Ví dụ, có thể chúng ta trình bày lời nhắc sao cho dùng ít token hơn?

  Để thay đổi số token dùng, bạn có thể sử dụng tham số `max_output_tokens`. Ví dụ, nếu bạn muốn dùng 100 token, bạn sẽ làm như sau:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Thử nghiệm với nhiệt độ**. Nhiệt độ là điều chúng ta chưa đề cập đến cho đến nay nhưng là bối cảnh quan trọng cho cách chương trình của chúng ta hoạt động. Giá trị nhiệt độ càng cao, đầu ra càng ngẫu nhiên. Ngược lại, giá trị nhiệt độ càng thấp, đầu ra càng dự đoán được. Cân nhắc bạn có muốn đầu ra đa dạng hay không.

  Để thay đổi nhiệt độ, bạn có thể sử dụng tham số `temperature`. Ví dụ, nếu bạn muốn dùng nhiệt độ 0.5, bạn sẽ làm như sau:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Lưu ý, càng gần 1.0, đầu ra càng đa dạng.

## Bài tập

Trong bài tập này, bạn có thể lựa chọn gì để xây dựng.

Dưới đây là một số gợi ý:

- Điều chỉnh ứng dụng tạo công thức nấu ăn để cải thiện hơn nữa. Thử nghiệm với các giá trị nhiệt độ và lời nhắc để xem bạn có thể tạo ra gì.
- Xây dựng một "bạn học". Ứng dụng này nên có khả năng trả lời các câu hỏi về một chủ đề, ví dụ như Python, bạn có thể dùng các lời nhắc như "Python có khái niệm gì?", hoặc lời nhắc hiển thị code cho một chủ đề cụ thể, v.v.
- Bot Lịch sử, làm cho lịch sử trở nên sống động, hướng dẫn bot đóng vai một nhân vật lịch sử nhất định và hỏi nó các câu hỏi về cuộc đời và thời kỳ của nhân vật đó.

## Giải pháp

### Bạn học

Dưới đây là một lời nhắc bắt đầu, xem cách bạn có thể sử dụng và điều chỉnh cho phù hợp.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Bot Lịch sử

Dưới đây là một số lời nhắc bạn có thể dùng:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Kiểm tra kiến thức

Khái niệm nhiệt độ có tác dụng gì?

1. Nó điều khiển mức độ ngẫu nhiên của đầu ra.
1. Nó điều khiển kích thước phản hồi.
1. Nó điều khiển số token được sử dụng.

## 🚀 Thử thách

Khi làm bài tập, cố gắng thay đổi nhiệt độ, thử thiết lập là 0, 0.5, và 1. Hãy nhớ rằng 0 là ít biến đổi nhất và 1 là biến đổi nhiều nhất. Giá trị nào phù hợp nhất cho ứng dụng của bạn?

## Rất tốt! Tiếp tục học tập

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) để tiếp tục nâng cao kiến thức Generative AI của bạn!

Đi đến Bài học 7, nơi chúng ta sẽ xem cách [xây dựng ứng dụng trò chuyện](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->