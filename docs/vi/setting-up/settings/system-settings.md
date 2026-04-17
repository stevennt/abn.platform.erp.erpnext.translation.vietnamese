<!-- add-breadcrumbs -->
# Cài đặt Hệ thống

**Cài đặt Hệ thống chứa các thiết lập cấu hình cho toàn bộ hệ thống của tài khoản.**

Bạn có thể bản địa hóa ERPNext để sử dụng múi giờ, định dạng ngày tháng, số hoặc tiền tệ cụ thể, đồng thời thiết lập thời gian hết hạn phiên làm việc toàn cầu thông qua Cài đặt Hệ thống.

Để mở Cài đặt Hệ thống, hãy đi tới:

> Trang chủ > Thiết lập > Cài đặt Hệ thống

<img class="screenshot" alt="System Settings" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/settings/system-settings.png">


## 1. Các phần trong Cài đặt Hệ thống

### 1.1 Tổng quát

* **Quốc gia**: Bạn có thể thiết lập quốc gia mặc định tại đây, thông tin này sẽ được lấy khi tạo địa chỉ mới. Nếu công ty của bạn có nhiều chi nhánh ở các quốc gia khác nhau, hãy chọn vị trí trụ sở chính.
* **Múi giờ**: Thiết lập thời gian tự động dựa trên múi giờ.
* **Ngôn ngữ**: Thiết lập ngôn ngữ toàn cầu cho tài khoản ERPNext. Sau đó, ngôn ngữ sẽ được thay đổi trong tất cả các menu, giao dịch, danh mục chính, v.v.

### 1.2 Định dạng Ngày và Số

* **Định dạng Ngày**: Định dạng mà ngày tháng sẽ được hiển thị. Ví dụ: dd.mm.yyyy hoặc mm/dd/yyyy. Điều này phụ thuộc vào cách định dạng ngày tháng ở khu vực của bạn.
* **Định dạng Thời gian**: Định dạng mà thời gian sẽ được hiển thị. Bạn có thể chọn hiển thị (`HH:mm:ss`) hoặc ẩn giây bằng cách đặt tùy chọn là (`HH:mm`).
* **Định dạng Số**: Định dạng mà các con số sẽ được định dạng. Ví dụ: 1,000 hoặc 1000.00.
* **Độ chính xác số thập phân**: Số chữ số thập phân hiển thị sau dấu phẩy cho số lượng, v.v. Phạm vi từ 2-9. Mặc định là 3.
* **Độ chính xác Tiền tệ**: Số chữ số thập phân hiển thị sau dấu phẩy cho các giá trị tiền tệ. Nếu để trống, nó sẽ dựa trên **Định dạng Số**.

### 1.3 Sao lưu

Trong ERPNext, bạn có thể sao lưu cơ sở dữ liệu cũng như các tệp của mình. Các bản sao lưu cơ sở dữ liệu được tạo tự động trong khi các bản sao lưu tệp cần được tải xuống một cách rõ ràng.

Trường này hiển thị số lượng bản sao lưu mà sau đó các bản cũ hơn sẽ bị xóa. Theo mặc định, 3 bản sao lưu được lưu trữ trong vòng 24 giờ. Các bản sao lưu mới được tạo tự động sau mỗi vài giờ và bản sao lưu mới nhất sẽ ghi đè lên bản cũ nhất. Để sao lưu tệp, hãy nhấp vào nút Tải xuống Bản sao lưu Tệp trong biểu mẫu Tải xuống Bản sao lưu.

Việc duy trì sao lưu hệ thống thường xuyên là một thói quen tốt trong trường hợp có bất kỳ sự cố nào xảy ra và bạn muốn khôi phục lại hoặc chỉ để lưu trữ hồ sơ.

### 1.4 Quyền hạn

Sử dụng quyền hạn, bạn có thể giới hạn quyền truy cập của người dùng vào các loại tài liệu. Sự giới hạn có thể dựa trên các trường như Công ty, Khu vực, Chi nhánh, v.v. Để biết thêm về Quyền người dùng, [nhấp vào đây](/docs/v13/user/manual/en/setting-up/users-and-permissions/user-permissions).


Nếu ô chọn Áp dụng Quyền người dùng nghiêm ngặt được tích và Quyền người dùng được xác định cho một DocType cho một Người dùng, thì tất cả các tài liệu mà giá trị của liên kết để **trống** sẽ không được hiển thị cho Người dùng đó.

Việc này được thực hiện từ:
> Trang chủ > Người dùng và Quyền > Quyền > Quyền người dùng

Ví dụ: Nếu bạn thiết lập Quyền người dùng cho Khu vực và đặt giá trị là Ấn Độ. Nếu ô chọn không được tích, tất cả các giao dịch (đơn bán hàng, báo giá) có Khu vực là Ấn Độ và **trống** sẽ được hiển thị cho người dùng.

