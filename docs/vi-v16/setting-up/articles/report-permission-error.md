<!-- add-breadcrumbs -->
# Giải quyết các vấn đề về lỗi phân quyền

**Câu hỏi:** Người dùng được gán các vai trò như Account User và Account Manager. Tuy nhiên, khi truy cập báo cáo Account Receivable, Người dùng lại nhận được thông báo lỗi không có quyền đối với Territory master.

<img alt="Report Permission Error" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/report-permission-1.png">

**Trả lời:**

Theo hệ thống phân quyền trong ERPNext, để Người dùng có thể truy cập một biểu mẫu hoặc một báo cáo, người đó ít nhất phải có quyền Read (Đọc) đối với tất cả các trường liên kết (link field) trong biểu mẫu/báo cáo đó. Vì Territory là một trường liên kết trong báo cáo Account Receivable, vui lòng thêm một quy tắc phân quyền để cho phép Account User/Manager có ít nhất quyền Read đối với Territory master. Vui lòng làm theo các bước dưới đây để giải quyết vấn đề này.

1. Các vai trò được gán cho Người dùng là Account User và Account Manager.

2. Như đã chỉ ra trong thông báo lỗi, người dùng không có quyền đối với Territory master. Theo phân quyền mặc định, không có vai trò nào được gán cho Người dùng đó có bất kỳ quyền nào đối với Territory master.

3. Để giải quyết vấn đề này, hãy gán quyền Read cho Account User đối với Territory master thông qua Role Permissions Manager.

    <img alt="Permission Manager" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/report-permission-2.png">

Sau khi cập nhật phân quyền này, Người dùng sẽ có thể truy cập báo cáo Account Receivable một cách bình thường.