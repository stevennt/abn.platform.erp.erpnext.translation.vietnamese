<!-- add-breadcrumbs -->
# Vấn đề

**Một Vấn đề là một truy vấn gửi đến từ Khách hàng, thường thông qua email hoặc từ phần *Liên hệ* trên trang web của bạn.**

> Mẹo: Một địa chỉ Email hỗ trợ chuyên dụng là cách tốt để theo dõi các truy vấn gửi đến. Ví dụ, bạn có thể gửi các truy vấn hỗ trợ đến ERPNext tại support@erpnext.com và nó sẽ tự động tạo một Vấn đề trong hệ thống của chúng tôi.

Để truy cập danh sách Vấn đề, hãy đi đến:
> Trang chủ > Hỗ trợ > Vấn đề > Vấn đề

![Issue](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/support/issue.png)

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Vấn đề, bạn nên tạo các mục sau trước:

* [Khách hàng](/docs/v16/user/manual/en/CRM/customer)
* [Tài khoản Email](/docs/v16/user/manual/en/setting-up/email/email-account)

## 2. Cách tạo Vấn đề
Vấn đề sẽ được tự động tạo nếu bạn sử dụng **tính năng nối tiếp (append to feature)** trong [Tài khoản Email](/docs/v16/user/manual/en/setting-up/email/email-account#32-incoming-email-accounts).

Bạn cũng có thể tạo một Vấn đề một cách thủ công, để làm điều đó:

1. Đi đến danh sách Vấn đề, nhấn vào Mới.
1. Nhập Chủ đề, Người tạo, và mô tả về Vấn đề.

### 2.1 Các tùy chọn bổ sung khi tạo Vấn đề
* **Trạng thái**: Khi một Vấn đề mới được tạo, trạng thái của nó sẽ là "Mở", khi được phản hồi, trạng thái sẽ trở thành "Đã phản hồi".
    * Mở: Vấn đề đã được tạo và chưa được phản hồi.
    * Đã phản hồi: Một phản hồi đã được gửi cho Vấn đề.
    * Tạm dừng: Vấn đề đang bị tạm dừng vì một lý do nào đó.
    * Đã giải quyết: Khi người dùng chắc chắn rằng họ đã cung cấp cho khách hàng một giải pháp cho vấn đề của họ nhưng chưa nhận được xác nhận về việc giải quyết từ khách hàng.
    * Đã đóng: Khách hàng đã nhận được giải pháp thỏa đáng mà họ đã xác nhận và Vấn đề đã được đóng.

    Nếu người gửi phản hồi vào luồng email, trạng thái sẽ trở lại thành "Mở". Người dùng có thể "Đóng" Vấn đề một cách thủ công bằng cách nhấn vào nút **Đóng** ở góc trên bên phải.

> Lưu ý: Nếu SLA đã được thiết lập, thì trạng thái hoàn thành của SLA sẽ được cập nhật ở cả trạng thái **Đã đóng** cũng như **Đã giải quyết**.

* **Khách hàng**: Nếu email được gửi từ một [Khách hàng](/docs/v16/user/manual/en/CRM/customer) được lưu trữ trong tài khoản ERPNext của bạn, thì liên kết Khách hàng sẽ xuất hiện trong trường này.
* **Mức độ ưu tiên**: Mức độ ưu tiên có thể được thiết lập theo yêu cầu. Theo mặc định, có ba mức độ ưu tiên--Thấp, Trung bình, và Cao. Bạn có thể xóa các mức này hoặc thêm nhiều hơn nếu cần.
* **Loại vấn đề**: Một Vấn đề có thể được phân loại bằng Loại vấn đề. Ví dụ về Loại vấn đề có thể là: 'Chức năng', 'Kỹ thuật', 'Phần cứng', v.v.
* **Người tạo (Email)**: ID email mà từ đó Vấn đề được gửi sẽ được hiển thị ở đây.

## 3. Các tính năng

### 3.1 Chi tiết
* **Mô tả**: Đây là một trường văn bản mà trong đó các chi tiết về Vấn đề có thể được xem. Trường này cũng có thể chứa một hình ảnh hoặc một bảng.

### 3.2 Thỏa thuận mức độ dịch vụ
Đây là một hợp đồng giữa nhà cung cấp dịch vụ và người dùng cuối nhằm xác định mức độ dịch vụ mong đợi từ nhà cung cấp dịch vụ.

Người dùng có thể chọn [Thỏa thuận mức độ dịch vụ](/docs/v16/user/manual/en/support/service-level-agreement) (SLA) từ danh sách.

* Mỗi Vấn đề sẽ có Thời gian phản hồi và Thời gian giải quyết mà trong đó đội ngũ Hỗ trợ phải Phản hồi và Giải quyết Vấn đề.
* Mức độ ưu tiên có thể được thay đổi để leo thang Vấn đề. Các mức độ ưu tiên cần được chỉ định trong Thỏa thuận mức độ dịch vụ.
* Nếu cần, Thỏa thuận mức độ dịch vụ có thể được thiết lập lại bằng cách nhấn vào nút **Thiết lập lại Thỏa thuận mức độ dịch vụ** trong Vấn đề được hiển thị như sau:

![SLA](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/support/new-issue.gif)

### 3.3 Phản hồi
* **Phút đến phản hồi đầu tiên**: Thời gian tính bằng phút từ khi Vấn đề được tạo cho đến khi phản hồi đầu tiên được gửi đi.

* **Phản hồi đầu tiên vào**: Khi một thành viên đội ngũ Hỗ trợ phản hồi vấn đề lần đầu tiên, ngày và giờ phản hồi đầu tiên sẽ được cập nhật.

* **Thời gian phản hồi trung bình**: Thời gian trung bình để phản hồi cho Khách hàng. Điều này được tính bằng cách lấy trung bình của tất cả các khoảng thời gian giữa các Liên lạc Đã nhận và Đã gửi. Trường này sẽ được cập nhật sau mỗi phản hồi được gửi cho khách hàng.

![Response Details](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/support/response.png)

### 3.4 Tham chiếu
Người dùng có thể lọc các vấn đề dựa trên các trường liên kết với Vấn đề này:

* Khách hàng tiềm năng
* Liên hệ
* Tài khoản Email
* Dự án
* Công ty

### 3.5 Giải quyết
* **Ngày mở**: Khi vấn đề được tạo hoặc ghi nhận, ngày sẽ được ghi lại.
* **Giờ mở**: Khi vấn đề được tạo hoặc ghi nhận, giờ chính xác sẽ tự động được ghi lại.
* **Ngày giải quyết**: Khi người dùng giải quyết vấn đề, Ngày và Giờ sẽ được cập nhật trong trường này.
* **Chi tiết giải quyết**: Người dùng có thể nhập chi tiết về vấn đề sau khi nó được giải quyết. Đây là một trường văn bản. Ngoài ra, người dùng có thể tải lên hình ảnh, nhập hoặc tạo một bảng.
* **Thời gian giải quyết**: Tổng thời gian để đóng phiếu (từ khi tạo Vấn đề đến khi đóng).
* **Thời gian giải quyết của người dùng**: Nhiều khi người dùng phải chờ phản hồi của khách hàng để giải quyết một Vấn đề nào đó. Khi đo lường năng suất của người dùng, thời gian chờ này không nên được tính vào. Do đó, thời gian giải quyết của người dùng là tổng thời gian mà người dùng thực hiện để đóng phiếu và có thể được tính như sau:

    _Thời gian giải quyết - Tổng thời gian mà người dùng phải chờ phản hồi của khách hàng_

Các chỉ số Thời gian giải quyết và Thời gian giải quyết của người dùng được thiết lập khi "Đóng". Các chỉ số này sẽ tự động đặt lại khi Vấn đề được mở lại hoặc chia tách.

![Resolution](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/support/resolution.png)

#### Qua Cổng thông tin Khách hàng
Nếu Khách hàng tạo Vấn đề là một Người dùng Website (không có quyền truy cập vào các phân hệ), ô kiểm này sẽ được tích để biểu thị điều đó.

## 4. Sau khi