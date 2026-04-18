<!-- add-breadcrumbs -->
# Thông báo Xác nhận Tài khoản Làm tròn

**Câu hỏi**

Khi Xác nhận một hóa đơn, tại sao hệ thống lại yêu cầu Tài khoản Làm tròn? Làm thế nào để cập nhật nó?

![Round off Account in Purchase Invoice](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/round-off-message-in-purchase-invoice.png)

**Trả lời**

Trong Hóa đơn mua hàng, Tổng cộng được tính toán dựa trên nhiều phép tính khác nhau như:

- Số lượng * Đơn giá = Số tiền
- Thuế và các khoản phí khác áp dụng cho từng mặt hàng
- Chiết khấu áp dụng cho một số hoặc tất cả các mặt hàng
- Nhân với tỷ giá hối đoái, trong trường hợp sử dụng đa tiền tệ

Do kết quả của nhiều phép tính, có thể xảy ra một chút chênh lệch làm tròn trong số tiền cuối cùng. Khoản chênh lệch làm tròn này thường rất nhỏ, ví dụ như 0.034. Tuy nhiên, để đảm bảo tính chính xác trong kế toán, khoản này cần phải được hạch toán vào các tài khoản. Do đó, bạn cần xác định một tài khoản Làm tròn mặc định trong danh mục Công ty, nơi mà số tiền phát sinh do chênh lệch làm tròn có thể được ghi nhận.

Bạn cần tạo Tài khoản Làm tròn trong Hệ thống tài khoản và cập nhật vào danh mục Công ty. Các bước thực hiện như sau:

* Tài khoản > Hệ thống tài khoản
* Trong Hệ thống tài khoản, kiểm tra hoặc tạo Tài khoản mới dưới mục Chi phí > Chi phí trực tiếp. Bỏ qua nếu tài khoản cho mục đích này đã tồn tại
* Đi tới danh mục Công ty
  Tài khoản > Công ty
* Mở Công ty cần cập nhật tài khoản Làm tròn.
* Trong danh mục Công ty, cuộn đến phần Cài đặt tài khoản và chọn Tài khoản Làm tròn và Trung tâm chi phí.
    ![Round Off Account in Company](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/round-off-account-in-company.png)

Sau khi Tài khoản Làm tròn đã được cập nhật trong danh mục Công ty, hãy thử Xác nhận Hóa đơn mua hàng một lần nữa.

{next}