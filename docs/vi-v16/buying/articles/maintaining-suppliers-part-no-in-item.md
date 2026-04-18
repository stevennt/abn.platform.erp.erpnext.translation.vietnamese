<!-- add-breadcrumbs -->
# Duy trì Mã mặt hàng của Nhà cung cấp trong Danh mục Mặt hàng

Đối với mỗi mặt hàng, mã được gán trong hệ thống có thể khác với mã mà nhà cung cấp cung cấp cho chính mặt hàng đó. ERPNext cho phép bạn theo dõi Mã mặt hàng của Nhà cung cấp trong danh mục Mặt hàng. Ngoài ra, bạn có thể lấy Mã mặt hàng của Nhà cung cấp trong các giao dịch mua hàng của mình, giúp nhà cung cấp dễ dàng nhận diện mặt hàng dựa trên mã riêng của họ.

#### 1. Cập nhật Mã mặt hàng của Nhà cung cấp trong Mặt hàng

Trong danh mục Mặt hàng, tại phần Chi tiết Nhà cung cấp (Supplier Details), hãy nhập Mã mặt hàng (Item Code) do Nhà cung cấp cung cấp cho mặt hàng này.

<img alt="Supplier Item Code" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/supplier-item-code.png">

#### 2. Mã mặt hàng của Nhà cung cấp trong các Giao dịch

Mỗi giao dịch mua hàng đều có trường trong bảng Mặt hàng, nơi Mã mặt hàng của Nhà cung cấp được tự động lấy ra. Trường này mặc định bị ẩn trong biểu mẫu cũng như trong Mẫu in Tiêu chuẩn. Bạn có thể làm cho nó hiển thị bằng cách thay đổi thuộc tính của trường này thông qua [Tùy chỉnh biểu mẫu](customize-form.md).

Đi tới chế độ xem in, nhấp vào Menu > Customize, nhập tên mẫu in mới, tìm bảng Mặt hàng (Items), nhấp vào nút **Select columns** trong đó. Bạn sẽ thấy màn hình như hình dưới đây. Hãy chọn ô "Supplier Part Number".

![Supplier item part print format](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/supplier-item-code-print-format.png)

Mã mặt hàng của Nhà cung cấp sẽ chỉ được lấy trong giao dịch mua hàng nếu cả Nhà cung cấp và Mặt hàng được chọn trong giao dịch đó đều khớp với thông tin đã được thiết lập trong danh mục Mặt hàng.

<img alt="Supplier Item Code in transaction" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/supplier-item-code-in-purchase-order.png">