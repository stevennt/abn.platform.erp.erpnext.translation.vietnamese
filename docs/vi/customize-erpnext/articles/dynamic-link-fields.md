<!-- add-breadcrumbs -->
# Trường Dynamic Link

Trường Dynamic Link là một trường có thể tìm kiếm và giữ giá trị của bất kỳ DocType nào. Hãy cùng xem xét một ví dụ để tìm hiểu cách thức hoạt động của trường Dynamic Link.

Khi tạo Cơ hội hoặc Báo giá, chúng ta phải xác định rõ ràng đó là dành cho Khách hàng tiềm năng hay Khách hàng. Dựa trên lựa chọn của chúng ta (Khách hàng tiềm năng/Khách hàng), một trường liên kết khác sẽ xuất hiện để chúng ta có thể chọn Khách hàng tiềm năng hoặc Khách hàng thực tế.

Nếu bạn thiết lập trường trước đó là Dynamic Link (nơi chúng ta chọn Khách hàng tiềm năng hoặc Khách hàng thực tế), thì trường sau đó sẽ tự động được liên kết với danh mục được chọn ở trường đầu tiên, tức là Khách hàng tiềm năng hoặc Khách hàng. Do đó, chúng ta không cần phải chèn các trường liên kết riêng biệt cho Khách hàng và Khách hàng tiềm năng.

Dưới đây là các bước để chèn Trường Dynamic Link tùy chỉnh. Ví dụ, chúng ta sẽ chèn trường Dynamic Link trong Bút toán.

#### Bước 1: Chèn trường Link cho DocType

Đầu tiên, chúng ta sẽ tạo một trường liên kết (link field) sẽ được liên kết với DocType.

<img alt="Custom Link Field" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/customize-dynamic-link-1.gif">

Khi đề cập đến **DocType** trong trường Option, ý chúng ta là DocType cha. Giống như Báo giá là một DocType, có nhiều bản ghi Báo giá bên dưới nó. Tương tự, DocType cũng là một DocType có các Đơn bán hàng, Đơn mua hàng và các doctype khác được tạo dưới dạng các bản ghi DocType.

**DocType**<br>
---- Đơn bán hàng<br>
---- Hóa đơn mua hàng<br>
---- Báo giá<br>
---- Hóa đơn bán hàng<br>
---- Nhân viên<br>
---- Lệnh sản xuất<br>
.. và vân vân.

Vì vậy, việc liên kết trường này với DocType cha sẽ liệt kê tất cả các bản ghi DocType.

<img alt="journal Voucher Link Field" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/customize-dynamic-link.png">

#### Bước 2: Chèn trường Dynamic Link

Loại của trường tùy chỉnh này sẽ là "Dynamic Link". Trong trường Option, tên của trường liên kết DocType sẽ được đề cập.

<img alt="Custom Dynamic Field" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/customize-dynamic-link-2.gif">

Trường này sẽ cho phép chọn ID tài liệu, dựa trên giá trị được chọn trong trường liên kết DocType. Ví dụ, nếu chúng ta chọn Đơn bán hàng ở trường trước đó, trường Dynamic Link sẽ liệt kê tất cả các ID của Đơn bán hàng.

<img alt="Custom Dynamic Field" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/customize-dynamic-link-3.gif">

**Tùy chỉnh các tùy chọn trong trường liên kết DocType**

Theo mặc định, trường liên kết DocType sẽ cung cấp tất cả các biểu mẫu/doctype để lựa chọn. Nếu bạn muốn trường này hiển thị một số doctype cụ thể trong kết quả tìm kiếm, bạn sẽ cần viết Custom Script cho nó.

{next}
<!-- markdown -->