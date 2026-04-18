---
title: Quy tắc sắp xếp hàng vào kho (Putaway Rule)
add_breadcrumbs: 1
show_sidebar: 0

metatags:
 description: Quy tắc sắp xếp hàng vào kho xác định chiến lược phân bổ Kho cho lượng tồn kho nhập về. Điều này đặc biệt hữu ích cho những người mua hàng có nhiều vị trí kho và khối lượng mua hàng lớn.
 keywords: Putaway Rule, Putaway, Put List, frappe, Warehouse Put Away, erpnext new features, WMS, Warehouse Capacity, erp, open source erp, free erp, stock, inventory
---

# Quy tắc sắp xếp hàng vào kho (Putaway Rule)

**Quy tắc sắp xếp hàng vào kho xác định Chiến lược phân bổ Kho cho lượng tồn kho nhập về.**

Một Quy tắc sắp xếp hàng vào kho được xác định duy nhất cho sự kết hợp giữa Mặt hàng và Kho trong một Công ty. Quy tắc này xem xét đến Sức chứa Kho và Độ ưu tiên.

Trong **Phiếu nhập hàng** và **Phiếu kho** (Nhập vật tư & Chuyển vật tư), các Quy tắc sắp xếp hàng vào kho sẽ được áp dụng và các Mặt hàng sẽ được **tự động phân bổ** vào các Kho dựa trên chiến lược đã cho.

Điều này đặc biệt hữu ích để quản lý sức chứa trong các Kho lớn có nhiều vị trí khác nhau.

Để truy cập Quy tắc sắp xếp hàng vào kho, hãy đi tới:

> Home > Stock > Stock Transactions > Putaway Rule

## 1. Điều kiện tiên quyết

Trước khi tạo và sử dụng Quy tắc sắp xếp hàng vào kho, bạn nên tạo các mục sau trước:

- [Mặt hàng](item.md)
- [Kho](warehouse.md)

## 2. Cách tạo Quy tắc sắp xếp hàng vào kho

1. Đi tới danh sách Quy tắc sắp xếp hàng vào kho, nhấn vào Mới.
 <img class='screenshot' alt='Unsaved Putaway Rule' src='https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/unsaved-putaway-rule.png'>

1. Thiết lập Công ty và Chọn một Mặt hàng.
1. Chọn Kho mà quy tắc này sẽ được áp dụng.
1. Thiết lập Sức chứa. Bạn cũng có thể chọn một Đơn vị tính nếu muốn thiết lập Sức chứa theo một Đơn vị tính khác. Sức chứa theo Đơn vị tính tồn kho sẽ được thiết lập tự động.
 <img class='screenshot' alt='Multi UOM Putaway Rule' src='https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/multi-uom-putaway-rule.png'>

1. Thiết lập Độ ưu tiên. Độ ưu tiên có thể bắt đầu từ 1 trở đi, trong đó 1 là độ ưu tiên cao nhất.
1. Lưu.
1. Bạn cũng có thể Vô hiệu hóa một Quy tắc sắp xếp hàng vào kho.

Quy tắc này là duy nhất cho mỗi sự kết hợp giữa Mặt hàng và Kho.

## 3. Chiến lược sắp xếp hàng vào kho được thực hiện như thế nào
1. Ở đây, chiến lược hoàn toàn dựa trên **Sức chứa** và **Độ ưu tiên**.
1. Các Kho sẽ được tự động phân bổ cho đến khi đạt đến mức sức chứa tối đa.
1. Độ ưu tiên sẽ được xem xét trước. Tiếp theo là không gian trống. Nếu hai quy tắc có cùng độ ưu tiên, quy tắc có nhiều không gian trống hơn sẽ được phân bổ.
1. Nếu bạn đang hoạt động ở mức tối đa công suất (không còn không gian trống trong bất kỳ Kho nào), ERPNext sẽ thông báo cho bạn.

## 4. Cách thức hoạt động

