<!-- add-breadcrumbs -->
# Cập nhật trường Ngày dựa trên giá trị của trường Ngày khác

Đoạn mã dưới đây sẽ tự động thiết lập giá trị cho trường ngày, dựa trên giá trị của một trường ngày khác.

Ví dụ: Ngày hạn sản xuất (Production Due Date) phải được thiết lập trước Ngày giao hàng (Delivery Date) hai ngày. Giả sử rằng Ngày giao hàng cho một dự án đã được xác định, và đã có sẵn một trường 'Production Due Date' với kiểu trường là 'Date' trong biểu mẫu. Việc áp dụng đoạn mã sau đây sẽ đảm bảo rằng Ngày hạn sản xuất sẽ tự động được cập nhật trước ngày giao hàng hai ngày.

```javascript
cur_frm.cscript.custom_delivery_date = function(doc, cdt, cd){
    cur_frm.set_value("production_due_date", frappe.datetime.add_days(doc.delivery_date, -2));
}
```

{next}