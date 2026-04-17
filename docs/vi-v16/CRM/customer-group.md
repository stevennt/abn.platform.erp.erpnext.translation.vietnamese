<!-- add-breadcrumbs -->
# Nhóm khách hàng

**Nhóm khách hàng là một tập hợp các khách hàng có điểm tương đồng theo một cách nào đó.**

Nhóm khách hàng cho phép bạn tổ chức các khách hàng của mình. Thông thường, Khách hàng được nhóm theo phân khúc thị trường dựa trên lĩnh vực mà doanh nghiệp hoạt động. Nhóm khách hàng được tạo theo cấu trúc phân cấp trong ERPNext. Bạn có thể tạo một nhóm khách hàng chính và thêm các nhóm khách hàng con bên dưới nó.

Bạn có thể xác định một Bảng giá sẽ được tự động áp dụng cho tất cả khách hàng thuộc nhóm đó. Bạn cũng có thể xem phân tích xu hướng cho từng nhóm. Các nhóm khách hàng Cá nhân, Thương mại và Chính phủ được tạo sẵn theo mặc định. Bạn có thể thêm các nhóm khách hàng của riêng mình dựa trên nhu cầu như bán lẻ, bán buôn, v.v.

### 1. Cách tạo Nhóm khách hàng
1. Đi đến **CRM > Settings > Customer Group**.
1. Nhấp vào một nhóm khách hàng cha như 'All Customer Groups'.
1. Nhấp vào 'Add Child'.
2. Nhập 'Customer Group Name'.
3. Đánh dấu vào 'Group Node' nếu bạn muốn thêm các nhóm khách hàng con bên dưới nhóm này.
4. Nhấp vào 'Create New'.

![Customer Group](https://docs.erpnext.com/docs/v16/assets/img/crm/customer-group.png)

> Mẹo: Nếu bạn thấy việc này quá tốn công sức, bạn có thể để mặc định là “Default Customer Group”. Nhưng tất cả nỗ lực này sẽ được đền đáp khi bạn bắt đầu nhận được các báo cáo. Một ví dụ về báo cáo mẫu được đưa ra dưới đây:

![Sales Analytics Customer Group](https://docs.erpnext.com/docs/v16/assets/img/crm/sales-analytics-customer-group.gif)

### 2. Các tính năng

#### 2.1 Gán Hạn mức tín dụng, Bảng giá mặc định và Mẫu điều khoản thanh toán mặc định

Bạn có thể gán hạn mức tín dụng, [Bảng giá](/docs/v16/user/manual/vi/stock/price-lists), và [Thanh toán](/docs/v16/user/manual/vi/accounts/payment-terms), chúng sẽ được tự động áp dụng khi một khách hàng thuộc nhóm khách hàng đó được chọn trong các giao dịch bán hàng như [Đơn bán hàng](/docs/v16/user/manual/vi/selling/sales-order) và [Hóa đơn](/docs/v16/user/manual/vi/accounts/sales-invoice).

#### 2.2 Tài khoản phải thu mặc định

Bạn không cần phải tạo một sổ cái kế toán riêng biệt cho từng khách hàng trong ERPNext. Đọc [Tài khoản phải thu chung](/docs/v16/user/manual/vi/accounts/articles/common-receivable-account) để biết thêm chi tiết.

Nếu bạn cần một tài khoản phải thu riêng cho một khách hàng, bạn có thể thêm nó vào phần 'Default Receivable Account'.

#### 2.3 Các tính năng nâng cao trên v16

* **Nút thao tác nhanh trên Khách hàng:** Trong biểu mẫu Khách hàng, bạn có thể truy cập nhanh các nút để tạo [Đơn bán hàng](/docs/v16/user/manual/vi/selling/sales-order) hoặc [Báo giá](/docs/v16/user/manual/vi/selling/quotation) trực tiếp từ giao diện Khách hàng.
* **Ngày chốt (Cutoff date) cho Phiếu giao hàng:** Khi tạo [Phiếu giao hàng](/docs/v16/user/manual/vi/selling/delivery-note) từ [Đơn bán hàng](/docs/v16/user/manual/vi/selling/sales-order), bạn có thể thiết lập ngày chốt để kiểm soát chính xác thời điểm xuất kho và ghi nhận doanh thu.
* **Giữ hàng tồn kho (Stock Reservation):** Hệ thống cho phép đặt chỗ trước [Mặt hàng](/docs/v16/user/manual/vi/stock/stock-reservation) dựa trên các đơn hàng đã xác nhận, giúp đảm bảo lượng [Tồn kho](/docs/v16/user/manual/vi/stock/stock-reservation) luôn sẵn sàng cho các khách hàng ưu tiên.

### 3. Các chủ đề liên quan
1. [Khách hàng](/docs/v16/user/manual/vi/CRM/customer)
1. [Bảng giá](/docs/v16/user/manual/vi/stock/price-lists)
1. [Thanh toán](/docs/v16/user/manual/vi/accounts/payment-terms)

{next}