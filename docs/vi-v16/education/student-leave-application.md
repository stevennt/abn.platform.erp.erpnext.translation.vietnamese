<!-- add-breadcrumbs -->
# Đơn xin nghỉ học của Học sinh

**Đơn xin nghỉ học của Học sinh là một tài liệu chính thức để theo dõi việc nghỉ học của học sinh.**

Để truy cập danh sách Đơn xin nghỉ học của Học sinh, hãy đi đến:

> Home > Education > Attendance > Student Leave Application

## 1 Cách tạo Đơn xin nghỉ học của Học sinh

1. Đi đến danh sách Đơn xin nghỉ học của Học sinh, và nhấn vào Mới.
2. Chọn Học sinh.
3. Thiết lập các trường 'Từ ngày' và 'Đến ngày' để chỉ định khoảng thời gian.
4. Việc đánh dấu Chấm công cho Đơn xin nghỉ học được điều khiển bởi trường 'Dựa trên Chấm công'. Trong ERPNext, Chấm công Học sinh có thể được đánh dấu theo hai cách:

    * **Lịch trình khóa học**: Nếu việc chấm công được thực hiện cho mỗi buổi học (tại các trường cao đẳng/đại học), thì đơn xin nghỉ học có thể được tạo cho khung giờ lịch trình khóa học cụ thể đó.

    * **Nhóm học sinh**: Nếu việc chấm công được thực hiện cho cả ngày, thì nhóm học sinh (lớp/khối) sẽ được sử dụng để đánh dấu chấm công để việc nghỉ học được tính cho cả ngày.

5. Dựa trên trường Chấm công, hãy chọn Nhóm học sinh hoặc Lịch trình khóa học. Có thể nhập thêm lý do.
6. Trong trường hợp học sinh không đến trường để tham gia hoặc đại diện cho trường trong bất kỳ sự kiện nào, học sinh đó có thể được đánh dấu là "Có mặt" ngay từ chính Đơn xin nghỉ học bằng cách tích vào ô _Đánh dấu là Có mặt_.
7. Lưu. 'Tổng số ngày nghỉ' sẽ được tính toán và thiết lập trong tài liệu sau khi loại trừ các ngày lễ nằm trong [Danh sách ngày lễ](/docs/v16/user/manual/en/human-resources/holiday-list) mặc định của bạn.

    ![Student Leave Application](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/student-leave-application.png)

### 1.2 Khi Xác nhận Đơn xin nghỉ học của Học sinh

Sau khi Đơn xin nghỉ học của Học sinh được Xác nhận, một bản ghi Chấm công Học sinh sẽ tự động được tạo với trạng thái là 'Vắng mặt'. Nếu ô _Đánh dấu là Có mặt_ được tích, thì trạng thái của Bản ghi Chấm công sẽ được thiết lập là 'Có mặt'. Đơn xin nghỉ học được liên kết với tài liệu Chấm công Học sinh này để tham chiếu.

![Student Attendance](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/leave-attendance-record.png)

Nếu bất kỳ ngày nào trong thời gian nghỉ là ngày lễ, thì việc tạo bản ghi Chấm công Học sinh cho ngày đó sẽ được bỏ qua.

### 1.3 Khi Hủy Đơn xin nghỉ học của Học sinh

Khi Hủy Đơn xin nghỉ học của Học sinh, bản ghi Chấm công Học sinh được liên kết cũng sẽ tự động bị Hủy.

## 2. Video hướng dẫn về Đơn xin nghỉ học của Học sinh

<div>
    <div class='embed-container'>
        <iframe src='https://www.youtube.com/embed/NwwH5t-NKBE' frameborder='0' allowfullscreen>
        </iframe>
    </div>
</div>

## 3. Các chủ đề liên quan

1. [Chấm công Học sinh](/docs/v16/user/manual/en/education/student-attendance).

{next}