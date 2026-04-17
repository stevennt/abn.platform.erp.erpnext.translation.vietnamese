# Điều hướng trên Cổng thông tin

## Trang chủ

Cổng thông tin được lưu trữ trên đường dẫn `/lms`. (Ví dụ: `hogwarts.erpnext.com/lms`) Tại đây, tất cả các chương trình được hiển thị dưới dạng thẻ. Mỗi thẻ đều có thể nhấp vào để điều hướng đến chương trình/khóa học/chủ đề/nội dung tương ứng. Cổng thông tin có thể truy cập ngay cả khi học viên chưa đăng nhập, tuy nhiên, nội dung (Bài viết, Video, v.v.) chỉ có thể truy cập được sau khi đăng nhập và đăng ký vào chương trình.

![LMS Navigation](https://docs.erpnext.com/docs/v16/assets/img/education/education-lmms-3.png)

## Trang Chương trình
Trên trang chương trình, học viên có thể xem phần mô tả cũng như danh sách các khóa học dưới dạng thẻ. Nếu học viên chưa đăng ký, một nút để đăng ký sẽ được hiển thị. Điều này chỉ xảy ra nếu tính năng tự đăng ký (self enroll) được bật trong DocType chương trình, nếu không, chương trình sẽ không hiển thị với học viên.

Sau khi đăng ký, trạng thái của mỗi khóa học sẽ được thêm vào phần chân của thẻ. Trạng thái này được cập nhật dựa trên hoạt động của học viên trên cổng thông tin.

![LMS Navigation](https://docs.erpnext.com/docs/v16/assets/img/education/education-navigation-1.png)

---

## Trang Khóa học
Tương tự như trang chương trình, trang này liệt kê tất cả các chủ đề cũng như trạng thái của từng chủ đề. Nhấp vào bất kỳ thẻ nào sẽ điều hướng đến trang chủ đề. Danh sách nội dung được hiển thị trong mỗi thẻ chủ đề, nhấp vào bất kỳ mục nào trong danh sách sẽ điều hướng đến nội dung đó.

![LMS Navigation](https://docs.erpnext.com/docs/v16/assets/img/education/education-lms-4.png)

---

## Trang Chủ đề
Trang chủ đề liệt kê tất cả các nội dung cũng như trạng thái hoàn thành của chúng. Nhấp vào bất kỳ thẻ nào sẽ điều hướng đến Trang nội dung:

![LMS Navigation](https://docs.erpnext.com/docs/v16/assets/img/education/education-lms-13.png)

---

## Các Trang Nội dung

Mỗi loại nội dung có chế độ xem riêng và cách điều hướng chung dựa trên loại nội dung đó.

<img alt="Portal Contents" src="https://docs.erpnext.com/docs/v16/assets/img/education/lms/content.png">

Khi học viên truy cập vào một trang nội dung cụ thể, học viên có thể điều hướng bằng các nút ở cuối nội dung.

> Lưu ý: Hoạt động của học viên chỉ được ghi lại sau khi học viên nhấp vào nút Tiếp theo (Next).

<img class="screenshot" alt="Portal Contents" src="https://docs.erpnext.com/docs/v16/assets/img/education/lms/content-navigation.png">

### Điều hướng Bài kiểm tra

Trong trường hợp là bài kiểm tra, trước tiên học viên phải Xác nhận bài kiểm tra, sau đó kết quả sẽ được tính toán và hiển thị, sau đó học viên mới có thể điều hướng đến nội dung tiếp theo.

<img class="screenshot" alt="Quiz Pass" src="https://docs.erpnext.com/docs/v16/assets/img/education/lms/quiz-pass.png">

Lần tiếp theo khi học viên truy cập trang bài kiểm tra, dựa trên các lần thử trước đó, cổng thông tin có thể cho phép hoặc không cho phép thực hiện thêm lần thử bài kiểm tra nào.
Trong trường hợp học viên đã đạt đến giới hạn tối đa, bài kiểm tra sẽ bị khóa. Điểm số trước đó dựa trên cơ sở chấm điểm của bài kiểm tra sẽ được hiển thị.
<img class="screenshot" alt="Quiz Limit" src="https://docs.erpnext.com/docs/v16/assets/img/education/lms/quiz-fail-no-attempt.png">
*Đã đạt giới hạn số lần thử tối đa*

Trong trường hợp học viên đã vượt qua bài kiểm tra, bài kiểm tra sẽ được đóng lại và điểm số sẽ được hiển thị.
<img class="screenshot" alt="Quiz Already Cleared" src="https://docs.erpnext.com/docs/v16/assets/img/education/lms/quiz-pass-cleared.png">
*Đã vượt qua bài kiểm tra*

{next}