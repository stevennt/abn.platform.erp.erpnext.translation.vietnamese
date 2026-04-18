<!-- add-breadcrumbs -->
#Duy trì Mã mặt hàng của Nhà cung cấp trong Danh mục Mặt hàng

Đối với mỗi mặt hàng, mã được gán có thể khác với mã mà nhà cung cấp của bạn cung cấp cho chính mặt hàng đó. ERPNext cho phép bạn theo dõi Mã mặt hàng của Nhà cung cấp trong danh mục Mặt hàng. Ngoài ra, bạn có thể lấy Mã mặt hàng của Nhà cung cấp trong các giao dịch mua hàng của mình, để họ có thể dễ dàng nhận diện mặt hàng dựa trên Mã mặt hàng của họ.

#### 1. Cập nhật Mã mặt hàng của Nhà cung cấp trong Mặt hàng

Trong danh mục Mặt hàng, tại phần Chi tiết Nhà cung cấp (Supplier Details), hãy nhập Mã mặt hàng (Item Code) do Nhà cung cấp cung cấp cho mặt hàng này.

<img alt="Supplier Item Code" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/supplier-item-code.png">

#### 2. Mã mặt hàng của Nhà cung cấp trong các Giao dịch

Mỗi giao dịch mua hàng đều có trường trong bảng Mặt hàng, nơi Mã mặt hàng của Nhà cung cấp được lấy ra. Trường này bị ẩn trong biểu mẫu cũng như trong Mẫu in Tiêu chuẩn. Bạn có thể làm cho nó hiển thị bằng cách thay đổi thuộc tính của trường này từ [Customize Form.](../../customize-erpnext/customize-form.html.md)

Đi tới chế độ xem in, nhấp vào Menu > customize, nhập tên mẫu in mới, tìm bảng Mặt hàng (Items), nhấp vào nút **Select columns** trong đó. Bạn sẽ thấy màn hình sau. Bây giờ hãy chọn ô "Supplier Part Number".

![Supplier item part print format](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/supplier-item-code-print-format.png)

Mã mặt hàng của Nhà cung cấp sẽ chỉ được lấy trong giao dịch mua hàng nếu cả Nhà cung cấp và Mã mặt hàng được chọn trong giao dịch mua hàng đều được ánh xạ với giá trị đã nêu trong danh mục Mặt hàng.

<img alt="Supplier Item Code in transaction" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/supplier-item-code-in-purchase-order.png">


<!-- markdown -->