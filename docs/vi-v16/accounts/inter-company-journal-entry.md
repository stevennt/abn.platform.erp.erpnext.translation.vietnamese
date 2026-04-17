<!-- add-breadcrumbs -->
# Bút toán nội bộ giữa các công ty

**Bút toán nội bộ giữa các công ty được thực hiện giữa các tổ chức thuộc cùng một tập đoàn.**

Bạn có thể tạo Bút toán nội bộ giữa các công ty nếu bạn đang thực hiện các giao dịch với nhiều Công ty khác nhau.
Bạn có thể chọn các Tài khoản mà bạn muốn sử dụng trong các giao dịch nội bộ giữa các công ty. Một trường hợp sử dụng khả thi là một công ty mua hàng thay mặt cho một công ty khác.

Trước khi tạo Bút toán nội bộ giữa các công ty, bạn cần thiết lập Hệ thống tài khoản của mình.

1. Đi đến: **Kế toán > Công ty và Tài khoản > Hệ thống tài khoản**.
1. Chọn Tài khoản mà bạn muốn thiết lập làm Tài khoản nội bộ cho giao dịch, và đánh dấu vào ô 'Tài khoản nội bộ giữa các công ty' (Inter Company Account). Tài khoản này hiện có thể được sử dụng cho các giao dịch Bút toán nội bộ giữa các công ty. Bạn nên tạo một tài khoản mới cho các giao dịch nội bộ giữa các công ty.

    ![Ledger For Intercompany Transactions](https://docs.erpnext.com/docs/v16/assets/img/accounts/ledger-for-intercompany-transactions.png)

Bạn cần thực hiện tương tự cho tất cả các Tài khoản của các Công ty mà bạn muốn sử dụng cho các giao dịch Bút toán nội bộ giữa các công ty.

Trong trường hợp các công ty mẹ-con, khi một tài khoản được tạo trong công ty mẹ, nó sẽ được thêm vào công ty con. Điều này chỉ hoạt động nếu bạn đã chọn tùy chọn tạo Hệ thống tài khoản cho công ty con dựa trên công ty mẹ.

Các Bút toán nội bộ giữa các công ty được tạo bằng cách sử dụng biểu mẫu Bút toán trong ERPNext. Để truy cập danh sách Bút toán, hãy đi đến:

> Trang chủ > Kế toán > Công ty và Tài khoản > Bút toán

## 1. Điều kiện tiên quyết
Trước khi tạo Bút toán nội bộ giữa các công ty, bạn cần có:

* Ít nhất hai [Công ty](company-setup.md)
* Thiết lập các tài khoản nội bộ giữa các công ty trong [Hệ thống tài khoản](chart-of-accounts.md)

## 2. Cách tạo Bút toán nội bộ giữa các công ty
1. Đi đến danh sách Bút toán, và nhấn vào Mới.
1. Chọn Loại bút toán (Entry Type) là 'Bút toán nội bộ giữa các công ty' (Inter Company Journal Entry).
1. Thiết lập Công ty đang mua Mặt hàng thay mặt cho công ty khác.
1. Thêm các dòng cho các bút toán kế toán riêng lẻ. Chỉ các tài khoản nội bộ giữa các công ty mới có thể được lấy ở đây.
1. Trong mỗi dòng, bạn phải chỉ định:
  * Tài khoản nội bộ sẽ bị ảnh hưởng.
  * Số tiền Nợ hoặc Có.
  * Trung tâm chi phí (Nếu đó là Thu nhập hoặc Chi phí).
1. **Xem trước Bút toán (Ledger Preview):** Trước khi nhấn **Xác nhận**, bạn có thể kiểm tra lại các dòng bút toán để đảm bảo tính chính xác của các tài khoản nội bộ.
1. Sau khi **Xác nhận** Bút toán, bạn sẽ thấy một nút ở góc trên bên phải, **Tạo Bút toán nội bộ giữa các công ty** (Make Inter Company Journal Entry).

   ![Inter Company Journal Entry](https://docs.erpnext.com/docs/v16/assets/img/accounts/inter-company-journal-entry.png)

1. Nhấp vào nút. Bây giờ, bạn sẽ được yêu cầu chọn Công ty mà bạn muốn tạo Bút toán liên kết.

    ![Company Master](https://docs.erpnext.com/docs/v16/assets/img/accounts/select-company-in-inter-company-journal-entry.png)

1. Sau khi chọn Công ty, bạn sẽ được chuyển hướng đến một Bút toán khác nơi các trường liên quan sẽ được ánh xạ, ví dụ: Công ty, Loại chứng từ, Tham chiếu Bút toán nội bộ giữa các công ty, v.v.

    ![Auto Generated Inter Company Journal Entry](https://docs.erpnext.com/docs/v16/assets/img/accounts/auto-generated-intercompany-journal-entry.png)

1. Chọn các tài khoản nội bộ cho Công ty thứ hai trong bảng.
1. **Xác nhận** Bút toán.
1. Đảm bảo rằng tổng Số tiền Nợ và Có giống với tổng Số tiền Có và Nợ của Bút toán đã tạo trước đó tương ứng, nhưng các khoản nợ và có sẽ ngược lại.

**Lưu ý:** Các tài khoản trong Bút toán thứ hai phải ngược lại với những gì bạn đã làm trong Bút toán đầu tiên.
Ví dụ: Công ty A đang mua thứ gì đó từ Công ty B. Đây là cách chu kỳ thanh toán giữa hai công ty sẽ diễn ra khi sử dụng Bút toán nội bộ giữa các công ty.

1. Nợ Tài khoản Ngân hàng 500 và có tài khoản Phải thu của Công ty B 500.
1. Bây giờ, trong Bút toán nội bộ giữa các công ty, nợ tài khoản Phải trả của Công ty A 500 và có Tài khoản Ngân hàng 500.
1. Bạn cũng cần chọn các đối tác cho tài khoản Phải trả và Phải thu trước khi tiến hành Bút toán.

Bạn cũng có thể tìm thấy liên kết tham chiếu ở phía dưới, liên kết này sẽ được thêm vào cả hai Bút toán liên kết và sẽ bị xóa nếu bất kỳ Bút toán nào bị **Hủy**.

### 3. Các chủ đề liên quan
1. [Bút toán](journal-entry.md)
1. [Hóa đơn nội bộ giữa các công ty](inter-company-invoices.md)

{next}