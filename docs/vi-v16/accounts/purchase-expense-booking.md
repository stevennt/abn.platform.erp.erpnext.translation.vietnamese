# Ghi nhận chi phí mua hàng (Purchase Expense Booking)

**Chủ đề:** Purchase Expense Booking trong v16 - ghi nhận COGS và chi phí dịch vụ riêng biệt. Tách COGS khỏi service expenses cho P&L sạch hơn.

![Ghi nhận chi phí mua hàng](../../screenshots/accounts/purchase-invoice-new.png)

### 1. Giới thiệu tính năng <span style="color: #2ecc71;">(Mới trong v16)</span>

Trong phiên bản ERPNext v16, quy trình ghi nhận chi phí mua hàng đã được cải tiến để tối ưu hóa báo cáo Kết quả hoạt động kinh doanh (P&L). Tính năng mới cho phép người dùng tách biệt rõ ràng giữa **Giá vốn hàng bán (COGS)** và **Chi phí dịch vụ (Service Expenses)** ngay trong quá trình xử lý hóa đơn.

Việc tách biệt này giúp bộ phận kế toán có cái nhìn chính xác hơn về biên lợi nhuận gộp bằng cách không trộn lẫn các chi phí vận hành/dịch vụ vào giá trị nhập kho của mặt hàng, từ đó giúp báo cáo P&L trở nên "sạch" và minh bạch hơn.

### 2. Điều kiện tiên quyết

Để thực hiện ghi nhận chi phí mua hàng một cách chính xác, bạn cần đảm bảo các điều kiện sau:
* Đã thiết lập danh mục **Nhà cung cấp (Supplier)**.
* Đã thiết lập danh mục **Mặt hàng (Item)** và **Tài khoản kế toán** liên quan.
* Đã có **Đơn mua hàng (PO)** hoặc **Phiếu nhập hàng (PR)** được tạo trước đó (nếu mua hàng có kho).
* Tài khoản chi phí (Expense Account) đã được cấu hình trong danh mục Mặt hàng hoặc trong Hóa đơn.

### 3. Hướng dẫn từng bước

Để ghi nhận chi phí mua hàng và tách biệt COGS/Service Expenses, hãy thực hiện theo các bước sau:

1. **Truy cập Hóa đơn:** Đi đến module **Mua hàng (Buying)** > **Hóa đơn (Invoice)** > **Hóa đơn mua hàng (Purchase Invoice)**.
2. **Tạo mới/Liên kết đơn hàng:** Nhấn **Thêm mới (New)** hoặc chọn **Liên kết (Get from)** từ **Đơn mua hàng (PO)** đã được **Xác nhận (Submit)** trước đó.
3. **Phân loại dòng chi phí:**
    * **Đối với hàng hóa (COGS):** Tại bảng chi tiết, chọn **Mặt hàng (Item)** cần mua. Hệ thống sẽ tự động tính toán giá trị dựa trên số lượng và giá mua để ghi nhận vào kho và giá vốn.
    * **Đối với chi phí dịch vụ (Service Expenses):** Thay vì chọn Mặt hàng, hãy chọn loại là "Service" hoặc chọn trực tiếp tài khoản chi phí tại cột **Tài khoản (Account)**. Nhập mô tả dịch vụ (ví dụ: Phí vận chuyển, Phí lắp đặt) và số tiền tương ứng.
4. **Kiểm tra hạch toán:** Kiểm tra tab **Bút toán (Journal Entry)** để đảm bảo các dòng nợ/có được phân bổ đúng vào tài khoản Kho/Giá vốn và tài khoản Chi phí dịch vụ riêng biệt.
5. **Lưu và Xác nhận:** Nhấn **Lưu (Save)** để kiểm tra dữ liệu, sau đó nhấn **Xác nhận (Submit)** để hoàn tất ghi nhận vào sổ cái.

### 4. Ảnh minh họa

*(Vui lòng xem hình ảnh minh họa cách phân bổ dòng hàng hóa và dòng chi phí dịch vụ tại giao diện Hóa đơn)*

![Giao diện Hóa đơn mua hàng](../../screenshots/accounts/purchase-invoice-new.png)

### 5. Các tùy chọn/cài đặt liên quan

* **Tài khoản chi phí (Expense Account):** Được thiết lập trong danh mục Mặt hàng hoặc trực tiếp trên dòng Hóa đơn.
* **Thuế (Tax):** Các thiết lập thuế sẽ được áp dụng dựa trên loại mặt hàng hoặc dịch vụ được chọn.
* **Tự động hạch toán (Auto Accounting):** Cấu hình trong bộ phận Kế toán để quyết định cách hệ thống tự động tạo **Bút toán (JE)** khi **Xác nhận (Submit)** hóa đơn.

### 6. Lưu ý quan trọng

* **Độ chính xác của P&L:** Nếu bạn nhập chi phí dịch vụ (như vận chuyển) trực tiếp vào giá của Mặt hàng, chi phí này sẽ được vốn hóa vào giá trị **Tồn kho (Stock)**. Nếu muốn tách riêng để theo dõi chi phí vận hành, hãy nhập thành một dòng dịch vụ riêng biệt.
* **Kiểm tra Kho:** Khi mua hàng, hãy đảm bảo số lượng trên **Phiếu nhập hàng (PR)** khớp với **Hóa đơn (Invoice)** để tránh sai lệch **Tồn kho (Stock)** và giá trị kho.
* **Hủy giao dịch:** Nếu phát hiện sai sót sau khi đã **Xác nhận (Submit)**, bạn phải thực hiện **Hủy (Cancel)** hóa đơn trước khi có thể chỉnh sửa hoặc tạo hóa đơn điều chỉnh.

### 7. Liên kết đến trang liên quan

* [Quy trình Mua hàng (Buying Process)](buying_process.md)
* [Quản lý Kho và Tồn kho (Stock Management)](stock_management.md)
* [Quản lý Tài khoản và Bút toán (Accounts & Journal Entry)](accounts_je.md)
* [Quản lý Nhà cung cấp (Supplier Management)](supplier_management.md)