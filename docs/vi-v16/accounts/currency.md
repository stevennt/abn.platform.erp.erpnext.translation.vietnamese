<!-- add-breadcrumbs -->
# Tiền tệ

Trong ERPNext, danh sách Tiền tệ lưu trữ giá trị tiền tệ, ký hiệu và đơn vị phân số của nó. Hầu hết các loại tiền tệ thông dụng đã có sẵn trong ERPNext. Tỷ giá hối đoái được tự động lấy theo tỷ giá thị trường hiện tại. Bạn cũng có thể cấu hình hệ thống để sử dụng các tỷ giá hối đoái cố định cũ hơn bằng cách tạo chúng trong biểu mẫu [Currency Exchange](currency-exchange.md).

Với phiên bản v16, việc quản lý đa tiền tệ được tối ưu hóa để hỗ trợ các báo cáo tài chính hợp nhất và các nghiệp vụ kế toán định kỳ phức tạp hơn.

Để truy cập danh sách Tiền tệ, hãy đi đến:
> Home > Accounting > Multi Currency > Currency

Ví dụ, đây là trang Tiền tệ cho đồng Euro:

![Currency](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/currency.png)

## Các tính năng mới trong v16 liên quan đến Tài chính & Tiền tệ

Trong phiên bản v16, các tính năng kế toán được nâng cấp mạnh mẽ để hỗ trợ quản lý dòng tiền và báo cáo chính xác hơn:

*   **Financial Report Templates (Mẫu báo cáo tài chính):** Cho phép tùy chỉnh cấu trúc báo cáo để phù hợp với các yêu cầu đặc thù của từng loại tiền tệ hoặc quốc gia.
*   **Consolidated Trial Balance (Bảng cân đối thử hợp nhất):** Hỗ trợ tổng hợp dữ liệu từ nhiều công ty hoặc nhiều loại tiền tệ khác nhau vào một bảng cân đối duy nhất.
*   **COGS tách Service Expenses (Giá vốn hàng bán tách chi phí dịch vụ):** Cải tiến cách tính toán giá vốn, cho phép tách biệt rõ ràng giữa giá vốn hàng hóa và chi phí dịch vụ để báo cáo lợi nhuận chính xác hơn.
*   **Ledger Preview trước khi Xác nhận (Submit):** Cho phép người dùng xem trước các [Bút toán](je.md) sẽ được tạo ra trước khi thực hiện lệnh [Xác nhận](submit.md), giúp giảm thiểu sai sót trong hạch toán đa tiền tệ.
*   **Automatic Closing Stock (Tự động tính giá trị tồn kho cuối kỳ):** Hệ thống tự động cập nhật giá trị [Tồn kho](stock.md) dựa trên các nghiệp vụ [Phiếu nhập hàng](pr.md) và [Phiếu kho](se.md) đã được [Xác nhận](submit.md).
*   **Periodic Accounting (Kế toán định kỳ):** Hỗ trợ các nghiệp vụ điều chỉnh tỷ giá và kết chuyển cuối kỳ một cách tự động theo chu kỳ.

## Các chủ đề liên quan
1. [Exchange Rate Revaluation](exchange-rate-revaluation.md)
2. [Multi Currency Accounting](multi-currency-accounting.md)
3. [Currency Exchange](currency-exchange.md)

{next}