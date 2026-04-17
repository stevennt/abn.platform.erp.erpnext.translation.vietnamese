<!-- add-breadcrumbs -->
# Giá Mặt hàng

**Giá Mặt hàng là bản ghi mà bạn có thể ghi lại đơn giá bán và mua của một mặt hàng.**

## 1. Cách tạo Giá Mặt hàng
1. Có hai cách để truy cập vào biểu mẫu Giá Mặt hàng mới:

    **Bán hàng/Mua hàng/Kho > Mặt hàng và Định giá > Giá Mặt hàng > Mới**.

    Hoặc

    **Kho > Mặt hàng > Nhấp vào dấu "+" bên cạnh Giá Mặt hàng**.
1. Chọn Mặt hàng. Tên, Đơn vị tính và mô tả sẽ được tự động lấy ra.
1. Chọn Bảng giá là giá Bán/Mua hoặc bất kỳ bảng giá nào khác mà bạn đã tạo.
1. Nhập đơn giá thực tế vào trường Đơn giá.
1. Lưu.
    <img class="screenshot" alt="Item Price list" src="https://docs.erpnext.com/docs/v16/assets/img/stock/item-price-1.png">


### 1.1 Chọn Bảng giá

Bạn có thể tạo nhiều Bảng giá cho một Mặt hàng trong ERPNext để theo dõi riêng biệt Giá Bán và Giá Mua của Mặt hàng đó. Ngoài ra, nếu giá bán của Mặt hàng thay đổi dựa trên Khu vực hoặc do các tiêu chí khác, bạn có thể tạo nhiều Bảng giá Bán cho mặt hàng đó.

Khi chọn Bảng giá, tiền tệ và phạm vi áp dụng (dành cho bán hàng/mua hàng hoặc cả hai) cũng sẽ được tự động lấy ra. Để Giá Mặt hàng được áp dụng trong giao dịch bán hàng hoặc mua hàng, bạn phải chọn đúng 'Bảng giá' trong phần Tiền tệ và Bảng giá của giao dịch đó.

Để kiểm tra tất cả Giá Mặt hàng cùng lúc, hãy đi đến:

**Kho > Báo cáo kho > Giá Mặt hàng trong kho**

Truy cập trang [Bảng giá](price-lists.md) để biết thêm chi tiết.

## 2. Các tính năng

### 2.1 Đơn vị đóng gói
Đây là số lượng phải được mua hoặc bán trên mỗi đơn vị tính. Ví dụ: nếu Đơn vị đóng gói là hai, và Đơn vị tính là một, thì số lượng giao dịch sẽ là hai mặt hàng. Giá trị mặc định là 0, bạn có thể sử dụng Đơn vị tính không nguyên như 1.5Kg Yến mạch cho 1 Đơn vị đóng gói. Nếu bạn để là 0, nó sẽ không ảnh hưởng đến bất kỳ giao dịch nào.

### 2.2 Số lượng tối thiểu
Đây là số lượng mặt hàng tối thiểu cần được giao dịch để mức giá này được áp dụng và cập nhật trong danh sách Giá Mặt hàng.

### 2.3 Áp dụng Bảng giá cho một Khách hàng/Nhà cung cấp cụ thể
Nếu bạn chọn một Bảng giá Bán, trường Khách hàng sẽ xuất hiện nơi bạn có thể gán Giá Mặt hàng này cho một Khách hàng cụ thể. Tương tự, nếu bạn chọn một Bảng giá Mua, trường Nhà cung cấp sẽ xuất hiện nơi bạn có thể chọn một Nhà cung cấp cụ thể.

### 2.4 Áp dụng Bảng giá cho một Lô hàng cụ thể
Bạn cũng có thể liên kết một Lô hàng cụ thể với một Giá Mặt hàng và khi chọn Lô hàng đó trong giao dịch, giá mặt hàng cho Lô hàng cụ thể đó sẽ được áp dụng.

### 2.5 Hiệu lực
Có hai trường ở đây—'Có hiệu lực từ' và 'Có hiệu lực đến'. 'Có hiệu lực từ' được đặt theo ngày bạn tạo Giá Mặt hàng, bạn cũng có thể đặt ngày 'Có hiệu lực đến' mà tại đó Giá Mặt hàng sẽ hết hạn.

### 2.6 Thời gian chờ (ngày)
Số ngày xấp xỉ để sản phẩm đến được kho. Bạn có thể thiết lập các Giá Mặt hàng khác nhau dựa trên khoảng thời gian mà cùng một sản phẩm sẽ đến tay bạn từ các Nhà cung cấp khác nhau.

### 2.7 Ghi chú
Bạn có thể thêm bất kỳ ghi chú nào về Giá Mặt hàng trong trường này.

## 3. Video

<div>
    <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style>
    <div class='embed-container'>
        <iframe src='https://www.youtube.com/embed/FcOsV-e8ymE?start=193' frameborder='0' allowfullscreen>
        </iframe>
    </div>
</div>

### 4. Các chủ đề liên quan
1. [Mặt hàng](item.md)
1. [Áp dụng Chiết khấu](../selling/articles/applying-discount.md)