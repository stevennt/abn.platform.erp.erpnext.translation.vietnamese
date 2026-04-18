<!-- add-breadcrumbs -->
# Hồ sơ Điểm bán hàng (POS Profile)

**Trong ERPNext, một hồ sơ POS cho phép sử dụng tính năng Điểm bán hàng.**

POS bao gồm các tính năng nâng cao để đáp ứng các chức năng khác nhau, chẳng hạn như quản lý tồn kho, CRM, tài chính, kho bãi, v.v., tất cả đều được tích hợp sẵn trong phần mềm POS. Trước khi có POS hiện đại, tất cả các chức năng này đều được thực hiện độc lập và yêu cầu phải nhập lại thông tin bằng tay, điều này có thể dẫn đến lỗi nhập liệu.

Nếu bạn đang trong hoạt động bán lẻ, bạn sẽ muốn Điểm bán hàng của mình nhanh chóng và hiệu quả nhất có thể. Để làm được điều này, bạn có thể tạo một Hồ sơ POS cho một người dùng.

Để truy cập danh sách Hồ sơ POS, hãy đi tới:
> Home > Retail > Retail Operations > Point-of-Sale Profile

## 1. Cách tạo Hồ sơ POS
1. Đi tới Point-of-Sale Profile và nhấn vào New.
1. Nhập tên cho hồ sơ.
1. Chọn một [Naming Series](https://docs.erpnext.com/docs/v16/user/manual/en/setting-up/settings/naming-series).
1. Thiết lập Tài khoản xóa nợ (Write Off Account) và Trung tâm chi phí xóa nợ (Write Off Cost Center) để ghi lại các giao dịch.
1. Thiết lập các phương thức thanh toán trong bảng, mặc định sẽ là tiền mặt nếu không có gì được thiết lập ở đây. Chỉ những phương thức được thiết lập ở đây mới có sẵn khi sử dụng POS. Sau khi thêm các phương thức thanh toán, hãy đặt một trong số chúng làm phương thức thanh toán mặc định bằng cách tích vào ô kiểm.

 ![Payment Method in POS Profile](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/payment-method-in-pos.png)

1. Thiết lập số tiền mặc định cho các phương thức thanh toán (khuyến nghị: 0).
1. Lưu.

 ![POS Profile](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/pos-profile.png)

### 1.1 Các tùy chọn bổ sung khi tạo Hồ sơ POS

* **Customer**: Người dùng có thể bán các sản phẩm cụ thể cho các Khách hàng cụ thể từ POS bằng cách thêm nhóm mặt hàng, nhóm khách hàng trong Hồ sơ POS.
* **Warehouse**: Số lượng tồn kho trong Kho được chọn sẽ bị ảnh hưởng đối với các giao dịch POS với Hồ sơ POS này.
* **Campaign**: Một [Campaign](https://docs.erpnext.com/docs/v16/user/manual/en/CRM/campaign) bán hàng có thể được liên kết tại đây để theo dõi tổng doanh số theo chiến dịch đó.
* **Company Address**: Nếu quầy POS được thiết lập tại một chi nhánh của Công ty, địa chỉ có thể được chọn tại đây.

* **Update Stock**: Nếu được bật, số lượng tồn kho sẽ bị ảnh hưởng khi thực hiện các giao dịch với Hồ sơ POS. Nghĩa là, các Phiếu nhập kho (Stock Ledger Entries) sẽ được tạo khi bạn "Xác nhận" Hóa đơn bán hàng này, từ đó loại bỏ nhu cầu cần một Phiếu giao hàng riêng biệt.
* **Ignore Pricing Rule**: Bất kỳ [Pricing Rule](pricing-rule.md) nào đang hoạt động sẽ bị bỏ qua đối với Hồ sơ POS này.
* **Allow Delete**: Trong POS Ngoại tuyến (Offline POS), dữ liệu được lưu tạm (cache). Tích vào ô này sẽ cho phép Người dùng xóa Hóa đơn bán hàng đang ở trạng thái Nháp.
* **Allow user to edit Rate**: Người dùng Hồ sơ POS sẽ được phép chỉnh sửa 'Đơn giá' của các Mặt hàng được thêm vào trong giao dịch.
* **Allow user to edit Discount**: Người dùng Hồ sơ POS sẽ được phép chỉnh sửa 'Chiết khấu' của các Mặt hàng được thêm vào trong giao dịch.
* **Allow Print Before Pay**: Điều này sẽ cho phép Người dùng POS in hóa đơn trước khi việc thanh toán được thực hiện.
* **Display Items In Stock**: Số lượng còn lại của các Mặt hàng từ Kho được chọn sẽ được hiển thị cho Người dùng POS.

## 2. Các tính năng

### 2.1 Áp dụng cho Người dùng
Theo mặc định, tất cả Người dùng Bán hàng đều có thể truy cập các Hồ sơ POS được tạo trong ERPNext. Tuy nhiên, nếu bạn chỉ muốn một số Người dùng nhất định truy cập các Hồ sơ POS nhất định, bạn có thể thêm họ vào bảng. Ngay khi có dù chỉ một Người dùng được thiết lập trong Hồ sơ POS, các Người dùng khác sẽ không thể sử dụng Hồ sơ POS này cho các giao dịch bán lẻ.

**Thiết lập Hồ sơ POS làm mặc định**: Khi tích vào ô Mặc định (Default) trong bảng, Hồ sơ POS hiện tại sẽ trở thành Hồ sơ POS mặc định cho Người dùng đó. Vì vậy, lần tới khi Người dùng đăng nhập vào hệ thống, Hồ sơ POS sẽ được thiết lập mặc định.

![POS User](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/pos-profile-default.png)

> Lưu ý: Nếu bạn chỉ định một Người dùng cụ thể, cài đặt POS sẽ chỉ được áp dụng cho Người dùng đó. Nếu tùy chọn Người dùng được để trống, cài đặt sẽ được áp dụng cho tất cả người dùng. Để hiểu cách POS hoạt động, hãy truy cập trang [Point of Sale](point-of-sales.md).


### 2.2 Thiết lập Nhóm mặt hàng và Nhóm khách hàng
Khi thiết lập Nhóm mặt hàng/Nhóm khách hàng trong Hồ sơ POS, nhóm đó sẽ tự động được chọn khi thực hiện các giao dịch với Hồ sơ POS.

![Filters in POS Profile](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/filters-in-pos-profile.png)

### 2.3 Cài đặt in

![POS Print Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/pos-profile-in-print-settings.png)

#### Mẫu in cho Trực tuyến
Bạn có thể thiết lập một Mẫu in để quyết định bố cục của tài liệu được in sẽ trông như thế nào. Để biết thêm, hãy truy cập trang [Print Format](https://docs.erpnext.com/docs/v16/user/manual/en/setting-up/print/print-format).

#### Tiêu đề thư (Letterhead)
Bạn có thể in Hóa đơn bán hàng POS trên tiêu đề thư của Công ty bạn. Tìm hiểu thêm [tại đây](https://docs.erpnext.com/docs/v16/user/manual/en/setting-up/print/letter-head).


#### Tiêu đề in
Tiêu đề Hóa đơn bán hàng POS cũng có thể được thay đổi khi in tài liệu. Ví dụ, tiêu đề có thể là 'Invoice' hoặc 'Bill'. Bạn có thể làm điều này bằng cách chọn **Print Heading**. Để tạo Tiêu đề in mới, hãy đi tới: Home > Settings > Printing > Print Heading. Tìm hiểu thêm [tại đây](https://docs.erpnext.com/docs/v16/user/manual/en/setting-up/print/print-headings).

#### Điều khoản và Điều kiện
Có thể có các điều khoản và điều kiện nhất định đối với Mặ