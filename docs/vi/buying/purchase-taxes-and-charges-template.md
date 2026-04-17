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
  1. On Net Total: Trên tổng cộng của tất cả các mặt hàng.
  1. On Previous Row Amount: Dùng để tính phí cộng dồn. Ví dụ: phí cess tính trên số tiền mà thuế đã được áp dụng ở dòng trước đó.
  1. On Previous Row Total: Tương tự như trên nhưng được áp dụng trên tổng hóa đơn chứ không chỉ là số tiền của một mặt hàng.
4. Chọn một tài khoản có sẵn tỷ lệ thuế hoặc tự tạo của riêng bạn.
1. Chọn mặc định (default) sẽ áp dụng mẫu này làm mặc định cho các giao dịch Mua hàng mới.
5. Lưu.
<img class="screenshot" alt="Purchase taxes" src="{{docs_base_url}}/v13/assets/img/buying/purchase-taxes.png">

Is Inter State: Dành cho Ấn Độ. Khi chọn Khách hàng trong Hóa đơn bán hàng hoặc Phiếu giao hàng, nếu mã GST của nơi cung ứng và địa chỉ giao hàng của khách hàng không khớp, mẫu có đánh dấu 'Is Inter State' sẽ được thiết lập làm mẫu thuế. Nếu nơi cung ứng và địa chỉ giao hàng giống nhau, mẫu thuế mặc định sẽ được áp dụng. Điều này cũng áp dụng cho Hóa đơn mua hàng, khi chọn Nhà cung cấp, các mẫu được thiết lập tùy thuộc vào địa chỉ. Ví dụ: IGST.

## 2. Các tính năng
### 2.1 Bảng Thuế và Phí Mua hàng

* **Consider Tax or Charge for**: Total - cho tổng của tất cả các mặt hàng. Valuation - cho từng mặt hàng. Valuation and total - áp dụng thuế/phí cho cả hai. [Xem bài viết này](/docs/v13/user/manual/en/accounts/articles/what-is-the-differences-of-total-and-valuation-in-tax-and-charges) để biết sự khác biệt.
* **Add or Deduct:** Bạn muốn cộng thêm hay trừ bớt thuế khỏi mặt hàng.

* **Reference Row #**: Nếu thuế dựa trên "Previous Row Total", bạn có thể chọn số dòng sẽ được lấy làm cơ sở cho tính toán này (mặc định là dòng trước đó).
   <img class="screenshot" alt="Purchase taxes table" src="{{docs_base_url}}/v13/assets/img/buying/purchase-taxes-table.png">

* **Is this Tax included in Basic Rate?**: Nếu được chọn, số tiền thuế sẽ được coi là đã bao gồm trong Giá in / Số tiền in.
* **Account Head:** Tài khoản sổ cái mà thuế này sẽ được ghi nhận. Nếu bạn chọn VAT hoặc bất kỳ tài khoản thiết lập sẵn nào khác, tỷ lệ sẽ được tự động điền.
* **Cost Center:** Nếu thuế/phí là một khoản thu nhập (như phí vận chuyển) hoặc chi phí, nó cần được ghi nhận vào một Trung tâm chi phí.
* **Description:** Mô tả về loại thuế (sẽ được in trong hóa đơn/báo giá).
* **Rate:** Tỷ lệ Thuế, ví dụ: 14 = thuế 14%.
* **Amount:** Số tiền Thuế được áp dụng, ví dụ: 100.00 = ₹100 thuế.


### 3. Các chủ đề liên quan
1. [Đơn mua hàng](/docs/v13/user/manual/en/buying/purchase-order)
1. [Thiết lập Mua hàng](/docs/v13/user/manual/en/buying/buying-settings)

{next}