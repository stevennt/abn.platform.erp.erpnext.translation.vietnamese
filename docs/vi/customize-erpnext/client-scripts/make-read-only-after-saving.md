<!-- add-breadcrumbs -->
# Chuyển sang Chế độ Chỉ đọc sau khi Lưu

Sử dụng phương thức `cur_frm.set_df_property` để cập nhật hiển thị của trường.

Trong tập lệnh này, chúng ta cũng sử dụng thuộc tính `__islocal` của DocType để kiểm tra xem tài liệu đã được lưu ít nhất một lần hay chưa hoặc chưa bao giờ được lưu. Nếu `__islocal` là `1`, thì tài liệu đó chưa bao giờ được lưu.

```js
frappe.ui.form.on("MyDocType", "refresh", function(frm) {
	// sử dụng phương thức is_new của frm để kiểm tra xem tài liệu đã được lưu hay chưa
	frm.set_df_property("myfield", "read_only", frm.is_new() ? 0 : 1);
}
```

{next}