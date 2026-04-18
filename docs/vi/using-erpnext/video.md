<!-- add-breadcrumbs -->
# Video

**Video có thể được thêm từ cả Vimeo và YouTube, sử dụng DocType Video.**

Bạn có thể thêm Video cùng với URL, mô tả, hình thu nhỏ (thumbnail), v.v. Một số công dụng của nó là để duy trì tài liệu khóa học giáo dục và theo dõi mức độ tương tác của video YouTube cá nhân.

Để truy cập Video, hãy đi tới:

> Trang chủ > Công cụ > Video

## 1. Cách tạo một Video mới

1. Đi tới danh sách Video và nhấp vào Mới.
2. Nhập tiêu đề cho Video.
3. Chọn Nhà cung cấp (Provider). Nhà cung cấp Video mặc định là YouTube.
4. Nhập URL để truy cập Video.
5. Bạn có thể tùy chọn thêm ngày xuất bản và thời lượng của Video theo định dạng ngày-giờ-phút-giây.
6. Bạn cũng phải thêm một số mô tả cho video.
7. Lưu.

Sau khi Lưu, bạn sẽ có tùy chọn để thêm một hình ảnh/hình thu nhỏ cho Video.
![Video](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/video-after-save.png)

Bạn cũng có thể xem Video ngay trong chính Tài liệu sau khi lưu nó.
![Video](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/video-watch.gif)

## 2. Các tính năng

### 2.1 Theo dõi phân tích Video qua YouTube

Các thống kê Video YouTube có thể được theo dõi và phân tích. Điều này hữu ích để theo dõi số lượt xem và mức độ tương tác của một Video mà bạn đã xuất bản.

Để làm điều này, trước tiên bạn phải bật Theo dõi YouTube trong **Cài đặt Video**:
> Cài đặt Video > Bật Theo dõi YouTube

Khi bạn bật tính năng này, các trường **API Key** và **Tần suất** sẽ hiển thị.
![Video](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/video-settings.png)

**API Key** : Bạn có thể tạo API Key trong [Google Developers Console](https://console.developers.google.com/). Bạn có thể tham khảo [Tài liệu YouTube Data API](https://developers.google.com/youtube/v3/getting-started) để biết các bước tạo.

**Tần suất**: Bạn có thể chọn tần suất hệ thống tự động cập nhật thống kê của bạn. Các tùy chọn có sẵn là mỗi 30 phút, 1 giờ, 6 giờ và Hàng ngày (mỗi ngày một lần).

Ngoài việc cập nhật tự động, các thống kê sẽ được cập nhật khi Lưu. Vì vậy, tất cả các Video được tạo/cập nhật **sau khi** bật theo dõi YouTube sẽ được cập nhật thống kê khi Lưu.
![Video](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/video-stats.png)

### 2.2 Báo cáo tương tác YouTube

Báo cáo tương tác YouTube cung cấp cái nhìn tổng hợp về mức độ tương tác của tất cả các video. Biểu đồ cột cung cấp phân tích trực quan về Lượt thích so với Lượt xem.

Bạn có thể lọc dữ liệu báo cáo theo phạm vi Ngày xuất bản.
![Video](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/youtube-interactions.png)

> **Lưu ý** : Hạn ngạch cho số lượng yêu cầu **không tính phí** tới YouTube Data API là 10.000 yêu cầu tính đến tháng 9 năm 2020. ERPNext tự động cập nhật lên đến 50 video trong 1 yêu cầu. Tương tự, đối với 100 video sẽ mất 2 yêu cầu.<br>
Giả sử 100 video được cập nhật **mỗi giờ** (tần suất = 1 giờ):<br>
>
- 2 yêu cầu sẽ được gửi mỗi giờ<br>
- 48 yêu cầu sẽ được gửi mỗi ngày<br>

> Vui lòng thiết lập tần suất sao cho phù hợp.

{next}