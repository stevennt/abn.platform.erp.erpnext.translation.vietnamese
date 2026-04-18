<!-- add-breadcrumbs -->
# Kiểm tra chất lượng

Trong ERPNext v16, bạn có thể đánh dấu các sản phẩm nhập hoặc xuất của mình để Kiểm tra chất lượng. Hệ thống cũng hỗ trợ liên kết chặt chẽ với việc quản lý tồn kho, truy xuất nguồn gốc theo Lô hàng/Số sê-ri và tính toán giá trị hàng tồn kho chi tiết.

Để truy cập tính năng này, hãy đi tới:
> Home > Stock > Tools > Quality Inspection

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Kiểm tra chất lượng, bạn nên thực hiện các bước sau:

* **Tạo một [Mặt hàng](item.md)**.
* **Bật Tiêu chí Kiểm tra chất lượng trong danh mục Mặt hàng**. Khi bật một trong hai ô đánh dấu, việc **Xác nhận** chứng từ giao/nhận kho sẽ chỉ được cho phép sau khi việc Kiểm tra chất lượng đối với chứng từ đó đã được thực hiện:
    ![Enable Quality Inspection](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/quality-inspection-pre-requisite.png)
* (Tùy chọn) **Tạo Mẫu Kiểm tra chất lượng**. Bạn có thể thêm các thông số kiểm tra và tiêu chí chấp nhận vào mẫu, các thông tin này có thể dễ dàng được lấy vào bất kỳ bản Kiểm tra chất lượng nào. Sau khi **Lưu** mẫu, bạn có thể thiết lập mẫu này trong danh mục Mặt hàng (như hiển thị ở trên).
    ![Quality Inspection Template](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/quality-inspection-template.png)

## 2. Cách tạo một Kiểm tra chất lượng mới

1. Từ một **Phiếu nhập hàng** hoặc **Phiếu giao hàng** đang ở trạng thái **Nháp**, đi tới trường Kiểm tra chất lượng trong bảng **Mặt hàng** và nhấp vào **Tạo Kiểm tra chất lượng mới**. Bạn cũng có thể tạo Kiểm tra chất lượng cho Thẻ công việc (Job Card) để giám sát chất lượng của các mặt hàng đang trong quá trình sản xuất.
2. Chọn loại kiểm tra là Nhập (Mua hàng), Xuất (Bán hàng), hoặc Đang sản xuất (Sản xuất).
3. Chọn Loại chứng từ tham chiếu là **Phiếu nhập hàng**, **Hóa đơn** mua hàng, **Phiếu giao hàng**, **Hóa đơn** bán hàng, **Phiếu kho**, hoặc Thẻ công việc.
4. Chọn **Mặt hàng** và thiết lập kích thước mẫu sẽ được kiểm tra. Lưu ý rằng chỉ những **Mặt hàng** đã được bật Tiêu chí Kiểm tra trong danh mục **Mặt hàng** mới được lấy ra.
5. Mẫu Kiểm tra chất lượng được thiết lập trong danh mục **Mặt hàng** sẽ được tự động lấy vào.
6. Bạn có thể thay đổi người thực hiện kiểm tra và cũng có thể thêm người xác nhận.
7. Có thể thêm bất kỳ Ghi chú bổ sung nào về việc Kiểm tra.
8. **Lưu**. Thiết lập Trạng thái. **Xác nhận**.

<img class="screenshot" alt="Quality Inspection" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/quality-inspection-1.png">

## 3. Các tính năng nâng cao trong v16

Bên cạnh các tính năng kiểm tra cơ bản, ERPNext v16 cung cấp khả năng quản lý chất lượng kết hợp với:
* **Hệ thống Giữ hàng (Stock Reservation System):** Đảm bảo các mặt hàng đã qua kiểm tra chất lượng được giữ đúng cho các đơn hàng dự kiến.
* **Báo cáo Truy xuất nguồn gốc (Serial/Batch Traceability Report):** Theo dõi lịch sử chất lượng dựa trên từng **Lô hàng** hoặc Số sê-ri cụ thể.
* **Kế toán tồn kho theo cấp độ Mặt hàng (Item-Level Stock Accounting):** Tự động cập nhật giá trị kho dựa trên các chi phí phát sinh trong quá trình kiểm tra hoặc xử lý chất lượng.

