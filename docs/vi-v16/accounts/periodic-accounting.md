# Kế toán theo kỳ (Periodic Accounting)

**Mới trong v16**

Tính năng **Kế toán theo kỳ (Periodic Accounting)** trong ERPNext v16 cho phép doanh nghiệp ghi nhận biến động Tồn kho (Nhập/Xuất) theo định kỳ thông qua Bút toán (Journal Entry) thay vì sử dụng phương pháp kê khai thường xuyên (Perpetual Inventory) tự động. Phương pháp này giúp đơn giản hóa quy trình kế toán, giảm tải khối lượng bút toán tự động, đặc biệt phù hợp cho các doanh nghiệp nhỏ hoặc các đơn vị có quy trình kiểm kê định kỳ.

## 1. Giới thiệu tính năng

Trong mô hình kế toán thông thường (Perpetual), mỗi khi có giao dịch Kho, hệ thống sẽ tự động tạo bút toán giá vốn. Với **Kế toán theo kỳ**, giá trị tồn kho và giá vốn hàng bán sẽ được cập nhật thủ công hoặc theo lô thông qua các Bút toán (Journal Entry) dựa trên kết quả kiểm kê hoặc giá trị nhập/xuất thực tế tại cuối kỳ.

## 2. Điều kiện tiên quyết

Trước khi thiết lập Kế toán theo kỳ, hãy đảm bảo các điều kiện sau đã được đáp ứng:
* Đã thiết lập danh mục **Mặt hàng (Item)** và **Kho (Warehouse)**.
* Đã thiết lập các tài khoản kế toán liên quan (Tài khoản kho, Tài khoản giá vốn).
* Đã hoàn tất cấu hình cơ bản về Hệ thống kế toán trong ERPNext.

## 3. Hướng dẫn từng bước

Để thực hiện ghi nhận giá trị tồn kho theo kỳ, hãy làm theo các bước sau:

1. **Tổng hợp dữ liệu tồn kho:** Truy xuất báo cáo Tồn kho để xác định giá trị nhập và xuất của các **Mặt hàng (Item)** trong kỳ.
2. **Tạo Bút toán (Journal Entry):** Truy cập vào module Kế toán và chọn **Tạo Bút toán (Journal Entry)** mới.
3. **Thiết lập dòng bút toán:**
    * Chọn loại Bút toán phù hợp.
    * Nhập tài khoản Kho (tăng/giảm tùy theo nghiệp vụ).
    * Nhập tài khoản Giá vốn hàng bán hoặc tài khoản điều chỉnh tương ứng.
    * Nhập số tiền dựa trên giá trị hàng nhập/xuất đã tổng hợp.
4. **Xác nhận:** Kiểm tra lại các dòng bút toán và nhấn **Lưu (Save)**, sau đó nhấn **Xác nhận (Submit)** để ghi nhận vào sổ cái.

![Minh họa giao diện Bút toán](../screenshots/accounts/journal-entry-new.png)

## 4. Các tùy chọn và cài đặt liên quan

* **Tài khoản kho (Stock Account):** Tài khoản phản ánh giá trị hàng hóa hiện có trong kho.
* **Tài khoản giá vốn (Cost of Goods Sold Account):** Tài khoản ghi nhận chi phí khi xuất kho.
* **Cấu hình Item:** Đảm bảo các thiết lập về thuế và giá bán trên **Mặt hàng (Item)** đã chính xác để việc tính toán giá trị thủ công không bị sai lệch.

## 5. Lưu ý quan trọng

* **Kiểm soát sai lệch:** Vì không ghi nhận tự động, doanh nghiệp cần thực hiện kiểm kê định kỳ để đảm bảo số dư trên **Bút toán (Journal Entry)** khớp với số lượng thực tế trong **Kho (Warehouse)**.
* **Không dùng cho kho tự động:** Nếu doanh nghiệp đang sử dụng các tính năng tự động hóa cao như sản xuất (Manufacturing) phức tạp, việc dùng Kế toán theo kỳ có thể gây khó khăn trong việc theo dõi giá thành tức thời.
* **Đối soát:** Luôn thực hiện đối soát giữa phiếu **Nhập hàng (PR)**, **Giao hàng (DN)** và các **Bút toán (JE)** cuối kỳ.

## 6. Liên kết đến trang liên quan

* [Quản lý Kho hàng (.md)](../../modules/stock/overview.md)
* [Quản lý Bút toán (.md)](../../modules/accounts/journal-entry.md)
* [Danh mục Mặt hàng (.md)](../../modules/stock/item.md)