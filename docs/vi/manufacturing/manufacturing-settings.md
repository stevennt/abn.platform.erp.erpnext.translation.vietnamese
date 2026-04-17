<!-- add-breadcrumbs -->
#Cài đặt Sản xuất

Cài đặt Sản xuất có thể được tìm thấy tại:

> Trang chủ > Sản xuất > Cài đặt > Cài đặt Sản xuất

<img class="screenshot" alt="Manufacturing Settings" src="https://docs.erpnext.com/docs/v13/assets/img/manufacturing/manufacturing-settings-1.png">

### Lập kế hoạch năng lực
[Lập kế hoạch năng lực](/docs/v13/user/manual/en/manufacturing/capacity-planning) là quá trình mà một tổ chức quyết định có chấp nhận các đơn hàng mới hay không dựa trên các nguồn lực và các lệnh sản xuất hiện có.

### Tỷ lệ phần trăm cho phép sản xuất vượt mức

Khi lập Lệnh sản xuất dựa trên Đơn bán hàng, hệ thống sẽ chỉ cho phép số lượng mặt hàng sản xuất nhỏ hơn hoặc bằng số lượng trong Đơn bán hàng. Trong trường hợp bạn muốn cho phép lập Lệnh sản xuất với số lượng lớn hơn, bạn có thể nhập Tỷ lệ phần trăm cho phép sản xuất vượt mức tại đây.

Ví dụ: Trong một số trường hợp, một Trạm làm việc phải sản xuất 100 đơn vị để đạt hiệu quả về chi phí nhưng Lệnh sản xuất có thể chỉ là 50 đơn vị. Trong trường hợp này, Tỷ lệ phần trăm cho phép sản xuất vượt mức sẽ là 100.

### Kho bán thành phẩm mặc định

Kho này sẽ được tự động cập nhật vào trường 'Kho đang sản xuất' (Work In Progress Warehouse) của Lệnh sản xuất.

### Kho thành phẩm mặc định

Kho này sẽ được tự động cập nhật vào trường 'Kho đích' (Target Warehouse) của Lệnh sản xuất.

### Cho phép tiêu hao nhiều nguyên vật liệu
Nếu được tích chọn, nhiều nguyên vật liệu có thể được sử dụng cho một Lệnh sản xuất duy nhất. Điều này hữu ích nếu một hoặc nhiều sản phẩm mất nhiều thời gian để sản xuất. Ví dụ, một sản phẩm duy nhất mất một tháng để sản xuất và nguyên vật liệu thô được tiêu thụ hàng ngày. Trong kịch bản thông thường, điều này sẽ không khả thi với các phiếu kho. Việc bật tùy chọn này sẽ cho phép bạn tạo các phiếu kho cho việc tiêu hao nguyên vật liệu mà không cần phải tạo một bút toán để trừ kho tự động (backflush). Kết quả cuối cùng là bạn có thể thấy lượng tồn kho đang được tiêu thụ trong các Kho và có thể cập nhật bút toán sản xuất cuối cùng ở giai đoạn sau.

### Tự động cập nhật chi phí BOM
Nếu được tích chọn, chi phí BOM sẽ được tự động cập nhật dựa trên Giá trị tính giá / Giá trong Bảng giá / giá mua gần nhất của nguyên vật liệu thô.