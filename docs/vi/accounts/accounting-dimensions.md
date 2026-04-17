<!-- add-breadcrumbs -->
# Chiều thông tin kế toán (Accounting Dimensions)

> Được giới thiệu trong Phiên bản 12

Kế toán theo chiều thông tin (Dimensional accounting) có nghĩa là gắn thẻ mỗi giao dịch với các chiều thông tin phù hợp như Chi nhánh, Đơn vị kinh doanh, v.v. Điều này cho phép bạn duy trì từng phân đoạn riêng biệt, từ đó hạn chế việc bảo trì tổng thể trên các tài khoản Sổ cái và giúp Hệ thống tài khoản của bạn luôn thuần nhất.

Trung tâm chi phí và Dự án được mặc định coi là các chiều thông tin trong ERPNext. Khi thiết lập một trường trong Chiều thông tin kế toán, trường đó sẽ được thêm vào các báo cáo giao dịch nếu có thể áp dụng.

Trong ERPNext, bạn có thể tạo các chiều thông tin kế toán có thể cấu hình và sử dụng chúng trong các giao dịch và báo cáo.

Để truy cập danh sách Chiều thông tin kế toán, hãy đi đến:
> Home > Accounting > Settings > Accounting Dimensions

## 1. Cách tạo Chiều thông tin kế toán trong ERPNext.

1. Đi đến danh sách Chiều thông tin kế toán và nhấn vào Mới.
1. Chọn Tài liệu tham chiếu (Reference Document) mà bạn muốn sử dụng làm chiều thông tin tùy chỉnh. Ví dụ: nếu bạn chọn Bộ phận (Department) làm Tài liệu tham chiếu, chiều thông tin sẽ dựa trên Bộ phận.
1. Nhập tên của chiều thông tin (Tên này sẽ xuất hiện trong các giao dịch mà chiều thông tin được tạo).
1. Trong bảng Giá trị mặc định của chiều thông tin (Dimension Defaults), bạn có thể chỉ định các chiều thông tin mặc định cụ thể cho công ty như trong ảnh chụp màn hình bên dưới. Chiều thông tin này sẽ được tự động lấy trong giao dịch đối với công ty cụ thể đó.
1. Tích vào ô "Bắt buộc" (Mandatory) nếu bạn muốn chiều thông tin này là bắt buộc trong các giao dịch.

![Creating Accounting Dimension](/docs/v13/assets/img/accounts/accounting-dimension.png)

## 2. Các tính năng

Khi bạn tạo chiều thông tin, các trường tùy chỉnh sẽ được tạo thông qua một tác vụ chạy ngầm cho chiều thông tin cụ thể đó. Bạn có thể thấy chúng trong phần Chiều thông tin kế toán bên trong các giao dịch có ảnh hưởng đến các bút toán kế toán (Bút toán Sổ cái).

### 2.1 Sử dụng các chiều thông tin trong giao dịch

Để gắn một giao dịch với một chiều thông tin, bạn có thể chọn chiều thông tin cụ thể trong phần Chiều thông tin kế toán như trong ảnh chụp màn hình bên dưới.

![Accounting Dimension in Sales Invoice](/docs/v13/assets/img/accounts/accounting-dimension-in-invoice.png)

### 2.2 Lọc Báo cáo dựa trên các chiều thông tin

Bạn cũng có thể lọc các báo cáo tài chính khác nhau như Báo cáo Kết quả hoạt động kinh doanh, Bảng cân đối kế toán, Sổ cái dựa trên các chiều thông tin này.

![Accounting Dimension in Reports](/docs/v13/assets/img/accounts/report-dimensions.png)

### 2.3 Thiết lập chiều thông tin kế toán là bắt buộc cho các Tài khoản "Kết quả hoạt động kinh doanh" và "Bảng cân đối kế toán"
Kết quả hoạt động kinh doanh là nhóm các tài khoản Thu nhập và Chi phí đại diện cho các giao dịch kế toán của bạn trong một khoảng thời gian.

Các tài khoản Bảng cân đối kế toán là Ứng dụng nguồn vốn (Tài sản) và Nguồn vốn (Nợ phải trả) thể hiện giá trị tài sản ròng của công ty bạn tại bất kỳ thời điểm nào.

Bằng cách chọn các ô 'Bắt buộc đối với Tài khoản Kết quả hoạt động kinh doanh' hoặc 'Bắt buộc đối với Bảng cân đối kế toán', bạn có thể cấu hình các chiều thông tin của mình thành bắt buộc đối với 'Tài khoản Kết quả hoạt động kinh doanh' và 'Tài khoản Bảng cân đối kế toán'.

![Accounting Dimension Mandatory in Transaction](/docs/v13/assets/img/accounts/dimension-mandatory.png)

### 2.4 Vô hiệu hóa các chiều thông tin kế toán khi không còn cần thiết

Bạn cũng có thể vô hiệu hóa các chiều thông tin nếu không còn cần đến chúng nữa. Các giao dịch cũ có chứa chiều thông tin kế toán vẫn sẽ được giữ nguyên.

![Disable Accounting Dimension](/docs/v13/assets/img/accounts/dimension-disable.png)

### Các chủ đề liên quan
1. [Trung tâm chi phí](/docs/v13/user/manual/en/accounts/cost-center)
1. [Lập ngân sách](/docs/v13/user/manual/en/accounts/budgeting)
1. [Báo cáo kế toán](/docs/v13/user/manual/en/accounts/accounting-reports)

{next}