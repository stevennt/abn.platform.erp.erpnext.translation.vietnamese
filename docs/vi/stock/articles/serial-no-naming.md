<!-- add-breadcrumbs -->
#Đặt tên Số serial

Số serial là giá trị duy nhất được gán cho mỗi đơn vị của một mặt hàng. Số serial giúp theo dõi chi tiết bảo hành và hạn sử dụng của mặt hàng. Thông thường, các mặt hàng có giá trị cao như máy móc, máy tính, thiết bị đắt tiền sẽ được quản lý theo số serial.

Để thiết lập mặt hàng là có quản lý theo số serial, trong danh mục Mặt hàng, hãy tích chọn **Has Serial No**.

Có hai cách để số serial có thể được tạo trong ERPNext.

###1. Quản lý số serial cho hàng mua về

Nếu các mặt hàng mua về đã được nhà sản xuất gốc (OEM) áp số serial, bạn có thể sử dụng chính số serial đó trong ERPNext. Khi tạo Phiếu nhập hàng, bạn sẽ quét mã hoặc nhập thủ công các số serial cho một mặt hàng. Khi Xác nhận Phiếu nhập hàng, các Số serial sẽ được tạo ở hệ thống phía sau dựa trên các Số serial đã cung cấp cho mặt hàng đó. Nếu sử dụng số serial của OEM, thì trong danh mục Mặt hàng, không nên điền Tiền tố (Prefix) cho việc quản lý số serial. Trong trường hợp này, trường Prefix nên được để trống.

Nếu các mặt hàng nhận về đã có mã vạch số serial, bạn chỉ cần quét mã vạch đó để nhập Số serial vào Phiếu nhập hàng. Nhấp [vào đây](https://frappe.io/blog/management/using-barcodes-to-ease-data-entry) để tìm hiểu thêm về vấn đề này.

Khi Xác nhận Phiếu nhập hàng hoặc Phiếu kho cho mặt hàng có quản lý số serial, các Số serial sẽ được tự động tạo.

<img alt="Serial Nos Entry" class="screenshot" src="{{docs_base_url}}/v13/assets/img/articles/serial-naming-1.png">

Các số serial đã tạo sẽ được cập nhật cho từng mặt hàng.

<img alt="Serial Nos Created" class="screenshot" src="{{docs_base_url}}/v13/assets/img/articles/serial-naming-2.png">

###2. Quản lý số serial cho hàng sản xuất

Để quản lý số serial cho hàng sản xuất, bạn có thể định nghĩa Chuỗi (Series) để tạo Số serial ngay trong danh mục Mặt hàng. Theo chuỗi đó, hệ thống sẽ tạo các Số serial cho Mặt hàng khi có bút toán sản xuất được thực hiện.

####2.1 Chuỗi Số serial

Khi Mặt hàng được thiết lập là có quản lý số serial, hệ thống sẽ cho phép bạn điền Chuỗi (Series) cho mặt hàng đó.

<img alt="Serial Nos Created" class="screenshot" src="{{docs_base_url}}/v13/assets/img/articles/serial-naming-3.png">

####2.2 Bút toán sản xuất cho mặt hàng có quản lý số serial

Khi Xác nhận bút toán sản xuất cho mặt hàng sản xuất, hệ thống sẽ tự động tạo các Số serial theo Chuỗi đã được chỉ định trong danh mục Mặt hàng.

<img alt="Serial Nos Created" class="screenshot" src="{{docs_base_url}}/v13/assets/img/articles/serial-naming-4.png">

<!-- markdown -->