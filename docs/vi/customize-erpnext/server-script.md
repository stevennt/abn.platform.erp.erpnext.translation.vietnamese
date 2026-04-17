<!-- add-breadcrumbs -->
# Server Script

**Server Script cho phép bạn định nghĩa một Python Script một cách linh hoạt để thực thi trên máy chủ dựa trên một sự kiện của tài liệu hoặc API**

> Được giới thiệu trong Phiên bản 12

## 1. Cách tạo Server Script

Để tạo một Server Script

1. Nếu trang web của bạn đang được lưu trữ trên [erpnext.com](https://erpnext.com/), hãy liên hệ với bộ phận hỗ trợ để kích hoạt Server Script.
	Trong trường hợp các tài khoản tự lưu trữ (self-hosted), hãy đặt `server_script_enabled` thành true trong file site_config.json của trang web.
2. Để thêm/chỉnh sửa Server Script, hãy đảm bảo vai trò của bạn là System Manager.
3. Tạo một server script mới thông qua "New Server Script" trong thanh công cụ.
4. Chọn loại server script: Document Event, API, Permission Query.
5. Thiết lập loại tài liệu và tên sự kiện, hoặc tên phương thức, mã script và Lưu.

## 2. Các tính năng

### 2.1 Kích hoạt Server Script

Server script phải được kích hoạt thông qua site_config.json

```
bench --site site1.local set-config server_script_enabled true
```

### 2.2 Document Events (Sự kiện tài liệu)

Đối với các script được gọi thông qua các sự kiện của tài liệu, bạn phải thiết lập Reference Document Type và Event Name để xác định trình kích hoạt

- Before Insert
- Before Save
- After Save
- Before Submit
- After Submit
- Before Cancel
- After Cancel
- Before Delete
- After Delete
- Before Save (Submitted Document)
- After Save (Submitted Document)

### 2.3 API Scripts

Bạn có thể tạo một API mới có thể được truy cập thông qua `api/method/[methodname]` bằng loại script là "API"

Nếu bạn muốn người dùng khách (guest user) có thể truy cập API, bạn phải tích vào "Allow Guest"

Phản hồi có thể được thiết lập thông qua đối tượng `frappe.response["message"]`

### 2.4 Permission Query (Truy vấn quyền)

Loại script này cho phép bạn thêm các điều kiện tùy chỉnh trong mệnh đề where cho một truy vấn danh sách DocType.

Ví dụ, giả sử bạn muốn chỉ hiển thị danh sách các bản ghi ToDo cho một người dùng nếu họ là người được giao bản ghi đó hoặc bản ghi đó được giao cho họ. Điều này có thể được thực hiện bằng script sau:

```py
conditions = 'owner = {user} or assigned_by = {user}'.format(user=frappe.db.escape(user))
```

Truy vấn `select` kết quả sẽ trông giống như thế này:
```sql
select * from `tabToDo` where owner = 'faris@erpnext.com' or assigned_by = 'faris@erpnext.com'
```

Giờ đây, chế độ xem danh sách của ToDo sẽ chỉ hiển thị các bản ghi bị giới hạn. Điều này cũng sẽ giới hạn các kết quả hiển thị trong các trường Link.

### 2.5 Bảo mật

Frappe Framework sử dụng thư viện RestrictedPython để hạn chế quyền truy cập vào các phương thức có sẵn cho server script. Chỉ những phương thức an toàn được liệt kê dưới đây mới có sẵn trong server script

```py
json # json module
dict # internal dict
_ # translator method
_dict # frappe._dict internal method
frappe.flags # global flags

# FORMATTING
frappe.format # frappe.format_value(value, dict(fieldtype='Currency'))
frappe.format_value # frappe.format_value(value, dict(fieldtype='Currency'))
frappe.date_format # default date format
frappe.format_date # returns date as "1st September 2019"

# SESSION
frappe.form_dict # form / request parameters
frappe.request # request object
frappe.response # response object
frappe.session.user # current user
frappe.session.csrf_token # CSRF token of the current session
frappe.user  # current user
frappe.get_fullname # fullname of the current user
frappe.get_gravatar # frappe.utils.get_gravatar_url
frappe.full_name = # fullname of the current user

# ORM
frappe.get_meta # get metadata object
frappe.get_doc
frappe.get_cached_doc
frappe.get_list
frappe.get_all
frappe.get_system_settings

# DB
frappe.db.get_list
frappe.db.get_all
frappe.db.get_value
frappe.db.get_single_value
frappe.db.get_default
frappe.db.escape

# UTILITIES
frappe.msgprint # msgprint
frappe.get_hooks # app hooks
frappe.utils # methods in frappe.utils
frappe.render_template # frappe.render_template,
frappe.get_url # frappe.utils.get_url
frappe.sendmail # send email via server script
frappe.get_print # get pdf for a doc
frappe.attach_print # attach PDF to an email
socketio_port # port for socketio
style.border_color # '#d1d8dd'
guess_mimetype = mimetypes.guess_type,
html2text = html2text,
dev_server # True if in developer mode
```

## 3. Ví dụ

### 3.1 Thay đổi giá trị của một thuộc tính trước khi thay đổi

Script Type: Before Save

```py
if "test" in doc.description:
	doc.status = 'Closed'
```

### 3.2 Xác thực tùy chỉnh

Script Type: "Before Save"

```py
if "validate" in doc.description:
	raise frappe.ValidationError
```

### 3.3. Tự động tạo To Do

Script Type: "After Save"

```py
if doc.allocated_to:
    frappe.get_doc(dict(
        doctype = 'ToDo'
        owner = doc.allocated_to,
        description = doc.subject
    )).insert()
```

### 3.4 API

- Script Type: API
- Method Name: `test_method`

```py
frappe.response['message'] = "hello"
```

Request: `/api/method/test_method`