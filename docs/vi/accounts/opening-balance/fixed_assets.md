<!-- add-breadcrumbs -->
# Cập nhật Tài sản cố định

Để nhập tất cả các tài sản cố định hiện có, trước tiên hãy tạo bản ghi tài sản và sau đó tạo một Bút toán để cập nhật Sổ cái.

## 1. Tạo bản ghi Tài sản

> Để biết thêm chi tiết về Tài sản, [vui lòng truy cập trang này](https://docs.erpnext.com/docs/v13/user/manual/en/asset/asset).

Tạo bản ghi Tài sản cho từng tài sản mà công ty bạn sở hữu mà chưa khấu hao hết.

Để tạo một Tài sản mới:

1. Tạo một [Mặt hàng](../../stock/item.md) với tùy chọn 'Is fixed Asset' được bật.
1. Đi đến **Assets > Assets > New**.
1. Nhập Tên tài sản (Asset Name).
1. Nhập Mã mặt hàng (Item Code).
1. Nhập Địa điểm (Location).
1. Nhập Ngày mua (Purchase Date).
1. Nhập Tổng giá trị (Gross Amount).
1. Tích vào **Is Existing Asset.**
1. Lưu.

 ![Opening Stock Balance](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/asset-opening-balance.png)

> Để biết thêm chi tiết về Tài sản, [vui lòng truy cập trang này](https://docs.erpnext.com/docs/v13/user/manual/en/asset/asset).

## 2. Tạo Bút toán để cập nhật Sổ cái

Khi bạn tạo một Tài sản mà có tích vào ô 'Is Existing Asset', Sổ cái sẽ không được cập nhật. Bạn sẽ phải cập nhật giá trị thông qua một Bút toán.

Để tạo một Bút toán mới:

1. Đi đến: **Accounting > Masters and Accounts > Journal Entry > New.**
1. Nhập Ngày hạch toán (Posting Date).
1. Chọn các tài khoản tài sản cố định phù hợp trong cột Tài khoản (Account) và nhập giá trị vào cột Nợ (Debit).
1. Chọn tài khoản 'Temporary Opening' trong cột Tài khoản (Account) và nhập số tiền chênh lệch vào cột Có (Credit).
1. Thiết lập 'Is Opening' thành Yes.

![Journal Entry Fixed Asset Opening](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/journal-entry-fixed-asset.png)

{next}