<!-- add-breadcrumbs -->
# Tính giá BOM bằng các loại Tiền tệ khác nhau

Người dùng có thể thay đổi Tiền tệ trong BOM *trước khi* Xác nhận. Hệ thống sẽ tính toán giá thành dựa trên tiền tệ của Bảng giá. Bạn có thể kiểm tra chi phí sản xuất bằng một loại Tiền tệ cụ thể bằng cách thay đổi Tiền tệ trong BOM.

Giả sử bạn nhập khẩu nhựa làm nguyên liệu thô từ Nhật Bản và các Hóa đơn sử dụng đồng Yên. Tiền tệ của công ty bạn là INR nhưng bạn muốn việc tính giá BOM được thực hiện bằng đồng Yên. Khi thiết lập 'Rate Of Materials Based On' thành 'Price List', các nguyên liệu thô được sử dụng trong BOM cũng sẽ có đơn giá được thiết lập bằng đồng Yên. Các đơn giá này được lấy từ Bảng giá mà bạn tạo cho Nhật Bản. Trong trường hợp này, đó là một Bảng giá mua hàng có tên là 'Import Japan'.

![BOM in different Currency](https://docs.erpnext.com/docs/v16/assets/img/manufacturing/bom-currency.png)

Nếu bạn chọn 'Rate Of Materials Based On' là 'Valuation Rate' hoặc 'Last Purchase Rate', giá sẽ được lấy tương ứng từ danh mục Mặt hàng hoặc Hóa đơn. Trong trường hợp lấy từ danh mục Mặt hàng, bạn sẽ cần nhập Giá trị tính giá bằng Tiền tệ của **bạn**. Trong BOM, Giá trị tính giá sẽ được chuyển đổi sang Tiền tệ đã thiết lập trong BOM.

![BOM in different Currency](https://docs.erpnext.com/docs/v16/assets/img/manufacturing/bom-currency-1.png)