<!-- add-breadcrumbs -->
# Hệ thống Điểm Năng lượng

**Hệ thống Điểm Năng lượng là một hệ thống xếp hạng/nghiệp lực (karma) mà bạn có thể kích hoạt cho tổ chức của mình.**

Hệ thống này có thể được sử dụng để theo dõi hiệu suất của từng người dùng.

> Để kích hoạt Hệ thống Điểm Năng lượng, hãy đi đến **Energy Point Settings**
 > tích chọn **Enabled**.


## 1. Cách sử dụng Hệ thống Điểm Năng lượng?
Để bắt đầu sử dụng hệ thống này, bạn cần tạo một số Quy tắc Điểm Năng lượng (xem phần 3. Cách tạo Quy tắc Điểm Năng lượng?) để người dùng có thể nhận được điểm năng lượng dựa trên các hoạt động của họ.

## 2. Quy tắc Điểm Năng lượng là gì?
Quy tắc Điểm Năng lượng lưu trữ thông tin về hoạt động và giá trị điểm sẽ được phân bổ.

Quy tắc Điểm Năng lượng có các trường sau:

| Trường | Mô tả |
| ------------- |:-------------|
| Reference DocType| Loại tài liệu mà bạn muốn áp dụng quy tắc, ví dụ: Task, ToDo, Issue, v.v. |
| For Document Event| Các tùy chọn: Lưu, Xác nhận, Hủy, và Custom.<br>**Lưu ý:** Nếu tùy chọn "Custom" được chọn, trường "Conditions" sẽ trở thành bắt buộc|
| Points | Số điểm được phân bổ.|
| Allot Points To Assigned Users | Nếu được tích, những người dùng được chỉ định trong tài liệu tham chiếu sẽ nhận được điểm. Ví dụ: Nếu người dùng Reema và Jai được chỉ định cho một Task cụ thể, thì cả hai người là Reema và Jai sẽ nhận được điểm khi tài liệu thỏa mãn điều kiện|
| User Field | Trường mà người dùng sẽ được chọn từ đó, ví dụ có thể dùng `Resolved By`, `Modified By`, `Owner`, v.v. Nếu `Modified By` được chọn, người cuối cùng thỏa mãn điều kiện của tài liệu sẽ nhận được điểm. |
| Multiplier Field | Trường lưu trữ giá trị cho hệ số nhân. Trường này có thể nhận các giá trị số và số thập phân, giá trị này sẽ được nhân với số điểm đã xác định trong quy tắc. <br> Ví dụ: 2 (hệ số nhân) * 10 (điểm thiết lập trong quy tắc) = 20 điểm |
| Condition | Điều kiện để phân bổ điểm. <br>ví dụ: `doc.status == 'Closed'`<br>Điều kiện trên sẽ kiểm tra xem trường `status` trong tài liệu có phải là 'Closed' hay không, và nếu đúng, điểm sẽ được phân bổ cho người dùng. |
| Apply Only Once | Quy tắc sẽ chỉ được áp dụng một lần duy nhất cho mỗi tài liệu.|

> **Lưu ý:** User Field và Multiplier Field được lấy từ DocType tham chiếu.

## 3. Cách tạo Quy tắc Điểm Năng lượng?

> Tìm kiếm **Energy Point Rule** > tạo mới Energy Point Rule

Hãy xem ví dụ về quy tắc sau:
<img class="screenshot" src="../assets/img/setup/energy-point-system/issue-closed-rule.png">
Ảnh chụp màn hình trên là quy tắc cho việc **Đóng Issue (Issue Closing)**.
Vì vậy, khi bất kỳ người dùng nào đóng issue, họ sẽ được thưởng **10** điểm.

Các trường hợp khác có thể được xử lý tương tự.

Giả sử, bạn muốn tạo một quy tắc nơi người dùng nhận được điểm khi hoàn thành một task,
bạn có thể thực hiện bằng cách tạo quy tắc sau:
<img class="screenshot" src="../assets/img/setup/energy-point-system/task-complete-rule.png">


## 4. Các tính năng:

### 4.1 Tự động phân bổ điểm
Dựa trên các quy tắc điểm năng lượng đã tạo, người dùng sẽ tự động nhận được điểm khi họ hoàn thành các hoạt động được theo dõi bằng Hệ thống Điểm Năng lượng.

### 4.2 Hệ thống Đánh giá
Hệ thống đánh giá có thể được sử dụng để "Khen ngợi" hoặc "Phê bình" công việc của ai đó.

Xem GIF sau để biết quy trình đánh giá.
<img class="screenshot" src="../assets/img/setup/energy-point-system/review-system.gif">
Để đánh giá, người dùng cần có điểm đánh giá, điểm này có thể được chỉ định bởi Quản trị viên hệ thống thông qua **Energy Point Settings**.

Bạn cũng có thể thiết lập tự động phân bổ điểm đánh giá từ 'Energy Point Settings':
<img class="screenshot" src="../assets/img/setup/energy-point-system/auto-review-point-allocation.png">

### 4.3 Bảng xếp hạng
Đi đến Social Home > Leaderboard (thanh điều hướng bên)

Bảng xếp hạng hiển thị thứ hạng của người dùng trong tổ chức.

<img class="screenshot" src="../assets/img/setup/energy-point-system/leaderboard.png">

### 5. Các chủ đề liên quan
1. [Milestone Tracking](../user/manual/en/automation/milestone-tracker)