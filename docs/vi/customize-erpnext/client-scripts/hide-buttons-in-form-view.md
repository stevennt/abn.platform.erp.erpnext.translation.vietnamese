<!-- add-breadcrumbs -->
# Ẩn các nút trong Chế độ xem biểu mẫu

Trong một Đơn bán hàng đã được Xác nhận, bạn có thể thấy các nút như **Update Items**, **Status**. Ngoài ra còn có nhiều tùy chọn dưới nút 'Create'.

<img alt="Custom Script" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/sales_order_buttons.png">

Bạn có thể viết script tùy chỉnh như hiển thị dưới đây để ẩn các nút này.

    frappe.ui.form.on('Sales Order', {
        refresh(frm) {
        setTimeout(() => {
            frm.remove_custom_button('Update Items');
            frm.remove_custom_button('Close', 'Status');
            frm.remove_custom_button('Work Order', 'Make');
            }, 10);
        }
    })

{next}