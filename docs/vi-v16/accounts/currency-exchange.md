<!-- add-breadcrumbs -->
# Tỷ giá hối đoái

Biểu mẫu Tỷ giá hối đoái trong ERPNext lưu trữ các tỷ giá hối đoái được Người dùng lưu trữ thủ công. Theo mặc định, ERPNext tự động lấy tỷ giá hối đoái hiện tại cho các loại tiền tệ theo thị trường. Tuy nhiên, bạn có thể lưu trữ các tỷ giá hối đoái cố định và sử dụng chúng. Bạn cần bật 'Allow Stale Exchange Rates' trong Cài đặt kế toán (Accounts Settings) để sử dụng các tỷ giá hối đoái được lưu trữ trong biểu mẫu Tỷ giá hối đoái.

Để truy cập danh sách Tỷ giá hối đoái, hãy đi đến:
> Trang chủ > Kế toán > Đa tiền tệ > Tỷ giá hối đoái

## 1. Cách tạo Tỷ giá hối đoái
1. Đi đến danh sách Tỷ giá hối đoái và nhấn vào Mới.
1. Nhập ngày mà từ đó tỷ giá hối đoái này có hiệu lực. Các biểu mẫu Tỷ giá hối đoái mới được Lưu với ngày mới hơn sẽ được sử dụng trong các giao dịch.
1. Thiết lập tiền tệ Từ (From) và Đến (To).
1. Nhập Tỷ giá hối đoái, ví dụ: 1 USD = 25.000 VND.
1. Chọn xem tỷ giá hối đoái áp dụng cho giao dịch bán, mua, hoặc cả hai.
1. Lưu.

    ![Currency Exchange](https://docs.erpnext.com/docs/v16/assets/img/accounts/currency-exchange.png)

## 2. Các tính năng mới trong v16 (Liên quan đến Kế toán)
Trong phiên bản v16, các tính năng kế toán được nâng cấp mạnh mẽ để hỗ trợ quản lý tài chính phức tạp hơn:
* **Financial Report Templates**: Tùy chỉnh mẫu báo cáo tài chính linh hoạt hơn.
* **Consolidated Trial Balance**: Bảng cân đối thử hợp nhất cho các doanh nghiệp có nhiều công ty con.
* **COGS tách Service Expenses**: Giá vốn hàng bán (COGS) được phân tách rõ ràng với chi phí dịch vụ để báo cáo chính xác hơn.
* **Ledger Preview trước Submit**: Cho phép xem trước các bút toán (JE) trước khi thực hiện Xác nhận (Submit) để tránh sai sót.
* **Automatic Closing Stock**: Tự động tính toán và kết chuyển giá trị tồn kho (Stock) cuối kỳ.
* **Periodic Accounting**: Hỗ trợ các phương pháp kế toán định kỳ.

## 3. Các chủ đề liên quan
1. [Đánh giá lại tỷ giá hối đoái](exchange-rate-revaluation.md)
1. [Kế toán đa tiền tệ](multi-currency-accounting.md)

{next}