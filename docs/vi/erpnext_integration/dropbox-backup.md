<!-- add-breadcrumbs -->
#Thiết lập Sao lưu Dropbox

Chúng tôi luôn khuyến nghị Khách hàng duy trì bản sao lưu dữ liệu của họ trong ERPNext. Bản sao lưu cơ sở dữ liệu được tải xuống dưới dạng tệp SQL. Nếu cần, tệp SQL sao lưu này cũng có thể được khôi phục vào một tài khoản ERPNext khác.

Bạn có thể tự động hóa việc tải xuống bản sao lưu cơ sở dữ liệu từ tài khoản ERPNext của mình vào tài khoản Dropbox.

Để thiết lập Sao lưu Dropbox,
> Trang chủ > Tích hợp > Cài đặt Dropbox

##Các bước thực hiện khác nhau giữa phiên bản ERPNext được quản lý (Managed Version) và phiên bản mã nguồn mở (Open-source)

###Hướng dẫn cho phiên bản ERPNext được quản lý

####Bước 1: Thiết lập Tần suất

Thiết lập Tần suất để tải xuống bản sao lưu vào tài khoản Dropbox của bạn.

<img class="screenshot" alt="set frequency" src="https://docs.erpnext.com/docs/v13/assets/img/setup/integrations/setup-backup-frequency.png">

####Bước 2: Cho phép truy cập Dropbox

Sau khi thiết lập tần suất và cập nhật các chi tiết khác, hãy nhấp vào `Allow Dropbox access`. Khi nhấp vào nút này, trang đăng nhập Dropbox sẽ mở ra trong một tab mới. Điều này có thể yêu cầu bạn cho phép hiển thị cửa sổ bật lên (pop-up) cho tài khoản ERPNext của mình.

####Bước 3: Đăng nhập vào Dropbox

Đăng nhập vào tài khoản Dropbox của bạn bằng cách nhập thông tin đăng nhập.

<img class="screenshot" alt="Login" src="https://docs.erpnext.com/docs/v13/assets/img/setup/integrations/dropbox-2.png">

####Bước 4: Cho phép

Sau khi đăng nhập thành công, bạn sẽ thấy một thông báo xác nhận như sau. Nhấp vào "Allow" để cho phép tài khoản ERPNext của bạn có quyền truy cập vào tài khoản Dropbox của bạn.

<img class="screenshot" alt="Allow" src="https://docs.erpnext.com/docs/v13/assets/img/setup/integrations/dropbox-3.png">

Với thao tác này, một thư mục có tên "ERPNext" sẽ được tạo trong tài khoản Dropbox của bạn, và bản sao lưu cơ sở dữ liệu sẽ bắt đầu được tự động tải xuống trong đó.


##Hướng dẫn cho phiên bản Mã nguồn mở

####Bước 1: Đăng nhập vào khu vực Nhà phát triển Dropbox

<a href="https://www.dropbox.com/developers/apps" target="_blank" style="line-height: 1.42857143;">https://www.dropbox.com/developers/apps</a>
####Bước 2: Tạo một ứng dụng Dropbox mới
<img class="screenshot" alt="Create new" src="https://docs.erpnext.com/docs/v13/assets/img/setup/integrations/dropbox-open-3.png">
####Bước 3: Điền thông tin chi tiết cho ứng dụng mới của bạn
<img class="screenshot" alt="Choose Dropbox API and type as APP Folder" src="https://docs.erpnext.com/docs/v13/assets/img/setup/integrations/dropbox-open-1.png">
-
<img class="screenshot" alt="Setup APP Name" src="https://docs.erpnext.com/docs/v13/assets/img/setup/integrations/dropbox-open-2.png">
####Bước 4: Chèn Redirect URI tên miền tùy chỉnh của bạn
`https://{yourwebsite.com}/api/method/frappe.integrations.doctype.dropbox_settings.dropbox_settings.dropbox_auth_finish`
<img class="screenshot" alt="Set Redirect URL" src="https://docs.erpnext.com/docs/v13/assets/img/setup/integrations/dropbox_redirect_uri.png">

####Bước 5: Trong một cửa sổ mới, hãy mở trang Cài đặt Dropbox trong bản cài đặt ERPnext của bạn
####Bước 6: Thiết lập tần suất sao lưu và email
Thiết lập tần suất để tải xuống các bản sao lưu trang web của bạn vào tài khoản Dropbox.
<img class="screenshot" alt="set frequency" src="https://docs.erpnext.com/docs/v13/assets/img/setup/integrations/setup-backup-frequency.png">

####Bước 7: Nhập các Khóa từ cửa sổ Ứng dụng Dropbox của bạn
Từ trang Ứng dụng Dropbox, hãy nhập app key và app secret (không bị ẩn) vào trang cài đặt Dropbox của ERPnext.

Ngoài ra, bạn có thể nhập thủ công vào tệp `sites/{sitename}/site_config.json` như sau,
<div>
	<pre>
		<code>{
 "db_name": "demo",
 "db_password": "DZ1Idd55xJ9qvkHvUH",
 "dropbox_access_key": "ACCESSKEY",
 "dropbox_secret_key": "SECRECTKEY"
}
		</code>
	</pre>
</div>

####Bước 8: Nhấp Lưu trước khi tiếp tục!!!
####Bước 9: Sau khi Lưu, nhấp vào "Allow Dropbox Access"
Trang đăng nhập Dropbox sẽ mở ra trong một tab mới. Điều này có thể yêu cầu bạn cho phép hiển thị cửa sổ bật lên (pop-up) cho tài khoản ERPNext của mình.
####Bước 11: Cho phép truy cập Dropbox
Sau khi đăng nhập thành công, bạn sẽ thấy một thông báo xác nhận như sau. Nhấp vào "Allow" để cho phép tài khoản ERPNext của bạn có quyền truy cập vào tài khoản Dropbox của bạn.
<img class="screenshot" alt="Allow" src="https://docs.erpnext.com/docs/v13/assets/img/setup/integrations/dropbox-3.png">
####Bước 12: Xác nhận Sao lưu hoạt động
Từ trang Dropbox của ERPnext, nhấp vào `Take Backup Now` và sau đó đi tới chế độ xem tệp Dropbox của bạn. Bạn sẽ thấy một thư mục mới trong Dropbox có tên là `Apps` và bên trong đó là thư mục {New App} của bạn. Bên trong đó sẽ có các thư mục sao lưu cho cả tệp và cơ sở dữ liệu.
Vì vậy, đối với một ứng dụng có tên là `erpnext`, các vị trí thư mục như sau:
```
Tệp cơ sở dữ liệu: /Apps/erpnext/database
Tệp công khai: /Apps/erpnext/files
Tệp riêng tư: /Apps/erpnext/private/files
```

> **Lưu ý**: Nếu kích thước bản sao lưu nén vượt quá 1GB (Gigabyte), hệ thống sẽ tải bản sao lưu mới nhất hiện có lên Dropbox thay vì tạo một tệp sao lưu mới.