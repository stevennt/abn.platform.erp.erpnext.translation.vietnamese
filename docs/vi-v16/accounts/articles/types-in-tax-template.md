<!-- add-breadcrumbs -->
# Các loại trong Mẫu thuế Bán hàng và Mua hàng

Trong danh mục Thuế Bán hàng và Thuế Mua hàng, bạn sẽ thấy một cột gọi là Loại (Type). Dưới đây là phần giải thích ngắn gọn về ý nghĩa của từng Loại và cách bạn có thể sử dụng chúng.

![Calculate Tax Based On](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/calculate-tax-based-on.png)

**Actual (Thực tế):** Tùy chọn này cho phép bạn nhập trực tiếp số tiền chi phí. Ví dụ: 500 Rs chi phí cho Vận chuyển.

**On Net Total (Trên Tổng ròng):** Nếu bạn muốn áp dụng bất kỳ loại thuế hoặc phí nào trên Tổng ròng, hãy chọn tùy chọn này. Ví dụ: 18% GST áp dụng cho tất cả các mặt hàng trong Đơn bán hàng.

**On Previous Row Amount (Trên Số tiền dòng trước):** Tùy chọn này giúp bạn tính số tiền thuế dựa trên một số tiền thuế khác.

Ví dụ: Thuế Giáo dục (Education Cess) được tính dựa trên số tiền thuế GST.

**On Previous Row Total (Trên Tổng dòng trước):** Đối với mỗi dòng Thuế, một khoản thuế lũy kế được tính trong cột Tổng. Đối với dòng đầu tiên, tổng thuế được tính bằng Tổng ròng + Số tiền thuế ở dòng đầu tiên. Nếu bạn muốn áp dụng thuế trên Tổng số tiền của một dòng thuế khác, hãy sử dụng tùy chọn này.

Nếu bạn chọn Loại là Previous Row Amount hoặc Previous Row Total, bạn cũng phải chỉ định Số dòng (Row No.) mà Số tiền (Amount) hoặc Tổng (Total) của dòng đó sẽ được xem xét để tính toán.

{next}