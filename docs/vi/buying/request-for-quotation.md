<!-- add-breadcrumbs -->
# Yêu cầu báo giá

**Yêu cầu báo giá là một tài liệu mà một tổ chức gửi cho một hoặc nhiều nhà cung cấp để yêu cầu báo giá cho các mặt hàng.**

![Buying Flow](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/buying/buying_flow_rfq.png)

Để truy cập Yêu cầu báo giá, hãy đi đến:
> Home > Buying > Purchasing > Request for Quotation

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Yêu cầu báo giá, bạn nên tạo các thông tin sau trước:

* [Supplier](supplier.md)
* [Item](../stock/item.md)

## 2. Cách tạo Yêu cầu báo giá
1. Đi đến danh sách Request for Quotation, nhấp vào New.
2. Nhập ngày.
3. Chọn Nhà cung cấp mà Yêu cầu báo giá sẽ được gửi đến.
4. Trong bảng tiếp theo, nhập các mặt hàng, số lượng và kho mục tiêu nơi bạn sẽ nhận các mặt hàng.
1. Kho có thể để trống nếu mục 'Maintain Stock' không được tích cho mặt hàng đó.
5. Lưu và Xác nhận.

![Create RFQ](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/buying/rfq-create.png)

Một Yêu cầu báo giá (RFQ) cũng có thể được tạo từ một Yêu cầu vật tư đã được Xác nhận. Sau khi RFQ được tạo, bạn có thể in và gửi cho nhà cung cấp bản PDF chứa tất cả các chi tiết bạn đã nhập liên quan đến RFQ. Bạn cũng có thể nhận được phản hồi của họ (Báo giá của nhà cung cấp) ngay trong ERPNext, xem phần [4.1 Supplier Quotation by User](#41-supplier-quotation-by-user).
Tuy nhiên, đối với số lượng mặt hàng lớn, nhà cung cấp của bạn có thể thấy thoải mái hơn với một bảng tính Excel, v.v.

## 3. Các tính năng

### 3.1 Lấy mặt hàng từ
Các mặt hàng trong bảng mặt hàng có thể được lấy từ các tài liệu khác. Các tùy chọn là: Yêu cầu vật tư, Cơ hội, và Nhà cung cấp tiềm năng.

* **Material Request**: Các mặt hàng sẽ được lấy từ một Yêu cầu vật tư đã được Xác nhận mà bạn chọn. Có thể tìm kiếm Yêu cầu vật tư bằng một số từ khóa khớp và có thể chọn một khoảng ngày để lọc các Yêu cầu vật tư.

* **Opportunity**: Các mặt hàng sẽ được lấy từ một Cơ hội đã được lưu. Một khoảng ngày cũng có thể được chọn tại đây.

* **Possible Supplier**: Chọn một nhà cung cấp tiềm năng. Sau đó, nếu bạn có bất kỳ Yêu cầu vật tư nào đã được Xác nhận dành cho nhà cung cấp này, các mặt hàng có thể được lấy từ đó.

![RFQ get items](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/buying/rfq-get-items.png)

### 3.2 Lấy Nhà cung cấp
Thay vì nhập nhà cung cấp thủ công vào bảng, bạn cũng có thể lấy họ bằng nút 'Get Suppliers'. Khi bạn nhấp vào **Tools > Get Suppliers**, bạn sẽ thấy trường 'Get Suppliers By'. Có hai tùy chọn để lấy nhà cung cấp: Theo Thẻ (Tag) hoặc Theo Nhóm (Group).

* **By tag**: Đi đến 'Tag Category' thông qua việc tìm kiếm từ thanh tìm kiếm. Bạn phải tạo các thẻ tại đây trước và gán chúng cho một Nhà cung cấp trong mô-đun Buying. Sau đó, bạn có thể chọn 'By Tag'. Khi nhấp vào Add 'All Suppliers', các nhà cung cấp có thẻ khớp sẽ được lấy ra.

* **By Group**: Chọn 'Supplier Group' và chọn nhóm nhà cung cấp mà bạn cần thêm vào. Ví dụ: nếu bạn chọn Hardware, tất cả các nhà cung cấp phần cứng của bạn sẽ được thêm vào để bạn có thể nhận báo giá từ tất cả họ.

![RFQ get suppliers](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/buying/rfq-get-suppliers.png)

Trong bảng Nhà cung cấp, khi mở rộng một dòng bằng hình tam giác ngược, bạn sẽ thấy tùy chọn 'Download PDF' để mở bản PDF của RFQ.

### 3.3 Liên kết với Yêu cầu vật tư:
Khi bạn nhấp vào **Tools > Link to Material Requests**, nó sẽ liên kết Yêu cầu báo giá với các Yêu cầu vật tư hiện có. Các mặt hàng trong Yêu cầu báo giá và Yêu cầu vật tư phải giống nhau.

![Link to Material Request](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/buying/link-to-material-request.png)

Bây giờ, khi Yêu cầu báo giá được Lưu, bạn có thể thấy trong Trang tổng quan rằng nó đã được liên kết với Yêu cầu vật tư.
Nếu có nhiều Yêu cầu vật tư có cùng các mặt hàng, thì liên kết sẽ được tạo với Yêu cầu vật tư mới nhất.

### 3.4 Xem trước Email
Trong phần 'Email Details' của một Yêu cầu báo giá ở trạng thái Nháp, có một tính năng để soạn thảo và xem trước email sẽ gửi cho Nhà cung cấp.
![Email Details Section](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/buying/email-details-section.png)

Nhập bất kỳ thông điệp bổ sung nào cho Nhà cung cấp vào trường 'Message for Supplier'. Trường này có thể được tự động điền bằng cách sử dụng trường 'Email Template'.

Có thể thêm lời chào và trường 'Subject' cũng có thể được thay đổi. Sau khi hoàn tất, bạn có thể nhấp vào nút 'Preview Email' để xem trước email sẽ được gửi đi.
![Preview Email](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/buying/email-preview.png)

### 3.5 Điều khoản và Điều kiện

Trong các giao dịch Bán hàng/Mua hàng, có thể có các Điều khoản và Điều kiện nhất định mà dựa vào đó Nhà cung cấp cung cấp hàng hóa hoặc dịch vụ cho Khách hàng. Bạn có thể áp dụng các Điều khoản và Điều kiện vào các giao dịch và chúng sẽ xuất hiện khi in tài liệu. Để biết thêm về Điều khoản và Điều kiện, [nhấp vào đây](../setting-up/print/terms-and-conditions.md)

### 3.6 Cài đặt In
#### Letterhead
Bạn có thể in yêu cầu báo giá/đơn mua hàng trên tiêu đề thư (letterhead) của công ty mình. Tìm hiểu thêm [tại đây](../setting-up/print/letter-head.md).

'Group same items' sẽ nhóm các mặt hàng giống nhau được thêm nhiều lần trong bảng mặt hàng. Điều này có thể được thấy khi bạn in.

#### Print Headings
Tiêu đề của tài liệu có thể được thay đổi. Tìm hiểu thêm [tại đây](../setting-up/print/print-headings.md).

## 4. Tạo Báo giá của nhà cung cấp sau RFQ
Sau khi tạo Yêu cầu báo giá, có hai cách để tạo Báo giá của nhà cung cấp từ Yêu cầu báo giá.

### 4.1 Supplier Quotation by User

1. Mở Yêu cầu báo giá và nhấp vào **Supplier Quotation > Create**.

    ![Supplier Quotation from RFQ](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/buying/make-supplier-quotation-from-rfq.png)

2. Chọn Nhà cung cấp, nhấp vào nhà cung cấp một lần nữa. Trong trang này, nhấp vào dấu + bên cạnh 'Supplier Quotation'. Một trang Báo giá của nhà cung cấp mới sẽ được mở ra, người dùng phải nhập số lượng, đơn giá và Xác nhận nó.

    ![Supplier Quotation fro