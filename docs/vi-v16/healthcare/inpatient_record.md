<!-- add-breadcrumbs -->
# Hồ sơ nội trú
ERPNext Healthcare ghi lại tất cả các chi tiết về việc Nhập viện của Bệnh nhân bằng cách sử dụng tài liệu này.

Hồ sơ nội trú được tự động tạo khi một nhân viên y tế yêu cầu nhập viện, bạn có thể tìm thấy tài liệu này bằng cách đi tới,

`Healthcare > Patient Care > Inpatient Record`

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/ip_admission_order.png">

Nhân viên y tế có thể yêu cầu nhập viện cho bệnh nhân từ tài liệu Patient Encounter bằng cách sử dụng nút `Schedule Admission`. Thao tác này sẽ tự động tạo một Hồ sơ nội trú cho Bệnh nhân ở trạng thái _Admission Scheduled_. Sau đó, nhân viên quản lý nhập viện có thể sắp xếp một phòng trống cho Bệnh nhân theo đề xuất của nhân viên y tế chuyển tuyến trong lệnh nhập viện.

Tất cả các chi tiết do Nhân viên y tế cung cấp trong lệnh nhập viện sẽ có sẵn trong Hồ sơ nội trú, và trang tổng quan sẽ liên kết đến tất cả các tài liệu khác được tạo trong giai đoạn nhập viện, bạn cũng được phép tạo các tài liệu mới từ trang tổng quan.

> Lưu ý: Quyền ở cấp độ trường được áp dụng theo mặc định để thông tin Chẩn đoán, Hướng dẫn nhập viện và các chi tiết khác chỉ hiển thị cho người dùng có các vai trò Physician và Nursing User được kích hoạt.

Quy trình ADT của Bệnh nhân cũng được quản lý trong Hồ sơ nội trú như được mô tả trong phần [Inpatient ADT](../user/manual/en/healthcare/inpatient_adt.md).

{next}