<!-- add-breadcrumbs -->

# Hành động Quy trình (Workflow Actions)

> Được giới thiệu trong Phiên bản 11

**Hành động Quy trình là một nơi duy nhất để quản lý tất cả các hành động đang chờ xử lý mà bạn có thể thực hiện đối với các Quy trình.**

Hành động Quy trình sẽ chỉ gửi thông báo email nếu ô 'Send Email Alert' được tích trong Quy trình mà bạn đã tạo.

Để truy cập Hành động Quy trình, hãy đi tới:
> Home > Settings > Workflow Actions

Nếu một Người dùng đủ điều kiện để thực hiện hành động trên một số quy trình, email sẽ được gửi đến người dùng đó với tài liệu liên quan được đính kèm. Từ đó, người dùng có thể `Approve` (Phê duyệt) hoặc `Reject` (Từ chối) Quy trình.

![Workflow Action Email](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/workflow-actions-email.png)

Ngoài ra, người dùng sẽ thấy các mục nhập trong danh sách Hành động Quy trình của họ:
![Workflow Action List](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/workflow-actions-list.png)

**Lưu ý:**

- Bạn có thể thiết lập mẫu email cho Hành động Quy trình tại mỗi trạng thái. Mẫu này có thể bao gồm một thông điệp để người dùng tiếp tục thực hiện các Hành động Quy trình tiếp theo.
- Hành động Quy trình sẽ không được tạo cho các chuyển đổi sang các trạng thái tùy chọn (optional states).

### Các chủ đề liên quan
1. [Workflows](workflows.md)
1. [Assignment Rule](../automation/assignment-rule.md)

{next}