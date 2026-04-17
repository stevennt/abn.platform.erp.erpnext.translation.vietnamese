<!-- add-breadcrumbs -->
# Mẫu Bút toán

**Mẫu Bút toán cho phép bạn thiết lập và lựa chọn một danh sách các tài khoản và tùy chọn đã được định sẵn khi thực hiện một Bút toán.**

Để truy cập Mẫu Bút toán, hãy đi đến:

> Home > Accounting > General Ledger > Journal Entry Template

## 1. Cách tạo và sử dụng Mẫu Bút toán:

![Journal Entry Template](https://docs.erpnext.com/docs/v13/assets/img/accounts/journal-entry-template.png)


  1. Đi đến Danh sách Mẫu Bút toán và nhấn vào Mới.
  2. Thêm các chi tiết sau:
      * **Template Title**: Tên này sẽ được sử dụng để chọn mẫu từ Bút toán.
      * **Company**: Theo mặc định, công ty được định nghĩa trong Global Defaults sẽ được chọn. Bạn cũng có thể chọn bất kỳ công ty nào khác.
      * **Entry Type**: Bạn có thể chọn từ [các loại bút toán có sẵn trong Bút toán](journal-entry.md#3-journal-entry-types) tại đây. Giá trị mặc định là [Bút toán](journal-entry.md#31-journal-entry).
        * Có 3 'Entry Type' đặc biệt ở đây:
          * [Opening Entry](journal-entry.md#311-opening-entry): Loại này sẽ lấy tất cả các tài khoản và tải chúng vào bảng "Accounting Entries". Để tìm hiểu thêm, hãy truy cập trang [Opening Balance](opening-balance.md).
          * [Bank Entry](journal-entry.md#33-bank-entry): Loại này sẽ lấy và tải Tài khoản Ngân hàng mặc định nếu đã được thiết lập.
          * [Cash Entry](journal-entry.md#34-cash-entry): Loại này sẽ lấy và tải Tài khoản Tiền mặt mặc định nếu đã được thiết lập.
      * **Is Opening**: Mục này sẽ tự động được đặt thành 'Yes' nếu 'Opening Entry' được chọn làm Entry Type.
      * **Series**: Bạn có thể chọn từ danh sách chuỗi đặt tên có sẵn cho Bút toán.
      * **Accounting Entries**: Tại đây bạn có thể chọn một danh sách các tài khoản để thêm vào bút toán.
  3. Lưu và đi đến [Journal Entry](journal-entry.md#1-how-to-create-a-journal-entry) và nhấn vào mới.
  4. Trong trường 'From Template', khi bạn chọn mẫu, nó sẽ tải các tài khoản và các tùy chọn khác đã được thiết lập trong đó. Lưu ý rằng nó sẽ xóa sạch bảng Accounting Entries trước, nhưng bạn có thể thêm nhiều tài khoản khác vào bảng ngoài những tài khoản được lấy từ mẫu.

![Creating Journal Entry From Template](https://docs.erpnext.com/docs/v13/assets/img/accounts/create-journal-entry-from-template.gif)

## 3. Các chủ đề liên quan
  1. [Journal Entry](journal-entry.md)

  {next}