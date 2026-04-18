<!-- add-breadcrumbs -->
# Đánh giá

**Đánh giá hiệu suất là một phương pháp để ghi chép và đánh giá kết quả công việc của một nhân viên.**

Trong ERPNext, bạn có thể quản lý Đánh giá nhân viên bằng cách tạo Mẫu đánh giá cho từng vị trí với các tham số xác định hiệu suất bằng cách đưa ra trọng số phù hợp cho từng tham số.


Để truy cập Đánh giá, hãy đi tới:

> Human Resources > Performance > Appraisal

## 1. Điều kiện tiên quyết

Trước khi tạo Đánh giá, hãy đảm bảo bạn đã tạo các mục sau:

* [Employee](employee.md)

## 2. Cách tạo Đánh giá

1. Đi tới: Appraisal > New.
1. Chọn Mẫu đánh giá. Nếu chưa có, hãy tạo một Mẫu đánh giá. Nhập Tên mẫu đánh giá và các Khu vực kết quả chính (KRAs) cùng với trọng số của chúng.

    <img class="screenshot" alt="Appraisal" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/appraisal-template.png">


1. Sau khi chọn Mẫu đánh giá, hãy chọn Nhân viên, Ngày bắt đầu và Ngày kết thúc.
1. Dựa trên mẫu đã chọn, các KRA sẽ được lấy vào phần Mục tiêu. Nhập điểm (0-5) cho mỗi KRA. Dựa trên trọng số đã nêu, Điểm đạt được sẽ được tính toán cho mỗi KRA.
1. Lưu và Xác nhận.

    <img class="screenshot" alt="Appraisal" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/appraisal.png">



Dựa trên số điểm đã nhập cho mỗi KRA, hệ thống sẽ tính toán Tổng điểm (trên thang điểm 5) cho Nhân viên.

## 3. Các chủ đề liên quan

1. [Energy Point](../setting-up/energy-point-system.md)