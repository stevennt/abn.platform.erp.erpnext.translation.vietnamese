<!-- add-breadcrumbs -->
# Tích hợp Phân hệ Kho và Kế toán

Giá trị hàng tồn kho lưu trữ trong các kho cần được theo dõi.

Mỗi kho được liên kết với một sổ cái trong hệ thống tài khoản thông qua trường 'Account' trong kho.

![Stock Asset Ledger in Warehouse](https://docs.erpnext.com/docs/v13/assets/img/articles/stock-asset-ledger-in-warehouse.png)

Nếu trường Account trong một kho để trống, thì Tài khoản được đề cập trong kho cha của kho đó sẽ được xem xét. Nếu không thể xác định được Tài khoản bằng cách truy vết phân cấp, thì Tài khoản tồn kho mặc định (Default Inventory Account) được đề cập trong hồ sơ Công ty sẽ được xem xét.

![Default Inventory Account in Company](https://docs.erpnext.com/docs/v13/assets/img/articles/default-inventory-account-in-company.png)

Khi một công ty được tạo, một sổ cái có tên 'Stock In Hand' sẽ được tạo mặc định trong Hệ thống tài khoản.

**Hệ thống tài khoản > Tài sản > Tài sản ngắn hạn > Tài sản tồn kho > Stock In Hand.**

Nếu cần, bạn có thể tạo thêm các sổ cái bổ sung dưới nhóm 'Stock Assets'.

![Stock Asset Ledger in Chart of Accounts](https://docs.erpnext.com/docs/v13/assets/img/articles/stock-asset-ledger-in-coa.png)

{next}