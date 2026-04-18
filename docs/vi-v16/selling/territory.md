# Khu vực

**Khu vực là một vùng địa lý nơi bạn thực hiện hoạt động kinh doanh.**

Trong ERPNext, Khu vực được sử dụng để phân loại Khách hàng, Địa chỉ, trong báo cáo kế toán và để phân bổ mục tiêu doanh số.

Để truy cập danh sách Khu vực, hãy đi tới:
> Home > Selling > Settings > Territory

## 1. Cách tạo một Khu vực
1. Đi tới danh sách Khu vực, nhấn vào **Mới**.
1. Tích vào 'Group Node' nếu sẽ có các khu vực con dưới Khu vực này. Ví dụ: Pháp là một Khu vực nhóm và Paris là một khu vực con.
1. **Lưu**.

    ![Territory List](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/territory-list.png)

Bạn có thể thêm nhiều khu vực con dưới một khu vực cha. Khi **Lưu**, một khu vực có thể được chọn trong các giao dịch và báo cáo.

## 2. Các tính năng

### 2.1 Chỉ định quản lý Khu vực
Bạn có thể chỉ định một Quản lý Khu vực để phụ trách việc Bán hàng của vùng này.

### 2.2 Thiết lập Mục tiêu doanh số
Tại đây bạn có thể thiết lập các mục tiêu doanh số cụ thể dựa trên các trường sau:

* Nhóm mặt hàng
* Năm tài chính
* Số lượng mục tiêu
* Số tiền mục tiêu
* Phân bổ mục tiêu

![Territory Target](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/territory-target.png)

Để biết thêm về việc thiết lập mục tiêu doanh số, hãy truy cập trang [Phân bổ mục tiêu Nhân viên bán hàng](sales-person-target-allocation.md)

### 2.3 Các tính năng mới trong v16
* **Nút SO/Quotation trên Khách hàng:** Từ biểu mẫu Khách hàng, bạn có thể nhanh chóng truy cập các nút để tạo Đơn bán hàng hoặc Báo giá.
* **Cutoff date cho DN từ SO:** Cho phép thiết lập ngày chốt (cutoff date) để kiểm soát việc tạo Phiếu giao hàng từ Đơn bán hàng, giúp quản lý chính xác kỳ kế toán và tồn kho.
* **Stock Reservation (Giữ hàng tồn kho):** Hỗ trợ tính năng giữ hàng trong kho dựa trên các đơn hàng đã xác nhận, giúp đảm bảo hàng hóa luôn sẵn sàng cho các giao dịch đã cam kết.

## 3. Các chủ đề liên quan
1. [Khách hàng](customer.md)
1. [Địa chỉ](address.md)