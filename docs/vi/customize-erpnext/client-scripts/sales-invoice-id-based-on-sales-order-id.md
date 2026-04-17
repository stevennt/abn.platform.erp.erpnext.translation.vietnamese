<!-- add-breadcrumbs -->
# ID Hóa đơn bán hàng dựa trên ID Đơn bán hàng

Đoạn mã dưới đây cho phép bạn áp dụng chuỗi đặt tên (naming series) cho Hóa đơn bán hàng giống như Đơn bán hàng tương ứng.
Hóa đơn bán hàng sử dụng tiền tố M- nhưng phần số sẽ được lấy trùng với Tên Đơn bán hàng.

Ví dụ: Nếu ID Đơn bán hàng là SO-12345, thì ID Hóa đơn bán hàng tương ứng sẽ được thiết lập là M-12345.

```js
frappe.ui.form.on("Sales Invoice", "refresh", function(frm){
	var sales_order = frm.doc.items[0].sales_order.replace("M", "M-");
	if (!frm.is_new() && sales_order && frm.doc.name!==sales_order){
		frappe.call({
		method: 'frappe.model.rename_doc.rename_doc',
		args: {
			doctype: frm.doctype,
			old: frm.docname,
			"new": sales_order,
			"merge": false
		},
	});
	}
});
```
{next}