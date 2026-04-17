<!-- add-breadcrumbs -->

# Loại trị liệu

> Được giới thiệu trong Phiên bản 13

Với tư cách là chuyên gia trị liệu, bạn có thể chỉ định nhiều loại trị liệu khác nhau cho bệnh nhân, từ Tập luyện chi trên cường độ cao đến Vận động chức năng, v.v. Mỗi liệu pháp có thể bao gồm một bộ các bài tập. ERPNext giúp bạn tạo mẫu cho các liệu pháp bằng cách sử dụng DocType "Loại trị liệu". Với tính năng này, bạn có thể tạo và liên kết các liệu pháp với Đơn vị dịch vụ y tế, thêm đơn giá tiêu chuẩn và chi tiết Mặt hàng để lập hóa đơn, đồng thời thêm các bài tập theo Bộ phận cơ thể.

Để tạo một Loại bài tập, hãy đi tới:

> Trang chủ > Y tế > Phục hồi chức năng và Vật lý trị liệu > Loại trị liệu

## 1. Cách tạo Loại trị liệu

1. Đi tới danh sách Loại trị liệu, nhấn vào Mới.
2. Nhập Tên trị liệu duy nhất.
3. Nhập chi tiết Mặt hàng như Mã mặt hàng, Tên mặt hàng, Nhóm mặt hàng và có thể thêm mô tả.
4. Tích chọn "Is Billable" (Có thể lập hóa đơn) nếu Loại trị liệu này sẽ được tính phí và nhập đơn giá cho một buổi trị liệu.
5. Bạn có thể tùy chọn thêm thời lượng mặc định cho một buổi trị liệu, thời lượng này sẽ được sử dụng khi đặt lịch hẹn cho liệu pháp đó.
6. Bạn cũng có thể thêm Đơn vị dịch vụ y tế và Khoa y tế cho Loại trị liệu.
7. Lưu.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v13/assets/img/healthcare/therapy-type.png">

## 2. Các tính năng

### 2.1 Thêm bài tập theo Bộ phận cơ thể

Nhiều khi, bạn có thể cần chỉ định các bài tập đặc thù cho các bộ phận cơ thể bị ảnh hưởng của Bệnh nhân. Bạn có thể dễ dàng thêm các Bộ phận cơ thể này vào trường _Therapy For_ (Trị liệu cho) và nhấp vào *Add Exercises* (Thêm bài tập) để thêm các Loại bài tập cho các bộ phận cơ thể đó. Để làm được điều này, bạn sẽ phải liên kết Loại bài tập với Bộ phận cơ thể trong tài liệu Loại bài tập.

Ví dụ:

- Bài tập "Wall Pushups" (Chống đẩy với tường) dành cho Tay, Cơ và Khớp.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v13/assets/img/healthcare/exercise-1.png">

- Bài tập "Sit to Stand" (Ngồi đứng) dành cho Chân và Cơ lõi.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v13/assets/img/healthcare/exercise-2.png">

- Bài tập "Thera-band Upper Body" (Dây kháng lực thân trên) dành cho Cơ, Khớp, Lưng, Chân.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v13/assets/img/healthcare/exercise-3.png">

Sau đó, khi tạo mẫu Loại trị liệu, bạn có thể chọn các bộ phận cơ thể trong trường "Therapy For" và các bài tập cho các Bộ phận cơ thể đó sẽ được thêm vào bảng Bài tập.

<img class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/healthcare/add-exercises.gif">

### 2.2 Vô hiệu hóa Loại trị liệu

Bạn cũng có thể vô hiệu hóa một số Loại trị liệu nếu bạn không thực hiện các buổi trị liệu đó. Ví dụ: Khoa Vật lý trị liệu của bạn đang được sửa chữa và một số Đơn vị dịch vụ y tế như hồ Trị liệu dưới nước không sẵn dụng, khi đó bạn có thể thiết lập tài liệu ở trạng thái vô hiệu hóa và nó sẽ bị lọc bỏ khi đặt lịch hẹn hoặc chỉ định trị liệu trong Gặp gỡ bệnh nhân, v.v.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v13/assets/img/healthcare/therapy-disabled.png">

### 2.3 Thay đổi Mã mặt hàng

Bạn cũng có thể thay đổi Mã mặt hàng sẽ được sử dụng để lập hóa đơn ngay từ màn hình Loại trị liệu. Nhấp vào nút **Change Item Code** (Thay đổi mã mặt hàng), nhập Mã mặt hàng mới và nhấp vào "Change Item Code" trong hộp thoại. Mặt hàng sẽ được đổi tên.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v13/assets/img/healthcare/therapy-change-item-code.png">

### 2.4 Chỉ định trị liệu trong Gặp gỡ bệnh nhân

Bạn có thể chỉ định các liệu pháp trong Gặp gỡ bệnh nhân và một Kế hoạch trị liệu sẽ được tự động tạo sau khi Xác nhận.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v13/assets/img/healthcare/therapy-encounter.jpg">

### 2.5 Đặt lịch hẹn cho Loại trị liệu

Để đặt Lịch hẹn bệnh nhân cho bất kỳ Loại trị liệu nào, hãy chọn liệu pháp trong trường _Therapy_ (Trị liệu). Bạn cũng có thể sử dụng nút **Get Prescribed Therapies** (Lấy các trị liệu đã chỉ định) để lấy tất cả các liệu pháp đã được chỉ định cho Bệnh nhân đó trong lần Gặp gỡ bệnh nhân trước đó.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v13/assets/img/healthcare/therapy-appointment.png">

## 3. Các chủ đề liên quan
1. [Loại bài tập](/docs/v13/user/manual/en/healthcare/exercise_type)
1. [Kế hoạch trị liệu](/docs/v13/user/manual/en/healthcare/therapy_plan)
1. [Buổi trị liệu](/docs/v13/user/manual/en/healthcare/therapy_session)
1. [Lịch hẹn bệnh nhân](/docs/v13/user/manual/en/healthcare/patient_appointment)
1. [Gặp gỡ bệnh nhân](/docs/v13/user/manual/en/healthcare/patient_encounter)

{next}