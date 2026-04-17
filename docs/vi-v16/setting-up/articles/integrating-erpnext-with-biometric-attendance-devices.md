---
title: Tích hợp ERPNext với Thiết bị Chấm công Sinh trắc học
add_breadcrumbs: 1
show_sidebar: 0

metatags:
 description: ERPNext có tính năng ghi nhận chấm công từ nhật ký Check-in và Check-out từ thiết bị sinh trắc học. Có nhiều phương pháp khác nhau để tích hợp thiết bị sinh trắc học của bạn dựa trên nhà cung cấp và các tính năng sẵn có của thiết bị.
 keywords: frappe, erpnext, erpnext attendance, biometric device integration, human resource, auto attendance
---

<!-- add-breadcrumbs -->
# Tích hợp ERPNext với Thiết bị Chấm công Sinh trắc học

Nhật ký chấm công (Attendance Punch Logs) từ thiết bị sinh trắc học là một loại nhật ký Check-in và Check-out của nhân viên.

ERPNext có tính năng lưu trữ các nhật ký này trong một tài liệu gọi là Employee Checkin.

Việc chấm công sau đó có thể được ghi nhận dựa trên các bản ghi Employee Checkin và ca làm việc của nhân viên thông qua [Cài đặt Chấm công tự động](/docs/v16/user/manual/vi/human-resources/shift-management#25-auto-attendance-settings) bằng cách sử dụng tính năng [Chấm công tự động](/docs/v16/user/manual/vi/human-resources/auto-attendance)

Do đó, việc tích hợp Thiết bị Sinh trắc học của bạn -- hoặc bất kỳ hệ thống kiểm soát ra vào nào có thu thập dữ liệu VÀO/RA -- có thể được thực hiện theo các bước sau:

  1. [Thiết lập Chấm công tự động để ghi nhận chấm công từ Employee Checkin](#1-thiết-lập-chấm-công-tự-động-để-ghi-nhận-chấm-công-từ-employee-checkin)
  2. [Đưa Nhật ký chấm công sinh trắc học vào Employee Checkin của ERPNext](#2-đưa-nhật-ký-chấm-công-sinh-trắc-học-vào-employee-checkin-của-erpnext)

## 1. Thiết lập Chấm công tự động để ghi nhận chấm công từ Employee Checkin

Trước khi bạn nhập nhật ký Check-in và Check-out của nhân viên vào hệ thống ERPNext, bạn cần phải thiết lập nhân viên và ca làm việc của họ để có thể tạo dữ liệu chấm công bằng tính năng Chấm công tự động trong ERPNext.

Vui lòng tham khảo liên kết sau để thiết lập Chấm công tự động: [Thiết lập Chấm công tự động](/docs/v16/user/manual/vi/human-resources/auto-attendance#steps-to-setup-auto-attendance)

Sau khi bạn đã thiết lập Nhân viên và phân ca làm việc cho nhân viên, bạn đã sẵn sàng để chuyển sang bước tiếp theo.

## 2. Đưa Nhật ký chấm công sinh trắc học vào Employee Checkin của ERPNext
Tùy thuộc vào hệ thống sinh trắc học và các tính năng của nó, có rất nhiều cách bạn có thể nhập nhật ký chấm công vào ERPNext:

1. Sử dụng Công cụ Nhập dữ liệu (Data Import Tool) của ERPNext:
    - Giải pháp đơn giản nhất (về mặt độ phức tạp khi triển khai) là tạo một tệp Excel/CSV chứa dữ liệu Check-in/Check-out và sử dụng công cụ nhập dữ liệu tích hợp sẵn trong ERPNext để nhập định kỳ vào tài liệu Employee Checkin của bạn.
    - Vui lòng tham khảo [Tài liệu hướng dẫn về Công cụ Nhập dữ liệu của ERPNext](/docs/v16/user/manual/vi/setting-up/data/data-import) để biết thêm về cách thực hiện việc này.

2. Tích hợp API:
    - Bạn có thể tự động hóa quy trình nhập Nhật ký chấm công sinh trắc học bằng cách tích hợp với API có sẵn trong ERPNext.
    - API này có thể được truy cập tại: `/api/method/erpnext.hr.doctype.employee_checkin.employee_checkin.add_log_based_on_employee_field`
    - Phương thức này yêu cầu kiến thức kỹ thuật và bạn có thể cần liên hệ với đơn vị triển khai ERPNext hoặc nhà cung cấp hệ thống sinh trắc học của mình.

3. Thiết lập một script python trên máy tính của bạn để tích hợp thiết bị ZKTeco hoặc các thiết bị tương tự:
    - Phương pháp này chỉ hoạt động với thiết bị ZKTeco hoặc các thiết bị tương tự sử dụng giao thức ZKProtocol để giao tiếp qua TCP/IP.
    - Script này có sẵn tại: [github:frappe/push-biometric-erpnext](https://github.com/frappe/push-biometric-erpnext).
    - Vui lòng làm theo hướng dẫn được cung cấp trong trang của script để thiết lập trên máy tính của bạn.
    - Script này sẽ lấy nhật ký sinh trắc học từ thiết bị được hỗ trợ và sử dụng API đã đề cập ở bước trên để đẩy dữ liệu vào ERPNext.