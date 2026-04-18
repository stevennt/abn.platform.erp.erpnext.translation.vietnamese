<!-- add-breadcrumbs -->
# Tỷ giá hối đoái

Biểu mẫu Tỷ giá hối đoái trong ERPNext lưu trữ các tỷ giá hối đoái được Người dùng lưu trữ thủ công. Theo mặc định, ERPNext tự động lấy tỷ giá hối đoái hiện tại cho các loại tiền tệ theo thị trường. Tuy nhiên, bạn có thể lưu trữ các tỷ giá hối đoái cố định và sử dụng chúng. Bạn cần bật 'Allow Stale Exchange Rates' trong Cài đặt kế toán (Accounts Settings) để sử dụng các tỷ giá hối đoái được lưu trữ trong biểu mẫu Tỷ giá hối đoái.

Để truy cập danh sách Tỷ giá hối đoái, hãy đi đến:
> Trang chủ > Kế toán > Đa tiền tệ > Tỷ giá hối đoái

## 1. Cách tạo Tỷ giá hối đoái
1. Đi đến danh sách Tỷ giá hối đoái và nhấn vào Mới.
1. Nhập ngày mà từ đó tỷ giá hối đoái này có hiệu lực. Các biểu mẫu Tỷ giá hối đoái mới được Lưu với ngày mới hơn sẽ được sử dụng trong các giao dịch.
1. Thiết lập tiền tệ Từ (From) và Đến (To).
1. Nhập Tỷ giá hối đoái, ví dụ: 1 USD = 65 INR.
1. Chọn xem tỷ giá hối đoái áp dụng cho giao dịch bán, mua, hoặc cả hai.
1. Lưu.

    ![Currency Exchange](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/currency-exchange.png)

## 2. Các chủ đề liên quan
1. [Đánh giá lại tỷ giá hối đoái](exchange-rate-revaluation.md)
1. [Kế toán đa tiền tệ](multi-currency-accounting.md)

{next}