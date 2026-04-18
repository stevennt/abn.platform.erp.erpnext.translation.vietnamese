<!-- add-breadcrumbs -->
# Cài đặt In

**Trong Cài đặt In, bạn có thể thiết lập các tùy chọn in như Kích thước giấy, kích thước văn bản mặc định, việc bạn muốn xuất ra định dạng PDF hay HTML, v.v.**

Vì ERPNext là một ứng dụng chạy trên trình duyệt, lệnh in thực tế sẽ được thực hiện bởi trình duyệt bạn đang sử dụng.

Để chỉnh sửa Cài đặt In, hãy đi tới:
> Trang chủ > Cài đặt > Cài đặt In

<img class="screenshot" alt="Print Settings" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/print/print-settings.png">

Có nhiều cấu hình khác nhau có sẵn trong Cài đặt In. Hãy cùng tìm hiểu về chúng.

## 1. Cài đặt PDF

### 1.1 PDF hoặc HTML

Khi bạn gửi email bất kỳ tài liệu nào (như Đơn bán hàng/Hóa đơn) từ ERPNext, nó sẽ được gửi dưới định dạng PDF hoặc HTML. Theo mặc định, tệp sẽ được gửi dưới dạng PDF. Nếu bạn muốn gửi tài liệu dưới định dạng HTML, chỉ cần bỏ chọn tùy chọn "Send Print as PDF".

### 1.2 Lặp lại Tiêu đề và Chân trang trong PDF

Letterhead (Tiêu đề thư) là một bản ghi master nơi bạn có thể xác định Tiêu đề và Chân trang tiêu chuẩn để đính kèm vào Mẫu in của tài liệu. Nếu thuộc tính này được bật, Tiêu đề và Chân trang sẽ được thêm vào mỗi trang. Nếu bạn không muốn tiêu đề và chân trang lặp lại trên mỗi trang, chỉ cần tắt cài đặt này.

### 1.3 Kích thước trang PDF
Kích thước mặc định để in các trang PDF là A4, bạn có thể thay đổi nó thành kích thước tiêu đề thư.

## 2. Cài đặt Trang

### 2.1 In kèm Tiêu đề thư

Bật thuộc tính này sẽ tự động tích chọn tùy chọn Letter Head khi in một tài liệu. Lưu ý rằng bạn cần phải thiết lập Letter Head làm mặc định hoặc chọn một cái trong giao dịch để nó xuất hiện trong chế độ xem in.

### 2.2 In Mặt hàng Thu gọn

Các giao dịch như đơn bán hàng/hóa đơn có một bảng chi tiết các mặt hàng đã mua hoặc bán. Nó có nhiều cột như Tên mặt hàng, Mô tả, Đơn vị tính, Đơn giá, Số tiền, v.v. Nếu có nhiều cột trong bảng Mặt hàng, thì Mẫu in trông sẽ hơi lộn xộn. Bạn có thể cải thiện chế độ xem của bảng bằng cách bật In Mặt hàng Thu gọn.

Theo cài đặt này, sẽ chỉ có bốn cột trong Mẫu in, cụ thể là: Mô tả, Số lượng, Đơn giá và Số tiền.

Giá trị của các cột khác (như tên, mô tả, hình ảnh, số serial, v.v.) sẽ được nối chuỗi trong cột Mô tả.

Khi ô kiểm không được tích, mẫu in trông như thế này:
![Incompact Print Format Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/print/incompact-print.png)

Đây là giao diện của Mẫu in Thu gọn:
![Compact Print Format Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/print/compact-print.png)


### 2.3 Cho phép In cho bản Nháp

Các tài liệu (chủ yếu là các giao dịch) có hai giai đoạn xác thực: Lưu và Xác nhận. Các tài liệu đã lưu là bản nháp đầu tiên và chưa được xác nhận vào hệ thống. Do đó, việc in ấn bị hạn chế đối với các tài liệu ở giai đoạn này. Tuy nhiên, nếu bạn muốn cho phép người dùng in tài liệu ở giai đoạn Nháp, hãy bật ô kiểm này.

### 2.4 Luôn thêm tiêu đề "Nháp" khi in các tài liệu nháp

Bật cài đặt này cũng sẽ in chữ "Nháp" trong Mẫu in, từ đó cho biết tài liệu được chia sẻ vẫn chưa được xác nhận hoàn toàn.

### 2.5 Cho phép Ngắt trang trong Bảng

Nếu mô tả của một mặt hàng chiếm nhiều không gian trang hơn bình thường, việc bật cài đặt này sẽ chia nhỏ chi tiết mặt hàng sang trang tiếp theo. Do đó, một dấu ngắt trang sẽ được chèn giữa Mô tả mặt hàng, và các chi tiết còn lại sẽ được đẩy sang trang tiếp theo.

### 2.6 Cho phép In cho các giao dịch đã Hủy

Các giao dịch đã Hủy là những giao dịch không có bất kỳ tác động nào đến các báo cáo. Nếu bạn muốn cho phép in các giao dịch đã Hủy, hãy bật cài đặt này. Một giao dịch chỉ có thể bị Hủy sau khi nó đã được Xác nhận.

### 2.7 In Thuế với Số tiền bằng Không

Trong các giao dịch bán hàng và mua hàng, bạn có thể áp dụng nhiều loại thuế cho mặt hàng. Theo mặc định, trong mẫu in, chỉ những loại thuế có tính toán ra số tiền mới hiển thị. Nếu bạn muốn in cả loại thuế không được áp dụng và có số tiền thuế bằng không, hãy bật cài đặt này.

## 3. Máy in Mạng / Máy chủ In

Bạn có thể bật máy chủ in bằng cách điền IP và cổng của máy chủ in. Sau đó chọn máy in mặc định.

Trước khi bật tính năng này, bạn phải cài đặt thư viện `pycups`.

Trước tiên, bạn có thể cần cài đặt thư viện `cups` nếu nó chưa có sẵn trên hệ thống của bạn.

Đối với dòng OS Debian:

`sudo apt-get install libcups2-dev`

Đối với dòng OS Red Hat:

`sudo yum install cups-libs`

Sau đó, cài đặt `pycups` trong môi trường bằng lệnh:

`./env/bin/pip install pycups`

Lệnh này được thực hiện từ thư mục `frappe-bench`.

## 4. In thô

Bạn có thể bật in thô và in tới nhiều loại máy in nhiệt được hỗ trợ. Đọc [In thô](raw-printing.md) để biết thêm chi tiết.

### 5. Các chủ đề liên quan
1. [Mẫu in](print-format.md)
1. [Kiểu in](print-style.md)
1. [Tiêu đề in](print-headings.md)
1. [Dịch tùy chỉnh](custom-translations.md)