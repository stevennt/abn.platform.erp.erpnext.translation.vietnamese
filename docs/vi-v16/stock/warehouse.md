<!-- add-breadcrumbs -->
# Kho

**Kho là một địa điểm lưu trữ hàng hóa. Kho được sử dụng bởi các nhà sản xuất, nhà nhập khẩu, nhà xuất khẩu, nhà bán buôn, doanh nghiệp vận tải, hải quan, v.v.**

Trong thực tế, kho thường là các tòa nhà lớn với bến bãi để bốc dỡ hàng hóa. Tuy nhiên, trong ERPNext, thuật ngữ 'Kho' rộng hơn và được hiểu là "các vị trí lưu trữ". Bạn có thể tạo các Kho phụ để quản lý chi tiết, ví dụ như một kệ hàng bên trong một vị trí thực tế.

Cấu trúc Kho có thể được tổ chức theo dạng cây phân cấp:

*Kho > Phòng > Dãy > Kệ > Ô hàng*

Để truy cập danh sách Kho, hãy đi tới:
> Home > Kho > Thiết lập > Kho

## 1. Cách tạo Kho
1. Đi tới danh sách Kho, nhấn vào **Mới**.
1. Nhập tên cho Kho.
1. Thiết lập/kiểm tra Kho cha (Parent Warehouse). Nếu bạn tích vào 'Is Group', bạn có thể tạo các Kho phụ dưới Kho nhóm này.
1. **Lưu**.

Các Kho thường được đặt tên theo mã viết tắt của Công ty để dễ dàng nhận diện và quản lý.

### 1.1 Các tùy chọn bổ sung khi tạo Kho
**Tài khoản (Account)**: Thiết lập một tài khoản kế toán mặc định cho tất cả các giao dịch liên quan đến Kho này. Việc thiết lập này giúp hiển thị các giao dịch kho tương ứng trong Sổ cái.

**Loại Kho (Warehouse Type)**: Bạn có thể phân loại Kho (ví dụ: Kho của Nhà cung cấp, Kho tồn kho, Kho bán thành phẩm (WIP), Kho vật tư tiêu hao, v.v.). Việc phân loại này hỗ trợ đắc lực cho việc lập báo cáo và lọc dữ liệu trong các giao dịch.

#### Địa chỉ và liên hệ
Bạn có thể thêm địa chỉ Thanh toán, địa chỉ Giao hàng và các loại địa chỉ khác cho Kho. Bạn cũng có thể thêm thông tin liên hệ, ví dụ như Quản lý Kho.

![Warehouse](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/warehouse.png)

### 1.2 Sau khi Lưu
Sau khi **Lưu** một Kho, bạn sẽ thấy các tùy chọn sau:

* **Tồn kho (Stock Balance)**: Mở báo cáo Số lượng tồn kho để xem số lượng, giá trị, số dư của các Mặt hàng trong kho này.
* **Sổ cái (General Ledger)**: Mở Sổ cái để xem các bút toán kế toán liên quan đến Kho này.
* **Từ Không phải nhóm sang Nhóm (Non-Group to Group)**: Nếu Kho hiện tại là Kho không phải nhóm (không chứa được kho con), nút này sẽ chuyển nó thành Kho nhóm.

## 2. Các tính năng mới và nâng cao (v16)

### 2.1 Chế độ xem Cây (Tree View)
Bạn có thể chuyển sang chế độ xem 'Tree' để quản lý trực quan cấu trúc phân cấp giữa Kho tổng và các Kho con.

<img class="screenshot" alt="Warehouse" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/warehouse-tree.png">

### 2.2 Hạch toán tồn kho theo Mặt hàng (Item-Level Stock Accounting)
Trong phiên bản v16, ERPNext nâng cao khả năng kiểm soát tài chính bằng cách cho phép hạch toán giá trị tồn kho chi tiết đến từng Mặt hàng tại từng Kho, giúp việc đối soát giữa số lượng thực tế và giá trị sổ cái trở nên chính xác tuyệt đối.

### 2.3 Hệ thống Giữ hàng (Stock Reservation System)
Tính năng mới cho phép bạn giữ trước một lượng tồn kho cho các Đơn bán hàng (SO) hoặc các yêu cầu cụ thể, giúp tránh tình trạng thiếu hụt hàng hóa khi có nhiều đơn hàng cùng lúc.

### 2.4 Truy xuất nguồn gốc Lô hàng/Số Serial (Serial/Batch Traceability Report)
Cung cấp báo cáo chi tiết về lịch sử di chuyển của một Lô hàng (Batch) hoặc Số Serial cụ thể qua các Kho khác nhau, hỗ trợ tối đa cho việc kiểm soát chất lượng (QI) và thu hồi hàng hóa.

### 2.5 Chi phí mua hàng cập nhật (Landed Cost cho Stock Entry)
Cho phép cập nhật các chi phí liên quan (như phí vận chuyển, thuế nhập khẩu) trực tiếp vào giá trị của Phiếu nhập hàng (PR) hoặc Phiếu kho (SE), giúp giá trị tồn kho phản ánh đúng chi phí thực tế đã bỏ ra.

### 2.6 Xem trước Sổ cái (Ledger Preview)
Cho phép người dùng xem nhanh các bút toán liên quan ngay tại giao dịch kho mà không cần phải chuyển sang phân hệ Kế toán, giúp kiểm tra tính chính xác của việc ghi nhận giá trị kho ngay lập tức.

## 3. Tài khoản Kho
Trong ERPNext, nếu bạn bật [Kiểm kê thường xuyên](perpetual-inventory.md), mọi Kho phải thuộc về một công ty cụ thể để duy trì số dư tồn kho theo từng công ty. Mỗi Kho nên được liên kết với một Tài khoản trong Hệ thống tài khoản để ghi nhận giá trị tiền tệ của hàng hóa.

**Mẹo quản lý:** Nếu bạn có cấu trúc cây kho quá chi tiết (đến tận Kệ hoặc Ô hàng), bạn nên chỉ liên kết tài khoản kế toán với Kho cấp cao nhất (Kho gốc). Điều này giúp tránh việc phải quản lý hàng trăm tài khoản kế toán không cần thiết, trong khi ERPNext vẫn đảm bảo theo dõi chính xác số lượng tồn kho cho từng Mặt hàng tại mọi vị trí.

> **Lưu ý:** ERPNext duy trì số dư tồn kho cho mọi sự kết hợp giữa Mặt hàng và Kho. Bạn có thể lấy báo cáo số dư tồn kho cho bất kỳ Mặt hàng nào tại một Kho cụ thể vào bất kỳ thời điểm nào.

## 4. Các chủ đề liên quan
1. [Mục đích Phiếu kho](articles/stock-entry-purpose.md)
2. [Báo cáo Mức tồn kho](stock-level-report.md)