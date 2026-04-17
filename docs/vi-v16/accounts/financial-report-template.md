# Mẫu báo cáo tài chính (Financial Report Template)

![Mẫu báo cáo tài chính](../../screenshots/reports/trial-balance.png)

## 1. Giới thiệu tính năng
**[Mới trong v16]** 

Tính năng **Mẫu báo cáo tài chính (Financial Report Template)** cung cấp khả năng tùy biến chuyên sâu cho các báo cáo kế toán cốt lõi như Báo cáo Kết quả hoạt động kinh doanh (P&L) và Bảng cân đối kế toán (Balance Sheet). Thay vì sử dụng các báo cáo mặc định, người dùng có thể tự xây dựng cấu trúc báo cáo theo nhu cầu riêng biệt, hỗ trợ đầy đủ các tiêu chuẩn kế toán quốc tế như **IFRS**, quản lý đa công ty (**multi-company**) và đặc biệt là khả năng sử dụng công thức toán học để tính toán các chỉ số tài chính ngay trong báo cáo.

## 2. Điều kiện tiên quyết
Để sử dụng tính năng này, bạn cần có các quyền và dữ liệu sau:
* Quyền truy cập vào module **Kế toán (Accounting)**.
* Đã thiết lập hệ thống **Sổ cái (General Ledger)** và các **Tài khoản (Account)** cơ bản.
* Có kiến thức về cấu trúc sơ đồ tài khoản để phân loại các dòng báo cáo.

## 3. Hướng dẫn từng bước

### Bước 1: Tạo Mẫu báo cáo mới
1. Truy cập vào thanh tìm kiếm, nhập **Financial Report Template** và chọn tài liệu này.
2. Nhấn nút **Thêm mẫu báo cáo mới (New Financial Report Template)**.
3. Nhập **Tên mẫu báo cáo** (Ví dụ: *Báo cáo P&L theo IFRS*).
4. Chọn **Loại báo cáo** (Ví dụ: *Profit and Loss Statement* hoặc *Balance Sheet*).

### Bước 2: Thiết lập cấu trúc dòng (Rows) và cột (Columns)
1. Tại mục **Cấu trúc báo cáo**, bạn sẽ thấy danh sách các dòng.
2. **Thêm dòng (Add Row):** Nhấn nút để thêm một dòng mới đại diện cho một chỉ tiêu tài chính (Ví dụ: *Doanh thu thuần*, *Giá vốn hàng bán*, *Lợi nhuận gộp*).
3. **Gán tài khoản:** Với mỗi dòng, bạn có thể chọn một hoặc nhiều tài khoản từ Sơ đồ tài khoản để hệ thống tự động lấy dữ liệu.
4. **Sử dụng công thức (Formula):** 
    * Để tính toán các dòng tổng hợp (như Lợi nhuận gộp), hãy chọn loại dòng là **Formula**.
    * Nhập công thức dựa trên tên của các dòng phía trên. 
    * *Ví dụ:* Nếu dòng "Doanh thu" có tên là `Revenue` và "Giá vốn" là `COGS`, bạn có thể nhập công thức: `Revenue - COGS`.

### Bước 3: Cấu hình đa công ty và bộ lọc
1. Nếu bạn làm việc trong môi trường đa công ty, hãy chọn **Company** cụ thể hoặc để trống để áp dụng cho tất cả các công ty trong cùng một nhóm.
2. Thiết lập các bộ lọc mặc định như **Kỳ báo cáo (Period)** hoặc **Phân khúc (Segment)**.

### Bước 4: Lưu và Sử dụng
1. Nhấn **Lưu (Save)** để hoàn tất thiết lập.
2. Để xem báo cáo, truy cập vào báo cáo tài chính tương ứng, chọn **Mẫu báo cáo (Report Template)** đã tạo và nhấn **Xem (Show)**.

## 4. Các tùy chọn/cài đặt liên quan
* **Include Group Totals:** Tự động tính tổng cho các nhóm dòng được phân cấp.
* **Drill Down:** Cho phép nhấn trực tiếp vào một con số trên báo cáo để xem các **Bút toán (JE)** chi tiết cấu thành nên con số đó.
* **Custom Columns:** Cho phép tạo các cột so sánh (Ví dụ: Cột năm nay so với năm trước).

## 5. Lưu ý quan trọng
* **Độ chính xác của công thức:** Khi sử dụng công thức, hãy đảm bảo tên các dòng (Row Name) được viết chính xác tuyệt đối để tránh lỗi tính toán.
* **Phân cấp dòng:** Việc sử dụng các dòng con (Child Rows) giúp báo cáo gọn gàng hơn, nhưng cần kiểm soát kỹ việc cộng dồn dữ liệu để tránh trùng lặp số liệu.
* **Sao lưu cấu hình:** Trước khi thay đổi cấu trúc của các mẫu báo cáo mặc định của hệ thống, hãy tạo một bản sao (Duplicate) để làm mẫu mới.

## 6. Liên kết đến trang liên quan
* [Sơ đồ tài khoản (Chart of Accounts)](chart-of-accounts.md)
* [Bút toán (Journal Entry)](journal-entry.md)
* [Báo cáo kết quả hoạt động kinh doanh (Profit and Loss)](profit-and-loss.md)
* [Bảng cân đối kế toán (Balance Sheet)](balance-sheet.md)