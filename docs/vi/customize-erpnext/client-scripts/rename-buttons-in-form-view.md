<!-- add-breadcrumbs -->
# Đổi tên các nút trong Chế độ xem biểu mẫu

Trong một Đơn bán hàng đã được Xác nhận, bạn có thể thấy nhiều tùy chọn dưới mục 'Create':

<img alt="Custom Script" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/customize-button-all.png">

Bạn có thể sử dụng đoạn script tùy chỉnh này để đổi tên các nút:

```
frappe.ui.form.on('Sales Order', {
	on_submit: function(frm){
	//	console.log('reloaded doc on submit')
		location.reload()
	},
	onload_post_render: function(frm){
		var bt = ['Delivery', 'Work Order', 'Invoice', 'Material Request', 'Request for Raw Materials', 'Purchase Order', 'Payment Request', 'Payment', 'Project', 'Subscription']
		bt.forEach(function(bt){
			frm.page.remove_inner_button(bt, 'Create')
			});
		frm.page.add_inner_button('Order Raw Materials', () => cur_frm.cscript.make_raw_material_request(), 'Create')
		}
	}
);
```

Sử dụng script này, chúng tôi đã loại bỏ/ẩn các nút không mong muốn, và sau đó đổi tên một nút:

<img alt="Custom Script" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/customize-button-rename.png">

**Lưu ý:** Để tìm hiểu thêm về các JS API, hãy truy cập [tài liệu frappe](https://frappe.io/docs/v13/user/en/api/form).

Để kiểm tra phương thức nào đang được gọi, bạn sẽ cần kiểm tra tệp JS của DocType đó. Trong ví dụ này, để đổi tên 'Request For Raw Materials', chúng tôi đang tham chiếu đến [dòng này](https://github.com/frappe/erpnext/blob/782f45ae5f272173b5daadb493d40cf7ccf131b4/erpnext/selling/doctype/sales_order/sales_order.js#L167).

{next}