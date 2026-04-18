<!-- add-breadcrumbs -->
# Ẩn các nút trong Chế độ xem biểu mẫu

Trong một Đơn bán hàng đã được Xác nhận, bạn có thể thấy các nút như **Cập nhật mặt hàng (Update Items)**, **Trạng thái (Status)**. Ngoài ra còn có nhiều tùy chọn khác dưới nút 'Tạo (Create)'.

<img alt="Custom Script" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/sales_order_buttons.png">

Bạn có thể viết script tùy chỉnh như hiển thị dưới đây để ẩn các nút này.

```javascript
frappe.ui.form.on('Đơn bán hàng', {
    refresh(frm) {
        setTimeout(() => {
            frm.remove_custom_button(__('Cập nhật mặt hàng'));
            frm.remove_custom_button(__('Đóng'), __('Trạng thái'));
            frm.remove_custom_button(__('Lệnh sản xuất'), __('Tạo'));
        }, 10);
    }
})
```

{next}