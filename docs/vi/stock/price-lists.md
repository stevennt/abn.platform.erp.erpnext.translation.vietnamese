<!-- add-breadcrumbs -->
# Bảng giá

**Bảng giá là một tập hợp các Giá Mặt hàng để Bán, để Mua, hoặc cả hai.**

ERPNext cho phép bạn duy trì nhiều [Giá Mặt hàng](item-price.md) Bán và Mua bằng cách sử dụng các Bảng giá.

Bảng giá có thể được sử dụng trong các trường hợp bạn có các mức giá khác nhau cho các khu vực khác nhau (dựa trên chi phí vận chuyển), cho các loại tiền tệ khác nhau, v.v. Một Mặt hàng có thể có nhiều mức giá dựa trên khách hàng, tiền tệ, khu vực, chi phí vận chuyển, v.v., những mức giá này có thể được lưu trữ dưới dạng các kế hoạch đơn giá khác nhau.

Trong ERPNext, tất cả các Giá Mặt hàng được lưu trữ riêng biệt. Giá Mua của một mặt hàng khác với Giá Bán và do đó chúng được lưu trữ riêng biệt.

Để truy cập Bảng giá, hãy đi tới:

> Home > Selling/Buying/Stock > Items and Pricing > Price List

<img class="screenshot" alt="Price List" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/price-list.png">

## 1. Cách sử dụng Bảng giá

* Bảng giá sẽ được sử dụng khi tạo [Giá Mặt hàng](item-price.md) để theo dõi giá bán hoặc giá mua của một mặt hàng.

* Có thể chỉ định các quốc gia cụ thể trong Bảng giá.

* Để vô hiệu hóa một Bảng giá cụ thể, hãy bỏ chọn ô 'Enabled'. Bảng giá đã bị vô hiệu hóa sẽ không có sẵn để lựa chọn trong các giao dịch Bán hàng và Mua hàng.

* **Giá không phụ thuộc vào Đơn vị tính**: Hãy xem xét một mặt hàng, Cà chua mà bạn mua theo Thùng và bán theo Kilo. 1 Thùng = 10 Kilo và giá mua 1 Kilo là 10rs. Nếu tùy chọn "Price Not UOM Dependent" này không được chọn và bạn chọn 1 Thùng trong giao dịch của mình, giá sẽ chỉ hiển thị cho 1 Kilo vì đó là Giá Mặt hàng duy nhất được lưu.

    Bây giờ, nếu bạn chọn ô này và thực hiện giao dịch với một Thùng Cà chua, thì giá sẽ tự động được thiết lập là 100 vì giá của 1 Thùng (10 Kilo) là 100.

* Các Bảng giá Mua và Bán tiêu chuẩn được tạo sẵn theo mặc định.

**Lưu ý**: Nếu bạn có nhiều Bảng giá, bạn có thể chọn một Bảng giá hoặc gắn nó với một Khách hàng (để nó được tự động chọn). Giá Mặt hàng của bạn sẽ tự động được cập nhật từ Bảng giá.

### Các chủ đề liên quan
1. [Giá Mặt hàng](item-price.md)