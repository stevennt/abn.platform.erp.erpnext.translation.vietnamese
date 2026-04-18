<!-- add-breadcrumbs -->
# Bán hàng với Đơn vị tính (UoM) khác nhau

Đơn vị tính (UoM) giá bán là đơn vị tính mà bạn dùng để định giá các mặt hàng. Bạn có thể có nhiều UoM giá bán cho bất kỳ mặt hàng tồn kho nào. Tuy nhiên, khi Khách hàng đặt hàng, UoM của một mặt hàng có thể thay đổi.

Ví dụ: một mặt hàng Bút được nhập kho theo đơn vị Cái, nhưng được bán theo đơn vị Hộp. Do đó, chúng ta sẽ lập Đơn bán hàng cho Bút theo đơn vị Hộp.

### Bước 1: Thiết lập Đơn vị tính trong danh mục Mặt hàng

Trong danh mục Mặt hàng, tại phần Đơn vị tính, bạn có thể liệt kê tất cả các UoM khả thi của một mặt hàng, cùng với Hệ số chuyển đổi UoM của nó. 

**Cập nhật Hệ số chuyển đổi UoM:**
Nếu trong một Hộp có 10 Cái Bút, Hệ số chuyển đổi UoM sẽ là 10.

![Item Unit of Measure](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/Item-UOM.png)

### Bước 2: Thiết lập trong Đơn bán hàng (SO)

Trong Đơn bán hàng, bạn sẽ thấy hai trường UoM:

- **UoM**: Đơn vị tính dùng để bán hàng.
- **Stock UoM (UoM Kho)**: Đơn vị tính dùng để quản lý tồn kho.

Trong cả hai trường, UoM mặc định của Mặt hàng sẽ được lấy tự động. Bạn nên chỉnh sửa trường UoM và chọn UoM bán hàng (trong trường hợp này là Hộp). Việc cập nhật UoM bán hàng chủ yếu để phục vụ tham chiếu cho Khách hàng. Trong mẫu in, bạn sẽ thấy số lượng mặt hàng theo UoM bán hàng.

![Sale Order Unit of Measure](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/Sale-Order-UOM.png)

**Lưu ý về tính toán:**
Dựa trên Số lượng và Hệ số chuyển đổi, số lượng sẽ được tính toán theo UoM Kho của Mặt hàng. Nếu bạn chỉ bán 1 Hộp, thì Số lượng theo UoM Kho sẽ được thiết lập là 10.

> [!TIP]
> **Mẹo vặt v16:** Tại giao diện Khách hàng, bạn có thể sử dụng các nút lệnh nhanh **SO** hoặc **Quotation** để tạo nhanh Đơn bán hàng hoặc Báo giá mà không cần tìm kiếm thủ công.

### Bước 3: Quản lý Phiếu giao hàng (DN) và Giữ hàng (Stock Reservation)

Khi bạn tiến hành lập Phiếu giao hàng (DN) từ Đơn bán hàng (SO), hệ thống v16 áp dụng cơ chế **Cutoff date** (Ngày chốt) để đảm bảo tính chính xác của tồn kho tại thời điểm giao hàng.

Ngoài ra, với tính năng **Stock Reservation (Giữ hàng)**, khi một Đơn bán hàng được Xác nhận, hệ thống có thể tự động giữ số lượng hàng trong Kho để đảm bảo hàng hóa luôn sẵn sàng cho đơn hàng đó, tránh việc bị xuất cho các đơn hàng khác.

### Ghi sổ Sổ cái kho

Bất kể UoM bán hàng được chọn trong Đơn bán hàng là gì, việc ghi sổ cái kho sẽ được thực hiện theo UoM mặc định của Mặt hàng. Do đó, bạn nên đảm bảo rằng hệ số chuyển đổi được nhập chính xác khi bán Mặt hàng bằng các UoM khác nhau.

![UOM in Stock Ledger](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/uom-in-stock-ledger.png)

{next}