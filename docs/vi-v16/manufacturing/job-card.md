---
parent: ../manufacturing/work-order.md
---

# Thẻ công việc

**Thẻ công việc lưu trữ thông tin sản xuất thực tế về một Công đoạn cụ thể được thực hiện tại một Nơi làm việc cụ thể.**

Thẻ công việc được tạo từ Lệnh sản xuất và được chuyển đến từng Nơi làm việc tại xưởng sản xuất để bắt đầu sản xuất một mặt hàng với số lượng nhất định trong mỗi công đoạn được xác định trong Lệnh sản xuất.

Thẻ công việc cho phép nơi làm việc của mỗi Công đoạn tạo "Yêu cầu vật tư" và "Chuyển kho để sản xuất" cho nguyên vật liệu cần thiết dựa trên "Thẻ công việc".

Việc hoàn thành Thẻ công việc sẽ thay đổi trạng thái sản xuất trong Lệnh sản xuất, chúng ta có thể theo dõi tiến độ hoàn thành sản xuất cho từng Công đoạn được xác định trong Lệnh sản xuất.

<img class="screenshot" alt="Work Order" src="../assets/img/manufacturing/manufacturing-flow-jc.png">

Để truy cập danh sách Thẻ công việc, hãy đi tới:
> Trang chủ > Sản xuất > Sản xuất > Thẻ công việc

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Thẻ công việc, bạn nên tạo các mục sau trước:

* [Định mức nguyên vật liệu](../manufacturing/bill-of-materials.md)
* [Công đoạn](../manufacturing/operation.md)
* [Nơi làm việc](../manufacturing/workstation.md)
* [Lệnh sản xuất](../manufacturing/work-order.md)

## 2. Cách tạo Thẻ công việc
Thẻ công việc cho các Công đoạn sẽ được tự động tạo khi Lệnh sản xuất được Xác nhận.

Đây là giao diện của một Thẻ công việc:

![Job Card](https://docs.erpnext.com/docs/v16/assets/img/manufacturing/job-card.png)

Để sử dụng Thẻ công việc, hãy làm theo các bước sau:

1. Nhấp vào nút Bắt đầu công việc (Start Job), sau đó nhấn Hoàn thành công việc (Complete Job) khi bạn làm xong.
2. Ngoài ra, bạn cũng có thể điền Thời gian bắt đầu (From Time) và Thời gian kết thúc (To Time) trong bảng Nhật ký thời gian (Time Logs).
3. Chọn Nhân viên được giao Thẻ công việc.
4. Nhập Số lượng hoàn thành (Completed Quantity). Đây là số lượng Mặt hàng mà Công đoạn đã thực hiện trong khoảng thời gian được chọn.
5. Thêm nhiều dòng hơn trong bảng Nhật ký thời gian và ghi lại thời gian bằng các nút Bắt đầu/Hoàn thành.
6. Nhấp vào Xác nhận.

Trong một Lệnh sản xuất, các Công đoạn và Nơi làm việc được lấy từ BOM của một Mặt hàng. Để dễ sử dụng, bạn nên đảm bảo rằng [Quy trình định tuyến](../manufacturing/routing.md) đã được cấu hình trong BOM.

Mỗi Thẻ công việc được tạo sẽ có Nơi làm việc & Công đoạn được chỉ định. Nguyên vật liệu cần thiết từ mỗi Kho nguồn sẽ được tính toán dựa trên số lượng cần thiết để sản xuất.

Khi Xác nhận một Lệnh sản xuất, các Thẻ công việc sẽ được tự động tạo dựa trên các giá trị trong bảng Công đoạn.

<img class="screenshot" alt="Create Shareholder" src="../assets/img/manufacturing/work-order-job-card-creation.gif">

### 2.1 Chọn Lệnh sản xuất với Mặt hàng cần sản xuất

Bạn có thể chọn 'Chuyển vật tư theo' (Transfer Material Against) là 'Thẻ công việc' (Job Card) trên Định mức nguyên vật liệu để chuyển nguyên vật liệu cho Sản xuất theo Thẻ công việc.

Trong Lệnh sản xuất, bạn có thể chọn tùy chọn:

<img class="screenshot" alt="Create Shareholder" src="../assets/img/manufacturing/work-order-transfer-against-job-card.png">

### 2.3 Sử dụng Thẻ công việc

Việc phân công Nhân viên và chi tiết thời gian cũng sẽ được xác định trong Thẻ công việc. Thời gian thực hiện một công việc có thể được ghi lại. Nếu có nhiều nhân viên cùng làm việc trên một Công đoạn, hãy thêm các thẻ công việc mới bằng cách nhấp vào nút 'Tạo thẻ công việc' (Create Job Card).

<img class="screenshot" alt="Create Shareholder" src="../assets/img/manufacturing/job-card-form.png">

### 2.4 Yêu cầu vật tư theo Thẻ công việc

Một Yêu cầu vật tư sẽ được tạo từ Thẻ công việc để làm cơ sở/đơn hàng chuẩn bị nguyên vật liệu cần thiết cho quá trình sản xuất. Yêu cầu vật tư được tạo sẽ có tham chiếu đến số Thẻ công việc gốc.

<img class="screenshot" alt="Create Shareholder" src="../assets/img/manufacturing/material-request-against-job-card.png">

Theo dõi Tiến độ sản xuất trong Lệnh sản xuất bằng việc Hoàn thành từng Công đoạn được xác định trong Lệnh sản xuất.

Việc hoàn thành Thẻ công việc cho phép bạn theo dõi tiến độ sản xuất bên trong Lệnh sản xuất bằng cách xem xét việc hoàn thành của từng Công đoạn liên quan đến Lệnh sản xuất đó.

<img class="screenshot" alt="Work Order Job Card Completion" src="../assets/img/manufacturing/work-order-job-card-completion.png">

## 3. Các tính năng

### 3.1 Theo dõi Kiểm tra chất lượng

Đối với các lệnh sản xuất, chất lượng của hàng hóa đang trong quá trình sản xuất (bán thành phẩm) cũng cần được theo dõi. Nó được xác định bởi quy trình (công đoạn) thực hiện trên đó, mà quy trình này lại được xác định trong Thẻ công việc. Các kiểm tra trong quá trình sản xuất khác với kiểm tra vật tư đầu vào và đầu ra. Việc giám sát chất lượng trong quá trình sản xuất giúp đảm bảo rằng thành phẩm được tạo ra đạt chất lượng mong muốn. Bạn có thể tạo một Kiểm tra chất lượng cho Mặt hàng sản xuất dựa trên Thẻ công việc.

<img class="screenshot" alt="Quality Inspection Against Job Card" src="../assets/img/manufacturing/qi-against-job-card.png">

<img class="screenshot" alt="Quality Inspection link in Job Card" src="../assets/img/manufacturing/qi-link-in-job-card.png">

Để biết thêm chi tiết, hãy tham khảo trang [Kiểm tra chất lượng](../stock/quality-inspection.md).

{next}