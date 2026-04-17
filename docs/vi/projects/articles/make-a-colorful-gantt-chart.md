<!--add breadcrumbs-->

# Tạo Biểu đồ Gantt Đa màu sắc

ERPNext cho phép người dùng thêm màu sắc vào một số tài liệu nhất định để có các gợi ý và biểu diễn trực quan tốt hơn. Một ví dụ điển hình cho việc này là [Lịch sự kiện](/docs/v13/user/manual/en/using-erpnext/calendar), nơi bạn có thể thêm màu sắc cho mỗi sự kiện.

Chúng ta sẽ thực hiện việc này bằng cách tùy chỉnh [Công việc](/docs/v13/user/manual/en/projects/tasks) trong module Dự án.

## Các bước để Thêm Màu sắc vào Biểu đồ Gantt

1. Đi tới [Tùy chỉnh biểu mẫu (Customize Form)](/docs/v13/user/manual/en/customize-erpnext/customize-form) trong hệ thống và chọn *Task* trong tùy chọn _Enter Form Type_. Ngoài ra, bạn có thể truy cập màn hình này bằng cách đi tới **Menu > Customize** từ danh sách hoặc biểu mẫu Công việc.

 <img class="screenshot" alt="customize-form" src="https://docs.erpnext.com/docs/v13/assets/img/articles/project-gantt-customize-form-1.gif">

1. Thêm một trường mới trong DocType với fieldtype là color.
1. Tích chọn tùy chọn *In List View*.

 <img class="screenshot" alt="customize-form" src="https://docs.erpnext.com/docs/v13/assets/img/articles/project-gantt-in-list.png">

1. Lưu biểu mẫu, quay lại danh sách Công việc và tải lại trang.
1. Khi mở một Công việc cũ hoặc mới, bạn sẽ thấy một trường màu sắc. Hãy chọn một màu cho Công việc đó.

 <img class="screenshot" alt="customize-form" src="https://docs.erpnext.com/docs/v13/assets/img/articles/project-gantt-pick-color.png">

1. Quay lại danh sách Công việc và chuyển sang chế độ xem Gantt.

  <img class="screenshot" alt="customize-form" src="https://docs.erpnext.com/docs/v13/assets/img/articles/project-gantt-colors.png">