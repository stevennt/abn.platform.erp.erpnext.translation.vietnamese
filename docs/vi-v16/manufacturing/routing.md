<!-- add-breadcrumbs -->
# Quy trình sản xuất

**Quy trình sản xuất là một mẫu của các Công đoạn trong BOM.**

Một Quy trình sản xuất lưu trữ tất cả các Công đoạn cùng với mô tả, đơn giá giờ, thời gian thực hiện công đoạn, kích thước lô, v.v. Việc tạo một Quy trình sản xuất cho các Công đoạn trong BOM sẽ rất hữu ích khi các Công đoạn tương tự được sử dụng để sản xuất các mặt hàng khác nhau.

Để truy cập danh sách Quy trình sản xuất, hãy đi tới:
> Home > Manufacturing > Bill of Materials > Routing

## 1. Điều kiện tiên quyết
* [Operation](/docs/v16/user/manual/vi/manufacturing/operation)
* [Workstation](/docs/v16/user/manual/vi/manufacturing/workstation)

## 2. Cách tạo Quy trình sản xuất
1. Đi tới danh sách Quy trình sản xuất, nhấn vào **Mới**.
1. Nhập tên cho Quy trình sản xuất.
1. Nhập các Công đoạn vào bảng BOM Operation:
    1. Chọn Công đoạn (Operation).
    1. Trạm làm việc (Workstation) mặc định sẽ được lấy tự động.
    1. Nhập Đơn giá giờ (Hourly Rate) để thực hiện Công đoạn này.
    1. Nhập Thời gian thực hiện công đoạn (Operation Time) theo phút.
    1. Nhập Kích thước lô (Batch Size), tức là số lượng đơn vị được xử lý trong Công đoạn này.
    1. Chi phí vận hành (Operating Cost) sẽ được tính toán dựa trên Đơn giá giờ và Thời gian thực hiện công đoạn.
1. **Lưu**.

    ![Routing](https://docs.erpnext.com/docs/v16/assets/img/manufacturing/routing.png)

Sau khi được tạo, một Quy trình sản xuất có thể được chọn trong BOM để lấy các Công đoạn đã được lưu trong Quy trình đó.
![Routing BOM](https://docs.erpnext.com/docs/v16/assets/img/manufacturing/routing-bom.png)

## 3. Sequence ID trong Quy trình sản xuất
![Routing Sequence ID](https://docs.erpnext.com/docs/v16/assets/img/manufacturing/sequence-id-routing.png)
Sequence ID bắt buộc người dùng phải hoàn thành các công đoạn theo trình tự thông qua Thẻ công việc (Job Card). Trong trường hợp người dùng cố gắng hoàn thành một công đoạn trước khi hoàn thành bất kỳ công đoạn tiền đề nào theo Sequence ID, hệ thống sẽ báo lỗi xác thực.

<!-- ![Error](https://docs.erpnext.com/docs/v16/assets/img/manufacturing/sequence-id-error.png) -->

## 4. Các chủ đề liên quan
1. [Work Order](/docs/v16/user/manual/vi/manufacturing/work-order)
1. [Bill Of Materials](/docs/v16/user/manual/vi/manufacturing/bill-of-materials)

{next}