<!-- add-breadcrumbs -->
# Thêm Nút Tùy chỉnh

Để thêm một nút tùy chỉnh vào giao diện người dùng (UI) của một Form trong ERPNext, bạn có thể sử dụng Client Script. Dưới đây là cách thực hiện:

```javascript
frappe.ui.form.on("Event", "refresh", function(frm) {
    // Thêm nút tùy chỉnh vào thanh công cụ của Form
    frm.add_custom_button(__("Thực hiện thao tác"), function() {
        // Mã xử lý khi nút này được nhấp vào
        
        var subject = frm.doc.subject;
        var event_type = frm.doc.event_type;
        
        // Ví dụ: Thực hiện một yêu cầu AJAX hoặc gọi hàm phía máy chủ bằng frappe.call
        $.ajax({
            url: "http://example.com/just-do-it",
            data: {
                "subject": subject,
                "event_type": event_type
            }
            
            // Tham khảo thêm về cú pháp $.ajax tại http://api.jquery.com/jquery.ajax/
        });
    });
});
```

### Giải thích chi tiết:

1.  **`frappe.ui.form.on("Event", "refresh", ...)`**: Đây là trình lắng nghe sự kiện (event listener). Nó sẽ kích hoạt hàm bên trong mỗi khi Form của loại tài liệu "Event" được tải lại hoặc làm mới.
2.  **`frm.add_custom_button(__("Tên nút"), function() { ... })`**: 
    *   Tham số thứ nhất là nhãn của nút (được bao quanh bởi `__()` để hỗ trợ đa ngôn ngữ).
    *   Tham số thứ hai là một hàm callback sẽ được thực thi khi người dùng nhấn vào nút.
3.  **`frm.doc`**: Đối tượng này chứa toàn bộ dữ liệu của bản ghi hiện tại đang hiển thị trên màn hình.

**Lưu ý:** Trong các phiên bản mới như v16, nếu bạn muốn nút nằm trong menu thả xuống (Menu) thay vì hiển thị trực tiếp trên thanh công cụ, bạn có thể sử dụng `frm.add_custom_button` kết hợp với tham số thứ ba để chỉ định nhóm nút.

{next}