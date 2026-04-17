<!-- add-breadcrumbs -->
# Tạo Báo cáo Tùy chỉnh

Có ba loại báo cáo trong ERPNext.

### 1. Report Builder

Report Builder là một công cụ tùy chỉnh báo cáo tích hợp sẵn trong ERPNext. Công cụ này cho phép bạn xác định các trường cụ thể của biểu mẫu sẽ được thêm vào báo cáo. Ngoài ra, bạn có thể thiết lập các bộ lọc bắt buộc, sắp xếp và đặt tên mong muốn cho báo cáo.

<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/TxJGUNarcQs?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
</div >

### 2. Query Report

Query Report được viết bằng SQL, giúp truy xuất các giá trị từ cơ sở dữ liệu của tài khoản và hiển thị chúng trong báo cáo. Mặc dù các truy vấn SQL có thể được viết từ giao diện người dùng, nhưng tính năng này có thể bị hạn chế tùy thuộc vào quyền quản trị hệ thống để đảm bảo an toàn dữ liệu.

Hãy kiểm tra báo cáo [Mặt hàng Đơn mua hàng cần nhận](https://frappe.io/docs/v16/user/en/guides/reports-and-printing/how-to-make-query-report.html) trong module Kho để xem ví dụ về một Query Report. [Nhấp vào đây](https://frappe.io/docs/v16/user/en/guides/reports-and-printing/how-to-make-query-report.html) để tìm hiểu cách tạo Query Report.

### 3. Script Report

Script Report được viết bằng Python và được lưu trữ ở phía máy chủ. Đây là những báo cáo phức tạp đòi hỏi các logic và tính toán chuyên sâu. Vì các báo cáo này được viết ở phía máy chủ, nên việc tùy chỉnh trực tiếp từ giao diện người dùng (trên các phiên bản Cloud) sẽ bị hạn chế.

Hãy kiểm tra báo cáo [Phân tích Tài chính](https://frappe.io/docs/v16/user/en/guides/reports-and-printing/how-to-make-script-reports.html) trong module Kế toán để xem ví dụ về một Script Report. [Nhấp vào đây](https://frappe.io/docs/v16/user/en/guides/reports-and-printing/how-to-make-script-reports.html) để tìm hiểu cách tạo Script Report.

> Lưu ý: **Bộ lọc động (Dynamic Filter)** có sẵn trong Script Report và Query Report; tuy nhiên, không có trong Report Builder.

{next}

<!-- markdown -->