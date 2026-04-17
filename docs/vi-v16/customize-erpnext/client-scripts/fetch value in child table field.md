# Hướng dẫn lấy giá trị vào trường của bảng con từ DocType chính

Tài liệu này hướng dẫn cách sử dụng Client Script để tự động truy xuất dữ liệu từ một DocType khác và điền vào các trường trong bảng con (Child Table) dựa trên một giá trị được chọn.

### Script mẫu: Lấy ngày hết hạn (`expiry_date`) từ **Lô hàng** (`Batch`) vào bảng **Mặt hàng** trong **Hóa đơn bán hàng** (`Sales Invoice Item`)

**Ngữ cảnh:** Khi người dùng chọn một **Lô hàng** (`Batch`) trong dòng hàng của **Hóa đơn bán hàng**, hệ thống sẽ tự động lấy ngày hết hạn của lô hàng đó và điền vào cột ngày hết hạn tương ứng trên dòng hàng.

#### Bước 1: Tạo Client Script
Truy cập vào **Client Script** và tạo mới với các thiết lập sau:
*   **DocType:** `Sales Invoice` (Hóa đơn bán hàng)
*   **Apply To:** `Form`

#### Bước 2: Nhập Script và **Lưu**

Sử dụng đoạn mã dưới đây để thực hiện logic:

```javascript
frappe.ui.form.on("Sales Invoice Item", "batch_no", function(frm, cdt, cdn) {
    // Lấy dữ liệu của dòng hiện tại (row)
    var d = locals[cdt][cdn];
    
    // Kiểm tra nếu trường Lô hàng có giá trị
    if (d.batch_no) {
        // Truy vấn giá trị expiry_date từ DocType Batch dựa trên batch_no đã chọn
        frappe.db.get_value("Batch", d.batch_no, "expiry_date", function(r) {
            if (r && r.expiry_date) {
                // Gán giá trị tìm được vào trường expiry_date của dòng hiện tại
                frappe.model.set_value(cdt, cdn, "expiry_date", r.expiry_date);
            } else {
                // Nếu không tìm thấy ngày hết hạn, xóa giá trị cũ ở dòng đó
                frappe.model.set_value(cdt, cdn, "expiry_date", null);
            }
        });
    } else {
        // Nếu xóa Lô hàng, xóa luôn ngày hết hạn tương ứng
        frappe.model.set_value(cdt, cdn, "expiry_date", null);
    }
});
```

---

### Giải thích kỹ thuật

1.  **`frappe.ui.form.on("Sales Invoice Item", "batch_no", ...)`**: Đây là trigger lắng nghe sự kiện thay đổi tại trường `batch_no` bên trong bảng con `Sales Invoice Item`.
2.  **`locals[cdt][cdn]`**: 
    *   `cdt` (Child DocType): Định danh loại bảng con.
    *   `cdn` (Child Docname): Định danh duy nhất của dòng hiện tại.
    *   Biến `d` đại diện cho toàn bộ dữ liệu của dòng đang được thao tác.
3.  **`frappe.db.get_value`**: Hàm dùng để truy vấn dữ liệu từ cơ sở dữ liệu. Ở đây chúng ta tìm trong DocType `Batch` với điều kiện tên khớp với `batch_no` đã chọn.
4.  **`frappe.model.set_value(cdt, cdn, fieldname, value)`**: Đây là phương thức chuẩn trong ERPNext để cập nhật giá trị vào một trường trong bảng con. Sử dụng hàm này giúp hệ thống nhận diện được sự thay đổi để cho phép **Lưu** dữ liệu chính xác.

**Lưu ý:** Sau khi viết script, hãy nhấn **Lưu** và tải lại (Reload) trang để áp dụng thay đổi.