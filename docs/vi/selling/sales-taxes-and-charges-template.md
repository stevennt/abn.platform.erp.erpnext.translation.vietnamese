<!-- add-breadcrumbs -->
# Mẫu Thuế và Phí Bán hàng

**Thuế và Phí Bán hàng có thể được áp dụng cho bất kỳ mặt hàng nào bạn bán.**

Các mẫu được tạo từ biểu mẫu này có thể được sử dụng trong Đơn bán hàng và Hóa đơn bán hàng.

Đối với các Tài khoản Thuế mà bạn muốn sử dụng trong các mẫu thuế, bạn phải thiết lập trường Loại tài khoản là 'Tax' cho tài khoản cụ thể đó. Cách ERPNext thiết lập thuế là thông qua các mẫu. Các loại phí khác có thể áp dụng cho hóa đơn của bạn (như vận chuyển, bảo hiểm, v.v.) cũng có thể được cấu hình như thuế.

Để biết về việc thiết lập thuế, hãy truy cập [trang này](../setting-up/setting-up-taxes.md).

Để truy cập Mẫu Thuế và Phí Bán hàng, hãy đi đến:
> Home > Selling > Settings > Sales Taxes and Charges Template

Để biết về việc thiết lập thuế, hãy truy cập [trang này](../setting-up/setting-up-taxes.md)

## 1. Cách thêm Thuế/Phí Bán hàng thông qua một mẫu
Trước khi tạo mẫu mới, hãy lưu ý rằng các mẫu đã được tạo sẵn cho nhiều loại thuế thường dùng.

1. Đi đến danh sách Mẫu Thuế và Phí Bán hàng, nhấp vào Mới.
2. Nhập tên tiêu đề cho Thuế.
3. Dưới mục loại (type), thiết lập loại cơ sở để tính thuế và tỷ lệ thuế. Có năm tùy chọn trong mục loại để tính thuế.
  1. Actual (Thực tế): Bạn có thể nhập trực tiếp số tiền cho chi phí.
  1. On Net Total (Trên Tổng ròng): Tính trên tổng ròng của tất cả các mặt hàng.
  1. On Previous Row Amount (Trên Số tiền dòng trước): Dùng để tính thuế chồng thuế. Ví dụ: phí phụ thu trên số tiền mà thuế đã được áp dụng ở dòng trước đó.
  1. On Previous Row Total (Trên Tổng dòng trước): Tương tự như trên nhưng áp dụng trên tổng hóa đơn chứ không chỉ là số tiền của một mặt hàng.
  1. On Item Quantity (Trên Số lượng mặt hàng): Thuế sẽ được tính bằng Tỷ lệ thuế * Số lượng mặt hàng. Ví dụ: nếu Tỷ lệ thuế là 2% và số lượng mặt hàng là 1, thì Thuế sẽ là 4; nếu số lượng mặt hàng là 5, Thuế sẽ là 10, v.v.
4. Chọn một tài khoản đầu mục có sẵn tỷ lệ thuế hoặc tạo tài khoản của riêng bạn.
1. Chọn mặc định (default) sẽ áp dụng mẫu này theo mặc định cho các giao dịch Bán hàng mới.
5. Lưu.
  ![Sales taxes](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/sales-taxes.png)

**Is Inter State (Có phải liên bang/tỉnh)**: Dành cho Ấn Độ. Khi chọn khách hàng trong Hóa đơn bán hàng hoặc Phiếu giao hàng, nếu mã GST của nơi cung ứng và địa chỉ giao hàng của khách hàng không khớp, mẫu có tích chọn 'Is Inter State' sẽ được thiết lập làm mẫu thuế. Nếu nơi cung ứng và địa chỉ giao hàng giống nhau, mẫu thuế mặc định sẽ được áp dụng. Điều này cũng áp dụng cho Hóa đơn mua hàng, khi chọn Nhà cung cấp, các mẫu được thiết lập tùy thuộc vào địa chỉ. Ví dụ: IGST.

## 2. Các tính năng
### 2.1 Bảng Thuế và Phí Bán hàng

* **Consider Tax or Charge for (Xét Thuế hoặc Phí cho)**: Total (Tổng) - cho tổng của tất cả các mặt hàng. Valuation (Giá trị) - cho từng mặt hàng. Valuation and total (Giá trị và tổng) - áp dụng thuế/phí cho cả hai. [Xem bài viết này](../accounts/articles/what-is-the-differences-of-total-and-valuation-in-tax-and-charges.md) để biết sự khác biệt.

* **Reference Row # (Số dòng tham chiếu)**: Nếu thuế dựa trên "On Previous Row Total", bạn có thể chọn số dòng sẽ được lấy làm cơ sở cho tính toán này (mặc định là dòng trước đó).
    ![Sales taxes table](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/sales-taxes-table.png)

* **Is this Tax included in Basic Rate? (Thuế này đã bao gồm trong Giá cơ bản chưa?)**: Nếu được tích chọn, số tiền thuế sẽ được coi là đã bao gồm trong Giá in / Số tiền in trong bảng Mặt hàng của một giao dịch. Điều này hữu ích khi bạn muốn đưa ra mức giá đã bao gồm thuế cho khách hàng. Để tính toán mức giá đã bao gồm thuế, hệ thống sẽ tính Tổng ròng bằng cách trừ đi số tiền thuế cần áp dụng, sau đó mới tính thuế trên số tiền đó.
* **Account Head (Đầu mục tài khoản):** Sổ cái tài khoản mà khoản thuế này sẽ được ghi sổ. Nếu bạn chọn VAT hoặc bất kỳ đầu mục thiết lập sẵn nào khác, tỷ lệ sẽ được tự động điền.
* **Cost Center (Trung tâm chi phí):** Nếu thuế/phí là thu nhập (như phí vận chuyển) hoặc chi phí, nó cần được ghi sổ vào một Trung tâm chi phí.
* **Description (Mô tả):** Mô tả về loại thuế (sẽ được in trong hóa đơn/báo giá).
* **Rate (Đơn giá):** Tỷ lệ thuế, ví dụ: 14 = thuế 14%.
* **Amount (Số tiền):** Số tiền thuế cần áp dụng, ví dụ: 100.00 = ₹100 thuế.

Các tỷ lệ thuế bạn xác định trong mẫu sẽ là tỷ lệ thuế tiêu chuẩn cho tất cả các Mặt hàng. Nếu có các Mặt hàng cần có tỷ lệ khác, bạn có thể ghi đè tỷ lệ thuế tiêu chuẩn bằng cách thiết lập Mẫu thuế mặt hàng cho Mặt hàng hoặc Nhóm mặt hàng đó.

### 3. Các chủ đề liên quan
1. [Sales Order](sales-order.md)
1. [Selling Settings](selling-settings.md)

{next}