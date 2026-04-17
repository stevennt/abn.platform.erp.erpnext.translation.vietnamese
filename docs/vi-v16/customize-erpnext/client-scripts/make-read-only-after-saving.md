<!-- add-breadcrumbs -->
# Chuyển sang Chế độ Chỉ đọc sau khi Lưu

Sử dụng phương thức `cur_frm.set_df_property` để cập nhật hiển thị của trường.

Trong tập lệnh này, chúng ta sử dụng thuộc tính `is_new()` của form để kiểm tra xem tài liệu đã được **Lưu** ít nhất một lần hay chưa. Nếu `is_new()` trả về `true`, tài liệu đó là tài liệu mới và chưa được lưu vào hệ thống.

```js
frappe.ui.form.on("MyDocType", "refresh", function(frm) {
	// Sử dụng phương thức is_new của frm để kiểm tra xem tài liệu đã được Lưu hay chưa
	// Nếu là tài liệu mới (is_new = true), đặt read_only = 0 (có thể chỉnh sửa)
	// Nếu đã được Lưu (is_new = false), đặt read_only = 1 (chỉ đọc)
	frm.set_df_property("myfield", "read_only", frm.is_new() ? 0 : 1);
});
```

{next}