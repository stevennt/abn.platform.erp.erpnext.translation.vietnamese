<!-- add-breadcrumbs -->
# Nhà cung cấp

**Nhà cung cấp là các công ty hoặc cá nhân cung cấp sản phẩm hoặc dịch vụ cho bạn.**

Để truy cập danh sách Nhà cung cấp, hãy đi tới:
> Trang chủ > Mua hàng > Nhà cung cấp > Nhà cung cấp

## 1. Cách tạo Nhà cung cấp
1. Đi tới danh sách Nhà cung cấp và nhấn vào Mới.
2. Nhập tên cho nhà cung cấp.
4. Chọn nhóm nhà cung cấp như Dược phẩm, Phần cứng, v.v.
5. Lưu.
    <img class="screenshot" alt="Supplier Master" src="https://docs.erpnext.com/docs/v13/assets/img/buying/supplier-master.png">

Các tùy chọn Cảnh báo RFQ, PO, Ngăn chặn RFQ, PO sẽ khả dụng sau khi bạn tạo [Bảng điểm Nhà cung cấp](supplier-scorecard.md) và các giao dịch được thực hiện.

## 2. Các tính năng

Các trường trong các giao dịch trong tương lai sẽ được tự động điền nếu các trường 'Mặc định' như Tài khoản ngân hàng mặc định, Mẫu điều khoản thanh toán mặc định, v.v., được thiết lập trong Nhà cung cấp.

### 2.1 Chi tiết thuế

* **Quốc gia**: Nếu nhà cung cấp đến từ quốc gia khác, bạn có thể thay đổi tại đây.
* **Mã số thuế**: Mã số định danh thuế của nhà cung cấp.
* **Danh mục thuế**: Mục này được liên kết với [Quy tắc thuế](../accounts/tax-rule.md). Nếu một Danh mục thuế được thiết lập tại đây, khi bạn chọn nhà cung cấp này, mẫu Thuế mua hàng và Phí tương ứng sẽ được áp dụng. Mẫu này được liên kết với Quy tắc thuế và Quy tắc thuế được liên kết với Danh mục thuế. Danh mục thuế có thể được sử dụng để nhóm các nhà cung cấp mà cùng một loại thuế sẽ được áp dụng. Ví dụ: Chính phủ, thương mại, v.v.
* **Ngôn ngữ in**: Ngôn ngữ mà tài liệu sẽ được in ra.
* **Danh mục khấu trừ thuế**: Đối với Ấn Độ, danh mục TDS cho Nhà cung cấp. Khi thiết lập một danh mục tại đây, nó sẽ được lấy vào [Hóa đơn mua hàng](../accounts/purchase-invoice.md). Để biết thêm thông tin, hãy truy cập trang [Danh mục khấu trừ thuế](../accounts/tax-withholding-category.md).
* **Vô hiệu hóa**: Vô hiệu hóa Nhà cung cấp và họ sẽ không được hiển thị trong Danh sách Nhà cung cấp.
* **Là đơn vị vận chuyển**: Nếu nhà cung cấp đang bán dịch vụ vận chuyển của bạn, hãy tích vào ô này. Trường 'GST Transporter ID' sẽ hiển thị nếu trường này được tích.
* **Nhà cung cấp nội bộ**: Nếu nhà cung cấp là công ty liên kết hoặc công ty mẹ/con, hãy tích vào trường này và chọn công ty mà họ đại diện.

Đối với Ấn Độ:

* **Danh mục GST**: Chọn Danh mục GST của nhà cung cấp.
* **PAN**: Đối với Ấn Độ, chi tiết thẻ PAN (Mã số tài khoản vĩnh viễn) của Nhà cung cấp.

### 2.2 Cho phép tạo Hóa đơn mua hàng mà không cần Đơn mua hàng và Phiếu nhập hàng

Nếu tùy chọn "Yêu cầu Đơn mua hàng" hoặc "Yêu cầu Phiếu nhập hàng" được cấu hình là "Có" trong [Cài đặt mua hàng](buying-settings.md), nó có thể được ghi đè cho một nhà cung cấp cụ thể bằng cách bật "Cho phép tạo Hóa đơn mua hàng không cần Đơn mua hàng" hoặc "Cho phép tạo Hóa đơn mua hàng không cần Phiếu nhập hàng" trong Danh mục Nhà cung cấp.

<img class="screenshot" alt="Supplier Master" src="https://docs.erpnext.com/docs/v13/assets/img/buying/supplier-po-pr-required.png">

