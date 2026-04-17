# Ví dụ hướng dẫn cách lấy giá trị vào trường của bảng con từ DocType chính


### Script mẫu để lấy trường expiry_date từ DocType Batch vào bảng Sales Invoice Item

Bước 1: Tạo Custom Script cho DocType _**Sales Invoice**_ (cha)

Bước 2: Sử dụng Script dưới đây & Lưu

```
frappe.ui.form.on("Sales Invoice Item", "batch_no", function(frm, cdt, cdn) {
	var d = locals[cdt][cdn];
    	frappe.db.get_value("Batch", {"name": d.batch_no}, "expiry_date", function(value) {
    		d.expiry_date = value.expiry_date;
    	});
});