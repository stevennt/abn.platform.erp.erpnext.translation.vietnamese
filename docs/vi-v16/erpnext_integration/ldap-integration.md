<!-- add-breadcrumbs -->
# Thiết lập LDAP

Lightweight Directory Access Protocol (LDAP) là một hệ thống kiểm soát truy cập tập trung được sử dụng bởi nhiều tổ chức quy mô vừa và nhỏ.

Bằng cách thiết lập dịch vụ LDAP, bạn có thể đăng nhập vào tài khoản ERPNext bằng thông tin đăng nhập LDAP.

## 1. Điều kiện tiên quyết
Để sử dụng LDAP, trước tiên bạn cần cài đặt mô-đun Python `ldap3`. Để thực hiện việc này, hãy mở một phiên làm việc terminal trên máy chủ đang chạy thực thể ERPNext. Đi tới thư mục `frappe-bench`.
Chạy lệnh: `./env/pip install ldap3`

Bây giờ bạn đã sẵn sàng để kích hoạt dịch vụ LDAP trong ERPNext.

## 2. Thiết lập LDAP
Để thiết lập LDAP, hãy đi tới
> Home > Integrations > LDAP Settings

Nhiều tham số là bắt buộc để cho phép ERPNext kết nối với LDAP. Chúng bao gồm:

  * **LDAP Server URL**: Đây là URL dẫn đến máy chủ LDAP của bạn. Phải ở dạng `ldap://yourserver:port` hoặc `ldaps://yourserver:port`

  * **Base Distinguished Name (DN)**: Đây là tên định danh (distinguished name) của người dùng có quyền tra cứu thông tin chi tiết người dùng trên máy chủ LDAP của bạn. Đây nên là một người dùng chỉ có quyền chỉ đọc trên Máy chủ LDAP của bạn.

  * **Password for Base DN**: Đây là mật khẩu cho người dùng nêu trên, được sử dụng để tra cứu thông tin chi tiết người dùng trên máy chủ LDAP của bạn.

  * **Organization Unit of Users**: DN của Đơn vị Tổ chức (Organizational Unit) mà tất cả người dùng trong máy chủ LDAP của bạn phải thuộc về để có thể đăng nhập vào ERPNext.

  * **Default Role on Creation**: Khi người dùng được tạo trong ERPNext, họ sẽ được gán vai trò mặc định này trong lần đầu tiên họ đăng nhập.

  * **LDAP Search String**: Trường này cho phép ERPNext khớp người dùng/email được nhập trong màn hình đăng nhập ERPNext với Máy chủ LDAP. Ví dụ, bạn có thể sử dụng địa chỉ email hoặc tên người dùng tùy theo sở thích của mình.

    Nó phải được nhập theo định dạng: `LDAPFIELD={0}`

    Ví dụ tên người dùng Active Directory: `sAMAccountName={0}`

    Ví dụ tên người dùng Open LDAP: `uid={0}`

  * **LDAP Email Field**: Chỉ định trường LDAP chứa địa chỉ email của người dùng.

    Ví dụ cho Active Directory và Open LDAP: `mail`

  * **LDAP Username Field**: Chỉ định trường LDAP chứa tên người dùng của người dùng.

    Ví dụ cho Active Directory: `sAMAccountName`

    Ví dụ cho Open LDAP: `uid`

  * **LDAP First Name Field**: Chỉ định trường LDAP chứa tên của người dùng.

    Ví dụ cho Active Directory: `givenName`

    Ví dụ cho Open LDAP: `sn`

Có nhiều trường không bắt buộc khác mà bạn có thể sử dụng để ánh xạ các trường người dùng LDAP của mình với các trường người dùng ERPNext. Chúng bao gồm:

  * Middle Name (Tên đệm)
  * Phone (Điện thoại)
  * Mobile (Di động)

<img class="screenshot" alt="LDAP Settings" src="../assets/img/setup/integrations/ldap_settings.png">

