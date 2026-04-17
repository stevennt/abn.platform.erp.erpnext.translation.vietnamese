<!-- add-breadcrumbs -->
# Các danh mục Thuế hoặc Chi phí mua hàng

Xét trường Thuế hoặc Chi phí (Tax or Charge) trong danh mục Thuế và Chi phí mua hàng (Purchase Taxes and Charges) có ba giá trị.

- Total (Tổng)
- Valuation (Giá trị tính giá)
- Total and Valuation (Tổng và Giá trị tính giá)

![Valuation And Total](https://docs.erpnext.com/docs/v13/assets/img/articles/valuation-and-total.png)

Hãy cùng xem xét một ví dụ để hiểu tác động của từng loại chi phí. Chúng ta mua mười đơn vị mặt hàng với đơn giá là 800. Tổng số tiền mua hàng là 8.000. Mặt hàng đã mua có áp dụng 4% VAT, và phát sinh 100 INR chi phí vận chuyển.

####Total:

Thuế hoặc Chi phí được phân loại là **Total** sẽ được bao gồm trong tổng số của các giao dịch mua hàng. Nhưng nó sẽ không có tác động đến giá trị tính giá của mặt hàng đã mua.

Nếu VAT 4% được áp dụng cho mặt hàng, số tiền sẽ là 32 INR (tính trên đơn giá 800 của mặt hàng). Vì VAT là thuế tiêu thụ, nó nên được cộng vào giá trị của Đơn mua hàng/Hóa đơn mua hàng, vì nó sẽ được bao gồm trong khoản phải trả cho nhà cung cấp. Nhưng nó không nên được cộng vào giá trị của mặt hàng đã mua.

Khi Hóa đơn mua hàng được Xác nhận, việc hạch toán sổ cái sẽ được thực hiện cho các khoản thuế/chi phí được phân loại là Total.

####Valuation:

Thuế hoặc chi phí được phân loại là **Valuation** sẽ được cộng vào giá trị của mặt hàng đã mua, nhưng không cộng vào tổng số của giao dịch mua hàng đó.

Chi phí vận chuyển 100 INR nên được phân loại là valuation. Với cách này, giá trị của mặt hàng đã mua sẽ tăng từ 800 lên 900. Ngoài ra, chi phí này sẽ không được cộng vào tổng số của giao dịch mua hàng, vì đó là chi phí của bạn và không nên phản ánh với nhà cung cấp.

Kiểm tra [tại đây](../../stock/perpetual-inventory.md) để tìm hiểu về việc hạch toán chung được thực hiện cho các chi phí được phân loại là Valuation.

####Total and Valuation:

Thuế hoặc Chi phí được phân loại là **Total and Valuation** sẽ được cộng vào giá trị tính giá của mặt hàng, cũng như vào tổng số của các giao dịch mua hàng.

Giả sử rằng việc vận chuyển được sắp xếp bởi nhà cung cấp của chúng ta, nhưng chúng ta cần phải trả chi phí vận chuyển cho họ. Trong trường hợp đó, đối với chi phí vận chuyển, danh mục được chọn nên là Total and Valuation. Với cách này, chi phí vận chuyển 100 INR sẽ được cộng vào số tiền mua hàng thực tế là 800. Ngoài ra, 100 INR cũng sẽ phản ánh trong tổng số, vì nó là khoản phải trả của chúng ta cho nhà cung cấp.

{next}