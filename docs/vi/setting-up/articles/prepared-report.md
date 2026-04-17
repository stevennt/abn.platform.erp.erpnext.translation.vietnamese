---
title: Sử dụng Báo cáo được chuẩn bị sẵn trong ERPNext
add_breadcrumbs: 1
show_sidebar: 0

metatags:
 description: ERPNext cho phép tạo báo cáo dưới nền để người dùng có thể tiếp tục các công việc thường ngày trong khi báo cáo đang được tạo cho họ.
 keywords: frappe, erpnext, erpnext reports, mis, prepared report, background reports
---

<!-- add-breadcrumbs -->
# Sử dụng Báo cáo được chuẩn bị sẵn

Nhiều khi khi tạo một báo cáo xử lý khối lượng dữ liệu lớn, chẳng hạn như báo cáo Sổ cái cho cả năm, bạn có thể gặp thông báo lỗi sau: **Request Timed Out** (Yêu cầu quá hạn thời gian). Điều này xảy ra do có quá nhiều dữ liệu cần được xử lý và hiển thị trên trang báo cáo, nhưng tài nguyên máy chủ không đủ dẫn đến việc hết thời gian chờ.

Để xử lý tốt hơn các báo cáo như vậy, ERPNext cung cấp tính năng Báo cáo được chuẩn bị sẵn (Prepared Reports) (từ phiên bản v11). Khi một báo cáo được thiết lập là Báo cáo được chuẩn bị sẵn, nó sẽ được tạo thông qua một [background job](https://frappe.io/docs/v13/user/en/guides/app-development/running-background-jobs), và khi đã sẵn sàng, người dùng có thể xem được.

## Các bước thiết lập Báo cáo được chuẩn bị sẵn

1. Đi tới [Role Permission for Page and Report](/docs/v13/user/manual/en/setting-up/users-and-permissions/role-permission-for-page-and-report).
1. Trong trường 'Set Role For', chọn **Report**.
1. Trong trường 'Report', chọn báo cáo mà bạn muốn bật/tắt tính năng báo cáo được chuẩn bị sẵn.
1. Sử dụng hộp kiểm **Disable Prepared Report** để bật/tắt báo cáo được chuẩn bị sẵn. Nếu tùy chọn này được chọn, tính năng báo cáo được chuẩn bị sẵn sẽ bị vô hiệu hóa cho báo cáo đã chọn.
1. Nhấp vào **Update**.

<img alt="Setup Prepared Report" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/set-prep-report.gif">

## Cách sử dụng Báo cáo được chuẩn bị sẵn

1. Mở báo cáo đã nói (ví dụ: Sổ cái) và áp dụng tất cả các bộ lọc cần thiết.
1. Nếu tùy chọn báo cáo được chuẩn bị sẵn đã được bật cho báo cáo đó, bạn sẽ thấy nút **Generate Report**. Hãy nhấp vào nút này.
    <img alt="Generate Prepared Report" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/prepared-report-generate.png">
1. Bạn sẽ thấy một thông báo ở góc dưới bên phải màn hình nói rằng "Report initiated. You can track its status _here_" (Báo cáo đã được khởi tạo. Bạn có thể theo dõi trạng thái của nó _tại đây_)
    <img alt="Prepared Report Initiated" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/prepared-report-bg.png">
1. Bạn có thể đợi ở màn hình đó hoặc nhấp vào _here_ trong thông báo trên để mở trang dành cho báo cáo. Thao tác này sẽ mở một trang mới cho báo cáo:
    <img alt="Prepared Report Queued" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/prepared-report-queued.png">
    Như bạn thấy, trang báo cáo có trạng thái là "Queued" (Đang chờ). Khi báo cáo đã sẵn sàng, bạn sẽ thấy nút **Show Report** mà bạn có thể nhấp vào để xem báo cáo:
     <img alt="Prepared Report Initiated" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/prepared-report-page.png">
1. Vì Báo cáo được chuẩn bị sẵn cũng là một DocType, để xem danh sách các Báo cáo được chuẩn bị sẵn, bạn có thể sử dụng [Role Permission Manager](/docs/v13/user/manual/en/setting-up/users-and-permissions/role-based-permissions) để cấp quyền truy cập vào đó.