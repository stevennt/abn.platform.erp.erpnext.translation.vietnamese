<!-- add-breadcrumbs -->
#Bán hàng với Đơn vị tính (UoM) khác nhau

Đơn vị tính (UoM) giá bán là đơn vị tính mà bạn dùng để định giá các mặt hàng. Bạn có thể có nhiều UoM giá bán cho bất kỳ mặt hàng tồn kho nào. Tuy nhiên, khi Khách hàng đặt hàng, UoM của một mặt hàng có thể thay đổi.

Ví dụ: một mặt hàng Bút được nhập kho theo đơn vị Cái, nhưng được bán theo đơn vị Hộp. Do đó, chúng ta sẽ lập Đơn bán hàng cho Bút theo đơn vị Hộp.

###Bước 1: Trong danh mục Mặt hàng, tại phần Đơn vị tính, bạn có thể liệt kê tất cả các UoM khả thi của một mặt hàng, cùng với Hệ số chuyển đổi UoM của nó. Cập nhật Hệ số chuyển đổi UoM
Trong một Hộp, nếu bạn có 10 Cái Bút, Hệ số chuyển đổi UoM sẽ là 10.

![Item Unit of Measure](https://docs.erpnext.com/docs/v13/assets/img/selling/Item-UOM.png)

###Bước 2: Trong Đơn bán hàng, bạn sẽ thấy hai trường UoM

-UoM
-Stock UoM (UoM Kho)

Trong cả hai trường, UoM mặc định của mặt hàng sẽ được lấy tự động. Bạn nên chỉnh sửa trường UoM và chọn UoM bán hàng (trong trường hợp này là Hộp). Việc cập nhật UoM bán hàng chủ yếu để phục vụ tham chiếu cho Khách hàng. Trong mẫu in, bạn sẽ thấy số lượng mặt hàng theo UoM bán hàng.

![Sale Order Unit of Measure](https://docs.erpnext.com/docs/v13/assets/img/selling/Sale-Order-UOM.png)

Dựa trên Số lượng và Hệ số chuyển đổi, số lượng sẽ được tính toán theo UoM Kho của mặt hàng. Nếu bạn chỉ bán một Hộp, thì Số lượng theo UoM Kho sẽ được thiết lập là 10.


###Ghi sổ Sổ cái kho

Bất kể UoM bán hàng được chọn trong Đơn bán hàng là gì, việc ghi sổ cái kho sẽ được thực hiện theo UoM mặc định của mặt hàng. Do đó, bạn nên đảm bảo rằng hệ số chuyển đổi được nhập chính xác khi bán mặt hàng bằng các UoM khác nhau.

![UOM in Stock Ledger](https://docs.erpnext.com/docs/v13/assets/img/selling/uom-in-stock-ledger.png)

{next}