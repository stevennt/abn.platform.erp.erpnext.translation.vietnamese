<!-- add-breadcrumbs -->
# Báo giá của Nhà cung cấp

**Báo giá của Nhà cung cấp là tài liệu do một nhà cung cấp tiềm năng lập, quy định chi phí hàng hóa hoặc dịch vụ mà họ sẽ cung cấp trong một khoảng thời gian nhất định.**

Báo giá của Nhà cung cấp cũng có thể bao gồm các điều khoản bán hàng, điều khoản thanh toán và bảo hành. Việc người mua chấp nhận báo giá có thể được coi là một thỏa thuận ràng buộc cả hai bên.

![Buying Flow](https://docs.erpnext.com/docs/v16/assets/img/buying/buying_flow_sq.png)

Để truy cập Báo giá của Nhà cung cấp, hãy đi đến:
> Home > Buying > Purchasing > Supplier Quotation

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Báo giá của Nhà cung cấp, bạn nên tạo các thông tin sau trước:

* [Supplier](supplier.md)
* [Item](../stock/item.md)

## 2. Cách tạo Báo giá của Nhà cung cấp

### 2.1 Báo giá của Nhà cung cấp từ Yêu cầu vật tư

Bạn có thể tạo báo giá của nhà cung cấp từ một Yêu cầu vật tư:
![Supplier Quotation from Material Receipt](https://docs.erpnext.com/docs/v16/assets/img/buying/supplier-quotation-from-mr.png)

Hoặc:

Một Báo giá của Nhà cung cấp có thể được tạo từ [Supplier master](supplier.md).

Hoặc:

Nhà cung cấp có thể tự gửi báo giá cho bạn thông qua ERPNext. Để biết thêm về điều này, hãy xem phần [Request for Quotation page](request-for-quotation.md#4-creating-a-supplier-quotation-after-rfq).

### 2.2 Tạo Báo giá của Nhà cung cấp thủ công
1. Bạn cũng có thể tạo Báo giá của Nhà cung cấp trực tiếp từ:

    **Buying > Purchasing > Supplier Quotation > New**.
1. Chọn Nhà cung cấp đã gửi báo giá cho bạn.
1. Địa chỉ và Liên hệ sẽ được tự động lấy về nếu bạn đã lưu chúng trong thông tin nhà cung cấp (supplier master).
1. Nhập mã Mặt hàng, chọn số lượng. Đơn giá sẽ được tự động lấy về nếu bạn đã thiết lập Đơn giá mua tiêu chuẩn cho mặt hàng đó trong [Item Price](../stock/item-price.md).
    <img class="screenshot" alt="Supplier Quotation" src="https://docs.erpnext.com/docs/v16/assets/img/buying/supplier-quotation.png">

Nếu bạn có nhiều Nhà cung cấp cung cấp cùng một Mặt hàng, bạn thường sẽ gửi [Request for Quotation](request-for-quotation.md) đến nhiều Nhà cung cấp khác nhau. Trong nhiều trường hợp, đặc biệt nếu bạn có quy trình mua hàng tập trung, bạn có thể muốn ghi lại tất cả các báo giá để:

  * Bạn có thể dễ dàng so sánh giá cả trong tương lai.
  * Kiểm tra xem tất cả các Nhà cung cấp đã được trao cơ hội báo giá hay chưa.

Báo giá của Nhà cung cấp không nhất thiết phải thực hiện đối với hầu hết các doanh nghiệp nhỏ. Hãy luôn đánh giá chi phí thu thập thông tin so với giá trị thực tế mà nó mang lại! Như một lời khuyên, bạn chỉ nên thực hiện việc này đối với các mặt hàng có giá trị cao.

## 3. Các tính năng mới trong v16
### 3.1 Lọc Nhà cung cấp không vận chuyển (Non-transporter supplier filtering)
Trong phiên bản v16, bạn có thể thiết lập bộ lọc để loại bỏ các Nhà cung cấp không có khả năng vận chuyển hoặc không phù hợp với các yêu cầu về logistics của bạn ngay từ bước chọn lọc, giúp tối ưu hóa quy trình mua hàng.

### 3.2 Số tham chiếu của Nhà cung cấp (Supplier reference numbers)
Bạn có thể lưu trữ và quản lý các số tham chiếu riêng của Nhà cung cấp (như số báo giá gốc của họ) ngay trong tài liệu ERPNext. Điều này giúp việc đối chiếu chứng từ giữa hai bên trở nên dễ dàng và chính xác hơn.

### 3.3 Ledger Preview (Xem trước Sổ cái)
Tính năng này cho phép bạn xem trước các tác động của Báo giá của Nhà cung cấp đối với các bút toán (JE) trước khi thực hiện các bước tiếp theo, giúp kiểm soát tài chính chặt chẽ hơn.

## 4. Các tính năng khác
### 4.1 Thuế và Phí
Nếu Nhà cung cấp của bạn sẽ tính thêm các khoản thuế hoặc phí như phí vận chuyển hoặc phí bảo hiểm, bạn có thể thêm chúng tại đây. Điều này sẽ giúp bạn theo dõi chi phí một cách chính xác. Ngoài ra, nếu một số khoản phí này làm tăng giá trị của sản phẩm, bạn sẽ phải ghi chúng vào bảng Thuế. Bạn cũng có thể sử dụng các mẫu cho các loại thuế của mình. Để biết thêm thông tin về việc thiết lập thuế, hãy xem [Purchase Taxes and Charges Template](purchase-taxes-and-charges-template.md).

### 4.2 Thêm
Có các trường cho Danh mục thuế, Quy tắc vận chuyển, Mẫu Thuế và Phí mua hàng, Chiết khấu, Điều khoản và Điều kiện, Cài đặt in. Bạn có thể điền các trường này để lưu hồ sơ. Truy cập trang [Quotation](../selling/quotation.md) để biết thêm về các phần này. Lưu ý rằng các chi tiết bạn điền ở đây như Quy tắc vận chuyển, thuế, Chiết khấu, Điều khoản và Điều kiện, v.v., là từ nhà cung cấp của bạn và có thể được ghi lại để theo dõi chính xác.

Lưu ý:

- Danh mục thuế sẽ được lấy từ thông tin nhà cung cấp nếu đã được thiết lập.
- Cài đặt in dùng để thực hiện các thay đổi đối với bản in báo giá của nhà cung cấp.
- Các Điều khoản và Điều kiện ở đây là của nhà cung cấp của bạn.
- Báo giá của Nhà cung cấp có thể được liên kết với các yêu cầu vật tư bằng nút 'Link to material requests'.

### 4.3 Sau khi Xác nhận
Các mục sau có thể được tạo sau khi Xác nhận Báo giá của Nhà cung cấp:

* Đơn mua hàng - Một Đơn mua hàng nếu bạn đồng ý với báo giá của nhà cung cấp.
* Báo giá - Một báo giá gửi cho khách hàng của bạn.
* Tự động lặp lại - Tự động lặp lại báo giá của nhà cung cấp theo các khoảng thời gian đã định.

## 5. Các chủ đề liên quan
1. [Supplier](supplier.md)
1. [Supplier Group](supplier-group.md)
1. [Purchase Order](purchase-order.md)
1. [Request for Quotation](request-for-quotation.md)

{next}