<!-- add-breadcrumbs -->
# Điểm bán hàng (Point of Sale)

**Điểm bán hàng đề cập đến thời gian và địa điểm nơi một giao dịch bán lẻ diễn ra.**

Đối với các hoạt động bán lẻ, việc giao hàng, ghi nhận doanh thu và thanh toán đều diễn ra trong cùng một sự kiện, thường được gọi là 'Điểm bán hàng' (POS).

Trong ERPNext, Hóa đơn bán hàng có thể được tạo từ POS. Có hai bước để thiết lập POS:

Để truy cập POS, hãy đi đến:
> Home > Retail > Retail Operations > POS

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Điểm bán hàng, bạn nên tạo các mục sau trước:

1. [Hồ sơ POS](pos-profile.md)

## 2. Cách tạo Hóa đơn POS
Sau khi bạn thiết lập hồ sơ POS, bạn có thể bắt đầu lập hóa đơn trên POS.

1. Đi đến POS và chọn một Khách hàng.
1. Thêm các Mặt hàng từ danh sách hiển thị bên phải bằng cách nhấp vào chúng.
1. Đảm bảo rằng Mặt hàng đã được thiết lập Đơn giá trong danh sách Bảng giá Mặt hàng.
1. Chỉnh sửa số lượng nếu cần.
1. Để chỉnh sửa Đơn giá và Chiết khấu, bạn cần kích hoạt chúng trong Hồ sơ POS.
1. Cần phải thiết lập một Kho mặc định để hoàn tất giao dịch. Nếu Kho được thiết lập trong cả Mặt hàng và hồ sơ POS, thì kho trong Hồ sơ POS sẽ được ưu tiên.
1. Lưu ý rằng bạn cần phải có Mặt hàng trong Kho trước khi có thể bán. Nếu Mặt hàng không có sẵn, một dấu chấm đỏ sẽ hiển thị bên cạnh Mặt hàng khi được chọn.
  ![Màn hình POS](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/pos-screen.png)
1. Khi tất cả các Mặt hàng đã được thêm vào, hãy nhấp vào Thanh toán (Pay). Bạn sẽ được yêu cầu Xác nhận Hóa đơn bán hàng.
1. Chọn phương thức thanh toán, Xác nhận (Submit)
1. Sau đó, bạn có thể in hóa đơn POS.
  ![Thanh toán POS](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/pos-checkout.gif)

Sau khi Hóa đơn bán hàng được Xác nhận, bạn có thể in hoặc gửi email trực tiếp cho khách hàng.


### 2.2 Thêm một Mặt hàng
Tại quầy thu ngân, người bán lẻ cần chọn các Mặt hàng mà Khách hàng mua. Trong giao diện POS, bạn có thể chọn một Mặt hàng bằng hai phương pháp. Một là nhấp vào hình ảnh Mặt hàng và hai là thông qua Mã vạch / Số serial.

* **Chọn Mặt hàng**: Để chọn một sản phẩm, hãy nhấp vào hình ảnh Mặt hàng và thêm nó vào giỏ hàng. Giỏ hàng là khu vực chuẩn bị cho khách hàng thanh toán bằng cách cho phép chỉnh sửa thông tin sản phẩm, điều chỉnh thuế và thêm chiết khấu.

* **Mã vạch / Số serial**: Mã vạch / Số serial là một dạng biểu diễn dữ liệu bằng máy quang học có thể đọc được liên quan đến đối tượng mà nó được gắn vào. Nhập Mã vạch / Số serial vào ô như trong hình dưới đây và dừng lại một giây, mặt hàng sẽ tự động được thêm vào giỏ hàng.

> Mẹo: Để thay đổi số lượng của một Mặt hàng, hãy nhập số lượng mong muốn vào ô số lượng. Điều này thường được sử dụng nếu cùng một Mặt hàng được mua với số lượng lớn.

Nếu danh sách sản phẩm của bạn quá dài, hãy sử dụng trường Tìm kiếm, nhập tên sản phẩm vào ô Tìm kiếm.

### 2.3 Loại bỏ một Mặt hàng khỏi Giỏ hàng
1. Chọn hàng trong giỏ hàng và nhấp vào nút 'Remove' (Xóa) trong bàn phím số.

  ![Loại bỏ Mặt hàng khỏi POS](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/remove-item-from-pos.png)

2. Đặt Số lượng (Qty) thành bằng không để loại bỏ Mặt hàng khỏi hóa đơn POS. Có hai cách để loại bỏ một Mặt hàng.
  * Nếu Số lượng của Mặt hàng là 1, hãy nhấp vào dấu trừ để đưa nó về bằng không.
  * Nhập thủ công số lượng là 0 (không).


### 2.4 Thay đổi Số tiền thừa (Change Amount)

POS tính toán số tiền thừa mà khách hàng đã trả, người dùng có thể trả lại từ tài khoản tiền mặt. Người dùng phải thiết lập tài khoản cho số tiền thừa trong hồ sơ POS.

  ![Thay đổi số tiền thừa trong POS](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/change-amount-in-pos.png)

## 3. Các tính năng

### 3.1 Thêm Khách hàng mới
Trong POS, người dùng có thể chọn Khách hàng hiện có trong khi tạo đơn hàng hoặc tạo một khách hàng mới. Tính năng này cũng hoạt động ở chế độ ngoại tuyến. Người dùng cũng có thể thêm chi tiết khách hàng như số điện thoại, địa chỉ, v.v. trên biểu mẫu. Khách hàng đã được tạo từ POS sẽ được đồng bộ hóa khi có kết nối internet.

![Thêm Khách hàng mới trong POS](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/pos-add-new-customer.gif)

### 3.2 Các bút toán kế toán (Bút toán sổ cái) cho Điểm bán hàng:

Nợ:

  * Khách hàng (tổng cộng)
  * Ngân hàng/Tiền mặt (thanh toán)

Có:

  * Thu nhập (tổng ròng, trừ thuế cho mỗi Mặt hàng)
  * Thuế (nghĩa vụ phải nộp cho chính phủ)
  * Khách hàng (thanh toán)
  * Xóa bỏ (tùy chọn)
  * Tài khoản cho Số tiền thừa (tùy chọn)

Để xem các bút toán sau khi xác nhận [Hóa đơn bán hàng](sales-invoice.md), hãy nhấp vào **Xem sổ cái (View Ledger)**.

### 3.3 Email

Bạn cũng có thể gửi biên lai qua email.

![Gửi Email kèm Biên lai POS](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/pos-email.png)

### 3.4 Chứng từ đóng POS

Vào cuối ngày, thu ngân có thể đóng ca POS của mình bằng cách tạo một Chứng từ đóng POS.
Nhấp vào Menu và chọn 'Close the POS'. Chọn khoảng thời gian, Hồ sơ POS của bạn và người dùng của bạn để truy xuất tất cả các doanh thu đã đăng ký.

Để đóng theo ca hoặc theo thu ngân, hãy sử dụng [Đóng ca thu ngân POS](pos-cashier-closing.md).

![Nhập đóng POS](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/pos-closing-entry.png)

Nhập số tiền đã thu được cho mỗi phương thức thanh toán. Nếu bạn nhận thấy bất kỳ sự khác biệt nào giữa số tiền trên hệ thống và số tiền mặt thực tế thu được, hãy tạo một Bút toán chênh lệch (Difference Posting).

### 4. Các chủ đề liên quan
1. [Hóa đơn bán hàng](sales-invoice.md)
1. [Đơn mua hàng](../buying/purchase-order.md)
1. [Bút toán thanh toán](payment-entry.md)
1. [Yêu cầu thanh toán](payment-request.md)

{next}