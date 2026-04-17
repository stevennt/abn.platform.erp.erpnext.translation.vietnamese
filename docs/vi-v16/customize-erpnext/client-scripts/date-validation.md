<!-- add-breadcrumbs -->
# Xác thực ngày tháng

```javascript
	frappe.ui.form.on("Task", "validate", function(frm) {
        if (frm.doc.from_date < frappe.datetime.get_today()) {
            frappe.msgprint(__("Bạn không thể chọn ngày trong quá khứ cho Ngày bắt đầu"));
            frappe.validated = false;
        }
	});
```

{next}