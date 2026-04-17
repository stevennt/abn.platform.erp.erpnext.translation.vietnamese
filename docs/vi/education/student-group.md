<!-- add-breadcrumbs -->
# Nhóm học sinh

**Nhóm học sinh là một tập hợp các học sinh cùng khóa hoặc cùng học một khóa học.**

Ví dụ, nếu một nhóm học sinh cùng học một chương trình sẽ được gọi là một khóa học sinh (student batch), thì từ trong nhóm này, một nhóm các học sinh đã đăng ký cùng một khóa học tự chọn sẽ được gọi là Nhóm học sinh (Student Group).

![Student Group](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/education-student-workflow.png)

Để truy cập Nhóm học sinh, hãy đi tới:

> Home > Education > Student > Student group

## 1. Điều kiện tiên quyết

Trước khi tạo Nhóm học sinh, bạn nên tạo các mục sau trước:

1. [Student](/docs/v13/user/manual/en/education/student)
1. [Program Enrollment](/docs/v13/user/manual/en/education/program-enrollment)
1. [Student Batch name](/docs/v13/user/manual/en/education/student-batch-name)
1. [Student Category](/docs/v13/user/manual/en/education/student-category)
1. [Instructor](/docs/v13/user/manual/en/education/instructor)

## 2. Tạo Nhóm học sinh

1. Đi tới Danh sách Nhóm học sinh và nhấn New.
1. **Group Based On**: Chọn cơ sở mà bạn muốn tạo nhóm học sinh. Có ba tùy chọn sẵn có là:
    * Batch: Danh sách tất cả học sinh trong một khóa học cụ thể sẽ được lấy ra trong trường hợp này.
    * Course: Danh sách tất cả học sinh đã đăng ký một khóa học cụ thể sẽ được lấy ra trong trường hợp này.
    * Activity: Bạn có thể chọn tùy chọn này khi muốn tạo một nhóm học sinh cho các hoạt động nhất định diễn ra trong trường.
1. **Student Group Name**: Nhập tên của nhóm học sinh.
1. Lưu.

![Student Group](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/education-student-group-1)

### 2.1. Các tùy chọn bổ sung khi tạo Nhóm học sinh

Ngoài các tùy chọn bắt buộc ở trên, các trường sau cũng cần được điền vào biểu mẫu để tạo Nhóm học sinh:

1. Chọn **Academic Year** và **Academic Term** mà Nhóm học sinh này được tạo cho.
1. **Program**: Chọn Chương trình mà Nhóm học sinh này được tạo cho.
1. **Batch**: Chọn Khóa học mà bạn muốn lấy danh sách học sinh cho nhóm học sinh.
1. **Max Strength**: Nhập Số lượng học sinh tối đa có thể tham gia Nhóm học sinh này. Nếu số lượng học sinh được chọn trong nhóm nhiều hơn Max Strength, hệ thống sẽ không cho phép bạn Lưu nhóm này và một thông báo lỗi sẽ hiển thị.

    ![Student Group](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/education-student-group-max-student-limit-error.png)

1. **Student Category**: Nếu bạn muốn học sinh thuộc một danh mục cụ thể tham gia nhóm này, bạn có thể chọn danh mục đó.
1. **Course**: Tùy chọn này chỉ xuất hiện khi Nhóm được Dựa trên Khóa học (Based on a Course). Bạn có thể chọn một khóa học cụ thể tại đây, và danh sách chỉ những học sinh đã đăng ký khóa học này sẽ được lấy ra để tạo nhóm học sinh này.

### 2.2. Các tính năng:

* **Students**: Nhập tên của các học sinh mà bạn muốn thêm vào Nhóm học sinh này. Danh sách học sinh sẽ được lấy ra theo các tham số đã chọn ở trên, như Năm học (Academic Year), Học kỳ (Academic Term), Khóa học (Batch), Chương trình (Program), Khóa học (Course), v.v.

* **Get Students**: Dựa trên các tham số đã chọn ở trên, hệ thống sẽ tự động lấy danh sách học sinh, và tất cả các học sinh có tiêu chí khớp với Nhóm học sinh sẽ được liệt kê trong danh sách Học sinh sau khi bạn nhấn 'Get students'.

 > Lưu ý: Bạn phải chọn học sinh một cách Thủ công cho nhóm Dựa trên Hoạt động (Activity-Based) vì nhóm này có thể không có bất kỳ tiêu chí xác định nào và bất kỳ học sinh nào cũng có thể được chọn để thêm vào nhóm này. Nút **Get Students** sẽ không hoạt động trong trường hợp này.

* **Instructors**: Chọn các Giảng viên sẽ giảng dạy hoặc hướng dẫn nhóm học sinh cụ thể này.

![Student Group](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/education-student-group-4.png)

## 3. Sau khi tạo Nhóm học sinh

Sau khi nhóm học sinh đã được tạo và Lưu, các mục sau có thể được tạo từ Nhóm học sinh:

1. **Attendance**: Bạn sẽ được chuyển hướng đến [Student Attendance Tool](/docs/v13/user/manual/en/education/student-attendance-tool), qua đó bạn có thể điểm danh cho tất cả học sinh vào một ngày cụ thể.
1. **Course Schedule**: Bạn sẽ được chuyển hướng đến [Course Schedule](/docs/v13/user/manual/en/education/course-schedule), tại đây bạn có thể xem lịch trình cho nhóm học sinh này và sau đó bạn cũng có thể tạo Lịch học mới cho các học sinh trong nhóm này.
1. **Assessment Plan**: Bạn sẽ được chuyển hướng đến danh sách [Assessment Plan](/docs/v13/user/manual/en/education/assessment_plan), nơi tất cả các kế hoạch đánh giá cho nhóm học sinh của bạn sẽ được liệt kê và bạn cũng sẽ được phép tạo Kế hoạch đánh giá mới cho nhóm.
1. **Update Email Group**: Khi bạn chọn tùy chọn này, các Địa chỉ Email của Học sinh trong nhóm này sẽ được thêm vào Nhóm Email và bạn sẽ có thể gửi bản tin cho tất cả những người đăng ký trong Nhóm học sinh này.

    ![Student Group](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/education-student-group-update-email.png)

1. **Newsletters**: Bạn sẽ có thể gửi [Newsletters](/docs/v13/user/manual/en/CRM/newsletter) đến tất cả những người đăng ký từ trong nhóm học sinh với tùy chọn này.

![Student Group](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/education-student-group-4.png)



## 4. Video

<div>
    <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }
    </style>
    <div class='embed-container'>
        <iframe src='https://www.youtube.com/embed/5K_smeeE1Q4'
        frameborder='0' allowfullscreen>
        </iframe>
    </div>
</div>

{next}