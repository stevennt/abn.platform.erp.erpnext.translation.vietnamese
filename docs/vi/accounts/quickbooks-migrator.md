# ERPNext QuickBooks Migrator

## Thiết lập QuickBooks Migrator như thế nào?

### Tạo một ứng dụng QuickBooks Online

1. Từ thanh Awesome-bar, đi đến DocType "QuickBooks Migrator".
1. Truy cập [Inuit Developer Portal](https://developer.intuit.com)
1. Đăng nhập bằng tài khoản hiện có của bạn hoặc Đăng ký.
1. Đi đến trang "My Apps".
1. Nhấp vào "Select APIs".
1. Trong mục "QuickBooks API", tích chọn "Accounting".
1. Nhấp vào "Create App".
    - Bạn sẽ được đưa đến Trang tổng quan của Ứng dụng.

1. Đi đến tab "Keys".
1. Đi đến phần "Production Keys".
    - Hoàn tất các yêu cầu.

1. Trong DocType "QuickBooks Migrator", một "Redirect URL" sẽ được tạo cho bạn, hãy thêm nó vào danh sách "Redirect URIs" trong ứng dụng Inuit của bạn (trong phần "Production Keys"). Nhấp Lưu.

    - Đảm bảo rằng Redirect URL bắt đầu bằng `https`.

1. Từ phần "Production Keys", sao chép "Client ID" và "Client Secret" vào DocType "QuickBooks Migrator".
1. Lưu "QuickBooks Migrator".


### Kết nối với QuickBooks Online API

1. Nhấp vào "Connect to QuickBooks".
1. Một tab mới sẽ mở ra trong trình duyệt của bạn và bạn sẽ được yêu cầu Đăng nhập.
1. Nếu bạn có nhiều hơn một công ty, hãy chọn công ty mà bạn muốn chuyển đổi dữ liệu.
1. Nhấp vào "Connect".
1. Sau khi ủy quyền thành công, tab sẽ đóng lại.
1. Trạng thái sẽ được đặt thành "Connected to QuickBooks".
1. Trong "QuickBooks Migrator", chọn "Company" nơi bạn muốn chuyển đổi dữ liệu của mình.
1. Lưu "QuickBooks Migrator".


### Chuyển đổi dữ liệu

1. Nhấp vào nút "Fetch Data".
1. Trạng thái sẽ thay đổi từ "Connected to QuickBooks" sang "In Progress".
1. Các thanh tiến trình sẽ hiển thị trạng thái chuyển đổi.
1. Quá trình này sẽ mất vài phút tùy thuộc vào kích thước dữ liệu.
1. Sau khi quá trình chuyển đổi hoàn tất, trạng thái sẽ thay đổi thành "Complete" hoặc "Failed".


## Điều gì sẽ xảy ra khi tôi nhấp vào Fetch Data?


## Tài khoản

### Hệ thống tài khoản hiện có
    Khi tạo một Công ty, ERPNext sẽ tạo một hệ thống tài khoản cho công ty đó, các tài khoản này sẽ được giữ nguyên.

### Đặt tên tài khoản
    Để tránh trùng tên với các tài khoản hiện có, tất cả các tài khoản từ QuickBooks sẽ được gán hậu tố "- QB".

    Ví dụ: `Job Expense` sẽ trở thành `Job Expense - QB`.

    **Lưu ý**: ERPNext cũng mã hóa tên tài khoản bằng chữ viết tắt của Công ty. Tính đến điều này, `Job Expense` sẽ trở thành `Job Expense - QB - AZ` (giả sử `AZ` là chữ viết tắt của công ty).

### Tài khoản gốc
    Năm tài khoản gốc, bao gồm `Asset`, `Equity`, `Expense`, `Liability`, `Income` sẽ được tạo và tất cả các tài khoản (tùy thuộc vào loại tài khoản) sẽ trở thành con của các tài khoản này.

### Tài khoản nhóm
    QuickBooks cho phép thực hiện giao dịch trên các tài khoản nhóm, điều mà ERPNext không cho phép. Để xử lý việc này, mỗi tài khoản nhóm sẽ có một tài khoản con với tên có dấu gạch nối.

    Ví dụ:

    ```
        Job Expenses
            Job Materials
    ```
    sẽ trở thành
    ```
        Job Expenses
            Job Expenses - 1
            Job Materials
    ```

### Trùng tên
    QuickBooks cho phép nhiều tài khoản có cùng tên, điều mà ERPNext không cho phép. Để xử lý việc này, mỗi tài khoản trùng lặp sẽ có một tên có dấu gạch nối.

    Ví dụ:
    ```
        Insurance
            Job Materials
        Job Expenses
            Job Materials
    ```
    sẽ trở thành
    ```
        Insurance
            Job Materials
        Job Expenses
            Job Materials - 1
    ```



## Mặt hàng

### Đặt tên
    Tất cả các Mặt hàng sẽ có tên được mã hóa theo công ty.

    Ví dụ: `Pen` sẽ trở thành `Pen - AZ` (giả sử `AZ` là chữ viết tắt của công ty).

### Đơn vị tính (UOM)
    Tất cả các Mặt hàng sẽ được gán `Unit` làm Đơn vị tính mặc định.

### Đơn vị tính phân số
    `Unit` sẽ được phép có giá trị phân số.

### Tồn kho
    Bất kể Mặt hàng là Mặt hàng Tồn kho hay Phi tồn kho trong QuickBooks, không có thông tin liên quan đến Tồn kho nào được giữ lại.

## Khách hàng và Nhà cung cấp
### Đặt tên
    Tất cả Khách hàng và Nhà cung cấp sẽ có tên được mã hóa theo công ty.

    Ví dụ: `Pen` sẽ trở thành `Pen - AZ` (giả sử `AZ` là chữ viết tắt của công ty).



## Hóa đơn

### Các biến thể
    QuickBooks có bốn biến thể giao dịch của Hóa đơn, tất cả chúng sẽ được lưu dưới dạng Hóa đơn bán hàng.

    - **Invoice** tương đương với Hóa đơn bán hàng.
    - **Sales Receipt** tương đương với Hóa đơn bán hàng POS.
    - **Credit Memo** tương đương với Hóa đơn bán hàng trả lại (Credit Note).
    - **Refund Receipt** tương đương với Hóa đơn bán hàng POS trả lại.

### Chiết khấu và Markup
    QuickBooks sử dụng các tài khoản đặc biệt cho cả Markup và Chiết khấu, ERPNext không xử lý chi phí chiết khấu và markup theo cách này, thay vào đó, tất cả các Mặt hàng sẽ thấy sự thay đổi trong các tài khoản Thu nhập của chúng.

### Vận chuyển
    Đối với các Hóa đơn có phí Vận chuyển, một Mặt hàng có tên Shipping sẽ được thêm vào bảng Mặt hàng.

### Làm tròn
    ERPNext sử dụng phương pháp làm tròn khác với QuickBooks, vì lý do này, trong các Hóa đơn có Thuế và có tiền tệ khác với tiền tệ của công ty, Hóa đơn bán hàng sẽ có Tổng cộng khác với Hóa đơn QuickBooks.

### Trường hợp đặc biệt
    Nếu một Hóa đơn QuickBooks được liên kết với một `Delayed Charge` hoặc `Statement Charge` thì một Bút toán tương đương sẽ được tạo cho Hóa đơn này.



## Hóa đơn mua hàng (Bill)

### Các biến thể
    QuickBooks có hai biến thể giao dịch của Bill, tất cả chúng sẽ được lưu dưới dạng Hóa đơn mua hàng.

    - **Bill** tương đương với Hóa đơn mua hàng.
    - **Supplier Credit** tương đương với Hóa đơn mua hàng trả lại.



## Khác

Các giao dịch sau sẽ được lưu dưới dạng Bút toán

- Thanh toán trước (Advance Payment)
- Thanh toán hóa đơn (Bill Payment)
- Séc (Cheque)
- Tín dụng thẻ (Credit Card Credit)
- Chi phí (Expense)
- Điều chỉnh số lượng tồn kho (Inventory Qty Adjustment)
- Bút toán (Journal Entry)
- Thanh toán (Payment)
- Thanh toán thuế (Tax Payment)



## Thuế

Đối với mỗi mức Thuế của QuickBooks, một tài khoản ERPNext sẽ được tạo.

## Trường tùy chỉnh

QuickBooks Migrator sẽ thêm các Trường tùy chỉnh sau

- Trường Công ty (Company field)
    - Khách hàng (Customer)
    - Mặt hàng (Item)
    - Nhà cung cấp (Supplier)

- Trường ID QuickBooks (QuickBooks ID field)
    - Khách hàng (Customer)
    - Mặt hàng (Item)
    - Bút toán (Journal Entry)
    - Hóa đơn mua hàng (Purchase Invoice)
    - Hóa đơn bán hàng (Sales Invoice)
    - Nhà cung cấp (Supplier)