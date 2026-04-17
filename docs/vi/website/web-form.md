<!-- add-breadcrumbs -->
# Web Form

Các bên liên quan không thuộc tổ chức của bạn có thể cần tương tác với hệ thống ERPNext của bạn. Bạn có thể cho phép Khách hàng, Nhà cung cấp, ứng viên xin việc, học sinh và người giám hộ truy cập vào một số thông tin nhất định hoặc thậm chí tạo một số giao dịch nhất định. Ví dụ: bạn có thể cho phép bất kỳ ai tạo tài khoản trên trang web của mình (được tạo bằng ERPNext) và ứng tuyển công việc. Bạn có thể cho phép Khách hàng xem chi tiết các khiếu nại mà họ đã đăng ký. Những việc này có thể được thực hiện bằng cách sử dụng Web Form.

> Có hai loại giao diện tích hợp sẵn trong ERPNext. Đó là *Desk View* và *Web View*. Desk dành cho những người dùng thường xuyên tương tác với hệ thống ERPNext, chẳng hạn như nhân viên trong tổ chức của bạn.

> Web View dành cho những người dùng cần tương tác với hệ thống ERPNext theo từng thời điểm. Web form tương tự như các biểu mẫu mà bạn thường điền trên các trang web khác nhau trên internet. Webform là một phần của giao diện *Web View* trong ERPNext.

Để tạo một **Web Form** mới, hãy đi tới:

> Home > Website > Web Site > Web Form

![New Web Form](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/new-web-form-1.png)
*Web Form mới*

Chọn **DocType** mà bạn muốn xây dựng Web Form của mình. **Route** sẽ được thiết lập dựa trên **Tiêu đề (Title)** của Web Form. Bạn cũng có thể thêm một văn bản Giới thiệu để hiển thị một thông điệp thân thiện phía trên biểu mẫu của mình.

Thêm các trường vào Web Form của bạn. Đây là các trường từ DocType mà bạn đã chọn. Bạn có thể thay đổi Nhãn (Label) cho các trường này. Hãy cố gắng giữ số lượng trường ở mức tối thiểu vì các biểu mẫu quá dài sẽ gây khó khăn khi điền.

![Web Form Fields](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/new-web-form-2.png)
*Các trường Web Form*

Nhấp vào **See on Website** ở thanh bên để xem Web form của bạn.
![Web Form](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/web-form.png)
*Web Form*

Dưới đây là giải thích cho từng ô kiểm ở bên phải.

1. **Published**: Web Form sẽ chỉ có thể truy cập được nếu tùy chọn này được bật.
1. **Login Required**: Người dùng chỉ có thể điền Web Form nếu họ đã đăng nhập.
    Khi Login Required được chọn,
1. **Route to Success Link**: Chuyển hướng đến Liên kết Thành công sau khi biểu mẫu được Xác nhận.
1. **Allow Edit**: Nếu không chọn mục này, biểu mẫu sẽ chỉ ở chế độ chỉ đọc sau khi được Lưu.
1. **Allow Multiple**: Cho phép người dùng tạo nhiều hơn một bản ghi.
1. **Show as Grid**: Hiển thị các bản ghi dưới dạng bảng.
1. **Allow Delete**: Cho phép người dùng xóa các bản ghi mà họ đã tạo.
1. **Allow Comments**: Cho phép người dùng thêm bình luận vào biểu mẫu đã tạo.
1. **Allow Print**: Cho phép người dùng in tài liệu theo Mẫu in đã chọn.
1. **Allow Incomplete Forms**: Cho phép người dùng gửi biểu mẫu với dữ liệu chưa đầy đủ.

## 2. Tính năng
### 2.1 Thanh bên (Sidebar)

Bạn cũng có thể hiển thị các liên kết ngữ cảnh trong thanh bên trên Web Form của mình. Thiết lập nó trong **Sidebar Settings**.

![Web Form Sidebar](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/web-form-sidebar.png)
*Thanh bên Web Form*

![Web Form with Sidebar](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/web-form-with-sidebar.png)
*Web Form có thanh bên*

### 2.2 Tạo Web Form với Bảng con (Child Table)

Bạn có thể thêm các bảng con vào web form của mình, giống như các biểu mẫu thông thường.

<img class="screenshot" alt="Web form Grid"
src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/grid-in-webform.png">


### 2.3 Tích hợp Cổng thanh toán

Giờ đây bạn có thể thêm Cổng thanh toán vào web form, để bạn có thể yêu cầu người dùng thanh toán cho một web form. Một ví dụ điển hình cho việc này là vé tham dự hội nghị.

<img class="screenshot" alt="Web form payment"
src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/payment-in-webform.png">

### 2.4 Người dùng Cổng thông tin (Portal User)

Chúng tôi cũng đã giới thiệu các vai trò cho người dùng Website. Trước phiên bản 11, nếu bạn gán bất kỳ 'Vai trò' (Role) nào cho một người dùng, họ sẽ có quyền truy cập vào 'Desk View'. Từ phiên bản 11, bạn có thể gán một 'Vai trò' nhưng vẫn có thể không cho phép truy cập vào 'Desk View' bằng cách bỏ chọn 'Desk Access' trong Vai trò đó.

<img class="screenshot" alt="Disallow Desk Access"
src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/disallow_desk_access.png">

Trong Cài đặt Cổng thông tin (Portal Settings), bạn có thể thiết lập một vai trò cho mỗi mục menu để chỉ những người dùng có vai trò đó mới được phép xem mục đó.

<img class="screenshot" alt="portal settings"
src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/portal-settings.png">

### 2.5 Script tùy chỉnh (Custom Script)

Bạn có thể viết các script tùy chỉnh cho Web Form của mình cho các việc như xác thực dữ liệu nhập vào, tự động điền giá trị, hiển thị thông báo thành công, hoặc bất kỳ hành động tùy ý nào khác.

Để tìm hiểu cách viết script tùy chỉnh cho Web Forms của bạn, hãy đọc [tài liệu Custom Scripts](https://frappe.io/docs/v13/user/en/web-forms#custom-script).

### 2.6 CSS tùy chỉnh (Custom CSS)

Bạn có thể tùy chỉnh giao diện của Web Form bằng cách viết CSS tùy chỉnh của riêng mình. Hãy kiểm tra các thành phần trên trang để xem các lớp (class) nào có sẵn để định dạng. Tìm hiểu thêm về CSS [tại đây](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics).

### 2.7 Hành động (Actions)

Bạn có thể thêm văn bản vào trường 'Success Message' và văn bản này sẽ được hiển thị cho người dùng sau khi họ Xác nhận web form thành công. Và người dùng sẽ được chuyển hướng đến URL được cung cấp tại 'Success URL' khi nhấp vào nút 'Continue'. Điều này chỉ áp dụng cho các webform có thể truy cập mà không cần đăng nhập người dùng (các webform không được chọn ô 'Login Required').

<img class="screenshot" alt="Success Message"
src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/success_message.png">


### 2.8 Kết quả

Khi một người dùng website gửi biểu mẫu, dữ liệu sẽ được lưu trữ trong tài liệu/DocType mà web form đó được tạo ra.

### 2.9 Tùy chỉnh

Để tùy chỉnh web form, hãy xem [Tài liệu Frappe Web Forms](https://frappe.io/docs/v13/user/en/guides/portal-development/web-forms)


{next}