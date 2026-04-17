<!-- add-breadcrumbs -->
# Hạn chế quyền Hủy

Thêm một trình xử lý (handler) vào sự kiện `custom_before_cancel` để kiểm soát quyền hủy giao dịch dựa trên vai trò người dùng và giá trị của tài liệu.

```javascript
cur_frm.cscript.custom_before_cancel = function(doc) {
    // Kiểm tra nếu người dùng có vai trò "Accounts User" nhưng KHÔNG có vai trò "Accounts Manager" hoặc "System Manager"
    if (frappe.user_roles.indexOf("Accounts User") != -1 && 
        frappe.user_roles.indexOf("Accounts Manager") == -1 && 
        frappe.user_roles.indexOf("System Manager") == -1) {
        
        // Nếu tổng tiền (grand total) lớn hơn 10,000
        if (flt(doc.grand_total) > 10000) {
            frappe.msgprint(__("Bạn không thể Hủy giao dịch này, vì tổng cộng lớn hơn 10,000"));
            frappe.validated = false;
        }
    }
}
```

**Giải thích:**
*   Đoạn mã trên ngăn chặn người dùng có vai trò kế toán thông thường (`Accounts User`) thực hiện lệnh **Hủy** đối với các tài liệu (như **Hóa đơn**, **Đơn bán hàng**, v.v.) có giá trị lớn hơn 10,000.
*   Người có vai trò `Accounts Manager` hoặc `System Manager` vẫn có toàn quyền **Hủy** mà không bị giới hạn bởi điều kiện này.