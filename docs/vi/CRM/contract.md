<!-- add-breadcrumbs -->
# Hợp đồng

**Hợp đồng là một thỏa thuận có tính ràng buộc pháp lý giữa Nhà cung cấp và Khách hàng về việc bán sản phẩm hoặc dịch vụ.**

Một hợp đồng có hiệu lực pháp lý vì nó đáp ứng các yêu cầu và sự phê duyệt của pháp luật. Một thỏa thuận thường bao gồm việc trao đổi hàng hóa, dịch vụ, tiền bạc hoặc các lời hứa về bất kỳ điều nào trong số đó.

Để truy cập danh sách Hợp đồng, hãy đi đến:
> Home > Sales Pipeline > Contract


## 1. Cách tạo Hợp đồng
1. Đi đến danh sách Hợp đồng và nhấn vào Mới.
1. Chọn Khách hàng.
1. Nhập Điều khoản Hợp đồng. Một mẫu cũng có thể được tạo để dễ dàng lấy các điều khoản.
1. Lưu.
    ![Contract](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/crm/contract.png)

**Party User**: Nhân viên từ Công ty của bạn, người đang liên hệ với Khách hàng.

### 1.1 Trạng thái

* **Unsigned**: Hợp đồng vẫn chưa được Khách hàng ký.
* **Active**: Hợp đồng đã được ký và có hiệu lực trong Thời hạn Hợp đồng.
* **Inactive**: Hợp đồng đã hết Thời hạn Hợp đồng và không còn giá trị.

## 2. Các tính năng
### 2.1 Thời hạn Hợp đồng
Ngày Bắt đầu và Kết thúc mà trong đó Hợp đồng có hiệu lực.

### 2.2 Chi tiết người ký
Phần này sẽ xuất hiện khi ô kiểm 'Signed' được tích để cho biết Khách hàng đã ký và chấp nhận Hợp đồng.

![Contract Signee](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/crm/contract-signee.png)

* **Signee**: Nhập tên của người đã ký Hợp đồng.
* **Signed On**: Ngày mà Hợp đồng được ký.

### 2.3 Chi tiết Hợp đồng
Nhập các điều khoản của Hợp đồng vào trường Điều khoản Hợp đồng. Bạn có thể tạo một Mẫu Hợp đồng và mẫu đó có thể được chọn để lấy các Điều khoản Hợp đồng.

### 2.4 Chi tiết thực hiện
Nếu Hợp đồng yêu cầu một số việc cần được thực hiện từ phía Nhà cung cấp (là bạn), các chi tiết của họ có thể được ghi lại trong bảng Điều khoản thực hiện.

![Contract Fulfilment](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/crm/contract-fulfilment.png)

* **Requirement**: Nhập một yêu cầu cần được thực hiện. Ví dụ: 'lắp đặt'.
* **Notes**: Bất kỳ ghi chú nào về yêu cầu có thể được nhập tại đây.

### 2.5 Mẫu Hợp đồng
Một mẫu hợp đồng là một khung chuẩn hóa của một hợp đồng mà không bao gồm các chi tiết cụ thể. Bạn có thể tạo một mẫu mới bằng cách đi đến:

> Home > CRM > Contract Template

Bạn có thể tạo các mẫu bằng cách sử dụng Jinja. Ví dụ:

```
Các bên tham gia hợp đồng này vào ngày {{ start_date }}.
```

Khi bạn tạo một hợp đồng mới bằng mẫu này, `{{ start_date }}` sẽ được thay thế bằng ngày được nhập vào trường có cùng tên.

![Contract Template](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/crm/contract-template-jinja.gif)

### 2.6 Tham chiếu
Nếu Hợp đồng có thể được liên kết với một giao dịch trong ERPNext. Chọn loại giao dịch và giao dịch cụ thể. Các tài liệu có thể được liên kết là:

* Báo giá
* Dự án
* Đơn bán hàng
* Đơn mua hàng
* Hóa đơn bán hàng
* Hóa đơn mua hàng

![Contract References](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/crm/contract-reference.png)

### 3. Các chủ đề liên quan
1. [Quotation](../selling/quotation.md)
1. [Purchase Order](../buying/purchase-order.md)
1. [Sales Order](../selling/sales-order.md)
1. [Purchase Receipt](../stock/purchase-receipt.md)
1. [Delivery Note](../stock/delivery-note.md)
1. [Sales Invoice](../accounts/sales-invoice.md)
1. [Purchase Invoice](../accounts/purchase-invoice.md)