### 2.3 Tiền tệ và Bảng giá
**Tiền tệ thanh toán**: Tiền tệ của nhà cung cấp có thể khác với tiền tệ của công ty bạn. Nếu bạn chọn JPY cho một nhà cung cấp, thì tiền tệ sẽ được điền là JPY và tỷ giá sẽ được hiển thị cho các giao dịch mua hàng trong tương lai.

![Supplier Currency](https://docs.erpnext.com/docs/v13/assets/img/buying/supplier-currency.gif)

Mỗi Nhà cung cấp có thể có một **Bảng giá** mặc định để mỗi khi bạn mua một mặt hàng mới từ nhà cung cấp này với các mức giá khác nhau, bảng giá liên kết với nhà cung cấp cũng sẽ được cập nhật. Dưới bảng giá là giá mặt hàng, bạn có thể xem giá tại Mua hàng > Mặt hàng và Định giá > Giá mặt hàng.

Nếu bạn chọn nhà cung cấp cụ thể này, thì Bảng giá liên kết sẽ được lấy vào các giao dịch Mua hàng.

### 2.4 Hạn mức tín dụng

* **Mẫu điều khoản thanh toán mặc định**: Nếu một mẫu Điều khoản thanh toán được thiết lập tại đây, nó sẽ tự động được chọn cho các giao dịch mua hàng trong tương lai.
* **Chặn Nhà cung cấp**: Bạn có thể chặn hóa đơn, thanh toán hoặc cả hai từ một nhà cung cấp cho đến một ngày cụ thể. Chọn 'Loại tạm dừng', nếu bạn không chọn loại tạm dừng, ERPNext sẽ đặt thành "Tất cả". Khi một nhà cung cấp bị chặn, trạng thái của họ sẽ được hiển thị là 'Tạm dừng'.

    Các loại tạm dừng như sau:
    - Hóa đơn: ERPNext sẽ không cho phép tạo Hóa đơn mua hàng hoặc Đơn mua hàng cho nhà cung cấp
    - Thanh toán: ERPNext sẽ không cho phép tạo Bút toán thanh toán cho Nhà cung cấp
    - Tất cả: ERPNext sẽ áp dụng cả hai loại tạm dừng trên

    Nếu bạn không thiết lập ngày giải tỏa, ERPNext sẽ tạm dừng Nhà cung cấp **vô thời hạn**.

### 2.5 Tài khoản phải trả mặc định
Thêm tài khoản mặc định mà các hóa đơn đối với nhà cung cấp này sẽ được thanh toán. Thêm các dòng bổ sung cho nhiều công ty hơn, bạn chỉ có thể chọn một tài khoản cho mỗi công ty.

Bạn có thể **tích hợp** một nhà cung cấp với một tài khoản. Đối với tất cả Nhà cung cấp, tài khoản "Chủ nợ" được thiết lập làm Tài khoản phải trả mặc định. Khi Hóa đơn mua hàng được tạo, khoản phải trả cho nhà cung cấp sẽ được ghi vào tài khoản "Chủ nợ".

Nếu bạn muốn tùy chỉnh tài khoản phải trả cho Nhà cung cấp, trước tiên bạn nên thêm một Tài khoản phải trả trong Hệ thống tài khoản, sau đó chọn Tài khoản phải trả đó trong danh mục Nhà cung cấp.

<img class="screenshot" alt="Supplier Master" src="https://docs.erpnext.com/docs/v13/assets/img/buying/supplier-payable-account.png">

Nếu bạn không muốn tùy chỉnh tài khoản phải trả và tiếp tục với tài khoản phải trả mặc định "Chủ nợ", thì đừng cập nhật bất kỳ giá trị nào trong bảng Tài khoản nhà cung cấp mặc định.

> Mẹo: Tài khoản phải trả mặc định được thiết lập trong danh mục Công ty. Nếu bạn muốn thiết lập một tài khoản khác làm Tài khoản mặc định cho khoản phải trả thay vì Tài khoản Chủ nợ, hãy đi tới danh mục Công ty và thiết lập tài khoản đó là "Tài khoản phải trả mặc định".

Tùy thuộc vào [gói dịch vụ](https://erpnext.com/pricing) của bạn, bạn có thể thêm nhiều công ty vào phiên bản ERPNext của mình. Một Nhà cung cấp có thể được sử dụng trên nhiều công ty. Trong trường hợp này, bạn nên xác định Tài khoản phải trả theo từng Công ty cho Nhà cung cấp trong bảng "Tài khoản phải trả mặc định", tức là thêm nhiều dòng.

### 2.6 Thông tin thêm
Yo