Như đã đề cập trước đó, các Quy tắc sắp xếp hàng vào kho được áp dụng cho **Phiếu nhập hàng** và **Phiếu kho** (Nhập vật tư & Chuyển vật tư).

Một ô kiểm có tên **Áp dụng Quy tắc sắp xếp hàng vào kho** (Apply Putaway Rule) sẽ phân bổ các mặt hàng vào các Kho dựa trên các Quy tắc sắp xếp hàng vào kho.
 <img class='screenshot' alt='Apply Putaway Rule checkbox' src='https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/apply-putaway-rule.png'>

Các Quy tắc sắp xếp hàng vào kho được áp dụng khi tích vào ô kiểm này. Chúng cũng được áp dụng lại khi Lưu nếu ô kiểm này được bật.

Hãy cùng xem ví dụ thực tế:

1. Đây là một Đơn mua hàng với yêu cầu 5 Thùng (60 Cái) Nước khoáng.
 <img class='screenshot' alt='Purchase Order' src='https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/po-putaway-demo.png'>

1. Hai Quy tắc sắp xếp hàng vào kho đang hoạt động đã được tạo dưới đây với sức chứa mỗi quy tắc là 4 Thùng (48 Cái). Một quy tắc có độ ưu tiên cao hơn quy tắc kia.
 <img class='screenshot' alt='Active Putaway Rules List' src='https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/active-putaway-rules-list.png'>

1. Một Phiếu nhập hàng được tạo từ Đơn mua hàng này.

1. Khi tích vào **Áp dụng Quy tắc sắp xếp hàng vào kho**, một dòng gồm 5 Thùng sẽ được chia nhỏ và phân bổ theo các quy tắc.
 <img class='screenshot' alt='Putaway Rules applied in a Purchase Receipt' src='https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/pr-putaway-apply.gif'>

1. Đầu tiên, 4 trong số 5 Thùng được đưa vào Kho 'Finished Goods - UPI'. Khi Kho này đạt đến sức chứa, hệ thống sẽ phân bổ phần còn lại (1 Thùng) vào Kho 'Stores - UPI'.

## 5. Tổng hợp Sức chứa Kho

Báo cáo **Tổng hợp Sức chứa Kho** (Warehouse Capacity Summary) hiển thị sức chứa của các Kho và mức tồn kho tương ứng của chúng.

Chỉ những Kho có Quy tắc sắp xếp hàng vào kho mới được liệt kê ở đây. Nút **Chỉnh sửa Sức chứa** (Edit Capacity) cho phép chỉnh sửa sức chứa của Quy tắc sắp xếp hàng vào kho.

 <img class='screenshot' alt='Warehouse Capacity Summary' src='https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/warehouse-capacity-summary.png'>


## 6. Các loại hình áp dụng sắp xếp hàng vào kho

### 6.1. Sắp xếp trực tiếp (Direct Putaway)

1. Ví dụ ở phần trước giải thích về **Sắp xếp trực tiếp**.
1. Về bản chất, đây là việc phân bổ trực tiếp lượng tồn kho nhập về vào các Kho nhất định dựa trên một chiến lược.
1. Điều này có thể dễ dàng thực hiện thông qua một Phiếu nhập hàng.

### 6.2. Sắp xếp gián tiếp (Combined Putaway)

1. Hàng hóa thường được nhận vào các Kho **tạm thời** hoặc Kho **đệm** trước.
2. Từ đây, hàng được đưa vào các vị trí phù hợp trong Kho.
3. Đây được gọi là Sắp xếp **Gián tiếp hoặc Kết hợp**.
4. Để mô phỏng điều này trong ERPNext, một Phiếu nhập hàng đơn giản có thể được tạo vào Kho tạm thời mà không áp dụng Quy tắc sắp xếp hàng vào kho.
5. Từ đây, một Phiếu kho (Chuyển vật tư) có thể được thực hiện, nơi các Quy tắc sắp xếp hàng vào kho có thể được áp dụng tương tự như Phiếu nhập hàng.

## 7. Các chủ đề liên quan

1. [Phiếu nhập hàng](purchase-receipt.md)