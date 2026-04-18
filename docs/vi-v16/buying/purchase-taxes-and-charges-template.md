<!-- add-breadcrumbs -->
# Mẫu Thuế và Phí Mua hàng

**Thuế và Phí Mua hàng có thể được áp dụng cho bất kỳ mặt hàng nào bạn mua.**

Mẫu Thuế và Phí Mua hàng tương tự như Mẫu Thuế và Phí Bán hàng. Các mẫu được tạo từ biểu mẫu này có thể được sử dụng trong Đơn mua hàng và Hóa đơn mua hàng để ghi chép nội bộ.

Đối với các Tài khoản Thuế mà bạn muốn sử dụng trong các mẫu thuế, bạn phải thiết lập trường Loại tài khoản là 'Tax' cho tài khoản cụ thể đó.

Để truy cập Mẫu Thuế và Phí Mua hàng, hãy đi đến:
> Trang chủ > Mua hàng > Thiết lập > Mẫu Thuế và Phí Mua hàng

## 1. Cách thêm Thuế/Phí Mua hàng thông qua một mẫu
Trước khi tạo mẫu mới, hãy lưu ý rằng các mẫu đã được tạo sẵn cho nhiều loại thuế thường dùng.

1. Nhấp vào Mới.
2. Nhập tên tiêu đề cho Thuế.
3. Trong phần loại, thiết lập căn cứ để tính thuế và tỷ lệ thuế. Có năm tùy chọn trong phần loại để tính thuế.
  1. Actual: Trên số tiền thực tế của mỗi mặt hàng.
  2. On Net Total: Trên tổng cộng của tất cả các mặt hàng.
  3. On Previous Row Amount: Dùng để tính phí cộng dồn. Ví dụ: phí cess tính trên số tiền mà thuế đã được áp dụng ở dòng trước đó.
  4. On Previous Row Total: Tương tự như trên nhưng được áp dụng trên tổng hóa đơn chứ không chỉ là số tiền của một mặt hàng.
4. Chọn một tài khoản có sẵn tỷ lệ thuế hoặc tự tạo của riêng bạn.
5. Chọn mặc định (default) sẽ áp dụng mẫu này làm mặc định cho các giao dịch Mua hàng mới.
6. Lưu.

<img class="screenshot" alt="Purchase taxes" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/buying/purchase-taxes.png">

**Is Inter State:** Dành cho các quy định về thuế liên bang/tỉnh. Khi chọn Nhà cung cấp trong Hóa đơn mua hàng, nếu mã thuế của nơi cung ứng và địa chỉ của Nhà cung cấp không khớp, mẫu có đánh dấu 'Is Inter State' sẽ được thiết lập làm mẫu thuế. Nếu nơi cung ứng và địa chỉ giống nhau, mẫu thuế mặc định sẽ được áp dụng.

## 2. Các tính năng mới trong v16
Trong phiên bản v16, quy trình mua hàng được tối ưu hóa với các tính năng:
* **Lọc Nhà cung cấp không vận chuyển (Non-transporter supplier filtering):** Cho phép lọc danh sách Nhà cung cấp dựa trên khả năng vận chuyển để tối ưu hóa quy trình mua hàng.
* **Số tham chiếu Nhà cung cấp (Supplier reference numbers):** Cho phép lưu trữ và quản lý các số tham chiếu riêng của Nhà cung cấp để đối chiếu dễ dàng hơn.
* **Email append-to tạo PI draft:** Tự nhiên hóa quy trình gửi email, cho phép đính kèm hoặc tạo bản nháp Phiếu nhập hàng (PI) trực tiếp qua email.
* **Xem trước Sổ cái (Ledger Preview):** Cho phép kiểm tra nhanh các bút toán (JE) sẽ được ghi nhận trước khi thực hiện Xác nhận giao dịch.

## 3. Các tính năng khác
### 3.1 Bảng Thuế và Phí Mua hàng

* **Consider Tax or Charge for**: Total - cho tổng của tất cả các mặt hàng. Valuation - cho từng mặt hàng. Valuation and total - áp dụng thuế/phí cho cả hai. [Xem bài viết này](../accounts/articles/what-is-the-differences-of-total-and-valuation-in-tax-and-charges.md) để biết sự khác biệt.
* **Add or Deduct:** Bạn muốn cộng thêm hay trừ bớt thuế khỏi mặt hàng.

* **Reference Row #**: Nếu thuế dựa trên "Previous Row Total", bạn có thể chọn số dòng sẽ được lấy làm cơ sở cho tính toán này (mặc định là dòng trước đó).
   <img class="screenshot" alt="Purchase taxes table" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/buying/purchase-taxes-table.png">

* **Is this Tax included in Basic Rate?**: Nếu được chọn, số tiền thuế sẽ được coi là đã bao gồm trong Giá in / Số tiền in.
* **Account Head:** Tài khoản sổ cái mà thuế này sẽ được ghi nhận. Nếu bạn chọn VAT hoặc bất kỳ tài khoản thiết lập sẵn nào khác, tỷ lệ sẽ được tự động điền.
* **Cost Center:** Nếu thuế/phí là một khoản thu nhập (như phí vận chuyển) hoặc chi phí, nó cần được ghi nhận vào một Trung tâm chi phí.
* **Description:** Mô tả về loại thuế (sẽ được in trong hóa đơn/báo giá).
* **Rate:** Tỷ lệ Thuế, ví dụ: 14 = thuế 14%.
* **Amount:** Số tiền Thuế được áp dụng, ví dụ: 100.00 = 100.00.


### 4. Các chủ đề liên quan
1. [Đơn mua hàng](purchase-order.md)
2. [Thiết lập Mua hàng](buying-settings.md)

{next}