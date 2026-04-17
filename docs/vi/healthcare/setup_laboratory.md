<!-- add-breadcrumbs -->
# Thiết lập Phòng xét nghiệm

Nếu bạn muốn sử dụng các tính năng của Phòng xét nghiệm, bạn có thể tạo Người dùng với vai trò _Laboratory User_. Các mục như Xét nghiệm Lab, Thu thập mẫu, v.v. chỉ hiển thị đối với những người dùng được bật Vai trò này.

Đọc [Cài đặt Y tế](/docs/v13/user/manual/en/healthcare/healthcare_settings) để thiết lập mô-đun Y tế.

### Mẫu xét nghiệm Lab (Lab Test Templates)
Mỗi khi bạn tạo một Xét nghiệm Lab mới, tài liệu Xét nghiệm Lab sẽ được tải dựa trên mẫu đã được cấu hình cho xét nghiệm cụ thể đó. Điều này có nghĩa là, bạn sẽ phải cấu hình các mẫu riêng biệt cho từng Xét nghiệm Lab.

Dưới đây là cách bạn có thể cấu hình các loại mẫu khác nhau.

`Healthcare > Setup > Lab Test Template > New Lab Test Template`

Sau khi cung cấp Tên cho Xét nghiệm, bạn sẽ phải chọn Mã (Code) và Nhóm mặt hàng (Item group) để tạo Mặt hàng (Item) được liên kết. ERPNext Healthcare liên kết mọi Xét nghiệm Lab (mọi dịch vụ y tế có tính phí khác) với một Mặt hàng có thiết lập "Maintain Stock" là false. Bằng cách này, Mô-đun Kế toán sẽ xuất hóa đơn cho Mặt hàng và bạn có thể xem các báo cáo liên quan đến Bán hàng của Mô-đun Bán hàng. Bạn cũng có thể thiết lập đơn giá bán của Xét nghiệm Lab tại đây - điều này sẽ cập nhật Bảng giá bán.

> Trường Đơn giá bán tiêu chuẩn (Standard Selling Rate) hoạt động tương tự như Đơn giá bán tiêu chuẩn của Mặt hàng, việc cập nhật trường này sẽ không cập nhật Bảng giá bán.

Cờ `Is Billable` trong Mẫu xét nghiệm Lab sẽ tạo ra Mặt hàng, nhưng ở trạng thái Bị vô hiệu hóa (Disabled). Tương tự, nếu bỏ chọn cờ này, Mặt hàng sẽ được Kích hoạt (Enable).

###### Định dạng kết quả (Result Format)
Dưới đây là các định dạng kết quả có sẵn trong ERPNext Healthcare

* Single (Đơn): chọn định dạng này cho các kết quả chỉ yêu cầu một đầu vào duy nhất, Đơn vị tính (UOM) kết quả và giá trị bình thường.
* Compound (Phức hợp): cho phép bạn cấu hình các kết quả yêu cầu nhiều trường đầu vào với tên sự kiện, Đơn vị tính kết quả và giá trị bình thường tương ứng.
* Descriptive (Mô tả): định dạng này hữu ích cho các kết quả có nhiều thành phần kết quả và các trường nhập kết quả tương ứng.
* Grouped (Nhóm): Bạn có thể nhóm các mẫu xét nghiệm đã được cấu hình và kết hợp chúng thành một xét nghiệm duy nhất. Đối với các mẫu như vậy, hãy chọn `Grouped`.
* No Result (Không có kết quả): Chọn mục này nếu bạn không cần nhập hoặc quản lý kết quả xét nghiệm. Ngoài ra, tài liệu Xét nghiệm Lab cũng sẽ không được tạo. Ví dụ: Các xét nghiệm phụ cho kết quả dạng Nhóm.

###### Giá trị bình thường (Normal values)
Đối với các định dạng kết quả Đơn (Single) và Phức hợp (Compound), bạn có thể thiết lập các giá trị bình thường.

###### Mẫu (Sample)
Bạn sẽ phải chọn Mẫu cần thiết cho xét nghiệm. Bạn cũng có thể ghi chú số lượng mẫu cần thu thập. Các chi tiết này sẽ được sử dụng khi tạo tài liệu Thu thập mẫu cho Xét nghiệm Lab.

### Khoa Y tế (Medical Department)
Để tổ chức phòng khám của bạn thành các khoa, bạn có thể tạo nhiều Khoa Y tế. Bạn có thể chọn các khoa phù hợp trong Mẫu xét nghiệm Lab và chúng sẽ được đưa vào bản in kết quả Xét nghiệm Lab.

`Healthcare > Setup > Medical Department > New Medical Department`

### Mẫu xét nghiệm Lab (Lab Test Sample)
Bạn có thể tạo các danh mục chính cho các Mẫu cần được thu thập cho một Xét nghiệm Lab.

`Healthcare > Setup > Lab Test Sample > New Lab Test Sample`

### Đơn vị tính xét nghiệm Lab (Lab Test UOM)
Bạn có thể tạo các danh mục chính cho các Đơn vị tính được sử dụng trong tài liệu Xét nghiệm Lab.

`Healthcare > Setup > Lab Test UOM > New Lab Test UOM`

### Kháng sinh (Antibiotic)
Bạn có thể tạo danh mục chính cho danh sách các loại Kháng sinh.

`Healthcare > Setup > Antibiotic > New Antibiotic`

### Độ nhạy (Sensitivity)
Bạn có thể tạo danh mục chính cho danh sách Độ nhạy với các loại Kháng sinh khác nhau.

`Healthcare > Setup > Sensitivity > New Sensitivity`

{next}