Khi các cài đặt của bạn đã chính xác, bạn có thể nhấp vào hộp kiểm `Enabled` ở phía trên. Khi cố gắng kích hoạt LDAP, ERPNext sẽ cố gắng kết nối với máy chủ LDAP để đảm bảo các cài đặt là chính xác. Nếu thất bại, bạn sẽ không thể kích hoạt LDAP và sẽ nhận được thông báo lỗi.

Thông báo lỗi sẽ cho biết vấn đề cần được giải quyết để tiếp tục.

Sau khi thiết lập kích hoạt LDAP, trên màn hình đăng nhập, hệ thống sẽ kích hoạt tùy chọn **Login Via LDAP**.

<img class="screenshot" alt="LOGIN via LDAP" src="../assets/img/setup/integrations/login_via_ldap.png">

### 2.1 Bảo mật LDAP

Trong phần LDAP Security, bạn có nhiều tùy chọn để kết nối an toàn với máy chủ LDAP của mình.

  * ##### SSL/TLS Mode
    Chỉ định liệu bạn có muốn bắt đầu một phiên TLS khi kết nối ban đầu với máy chủ LDAP hay không.

  * ##### Require Trusted Certificate
    Chỉ định liệu bạn có yêu cầu một chứng chỉ đáng tin cậy để kết nối với máy chủ LDAP hay không.


  Nếu bạn chỉ định một chứng chỉ đáng tin cậy, bạn sẽ cần chỉ định đường dẫn đến các tệp chứng chỉ của mình. Các tệp này phải được đặt trên máy chủ ERPNext của bạn, và các trường sau đây phải là đường dẫn tuyệt đối đến các tệp trên máy chủ của bạn.
    Các trường chứng chỉ bao gồm:

  * Path to private Key File (Đường dẫn đến tệp Khóa riêng)

  * Path to Server Certificate (Đường dẫn đến Chứng chỉ Máy chủ)

  * Path to CA Certs File (Đường dẫn đến tệp Chứng chỉ CA)


### 2.2 Ánh xạ Nhóm LDAP (LDAP Group Mappings)
ERPNext cũng cho phép bạn tự động ánh xạ nhiều nhóm LDAP với các vai trò ERPNext tương ứng.
Ví dụ, bạn có thể muốn tất cả nhân viên Kế toán của mình tự động có Vai trò Người dùng Kế toán (Accounts User Role).

Đảm bảo rằng bạn điền đầy đủ trường LDAP Group để cho phép điều này. Đây là trường LDAP được tìm thấy trong đối tượng người dùng trong LDAP, chứa tất cả các nhóm mà người dùng đó là thành viên.

Đối với Active Directory và Open LDAP, trường này nên được đặt là `memberOf`.

Open LDAP có thể cần trường này được kích hoạt trên máy chủ LDAP của bạn. Vui lòng xem các ví dụ trên internet để biết thêm chi tiết.

> Lưu ý rằng tất cả các vai trò ERPNext sẽ được kiểm tra mỗi khi người dùng đăng nhập và sẽ được thêm vào hoặc xóa khỏi quyền của người dùng.

<img class="screenshot" alt="LDAP Group Mappings" src="../assets/img/setup/integrations/ldap_group_mappings.png">

Trong khu vực LDAP Settings, có hai menu thả xuống.
1. SSL/TLS Mode - hãy đặt thành **StartTLS** để kết nối với máy chủ LDAP của bạn bằng StartTLS. Nếu máy chủ LDAP của bạn không hỗ trợ StartTLS, việc đặt thành StartTLS sẽ dẫn đến lỗi `StartTLS is not supported`. Hãy kiểm tra cấu hình trên máy chủ LDAP của bạn nếu bạn nhận được lỗi này.
2. Require Trusted Certificate - nếu bạn chuyển tùy chọn này thành **Yes** thì chứng chỉ do máy chủ LDAP cung cấp phải được máy chủ Frappe/ERPNext tin tưởng. Nếu bạn muốn sử dụng StartTLS với một chứng chỉ tự ký (không đáng tin cậy), hãy đặt thành **No**. Nếu bạn không sử dụng StartTLS, cài đặt này sẽ bị bỏ qua.