Nếu ô chọn Áp dụng Quyền người dùng nghiêm ngặt được tích, các tài liệu mà Khu vực để trống sẽ không được hiển thị cho người dùng.

### 1.5 Bảo mật

* **Hết hạn phiên**: Số giờ không hoạt động mà sau đó bạn sẽ bị đăng xuất khỏi phiên làm việc. Điều này giúp bảo mật tốt hơn. Ví dụ: nếu không có hoạt động nào trong 6 giờ, tài khoản của bạn sẽ bị đăng xuất.
* **Hết hạn phiên trên Di động**: Thời gian hết hạn phiên khi đăng nhập từ điện thoại di động.
* **Chỉ cho phép một phiên cho mỗi người dùng**: Nếu bạn muốn sử dụng một bộ thông tin đăng nhập duy nhất cho nhiều người dùng, hãy tích vào ô này. Số lượng phiên đồng thời có thể được thay đổi trong danh mục Người dùng. Các phiên trên điện thoại di động không được tính ở đây.
* **Cho phép Đăng nhập bằng Số điện thoại**: Bằng cách tích vào ô 'Cho phép Đăng nhập bằng Số điện thoại', bạn có thể đăng nhập vào ERPNext bằng số điện thoại hợp lệ đã được thiết lập trong tài khoản Người dùng của mình.

* **Cho phép Đăng nhập bằng Tên người dùng**: Cho phép người dùng đăng nhập thông qua tên người dùng được thiết lập trong [danh mục Người dùng](/docs/v13/user/manual/en/setting-up/users-and-permissions/adding-users).
* **Hiển thị Lỗi đầy đủ và Cho phép Báo cáo sự cố cho Nhà phát triển**: Điều này sẽ hiển thị toàn bộ lỗi trên màn hình và cho phép báo cáo sự cố. Nếu bạn có kiến thức kỹ thuật trong lĩnh vực này, bạn có thể hiểu rõ hơn về lỗi bằng cách đọc toàn bộ thông báo.
* **Xóa thẻ EXIF từ ảnh đã tải lên**: Siêu dữ liệu được lưu trữ trong các tệp ảnh ở định dạng EXIF có thể bị khai thác để lấy thông tin nhạy cảm của người dùng. Tùy chọn này cho phép người dùng xóa dữ liệu đó khỏi ảnh trước khi tải lên.

### 1.6 Mật khẩu

* **Buộc Người dùng phải Đặt lại Mật khẩu**: Số ngày mà sau đó việc đặt lại mật khẩu là bắt buộc. 0 có nghĩa là không giới hạn.
* **Bật Chính sách Mật khẩu**: Bật trình kiểm tra độ mạnh mật khẩu để người dùng phải sử dụng mật khẩu mạnh khi đăng nhập.
* **Điểm mật khẩu tối thiểu**: Điểm cho trình kiểm tra độ mạnh mật khẩu
    * 2 là trung bình
    * 3 là mạnh
    * 4 là rất mạnh

    Độ phức tạp dựa trên số lượng ký tự, viết hoa, ký tự đặc biệt, v.v.
* **Giới hạn Tạo liên kết Đặt lại mật khẩu**: Điều này cho phép giới hạn số lượng yêu cầu đặt lại mật khẩu mỗi giờ, mặc định là 3. Thiết lập thành 0 sẽ cho phép tạo yêu cầu liên kết đặt lại mật khẩu không giới hạn.

### 1.7 Bảo mật chống tấn công Brute Force

* **Cho phép các lần Đăng nhập liên tiếp**: Số lần đăng nhập liên tiếp mà sau đó bạn sẽ bị khóa tài khoản trong một khoảng thời gian cụ thể. Điều này giúp ích nếu có kẻ xâm nhập cố gắng đăng nhập vào tài khoản của bạn.
* **Cho phép Đăng nhập sau khi Thất bại**: Số giây mà sau đó một lần thử đăng nhập sẽ được cho phép sau các lần thử không thành công liên tiếp.

### 1.8 Xác thực hai yếu tố
Các thiết lập cho Xác thực hai yếu tố có thể được cấu hình tại đây.

Khi tích vào 'Bật Xác thực hai yếu tố', hai tùy chọn sau sẽ được hiển thị.

* **Bỏ qua Xác thực hai yếu tố cho người dùng đăng nhập từ Địa chỉ IP bị hạn chế**: Người dùng đăng nhập từ các địa chỉ IP bị hạn chế sẽ không được yêu cầu Xác thực hai yếu tố. Bạn có thể hạn chế các IP từ danh mục Người dùng dưới phần...