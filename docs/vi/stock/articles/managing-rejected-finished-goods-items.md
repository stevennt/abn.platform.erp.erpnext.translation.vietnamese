<!-- add-breadcrumbs -->
#Quản lý các Mặt hàng Thành phẩm bị Loại bỏ

Có thể có những Mặt hàng được sản xuất nhưng không vượt qua được kiểm tra chất lượng, do đó bị loại bỏ.

Quy trình sản xuất tiêu chuẩn trong ERPNext không bao gồm việc quản lý các mặt hàng bị loại bỏ. Vì vậy, bạn nên tạo phiếu nhập thành phẩm cho cả các mặt hàng được chấp nhận cũng như các mặt hàng bị loại bỏ. Bằng cách này, các mặt hàng bị loại bỏ cũng sẽ được ghi nhận là đã nhập vào kho thành phẩm.

Để chuyển các mặt hàng bị loại bỏ từ kho thành phẩm, bạn nên tạo một phiếu Phiếu kho (Material Transfer). Các bước dưới đây để tạo phiếu Phiếu kho.

####Bước 1: Phiếu kho mới

`Kho > Tài liệu > Phiếu kho > Mới`

####Bước 2: Mục đích

Mục đích = Chuyển kho (Material Transfer)

####Bước 3: Kho

Kho nguồn = Kho thành phẩm
Kho đích = Kho hàng lỗi/loại bỏ

####Bước 4: Mặt hàng

Chọn mặt hàng không vượt qua kiểm tra chất lượng, và nhập tổng số lượng mặt hàng bị loại bỏ vào ô Số lượng.

####Bước 5: Xác nhận Phiếu kho

Khi Lưu và Xác nhận Phiếu kho, tồn kho của các mặt hàng bị loại bỏ sẽ được chuyển từ Kho thành phẩm sang Kho hàng lỗi/loại bỏ.


<!-- markdown -->