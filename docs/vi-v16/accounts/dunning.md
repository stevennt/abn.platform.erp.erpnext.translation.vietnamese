<!-- add-breadcrumbs -->
# Đôn đốc nợ

**Một chứng từ được gửi đi như một yêu cầu thanh toán nợ liên tục.**

Đôn đốc nợ là một chứng từ dùng để lưu trữ và gửi đi như một yêu cầu thanh toán nợ liên tục đối với một Hóa đơn bán hàng chưa thanh toán.

Để truy cập danh sách Đôn đốc nợ, hãy đi tới:
> Home > Accounting > Dunning

## 1. Điều kiện tiên quyết
Trước khi tạo Đôn đốc nợ, phải có một Hóa đơn bán hàng vì chứng từ này được tạo dựa trên hóa đơn đó.

* [Sales Invoice](sales-invoice.md)

## 2. Cách tạo Đôn đốc nợ
Một bản Đôn đốc nợ được tạo dựa trên một Hóa đơn bán hàng.

Để tạo thủ công, hãy làm theo các bước sau:

1. Đi tới danh sách Đôn đốc nợ và nhấn **New**.
1. Chọn một Hóa đơn bán hàng đã quá hạn.
1. Thiết lập Loại đôn đốc (Dunning Type) trong trường liên kết loại đôn đốc.
1. Thiết lập cài đặt in cho mẫu in của thư Đôn đốc nợ.
1. Ngày và giờ hạch toán sẽ được đặt theo thời gian hiện tại, bạn có thể chỉnh sửa sau khi tích vào ô kiểm bên dưới Posting Time để tạo một bút toán lùi ngày.
1. **Lưu** và **Xác nhận**.

 ![Dunning example](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/new-dunning.png)

### 2.1 Loại đôn đốc (Dunning Type) là gì?
Loại đôn đốc lưu trữ các giá trị mặc định cho số ngày quá hạn, phí đôn đốc, lãi suất và các khối văn bản sẽ được đưa vào. Ví dụ, Loại đôn đốc "Thông báo lần 1" sẽ không có bất kỳ khoản phí nào, nhưng Loại đôn đốc "Thông báo lần 2" sẽ có phí đôn đốc và lãi suất tính trên số tiền còn nợ.

 ![Dunning Type](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/dunning-document-type.png)

### 2.2 Trạng thái

Đây là các trạng thái được tự động gán cho Đôn đốc nợ.

* **Draft**: Bản nháp đã được **Lưu** nhưng chưa được **Xác nhận**.
* **Unresolved**: Đôn đốc nợ ở trạng thái chưa giải quyết khi nó đã được **Xác nhận** nhưng chưa nhận được thanh toán.
* **Resolved**: Đôn đốc nợ được giải quyết khi khoản thanh toán còn thiếu đã được nhận.
* **Cancelled**: Trạng thái **Hủy** là một chứng từ Đôn đốc nợ đã bị **Hủy**.

## 3. Thanh toán

Một [Payment Entry](payment-entry.md) có thể được tạo từ Đôn đốc nợ. Thông tin sẽ được lấy cùng với các chi tiết của Hóa đơn bán hàng mà nó đối chiếu.

![Dunning Payment](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/dunning-payment-entry.png)

## 4. Các chủ đề liên quan
1. [Payment Entry](payment-entry.md)
1. [Sales Invoice](sales-invoice.md)

{next}