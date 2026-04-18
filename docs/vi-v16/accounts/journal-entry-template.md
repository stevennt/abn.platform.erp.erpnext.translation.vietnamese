<!-- add-breadcrumbs -->
# Mẫu Bút toán

**Mẫu Bút toán cho phép bạn thiết lập và lựa chọn một danh sách các tài khoản và tùy chọn đã được định sẵn khi thực hiện một Bút toán.**

Để truy cập Mẫu Bút toán, hãy đi đến:

> Home > Kế toán > Sổ cái > Mẫu Bút toán

## 1. Cách tạo và sử dụng Mẫu Bút toán:

![Journal Entry Template](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/journal-entry-template.png)

1. Đi đến Danh sách Mẫu Bút toán và nhấn vào **Mới**.
2. Thêm các chi tiết sau:
    * **Template Title**: Tên này sẽ được sử dụng để chọn mẫu từ Bút toán.
    * **Company**: Theo mặc định, công ty được định nghĩa trong Cấu hình chung sẽ được chọn. Bạn cũng có thể chọn bất kỳ công ty nào khác.
    * **Entry Type**: Bạn có thể chọn từ [các loại bút toán có sẵn trong Bút toán](journal-entry.md#3-journal-entry-types) tại đây. Giá trị mặc định là [Bút toán](journal-entry.md#31-journal-entry).
        * Có 3 'Entry Type' đặc biệt ở đây:
            * [Opening Entry](journal-entry.md#311-opening-entry): Loại này sẽ lấy tất cả các tài khoản và tải chúng vào bảng "Accounting Entries". Để tìm hiểu thêm, hãy truy cập trang [Số dư đầu kỳ](opening-balance.md).
            * [Bank Entry](journal-entry.md#33-bank-entry): Loại này sẽ lấy và tải Tài khoản Ngân hàng mặc định nếu đã được thiết lập.
            * [Cash Entry](journal-entry.md#34-cash-entry): Loại này sẽ lấy và tải Tài khoản Tiền mặt mặc định nếu đã được thiết lập.
    * **Is Opening**: Mục này sẽ tự động được đặt thành 'Yes' nếu 'Opening Entry' được chọn làm Entry Type.
    * **Series**: Bạn có thể chọn từ danh sách chuỗi đặt tên có sẵn cho Bút toán.
    * **Accounting Entries**: Tại đây bạn có thể chọn một danh sách các tài khoản để thêm vào bút toán.
3. **Lưu** và đi đến [Bút toán](journal-entry.md#1-how-to-create-a-journal-entry) và nhấn vào **Mới**.
4. Trong trường 'From Template', khi bạn chọn mẫu, nó sẽ tải các tài khoản và các tùy chọn khác đã được thiết lập trong đó. Lưu ý rằng hệ thống sẽ xóa sạch bảng Accounting Entries trước khi tải mẫu, nhưng bạn có thể thêm nhiều tài khoản khác vào bảng ngoài những tài khoản được lấy từ mẫu.

*Lưu ý trong phiên bản v16: Bạn có thể sử dụng tính năng **Xem trước Sổ cái (Ledger Preview)** để kiểm tra các bút toán trước khi thực hiện **Xác nhận (Submit)** nhằm đảm bảo tính chính xác của dữ liệu kế toán.*

![Creating Journal Entry From Template](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/create-journal-entry-from-template.gif)

## 2. Các tính năng nâng cao trong v16
Trong phiên bản v16, việc quản lý tài chính được tối ưu hóa với các tính năng:
* **Mẫu Báo cáo Tài chính (Financial Report Templates)**: Cho phép tùy chỉnh cấu trúc báo cáo linh hoạt hơn.
* **Bảng Cân đối Thử toán Hợp nhất (Consolidated Trial Balance)**: Xem dữ liệu tổng hợp từ nhiều công ty.
* **Tách chi phí dịch vụ khỏi Giá vốn hàng bán (COGS tách Service Expenses)**: Giúp báo cáo kết quả kinh doanh chi tiết hơn.
* **Tự động tính Giá trị tồn kho cuối kỳ (Automatic Closing Stock)**.
* **Kế toán định kỳ (Periodic Accounting)**.

## 3. Các chủ đề liên quan
1. [Bút toán](journal-entry.md)