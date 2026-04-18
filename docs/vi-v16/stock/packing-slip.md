<!-- add-breadcrumbs -->
# Phiếu đóng gói

**Phiếu đóng gói là một chứng từ liệt kê các mặt hàng trong một lô hàng.**

Nó thường được đính kèm cùng với hàng hóa được giao.

Từ một Phiếu giao hàng duy nhất, có thể tạo ra nhiều Phiếu đóng gói. Điều này hữu ích khi lô hàng được đóng trong các thùng khác nhau. Mỗi thùng có thể có trọng lượng và số lượng Mặt hàng chứa bên trong. Ví dụ, nếu bạn đang giao 20 chiếc ghế trong 4 thùng, mỗi thùng có thể chứa 5 chiếc ghế với các Phiếu đóng gói khác nhau cho mỗi thùng.

Để truy cập danh sách Phiếu đóng gói, hãy đi đến:
> Trang chủ > Kho > Công cụ > Phiếu đóng gói
<p></p>
> Lưu ý: Để tạo Phiếu đóng gói từ Phiếu giao hàng, Phiếu giao hàng cần phải ở trạng thái Nháp.

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Phiếu đóng gói, bạn nên tạo các chứng từ sau trước:

* [Phiếu giao hàng](delivery-note.md)


## 2. Cách tạo Phiếu đóng gói mới
Thông thường, bạn nên tạo Phiếu đóng gói từ Phiếu giao hàng khi nó đang ở trạng thái Nháp, tuy nhiên, nếu bạn muốn tạo Phiếu đóng gói một cách thủ công, hãy làm theo các bước sau.

1. Đi đến danh sách Phiếu đóng gói, nhấn vào Mới.
1. Chọn Phiếu giao hàng.
1. Nhập Số kiện từ (From Package No) của Phiếu đóng gói này.
1. Nhấn vào nút Lấy Mặt hàng (Get Items) để lấy các Mặt hàng và Số lượng vào bảng Mặt hàng.
1. Lưu.

Hầu hết các chi tiết này sẽ được tự động lấy về nếu bạn tạo Phiếu đóng gói từ Phiếu giao hàng.

<img class="screenshot" alt="Packing Slip" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/packing-slip.png">


### 1.1 Các tùy chọn bổ sung khi tạo Phiếu đóng gói
**Số kiện từ đến (To Package No)**: Nếu có nhiều kiện hàng cùng loại được giao cùng một lúc, hãy thiết lập số kiện Từ và Đến. Ví dụ, số kiện từ 1 đến 5 trong một Phiếu đóng gói, sau đó số kiện từ 6 đến 10 trong Phiếu đóng gói tiếp theo, v.v. Thông tin này sẽ được hiển thị khi bạn in Phiếu đóng gói. Lưu ý rằng điều này chỉ hoạt động nếu Lô hàng của bạn có số lượng Mặt hàng tương ứng.

## 2. Các tính năng

### 2.1 Bảng Mặt hàng

* Nếu đây là Mặt hàng theo Lô hàng, bạn sẽ phải chọn Lô hàng.
* Số lượng, Đơn vị tính, Trọng lượng tịnh và Đơn vị tính trọng lượng sẽ được lấy từ Phiếu giao hàng.
* Ngắt trang (Page Break) sẽ tạo một điểm ngắt trang ngay trước mặt hàng này khi in.

### 2.2 Chi tiết trọng lượng kiện hàng

Các chi tiết này sẽ được hiển thị khi in Phiếu đóng gói.

**Trọng lượng tịnh**: Được tính bằng tổng trọng lượng của tất cả các Mặt hàng trong bảng.
**Trọng lượng tổng**: Đây là tổng trọng lượng cuối cùng bao gồm cả trọng lượng của vật liệu đóng gói được sử dụng.
**Đơn vị tính trọng lượng tổng**: Có thể thiết lập một Đơn vị tính cho trọng lượng cuối cùng của sản phẩm.

### 2.3 Tiêu đề thư
Bạn có thể in Phiếu đóng gói trên tiêu đề thư của công ty mình. Tìm hiểu thêm [tại đây](setting-up/print/letter-head.md).


### 2. Các chủ đề liên quan
1. [Kiểm tra chất lượng](quality-inspection.md)
1. [Phiếu giao hàng](delivery-note.md)