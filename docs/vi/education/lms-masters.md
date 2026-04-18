# Thiết lập các Master cho Hệ thống Quản lý Học tập (LMS)

Hệ thống Quản lý Học tập của ERPNext sử dụng các master sau để hiển thị nội dung trên cổng thông tin.

![LMS Setting](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/education-lms-masters.png)

---

## 1. Chương trình (Programs)
Để Chương trình có thể truy cập được trên cổng thông tin, hãy tích vào ô 'Is Published' trong biểu mẫu Chương trình. Bạn cũng có thể tích vào ô 'Is Featured' để hiển thị chương trình đó trên trang chủ của cổng thông tin. Cổng thông tin sẽ tự động lấy các khóa học từ bảng khóa học trong chương trình.

## 2. Cài đặt Cổng thông tin (Portal Settings)
Trên cổng thông tin, để học viên có thể xem các chương trình, một chương trình phải được đánh dấu là Đã xuất bản (Published). Trên cổng thông tin, học viên sẽ chỉ có thể thấy những khóa học mà họ đã đăng ký hoặc được phép đăng ký.

Nếu không tích vào 'Allow Self Enroll', chương trình sẽ chỉ hiển thị với những học viên đã đăng ký vào chương trình đó, bằng cách này bạn có thể tổ chức các chương trình riêng tư trên cổng thông tin của mình.

![LMS Setting](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/education-lms-settings-1.png)

![LMS Setting](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/education-lms-3.png)

Đọc về [Program](program.md) để biết thêm chi tiết.

---

## 3. Khóa học (Courses)

Đối với mỗi khóa học trong một chương trình cụ thể, bạn có thể thiết lập phần giới thiệu khóa học và hình ảnh đại diện (hero image) để sử dụng trên cổng thông tin. Có một bảng để thêm các chủ đề, các chủ đề này sẽ được hiển thị trên LMS cho tất cả học viên đã đăng ký.

![LMS Setting](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/education-lms-4.png)

Đọc [Courses](course.md) để tìm hiểu thêm.

---

## 4. Chủ đề (Topics)
Tương tự như khóa học, Chủ đề có một bảng nơi bạn có thể thêm nội dung. Bạn có thể thêm ba loại nội dung khác nhau bao gồm: Video, Bài viết và Câu đố (Quiz).

![LMS Setting](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/education-lms-13.png)

Đọc [Topics](topic.md) để tìm hiểu thêm.

---

## 5. Content Masters
Các Bài viết, Câu đố & Video đều được phân loại dưới Content Masters, để thêm bất kỳ bài viết hoặc video nào, bạn chỉ cần điều hướng đến chế độ xem danh sách của master đó và nhấp vào nút **New**

> Education > Content Masters > Article > New Article

### 5.1 Bài viết (Articles)
Việc thêm bài viết khá đơn giản, trường nội dung là một trường văn bản giàu định dạng (rich-text), bạn có thể thêm hình ảnh, bảng, liên kết và nhiều thứ khác vào bài viết của mình. Có một trường tiêu đề được sử dụng làm tên của bài viết để dùng trong các liên kết, tiêu đề này sẽ được hiển thị trên cổng thông tin.
Các chi tiết khác bao gồm Tác giả (Author) và Ngày xuất bản (Publish Date), đây là các trường tùy chọn và có thể được sử dụng để ghi nhận nguồn tài liệu.

![LMS Setting](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/education-lms-8.png)

Bài viết sẽ được xuất bản nếu chương trình cha của nó được xuất bản, nó sẽ hiển thị như sau trên cổng thông tin.

![LMS Setting](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/education-lms-settings-8.png)

### 5.2 Video

Video có thể được thêm từ cả Vimeo và YouTube, sử dụng DocType [Video](../using-erpnext/video.md). Nhà cung cấp phù hợp phải được thiết lập, nhưng theo mặc định, nhà cung cấp được đặt là YouTube.

Trường Tiêu đề (Title) lưu trữ tên của tài liệu cũng như tiêu đề sẽ được hiển thị trên cổng thông tin. Bạn cũng có thể thêm ngày xuất bản cũng như thời lượng của video tính bằng phút.

![LMS Setting](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/education-lms-9.png)

Giống như bài viết, video sẽ được xuất bản nếu chương trình cha của nó được xuất bản, nó sẽ hiển thị như sau trên cổng thông tin.

![LMS Setting](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/education-lms-7.png)

### 5.3 Câu đố (Quizzes)
Giảng viên cũng có thể thêm các câu đố vào các chủ đề mà họ xuất bản trong một chương trình. Một câu đố là một tập hợp các câu hỏi trắc nghiệm có thể được thêm từ master Câu hỏi (Question).

Bạn cần thiết lập điểm đạt (passing score), số lần thử tối đa (max attempts) cũng như cơ sở chấm điểm (grading basis) cho câu đố. Dưới đây là mô tả cho từng tùy chọn này:

1. **Passing Score**: Điểm trên thang 100 cần thiết để vượt qua câu đố (Mặc định: 75).
1. **Max Attempts**: Số lần thử tối đa mà học viên được phép thực hiện. Nếu đặt là 0, giới hạn này sẽ được bỏ qua và học viên có thể thử câu đố bất kỳ số lần nào cho đến khi vượt qua.
1. **Grading Basis**: Sau khi hết số lần thử tối đa, điểm cuối cùng sẽ được lấy dựa trên cơ sở chấm điểm. Dưới đây là các tùy chọn có sẵn:
    - Latest Highest Score: Điểm cao nhất từ tất cả các lần thử.
    - Latest Attempt: Điểm từ lần thử cuối cùng.
1. **Is Time-Bound**: Nếu được tích, câu đố sẽ có giới hạn thời gian.
1. **Duration**: Nếu câu đố có giới hạn thời gian, trường này có thể được sử dụng để thiết lập giới hạn thời gian.

![LMS Setting](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/education-lms-10.png)

#### Câu hỏi (Questions)
Bạn có thể thêm các câu hỏi để liệt kê trong các câu đố. Dựa trên số lượng các tùy chọn được đánh dấu là đúng, loại câu hỏi sẽ tự động được thiết lập là *Single Correct Answer* (Một đáp án đúng) hoặc *Multiple Correct Answers* (Nhiều đáp án đúng).

![LMS Setting](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/education-lms-11.png)

![LMS Setting](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/education-lms-12.png)

Các câu đố cũng được tự động xuất bản cùng với chương trình cha của nó, nó sẽ hiển thị như sau trên cổng thông tin.

![LMS Setting](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/education-lms-5.png)

{next}