### 3.1 Kiểm tra chất lượng dạng số
Kiểm tra chất lượng dạng số bao gồm tất cả các kiểm tra yêu cầu các giá trị đọc dựa trên số và tiêu chí chấp nhận.

Ví dụ: kiểm tra xem một giá trị đọc có nằm trong một phạm vi nhất định hay không.

Theo mặc định, các kiểm tra là dạng số. Có hai trường: **Giá trị tối thiểu** và **Giá trị tối đa**, để xác định một phạm vi mà **mỗi** giá trị đọc phải nằm trong đó. Các trường này có thể được thiết lập một lần trong Mẫu Kiểm tra chất lượng và sau đó chỉ cần được lấy vào bản Kiểm tra chất lượng.

<img class="screenshot" alt="Numeric Quality Check" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/quality-inspection-numeric-reading.png">

Nếu bất kỳ giá trị đọc nào được nhập không nằm trong phạm vi này, trạng thái của dòng đó sẽ tự động được đặt thành 'Rejected' (Bị loại) khi **Lưu**.

### 3.2 Kiểm tra chất lượng không phải số (Dựa trên giá trị)
Kiểm tra chất lượng không phải số bao gồm các kiểm tra yêu cầu các giá trị chữ cái hoặc những kiểm tra không yêu cầu bất kỳ tính toán toán học nào.

Ví dụ: kiểm tra xem màu sắc có phải là màu trắng trong kiểm tra chất lượng màu sắc hay không, các giá trị Có/Không cho một số thông số nhất định, v.v.

Đối với các kiểm tra không phải số, hãy bật ô đánh dấu 'Non-numeric'. Bạn sẽ thấy trường **Giá trị tiêu chí chấp nhận** và phần **Kiểm tra dựa trên giá trị** hiển thị.

Nhập vào trường Giá trị đọc. Giá trị tiêu chí chấp nhận có thể được thiết lập một lần trong Mẫu Kiểm tra chất lượng và sau đó được lấy vào bản Kiểm tra chất lượng.

<img class="screenshot" alt="Non-numeric Quality Check" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/quality-inspection-non-numeric-reading.png">

Nếu Giá trị đọc không khớp với Giá trị tiêu chí chấp nhận, trạng thái của dòng đó sẽ tự động được đặt thành 'Rejected' (Bị loại) khi **Lưu**.

### 3.3 Kiểm tra chất lượng dựa trên công thức
Kiểm tra chất lượng dựa trên công thức hữu ích cho các kịch bản phức tạp hơn, nơi mà việc chỉ chỉ định một phạm vi hoặc một giá trị chấp nhận là không đủ.

Ví dụ: kiểm tra xem cấp độ của vật liệu là A/B/C hay không, kiểm tra xem giá trị trung bình của một số lần đọc có nằm trong một phạm vi nhất định hay không, v.v.

Kiểm tra chất lượng dựa trên công thức có thể áp dụng cho cả Kiểm tra chất lượng dạng số và không phải số.

Bật ô đánh dấu 'Formula Based Criteria' để thực hiện Kiểm tra chất lượng dựa trên công thức. Sau đó, bạn sẽ thấy một trường gọi là **Công thức tiêu chí chấp nhận**, nơi bạn có thể chỉ định một công thức để xác định xem một mục kiểm tra nhất định là Được chấp nhận hay Bị loại.
Công thức này có thể được thiết lập một lần trong Mẫu Kiểm tra chất lượng và sau đó được lấy vào bản Kiểm tra chất lượng.

<img class="screenshot" alt="Acceptance Criteria Formula" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/acceptance-criteria-formula.png">

Công thức này phụ thuộc vào nhiều trường Giá trị đọc trong bảng Giá trị đọc.

Đối với các giá trị đọc dạng số, `reading_1`, `reading_2`, v.v. được chấp nhận trong công thức.

Đối với các giá trị đọc không phải số, chỉ có `reading_value` được chấp nhận trong công thức.