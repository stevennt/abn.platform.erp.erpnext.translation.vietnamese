<!-- add-breadcrumbs -->
# Kiểu in

**Trong Kiểu in, bạn có thể định nghĩa các kiểu CSS tùy chỉnh được áp dụng cho các Mẫu in.**

ERPNext đi kèm với các kiểu có sẵn để in tài liệu. Bạn cũng có thể tạo các kiểu mới bằng CSS để áp dụng cho tất cả các mẫu in của mình.

Các Kiểu in tiêu chuẩn trong ERPNext là: Monochrome, Modern, và Classic.
Để tạo một **Kiểu in** mới, hãy đi tới:

> Trang chủ > Cài đặt > Kiểu in

## 1. Cách tạo một Kiểu in mới
1. Đi tới danh sách Kiểu in, nhấn vào Mới.
1. Nhập tên cho Kiểu in.
1. Nhập CSS để định nghĩa giao diện của kiểu in đó.
1. Lưu.

Các kiểu bạn tạo ở đây sẽ được áp dụng cho cả mẫu in tiêu chuẩn và mẫu in tùy chỉnh. Để tìm hiểu các lớp CSS khác nhau hiện có, bạn có thể tạo một mẫu in tiêu chuẩn, mở trong trang mới và xem mã nguồn.

Một Kiểu in mặc định có thể được thiết lập từ [Cài đặt in](/docs/v13/user/manual/en/setting-up/print/print-settings).

Tất cả các kiểu Mẫu in đều dựa trên Bootstrap (Phiên bản 3) CSS Framework.

<img class="screenshot" alt="Print Style" src="https://docs.erpnext.com/docs/v13/assets/img/setup/print/print-style.png">

Nếu bạn đã bật chế độ nhà phát triển (developer mode) và tích vào Standard, hệ thống sẽ tạo tệp JSON cho Kiểu in đó. Bạn có thể đóng góp một kiểu in mặc định bằng cách này.

### 2. Các chủ đề liên quan
1. [Mẫu in](/docs/v13/user/manual/en/setting-up/print/print-format)
1. [Tiêu đề in](/docs/v13/user/manual/en/setting-up/print/print-headings)
1. [Tiêu đề thư](/docs/v13/user/manual/en/setting-up/print/letter-head)
1. [Mẫu in séc](/docs/v13/user/manual/en/setting-up/print/cheque-print-template)