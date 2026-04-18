<!-- add-breadcrumbs -->
#Mua hàng với Đơn vị tính (UoM) khác nhau

Mỗi mặt hàng đều có một đơn vị tính (UoM) tồn kho đi kèm. Ví dụ, UoM của bút có thể là cái (Nos) và cát có thể được lưu kho theo kg. Tuy nhiên, khi chúng ta đặt hàng với Nhà cung cấp, UoM của một mặt hàng có thể thay đổi. Chẳng hạn như chúng ta có thể đặt mua 1 bộ/hộp Bút, hoặc một xe tải cát từ Nhà cung cấp. Khi tạo giao dịch mua hàng, bạn có thể thay đổi UoM mua hàng cho một mặt hàng.

### Kịch bản:

Mặt hàng `Pen` được lưu kho theo đơn vị Nos, nhưng được mua theo đơn vị Box. Do đó, chúng ta sẽ lập Đơn mua hàng cho mặt hàng Pen theo đơn vị Box.

#### Bước 1: Chỉnh sửa UoM trong Đơn mua hàng

Trong Đơn mua hàng, bạn sẽ thấy hai trường UoM.

- UoM
- Stock UoM

Trong cả hai trường này, UoM mặc định của mặt hàng sẽ được tự động lấy ra. Bạn nên chỉnh sửa trường UoM và chọn UoM mua hàng (trong trường hợp này là Box). Việc cập nhật UoM mua hàng chủ yếu để tham chiếu cho nhà cung cấp. Trong mẫu in, bạn sẽ thấy số lượng mặt hàng theo UoM mua hàng.

<img alt="Item Purchase UoM" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/editing-uom-in-po.gif">

#### Bước 2: Cập nhật Hệ số chuyển đổi UoM

Trong một Hộp (Box), nếu bạn có 20 cái (Nos) Bút, thì Hệ số chuyển đổi UoM sẽ là 20.

<img alt="Item Conversion Factor" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/po-conversion-factor.png">

Dựa trên Số lượng và Hệ số chuyển đổi, số lượng sẽ được tính toán theo Stock UoM của mặt hàng. Nếu bạn chỉ mua một Hộp, thì Số lượng trong Stock UoM sẽ được thiết lập là 20.

<img alt="Purchase Qty in Default UoM" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/po-qty-in-stock-uom.png">

### Ghi sổ Sổ cái kho

Bất kể UoM mua hàng nào được chọn, việc ghi sổ cái kho sẽ được thực hiện theo UoM mặc định của mặt hàng. Do đó, bạn nên đảm bảo rằng hệ số chuyển đổi được nhập chính xác khi mua mặt hàng bằng các UoM khác nhau.

<img alt="Print Format in Purchase UoM" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/po-stock-uom-ledger.png">

### Thiết lập Hệ số chuyển đổi trong Mặt hàng

Trong danh mục Mặt hàng, tại phần Mua hàng, bạn có thể liệt kê tất cả các UoM mua hàng khả thi của một mặt hàng, cùng với Hệ số chuyển đổi UoM của nó.

<img alt="Purchase UoM master" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/item-purchase-uom-conversion.png">

<!-- markdown -->