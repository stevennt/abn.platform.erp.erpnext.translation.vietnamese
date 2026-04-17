# Tự động đóng sổ kho (Automatic Closing Stock Posting)

**Mới trong v16**

Tính năng **Tự động đóng sổ kho (Automatic Closing Stock Posting)** trong ERPNext v16 cho phép hệ thống tự động tính toán và ghi nhận giá trị chênh lệch tồn kho vào sổ cái (General Ledger) vào cuối kỳ kế toán. Tính năng này giúp loại bỏ quy trình đóng sổ thủ công phức tạp, đảm bảo giá trị tồn kho trên Bảng cân đối kế toán luôn khớp với giá trị thực tế trong kho.

![Ảnh minh họa cài đặt tài khoản](../screenshots/accounts/accounts-settings.png)

---

### 1. Giới thiệu tính năng
Trước phiên bản v16, việc điều chỉnh giá trị tồn kho để khớp với sổ cái thường yêu cầu các bút toán điều chỉnh thủ công hoặc các quy trình kiểm kê phức tạp. Với tính năng mới này, khi bạn thực hiện khóa kỳ kế toán hoặc chạy tiến trình cuối kỳ, hệ thống sẽ tự động so sánh giá trị tồn kho hiện tại với tài khoản kho trên sổ cái và tạo **Bút toán (JE)** chênh lệch một cách chính xác.

### 2. Điều kiện tiên quyết
Để sử dụng tính năng này, hệ thống của bạn cần đáp ứng các điều kiện sau:
* Đã thiết lập danh mục **Mặt hàng (Item)** với phương pháp tính giá tồn kho (FIFO hoặc Moving Average).
* Đã thiết lập các tài khoản kế toán liên quan trong **Thiết lập kho (Stock Settings)**.
* Đã thực hiện đầy đủ các giao dịch **Phiếu nhập hàng (PR)**, **Phiếu giao hàng (DN)** và **Phiếu kho (SE)**.

### 3. Hướng dẫn từng bước

Để kích hoạt tính năng tự động đóng sổ kho, hãy làm theo các bước sau:

1. Truy cập vào module **Kế toán (Accounting)**.
2. Tìm kiếm và chọn **Thiết lập tài khoản (Accounts Settings)**.
3. Cuộn xuống phần **Quản lý tồn kho (Stock Management)**.
4. Tích chọn vào ô **Tự động đóng sổ kho (Automatic Closing Stock Posting)**.
5. Nhấn **Lưu (Save)** để hoàn tất cấu hình.
6. Vào cuối kỳ kế toán, khi bạn thực hiện **Khóa kỳ (Period Closing)**, hệ thống sẽ tự động quét các biến động **Tồn kho (Stock)** và tạo **Bút toán (JE)** chênh lệch.

### 4. Các tùy chọn/cài đặt liên quan
* **Tài khoản chênh lệch giá kho (Stock Adjustment Account):** Tài khoản dùng để ghi nhận phần chênh lệch giữa giá trị kho thực tế và giá trị trên sổ cái.
* **Phương pháp tính giá (Valuation Method):** Ảnh hưởng trực tiếp đến cách hệ thống tính toán giá trị trước khi thực hiện đóng sổ.
* **Kiểm tra chất lượng (QI):** Nếu mặt hàng đang trong trạng thái chờ **Kiểm tra chất lượng (QI)**, giá trị này sẽ được xem xét trong quá trình tính toán tồn kho khả dụng.

### 5. Lưu ý quan trọng
* **Kiểm tra dữ liệu:** Trước khi để hệ thống tự động đóng sổ, hãy đảm bảo tất cả các **Đơn mua hàng (PO)** và **Đơn bán hàng (SO)** đã được **Xác nhận (Submit)** và các giao dịch kho đã được hoàn tất.
* **Đồng bộ hóa:** Nếu có sự sai lệch lớn giữa **Kho (Warehouse)** và sổ cái, hãy thực hiện kiểm kê và điều chỉnh **Lô hàng (Batch)** trước khi chạy tính năng đóng sổ.
* **Không thể hoàn tác tự động:** Một khi **Bút toán (JE)** chênh lệch đã được tạo, bạn không thể xóa trực tiếp mà phải thực hiện bút toán đảo hoặc hủy kỳ kế toán (nếu được phép).

### 6. Liên kết đến trang liên quan
* [Quản lý Tồn kho (Stock Management)](../stock/stock-management.md)
* [Thiết lập Kế toán (Accounting Setup)](../accounts/accounting-setup.md)
* [Hướng dẫn Kiểm kê Kho (Stock Reconciliation)](../stock/stock-reconciliation.md)