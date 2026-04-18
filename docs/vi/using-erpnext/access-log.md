---
title: Nhật ký truy cập
add_breadcrumbs: 1
show_sidebar: 0

metatags:
 description: Nhật ký truy cập là một tính năng bảo mật giúp ghi lại tất cả các hoạt động xuất dữ liệu dưới dạng in các Biểu mẫu và báo cáo, tải xuống tệp riêng tư và xuất báo cáo dưới định dạng excel/csv.
 keywords: frappe, access log, erpnext v12, erpnext release notes, erpnext new features, erp, open source erp, free erp, security
---

# Nhật ký truy cập

> Được giới thiệu trong Phiên bản 13

**Nhật ký truy cập là một tính năng bảo mật giúp ghi lại tất cả các hoạt động xuất dữ liệu của tất cả người dùng trong hệ thống.**

Đây là một công cụ dành cho Quản trị viên hệ thống để theo dõi những tệp nào đã được người dùng truy cập hoặc xuất trên hệ thống. Điều này rất hữu ích để theo dõi các thông tin nhạy cảm của công ty bạn như các giao dịch hoặc dữ liệu tài chính.

Nhật ký truy cập được tạo trong các sự kiện sau:

 - In tất cả các Biểu mẫu và Báo cáo
 - Tải xuống tệp riêng tư
 - Xuất dữ liệu qua định dạng XLSX/CSV

Trong ERPNext, Nhật ký truy cập có sẵn cho Quản trị viên hệ thống, có thể truy cập bằng Tìm kiếm toàn cầu hoặc thông qua:

> Trang chủ > Người dùng và Quyền > Nhật ký > Nhật ký truy cập

![Access Log](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/using-erpnext/using-access-log-3.png)

Trong trường hợp nhật ký truy cập được tạo khi thực hiện sự kiện xuất một Báo cáo, nút **Hiển thị báo cáo** sẽ được tạo trong nhật ký tương ứng. Khi nhấp vào nút này, báo cáo đã xuất có thể được xem cùng với các bộ lọc đã thiết lập.

![Access Log](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/using-erpnext/using-access-log-1.png)

Tương tự, một nút **Hiển thị tài liệu** sẽ được tạo trong trường hợp các sự kiện liên quan trực tiếp đến tài liệu như In tài liệu và Tải xuống tệp riêng tư.

![Access Log](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/using-erpnext/using-access-log-2.png)

Các sự kiện như [In thô](../setting-up/print/raw-printing.md) sẽ lưu thông tin cùng với mẫu đã chọn cho tài liệu đó.

![Access Log](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/using-erpnext/using-acces-log-4.png)