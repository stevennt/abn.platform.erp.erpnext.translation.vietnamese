# Theo dõi Tiến độ

Học viên có thể xem tiến độ của mình ngay trên cổng thông tin và không có quyền truy cập vào desk. Đối với giảng viên và những người dùng khác của ERPNext, các DocType sau đây được sử dụng để theo dõi tiến độ của học viên:

- Program Enrollment
- Course Enrollment
- Course Activity
- Quiz Activity

---

## Program Enrollment

Nếu 'Allow Self Enroll' được bật cho một chương trình cụ thể, một bản ghi sẽ được tạo tự động thay mặt cho học viên. Mỗi học viên sẽ chỉ có một bản ghi đăng ký chương trình cho mỗi chương trình. Bạn có thể tìm hiểu thêm về đăng ký chương trình [tại đây]({{ docs_base_url }}/user/manual/vi/education/program-enrollment)
<img class="screenshot" alt="Program Enrollment" src="https://docs.erpnext.com/docs/v16/assets/img/education/lms/desk-program-enrollment.png">

---

## Course Enrollment

Đối với một khóa học cụ thể trong một chương trình, một bản ghi đăng ký khóa học sẽ được tạo tự động cho mỗi khóa học như hiển thị dưới đây.
<img class="screenshot" alt="Course Enrollment List" src="https://docs.erpnext.com/docs/v16/assets/img/education/lms/desk-course-enrollment-list.png">

Đối với một chương trình cụ thể và các khóa học con của nó, chỉ có một bản ghi đăng ký khóa học được tạo cho một học viên. Trong trường hợp một khóa học được thêm vào chương trình sau đó, học viên sẽ tự động được đăng ký vào khóa học đó khi học viên truy cập vào cổng thông tin lần tiếp theo.

---

## Course Activity

Đối với mỗi nội dung không phải loại bài kiểm tra (quiz) trong một khóa học, một hoạt động khóa học sẽ được tạo ra mỗi khi học viên xem qua nội dung đó. Hoạt động này chỉ được tạo một lần cho mỗi nội dung.

<img class="screenshot" alt="Course Activity List" src="https://docs.erpnext.com/docs/v16/assets/img/education/lms/desk-course-activity-list.png">
<img class="screenshot" alt="Course Activity" src="https://docs.erpnext.com/docs/v16/assets/img/education/lms/desk-course-activity.png">

---

## Quiz Activity

Đối với mỗi lần làm bài kiểm tra, cho đến khi học viên được phép làm bài, một hoạt động bài kiểm tra sẽ được tạo. DocType này có tất cả thông tin về lần làm bài, cụ thể là: các tùy chọn đã chọn cho mỗi câu hỏi, ngày làm bài, kết quả bài kiểm tra, và thời gian hoàn thành nếu bài kiểm tra bị giới hạn thời gian.

<img class="screenshot" alt="Quiz Activity" src="https://docs.erpnext.com/docs/v16/assets/img/education/lms/desk-quiz-activity.png">