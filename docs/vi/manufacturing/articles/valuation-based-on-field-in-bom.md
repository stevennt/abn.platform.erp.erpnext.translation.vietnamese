<!-- add-breadcrumbs -->
#Xác định giá trị dựa trên trong BOM

**Câu hỏi:** Các tùy chọn khác nhau trong trường `Valuation Based On` trong Định mức nguyên vật liệu (BOM) là gì?

**Trả lời:** Có 3 tùy chọn có sẵn trong trường <i>Valuation Based On</i>:

<img alt="Nested BOM" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/valuation-based-on-1.png">

**Valuation Rate:** Giá trị tính giá của mặt hàng được xác định dựa trên giá trị mua hoặc sản xuất của nó.

Đối với Mặt hàng mua, nó được xác định dựa trên các chi phí được nhập trong Phiếu nhập hàng. Nếu bạn không có bất kỳ Phiếu nhập hàng nào được lập cho một mặt hàng hoặc một bản Đối chiếu tồn kho, thì mặt hàng đó sẽ không có Giá trị tính giá.

**Price List Rate:** Tùy chọn này cho phép lấy đơn giá mặt hàng từ [Bảng giá.](../../stock/item-price.md)

**Last Purchase Rate:** Đây sẽ là Đơn giá (Đơn mua hàng) cuối cùng của một mặt hàng.