<!-- add-breadcrumbs -->
# Cài đặt Kho

Bạn có thể thiết lập các cài đặt mặc định cho các giao dịch liên quan đến kho từ trang Cài đặt Kho.


## 1. Đặt tên Mặt hàng theo

![Stock Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/stock-settings-1.png)

Theo mặc định, Tên Mặt hàng được đặt theo Mã Mặt hàng đã nhập. Nếu bạn muốn các Mặt hàng được đặt tên theo một [Chuỗi đặt tên](https://docs.erpnext.com/docs/v13/user/manual/en/setting-up/settings/naming-series) nhất định, hãy chọn tùy chọn 'Naming Series'.


## 2. Các giá trị mặc định

### 2.1 Nhóm mặt hàng mặc định
Đây sẽ là Nhóm mặt hàng mặc định được gán cho một mặt hàng mới được tạo. Các Nhóm mặt hàng rất hữu ích để phân loại và thiết lập các thuộc tính cho toàn bộ nhóm. Để biết thêm, hãy truy cập trang [Nhóm mặt hàng](item-group.md).

### 2.2 Đơn vị tính kho mặc định
Đơn vị tính mặc định cho kho được thiết lập là số (Nos), có thể thay đổi tại đây.

### 2.3 Kho mặc định
Thiết lập Kho mặc định nơi thực hiện các giao dịch kho. Giá trị này sẽ được lấy vào mục Kho mặc định trong danh mục Mặt hàng:
    ![Stock Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/stock-settings-def.png)

### 2.4 Kho lưu mẫu
Đây là Kho nơi lưu trữ các mẫu lưu. Để biết thêm, hãy truy cập [trang này](retain-sample-stock.md).

### 2.5 Phương pháp tính giá mặc định
FIFO - nhập trước xuất trước hoặc giá bình quân gia quyền cho các mặt hàng của bạn. Phương pháp mặc định là FIFO. Nếu bạn chọn Giá bình quân, các Mặt hàng mới sẽ được tính giá theo Giá bình quân. Bạn có thể thay đổi điều này khi tạo Mặt hàng mới trong biểu mẫu Mặt hàng. Sau khi Mặt hàng đã được Lưu, Phương pháp tính giá không thể thay đổi. Đọc thêm [tại đây](https://frappe.io/blog/erpnext-features/inventory-valuation-method-fifo-vs-moving-average).

## 3. Tỷ lệ phần trăm giới hạn
Đây là tỷ lệ phần trăm bạn được phép nhận hoặc giao nhiều hơn so với số lượng đã đặt hàng. Ví dụ: Nếu bạn đặt 100 đơn vị, Nhà cung cấp gửi 120 đơn vị và tỷ lệ được thiết lập là 10%, thì bạn được phép nhận 110 đơn vị. Theo mặc định, giá trị này được thiết lập là 0.

## 4. Vai trò được phép Giao/Nhận vượt mức
Người dùng có vai trò này được phép giao/nhận vượt mức so với đơn hàng cao hơn tỷ lệ cho phép.

## 5. Hiển thị trường Mã vạch
Một trường để nhập chi tiết Mã vạch cho một mặt hàng. Nếu không được tích, trường này sẽ không hiển thị trong biểu mẫu Mặt hàng.

## 6. Chuyển đổi Mô tả Mặt hàng sang HTML sạch
Thông thường, các mô tả được sao chép từ một trang web hoặc tệp Word/PDF và chúng chứa nhiều định dạng nhúng. Điều này làm xáo trộn chế độ xem Bản in của hóa đơn hoặc báo giá của bạn.

Để khắc phục điều này, bạn có thể tích chọn "Chuyển đổi Mô tả Mặt hàng sang HTML sạch" trong Cài đặt Kho. Điều này sẽ đảm bảo rằng khi bạn Lưu các Mặt hàng, mô tả của chúng sẽ được làm sạch.

Nếu bạn muốn kiểm soát mô tả, chế độ xem và cho phép bất kỳ mã HTML nào được nhúng, bạn có thể bỏ tích thuộc tính này.

## 7. Tự động chèn

![Stock Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/stock-settings-2.png)

### 7.1 Tự động chèn Đơn giá Bảng giá nếu thiếu
Bật tính năng này sẽ tự động chèn Giá Mặt hàng vào Bảng giá của một Mặt hàng khi sử dụng Mặt hàng đó trong giao dịch đầu tiên. Mức giá này được lấy từ 'Đơn giá' được thiết lập trong giao dịch đầu tiên với Mặt hàng đó. Bảng giá phụ thuộc vào việc bạn đang sử dụng giao dịch Mua hay Bán.

Lưu ý rằng, Giá Mặt hàng sẽ chỉ được tự động chèn trong giao dịch đầu tiên nếu nó chưa tồn tại.

Nếu không được tích, 'Đơn giá bán tiêu chuẩn' được thiết lập trong Mặt hàng khi tạo Mặt hàng sẽ được thêm vào làm Giá Mặt hàng.

### 7.2 Tự động thiết lập Số serial dựa trên FIFO
Số serial cho kho sẽ được thiết lập tự động dựa trên các Mặt hàng được nhập theo nguyên tắc nhập trước xuất trước. Số Serial sẽ được thiết lập tự động trong các giao dịch như Hóa đơn mua/bán, Phiếu giao hàng, v.v.

## 8. Cho phép tồn kho âm
Tính năng này sẽ cho phép các mặt hàng trong kho hiển thị giá trị âm. Việc sử dụng tùy chọn này tùy thuộc vào trường hợp sử dụng của bạn. Ví dụ, các bút toán giao dịch kho được nhập vào cuối tuần hoặc cuối tháng. Trong trường hợp này, cần cho phép tồn kho âm để bạn có thể tiếp tục các bút toán giao dịch mua/bán.

## 9. Thiết lập Số lượng trong Giao dịch dựa trên đầu vào Số serial
Số lượng mặt hàng sẽ được thiết lập theo các số serial. Ví dụ, nếu người dùng đã thêm các số serial như A001, A002 và A003 thì hệ thống sẽ thiết lập số lượng là 3 trong giao dịch.

## 10. Tự động tạo Yêu cầu vật tư

![Stock Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/stock-settings-3.png)

### 10.1 Tạo Yêu cầu vật tư khi kho đạt mức đặt hàng lại

Tùy chọn này hữu ích nếu bạn muốn đảm bảo nguồn cung nguyên vật liệu/sản phẩm liên tục và tránh tình trạng thiếu hụt.
Một [Yêu cầu vật tư](material-request.md) sẽ được tạo tự động khi kho đạt đến mức đặt hàng lại được xác định trong [biểu mẫu Mặt hàng](item.md#34-automatic-reordering).

### 10.2 Thông báo qua Email khi tạo Yêu cầu vật tư tự động
Một email sẽ được gửi để thông báo cho Người dùng có vai trò 'Quản lý mua hàng' khi một Yêu cầu vật tư tự động được tạo.

## 11. Cài đặt Chuyển kho giữa các kho

<img class="screenshot" alt="Delivery Note Material Transfer" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/inter-warehouse.png">

### 11.1 Cho phép kho khách hàng để chuyển vật tư từ Phiếu giao hàng và Hóa đơn bán hàng

Tùy chọn này hữu ích khi việc chuyển vật tư cần được thể hiện dưới dạng Phiếu giao hàng. Ví dụ, nếu có các yêu cầu pháp lý về việc áp thuế cho mỗi lần chuyển Vật tư. Việc quản lý trong một giao dịch như Phiếu giao hàng sẽ dễ dàng hơn so với Phiếu kho.

### 11.2 Cho phép kho nhà cung cấp để chuyển vật tư từ Phiếu nhập hàng và Hóa đơn mua hàng

Tương tự như tùy chọn trên, tùy chọn này hữu ích khi việc chuyển vật tư cần được thể hiện dưới dạng Phiếu nhập hàng.

Để biết thêm về việc chuyển vật tư giữa các kho thông qua Phiếu giao hàng và Hóa đơn mua hàng, vui lòng tham khảo bài viết này [Chuyển vật tư từ Phiếu giao hàng](/docs/v13/user/manual/en/stock/articles/material-transfer-from-deliv