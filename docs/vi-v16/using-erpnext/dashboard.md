<!-- add-breadcrumbs -->
# Trang tổng quan

> Được giới thiệu trong Phiên bản 12

**Trang tổng quan cung cấp cái nhìn nhanh về các chỉ số hiệu suất chính liên quan đến quy trình kinh doanh.**

Mỗi Trang tổng quan bao gồm một hoặc nhiều Biểu đồ Trang tổng quan, mỗi biểu đồ được cấu hình với một nguồn dữ liệu được gọi là Nguồn Biểu đồ Trang tổng quan.

Để truy cập Trang tổng quan, hãy đi tới,

> Trang chủ > Tùy chỉnh > Trang tổng quan > Trang tổng quan

## 1. Cách tạo Trang tổng quan mới

1. Đi tới Danh sách Trang tổng quan và nhấp vào Mới.
2. Nhập Tên Mô-đun mà bạn muốn xem Trang tổng quan.
3. Nhập các Biểu đồ Trang tổng quan mà bạn muốn tham số hóa cho Trang tổng quan này.
4. Lưu.

Khi bạn nhấp vào `Show Dashboard`, bạn sẽ có thể xem Trang tổng quan hiển thị các biểu diễn đồ họa cho các giao dịch của mình.

![Accounting Dashboard](https://docs.erpnext.com/docs/v16/assets/img/customize/dashboard.png)

## 2. Thêm Biểu đồ vào Trang tổng quan

Thêm các biểu đồ vào trang tổng quan này bằng cách chọn `Dashboard Chart` hiện có hoặc tạo mới.

![Adding Dashboard to Charts](https://docs.erpnext.com/docs/v16/assets/img/customize/dashboard-add-charts.png)

Lưu các thay đổi và nhấp vào nút `Show Dashboard` để xem trang tổng quan.

![Show Dashboard Button](https://docs.erpnext.com/docs/v16/assets/img/customize/dashboard-show-dashboard-button.png)

## 3. Tạo Biểu đồ Trang tổng quan mới

Để tạo một Biểu đồ Trang tổng quan mới, hãy đi tới

> Trang chủ > Tùy chỉnh > Trang tổng quan > Biểu đồ Trang tổng quan > Mới

Cung cấp tên cho biểu đồ, tên này sẽ hiển thị trong trang tổng quan dưới dạng nhãn biểu đồ và chọn một `Dashboard Chart Source` làm nguồn dữ liệu cho biểu đồ này.

**Lưu ý:** `Dashboard Chart Source` mới chỉ có thể được tạo bởi Người dùng Quản trị viên trong Chế độ Nhà phát triển (Developer Mode).

![Select Dashboard Chart Source](https://docs.erpnext.com/docs/v16/assets/img/customize/dashboard-chart-from-source.png)

Sau khi thiết lập trường Nguồn Biểu đồ, bảng bộ lọc sẽ được hiển thị.

Nhấp vào bảng để chỉnh sửa các bộ lọc.

![Dashboard Chart Filter](https://docs.erpnext.com/docs/v16/assets/img/customize/dashboard-chart-filter.png)

Một cửa sổ modal sẽ hiển thị để thiết lập bộ lọc. Nhấp vào `Set` để thiết lập bộ lọc.
![Dashboard Chart Filter Modal](https://docs.erpnext.com/docs/v16/assets/img/customize/dashboard-chart-filter-modal.png)

Sau khi thiết lập trường Nguồn Biểu đồ, bảng Bộ lọc sẽ được cập nhật với các giá trị bộ lọc đã chọn.
![Dashboard Chart Filter](https://docs.erpnext.com/docs/v16/assets/img/customize/dashboard-chart-filter-updated.png)

## 4. Sử dụng Trang tổng quan

Mỗi biểu đồ sẽ được hiển thị theo các trường được thiết lập trong Biểu đồ Trang tổng quan tương ứng. Kết quả từ nguồn biểu đồ trang tổng quan được lưu vào bộ nhớ đệm để tránh các truy vấn dư thừa. Vì dữ liệu biểu đồ có thể bị cũ, mỗi biểu đồ cũng sẽ hiển thị thời gian đồng bộ hóa cuối cùng.

![Dashboard Last Synced](https://docs.erpnext.com/docs/v16/assets/img/customize/dashboard-last-synced.png)

Các bộ lọc được sử dụng để tạo dữ liệu biểu đồ cũng có thể được thay đổi bằng cách nhấp vào `Set Filters`. Biểu đồ sẽ được làm mới tự động theo các bộ lọc vừa được thiết lập.

![Dashboard Filters](https://docs.erpnext.com/docs/v16/assets/img/customize/dashboard-filters.png)

Để lấy dữ liệu mới nhất, mỗi biểu đồ phải được làm mới một cách cưỡng bách bằng cách nhấp vào nút **Force Refresh** từ menu thả xuống.

{next}