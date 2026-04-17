---
title: Shipment
show_sidebar: 0

metatags:
 description: Shipment là một chứng từ dùng để theo dõi các lô hàng thực tế được tạo dựa trên Phiếu giao hàng hoặc được tạo độc lập. Điều này đặc biệt hữu ích cho các đơn vị vận chuyển muốn theo dõi tất cả thông tin lô hàng như Số vận đơn (AWB Number), Trạng thái lô hàng, Đơn vị vận chuyển, v.v. trong ERPNext.
 keywords: Shipment, Shipping, frappe, Delivery, erpnext new features, erp, open source erp, free erp, stock
---

<!-- add-breadcrumbs -->
# Shipment

**Shipment là một chứng từ dùng để theo dõi các lô hàng thực tế được tạo dựa trên Phiếu giao hàng hoặc được tạo độc lập.**

> Được giới thiệu trong phiên bản 13

Shipment đặc biệt hữu ích cho các đơn vị vận chuyển muốn theo dõi tất cả thông tin lô hàng như Số vận đơn (AWB Number), Trạng thái lô hàng, Đơn vị vận chuyển, v.v. trong ERPNext.

Để truy cập danh sách Shipment, hãy đi tới:
> Home > Stock > Stock Transactions > Shipment

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Shipment, bạn nên tạo các thông tin sau trước:

* Công ty và [Địa chỉ](https://docs.erpnext.com/docs/v13/user/manual/en/CRM/address) của Khách hàng đã được thiết lập Mã bưu điện, Địa chỉ Email và Số điện thoại.
* [Liên hệ](https://docs.erpnext.com/docs/v13/user/manual/en/CRM/contact) của Khách hàng.

## 2. Cách tạo Shipment
Shipment có thể được tạo thủ công hoặc từ Phiếu giao hàng:

### 2.1. Shipment thủ công
Để tạo Shipment thủ công, hãy làm theo các bước sau:

1. Đi tới danh sách Shipment, nhấn vào New.

 <img class="screenshot" alt="Unsaved Shipment" src="https://docs.erpnext.com/docs/v13/assets/img/stock/unsaved-shipment.png">
1. Chọn một tùy chọn trong trường **Pickup from**. Sau khi chọn một trong ba tùy chọn, bạn sẽ được yêu cầu chọn Công ty/Nhà cung cấp/Khách hàng dựa trên lựa chọn của mình.
1. Nếu bạn chọn 'Company' trong trường **Pickup from**, cùng với Địa chỉ, bạn cũng phải chọn một **Pickup Contact Person** (Người liên hệ lấy hàng), người này phải là một người dùng trong tổ chức của bạn trong ERPNext. Hãy đảm bảo Họ, Địa chỉ Email và Số điện thoại đã được thiết lập cho người dùng này.
1. Bạn cũng có thể điền phần **Delivery To** (Giao đến) tương tự.
1. Thêm Thông tin kiện hàng trong bảng **Shipment Parcel**.
1. Điền Giá trị hàng hóa.
1. Chọn Ngày lấy hàng.
1. Thêm Mô tả nội dung trong lô hàng này.
1. Bạn có thể tùy chọn điền phần Shipment Information nếu bạn đang theo dõi các lô hàng một cách thủ công.
1. Lưu và Xác nhận.

 <img class="screenshot" alt="Submitted Shipment" src="https://docs.erpnext.com/docs/v13/assets/img/stock/shipment-submitted.png">

### 2.1. Shipment từ Phiếu giao hàng
Để tạo Shipment từ Phiếu giao hàng:

1. Nhấp vào **Create** > **Shipment** trong Phiếu giao hàng.

 <img class="screenshot" alt="Submitted Shipment" src="https://docs.erpnext.com/docs/v13/assets/img/stock/shipment-from-delivery-note.png">

1. Điền biểu mẫu như đã đề cập ở phần trước.

## 3. Các tính năng

### 3.1. Shipment Parcel (Kiện hàng)

Bạn có thể chỉ định chiều dài, chiều rộng, chiều cao và trọng lượng của một kiện hàng trong Shipment. Nếu có nhiều kiện hàng có kích thước giống nhau, trường **count** (số lượng) có thể được thiết lập tương ứng.

Để tự động lấy các kích thước kiện hàng thường xuyên sử dụng, một Mẫu kiện hàng (Parcel Template) có thể được tạo và thiết lập trong trường **Parcel Template**. Sau khi thêm mẫu, hãy nhấp vào nút **Add template**.

 <img class="screenshot" alt="Submitted Shipment" src="https://docs.erpnext.com/docs/v13/assets/img/stock/shipment-parcel.png">

### 3.2. Shipment Information / Details (Thông tin / Chi tiết lô hàng)
Phần Shipment Information là một phần **tùy chọn**, nơi người dùng có thể theo dõi thông tin lô hàng một cách thủ công. Dưới đây là một số trường:

1. **Service Provider** (tùy chọn): Nhà cung cấp dịch vụ có thể là một dịch vụ bên thứ ba cung cấp các dịch vụ vận chuyển từ nhiều đơn vị vận chuyển khác nhau.
1. **Shipment ID**: ID lô hàng duy nhất trên nền tảng vận chuyển của bạn.
1. **Shipment Amount**: Tổng chi phí phát sinh cho lô hàng.
1. **Carrier**: Đơn vị vận chuyển xử lý và giao lô hàng của bạn.
1. **Carrier Service** (tùy chọn): Loại/danh mục dịch vụ được cung cấp bởi đơn vị vận chuyển. Ví dụ: một số đơn vị vận chuyển có các danh mục như Tiết kiệm (Economy), Hỏa tốc (Express), v.v.
1. **AWB Number**: Một vận đơn hàng không (AWB) đi kèm với hàng hóa hàng không **quốc tế**. Nó thường có một **Số vận đơn (AWB Number)** duy nhất, giúp dễ dàng nhận diện và theo dõi đơn vị chuyển phát hàng không.
1. **Incoterm**: Đây là một bộ các quy tắc được quốc tế công nhận nhằm xác định trách nhiệm của người bán và người mua. [Tìm hiểu thêm về nó tại đây.](https://iccwbo.org/resources-for-business/incoterms-rules/incoterms-2020/)

### 3.3. Tự động hóa

Bạn cũng có thể tự động hóa việc so sánh giá cước, tạo nhãn, theo dõi, v.v. bằng cách sử dụng [Tích hợp vận chuyển](https://docs.erpnext.com/docs/v13/user/manual/en/erpnext_integration/erpnext_shipping) của chúng tôi.

### 4. Các chủ đề liên quan
1. [Phiếu giao hàng](delivery-note.md)
1. [Phiếu đóng gói](packing-slip.md)