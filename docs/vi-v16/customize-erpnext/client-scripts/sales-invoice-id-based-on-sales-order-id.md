<!-- add-breadcrumbs -->
# ID Hóa đơn bán hàng dựa trên ID Đơn bán hàng

Đoạn mã dưới đây cho phép bạn áp dụng chuỗi đặt tên (naming series) cho Hóa đơn bán hàng giống như Đơn bán hàng tương ứng.
Hóa đơn bán hàng sử dụng tiền tố `M-` nhưng phần số sẽ được lấy trùng với Tên Đơn bán hàng.

Ví dụ: Nếu ID Đơn bán hàng là `SO-12345`, thì ID Hóa đơn bán hàng tương ứng sẽ được thiết lập là `M-12345`.

```js
frappe.ui.form.on("Sales Invoice", "refresh", function(frm){
	var sales_order = frm.doc.items[0].sales_order.replace("SO", "M-");
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

---

### Các cập nhật mới trong ERPNext v16

#### 1. Ngày chốt (Cutoff date) cho Phiếu giao hàng (DN) từ Đơn bán hàng (SO)
Trong phiên bản v16, khi bạn tạo Phiếu giao hàng (DN) từ Đơn bán hàng (SO), hệ thống bổ sung tính năng **Cutoff date**. Tính năng này cho phép bạn giới hạn số lượng mặt hàng được phép xuất kho dựa trên một ngày cụ thể, giúp kiểm soát việc giao hàng theo từng giai đoạn hoặc theo tiến độ hợp đồng.

#### 2. Nút bấm SO/Quotation trên Form Khách hàng
Để tối ưu hóa quy trình bán hàng, tại giao diện thông tin **Khách hàng (Customer)**, ERPNext v16 bổ sung các nút truy cập nhanh. Bạn có thể tạo nhanh **Báo giá (Quotation)** hoặc **Đơn bán hàng (SO)** trực tiếp từ màn hình Khách hàng mà không cần phải chuyển đổi qua lại giữa các module.

#### 3. Giữ chỗ tồn kho (Stock Reservation)
Tính năng **Stock Reservation** được cải tiến mạnh mẽ trong v16. Khi một Đơn bán hàng (SO) được xác nhận, bạn có thể thực hiện giữ chỗ các mặt hàng trong **Kho (Warehouse)**. Việc giữ chỗ này đảm bảo rằng số lượng hàng hóa đã được cam kết cho khách hàng sẽ không bị trừ vào các đơn hàng khác, giúp quản lý **Tồn kho (Stock)** chính xác hơn và tránh tình trạng thiếu hụt hàng khi chuẩn bị làm **Phiếu giao hàng (DN)**.

{next}