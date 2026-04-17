# Hạn chế người dùng dựa trên bản ghi con

Dưới đây là hướng dẫn tùy chỉnh logic để hạn chế quyền truy cập của người dùng đối với các kho hàng cụ thể trong Phiếu kho (Stock Entry).

### Mục tiêu
Ngăn chặn người dùng không có vai trò "Material Manager" thực hiện các Phiếu kho có liên quan đến kho hàng bị hạn chế ("Restricted").

### Mã tùy chỉnh (Custom Script)

Bạn có thể thêm đoạn mã sau vào phần **Client Script** của DocType **Phiếu kho (Stock Entry)** để kiểm tra điều kiện khi người dùng nhấn **Lưu (Save)**.

```javascript
// Hạn chế một số kho nhất định đối với Material Manager
cur_frm.cscript.validate = function(doc) {
    // Kiểm tra nếu người dùng KHÔNG có vai trò "Material Manager"
    if (frappe.user_roles.indexOf("Material Manager") == -1) {

        // Kiểm tra xem có dòng chi tiết nào có Kho xuất (s_warehouse) là "Restricted" không
        var restricted_in_source = frappe.model.get_list("Stock Entry Detail", {
            parent: cur_frm.doc.name, 
            s_warehouse: "Restricted"
        });

        // Kiểm tra xem có dòng chi tiết nào có Kho nhập (t_warehouse) là "Restricted" không
        var restricted_in_target = frappe.model.get_list("Stock Entry Detail", {
            parent: cur_frm.doc.name, 
            t_warehouse: "Restricted"
        });

        // Nếu tìm thấy kho bị hạn chế trong danh sách chi tiết
        if (restricted_in_source.length || restricted_in_target.length) {
            frappe.msgprint(__("Chỉ Material Manager mới có quyền thực hiện Phiếu kho tại Kho bị hạn chế (Restricted Warehouse)"));
            frappe.validated = false; // Ngăn chặn việc Lưu (Save) bản ghi
        }
    }
};
```

### Giải thích logic

1.  **Kiểm tra vai trò**: Hệ thống kiểm tra danh sách vai trò của người dùng hiện tại. Nếu không tìm thấy vai trò `Material Manager`, các bước kiểm tra tiếp theo sẽ được thực hiện.
2.  **Truy vấn bản ghi con**: 
    *   Sử dụng `frappe.model.get_list` để quét các dòng trong bảng **Chi tiết Phiếu kho (Stock Entry Detail)**.
    *   `s_warehouse`: Kiểm tra kho xuất hàng.
    *   `t_warehouse`: Kiểm tra kho nhập hàng.
3.  **Ngăn chặn hành động**: Nếu phát hiện có sự xuất hiện của kho `"Restricted"`, hệ thống sẽ hiển thị thông báo lỗi và đặt `frappe.validated = false`, khiến người dùng không thể **Lưu (Save)** hoặc **Xác nhận (Submit)** Phiếu kho đó.

---
*Lưu ý: Đảm bảo tên kho `"Restricted"` khớp chính xác với tên kho đã thiết lập trong danh mục **Kho (Warehouse)** của hệ thống.*