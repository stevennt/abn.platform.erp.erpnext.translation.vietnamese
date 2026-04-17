<!-- add-breadcrumbs -->
# Giao dịch ngân hàng

Biểu mẫu này hiển thị các giao dịch ngân hàng trong ERPNext.

## 1. Điều kiện tiên quyết
Trước khi sử dụng Nhập giao dịch ngân hàng, bạn nên tạo các mục sau trước:

1. [Ngân hàng](/docs/v13/user/manual/en/accounts/bank)
1. [Tài khoản ngân hàng](/docs/v13/user/manual/en/accounts/bank-account)

## 2. Cách sử dụng Giao dịch ngân hàng
Một Nhập giao dịch ngân hàng không nhằm mục đích được tạo thủ công. Nó được tạo tự động bằng cách sử dụng:

1. [Đối chiếu ngân hàng](/docs/v13/user/manual/en/accounts/bank-reconciliation)
    Hoặc
1. [Tích hợp Plaid](/docs/v13/user/manual/en/erpnext_integration/plaid_integration) để đồng bộ hóa với các Ngân hàng

### 2.1 Các trường bổ sung trong Giao dịch ngân hàng

* Ngày
* Trạng thái:
    * Đang chờ xử lý
    * Đã quyết toán
    * Chưa đối chiếu
    * Đã đối chiếu
* **Tài khoản ngân hàng**: Tài khoản ngân hàng mà các giao dịch được thực hiện.

## 3. Tính năng/Trường

> Các trường này được cập nhật thông qua Đối chiếu ngân hàng và không nhằm mục đích sửa đổi tại đây.

### 3.1 Tiền tệ và nợ/có

* **Nợ**: Số tiền ghi nợ.
* **Có**: Số tiền ghi có.
* **Tiền tệ**: Tiền tệ mà giao dịch được thực hiện.
* **Mô tả:** Mô tả cho sao kê.

### 3.2 Tham chiếu

**Số tham chiếu**: Số séc hoặc số tham chiếu khác.

### 3.3 Bút toán thanh toán

* **Chứng từ thanh toán**: Chứng từ mà giao dịch được thực hiện, có thể là Hóa đơn bán hàng, Yêu cầu thanh toán chi phí, Hóa đơn mua hàng, Bút toán thanh toán, hoặc Bút toán.
* **Bút toán thanh toán**: Giao dịch cụ thể.
* **Số tiền phân bổ**: Số tiền được phân bổ cho giao dịch cụ thể này.

**Số tiền phân bổ**: Tổng số tiền đã phân bổ.
**Số tiền chưa phân bổ**: Tổng số tiền chưa phân bổ.