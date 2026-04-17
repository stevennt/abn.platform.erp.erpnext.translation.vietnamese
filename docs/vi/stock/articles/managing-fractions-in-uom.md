<!-- add-breadcrumbs -->
#Quản lý số thập phân trong Đơn vị tính

UoM viết tắt của Unit of Measurement (Đơn vị tính). Một vài ví dụ về UoM là Số (Nos), Kgs, Lít, Mét, Hộp, Thùng, v.v.

Có một số UOM không thể có giá trị ở phần thập phân. Ví dụ, nếu chúng ta có mặt hàng là tivi với UoM là Nos, chúng ta không thể có 1.5 Nos tivi, hoặc 3.7 Nos bộ máy tính. Giá trị số lượng cho các mặt hàng này phải là số nguyên.

Bạn có thể cấu hình xem một UoM cụ thể có được phép có giá trị thập phân hay không. Theo mặc định, giá trị thập phân sẽ được cho phép đối với tất cả các UOM. Để hạn chế phần thập phân hoặc giá trị phân số cho bất kỳ UoM nào, bạn nên thực hiện theo các bước sau.

####Danh sách UOM

Để xem danh sách UOM, hãy đi tới:

`Stock > Setup > UoM`

Từ danh sách UOM, hãy chọn UOM mà bạn muốn hạn chế giá trị thập phân. Giả sử UoM đó là Nos.

####Cấu hình

Trong danh mục UoM, bạn sẽ thấy một trường gọi là "Must be whole number" (Phải là số nguyên). Hãy tích vào trường này để hạn chế người dùng nhập giá trị thập phân vào trường số lượng đối với mặt hàng có UOM này.

<img alt="UoM Must be Whole No" class="screenshot" src="{{docs_base_url}}/v13/assets/img/articles/uom-fraction-1.png">

####Xác thực

Khi tạo giao dịch, nếu bạn nhập giá trị phân số cho mặt hàng có UOM đã được tích chọn "Must be whole number", bạn sẽ nhận được thông báo lỗi:

`Quantity cannot be a fraction at row #` (Số lượng không thể là số phân số tại dòng #)

<img alt="UoM Validation Message" class="screenshot" src="{{docs_base_url}}/v13/assets/img/articles/uom-fraction-2.png">


<!-- markdown -->