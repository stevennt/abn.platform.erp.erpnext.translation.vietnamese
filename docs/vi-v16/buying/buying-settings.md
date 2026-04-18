<!-- add-breadcrumbs -->
# Cài đặt Mua hàng

Cài đặt Mua hàng là nơi bạn có thể xác định các thuộc tính sẽ được áp dụng trong các giao dịch của phân hệ Mua hàng.
Bạn có thể tìm thấy Cài đặt Mua hàng tại:
> Trang chủ > Mua hàng > Cài đặt > Cài đặt Mua hàng

![Buying Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/buying/buying-settings.png)

Hãy cùng xem xét các tùy chọn khác nhau có thể được cấu hình:

## 1. Nhà cung cấp
### 1.1 Đặt tên Nhà cung cấp theo

Khi một Nhà cung cấp được Lưu, hệ thống sẽ tạo ra một định danh hoặc tên duy nhất cho Nhà cung cấp đó để có thể dùng để tham chiếu Nhà cung cấp trong các giao dịch Mua hàng khác nhau.

Nếu không được cấu hình khác, ERPNext sử dụng Tên của Nhà cung cấp làm tên duy nhất. Nếu bạn muốn định danh các Nhà cung cấp bằng các tên như SUPP-00001, SUPP-00002, hoặc các chuỗi định dạng tương tự khác, hãy chọn giá trị của Đặt tên Nhà cung cấp theo là "Naming Series".

Bạn có thể xác định hoặc chọn mẫu Naming Series từ: **Cài đặt > Dữ liệu > Naming Series**

Đọc [Naming Series](naming-series.md) để biết thêm về cách xác định Naming Series.

### 1.2 Nhóm Nhà cung cấp mặc định

Cấu hình giá trị mặc định của Nhóm Nhà cung cấp khi tạo một Nhà cung cấp mới. Ví dụ, nếu hầu hết các nhà cung cấp của bạn cung cấp phần cứng, bạn có thể đặt mặc định là 'Hardware'.

### 1.3 Lọc Nhà cung cấp không phải đơn vị vận chuyển (Non-transporter supplier filtering)

Tính năng này cho phép bạn lọc danh sách Nhà cung cấp để loại bỏ các đơn vị chỉ chuyên về vận chuyển khi bạn đang thực hiện các giao dịch mua hàng hàng hóa hoặc dịch vụ khác. Điều này giúp làm sạch danh sách lựa chọn và tăng tốc độ tìm kiếm Nhà cung cấp phù hợp.

### 1.4 Số tham chiếu Nhà cung cấp (Supplier reference numbers)

Cho phép bạn quản lý và sử dụng các số tham chiếu riêng của Nhà cung cấp trong các giao dịch mua hàng. Điều này hữu ích khi bạn cần đối chiếu các chứng từ của mình với số hóa đơn hoặc số tham chiếu nội bộ mà Nhà cung cấp đã gửi.

## 2. Thu mua
### 2.1 Bảng giá Mua hàng mặc định

Cấu hình Bảng giá mặc định khi tạo một giao dịch Mua hàng mới, mặc định được đặt là 'Standard Buying'. Giá Mặt hàng sẽ được lấy từ Bảng giá này. Bạn có thể sửa đổi 'Bảng giá' bằng cách sử dụng mũi tên ở cuối trường để thay đổi tiền tệ và quốc gia.

### 2.2 Yêu cầu Đơn mua hàng

Nếu tùy chọn này được cấu hình là "Yes", ERPNext sẽ ngăn bạn tạo Hóa đơn mua hàng hoặc Phiếu nhập hàng trực tiếp mà không tạo Đơn mua hàng trước. Nếu các giao dịch bán lẻ liên quan đến việc đặt hàng ngoại tuyến, thì có thể bỏ qua Đơn mua hàng. Nếu bạn đang nhận các Mặt hàng mẫu, bạn có thể tạo trực tiếp Phiếu nhập hàng để nhận Mặt hàng vào Kho của mình.

Cấu hình này có thể được ghi đè cho một nhà cung cấp cụ thể bằng cách bật hộp kiểm "Cho phép tạo Hóa đơn mua hàng mà không cần Đơn mua hàng" trong danh mục nhà cung cấp.

<img alt="Purchase Order Required" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/buying/po-required.png">

### 2.3 Yêu cầu Phiếu nhập hàng

Nếu tùy chọn này được cấu hình là "Yes", ERPNext sẽ ngăn bạn tạo Hóa đơn mua hàng mà không tạo Phiếu nhập hàng trước. Trong trường hợp Mặt hàng được giao dịch là dịch vụ, nó sẽ không yêu cầu phiếu nhập hàng, bạn có thể tạo trực tiếp Hóa đơn.

Cấu hình này có thể được ghi đè cho một nhà cung cấp cụ thể bằng cách bật hộp kiểm "Cho phép tạo Hóa đơn mua hàng mà không cần Phiếu nhập hàng" trong danh mục nhà cung cấp.

<img alt="Purchase Receipt Required" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/buying/pr-required.png">

### 2.4 Duy trì cùng Đơn giá trong suốt Chu kỳ mua hàng

Nếu tùy chọn này được bật, ERPNext sẽ kiểm tra xem giá của một Mặt hàng có thay đổi trong Hóa đơn mua hàng hoặc Phiếu nhập hàng được tạo từ Đơn mua hàng hay không, tức là nó sẽ giúp bạn duy trì cùng một đơn giá trong suốt chu kỳ mua hàng.

Bạn có thể cấu hình hành động mà hệ thống nên thực hiện nếu không duy trì cùng đơn giá trong trường hợp "Hành động nếu không duy trì cùng đơn giá":

- **Stop (Dừng)**: ERPNext sẽ ngăn bạn thay đổi giá bằng cách đưa ra thông báo lỗi xác thực.
- **Warn (Cảnh báo)**: Hệ thống sẽ cho phép bạn Lưu giao dịch nhưng sẽ cảnh báo bạn bằng một thông báo nếu đơn giá bị thay đổi.

### 2.5 Xem trước Sổ cái (Ledger Preview)

Tính năng này cho phép bạn xem trước các bút toán (JE) sẽ được tạo ra từ giao dịch mua hàng ngay trên giao diện trước khi bạn thực hiện Xác nhận. Điều này giúp đảm bảo tính chính xác của các tài khoản kế toán liên quan đến Kho, Thuế và Phải trả người bán.

## 3. Cho phép thêm Mặt hàng nhiều lần trong một giao dịch

Khi hộp kiểm này không được chọn, một mặt hàng không thể được thêm nhiều lần trong cùng một Đơn mua hàng. Tuy nhiên, bạn vẫn có thể thay đổi số lượng một cách rõ ràng. Đây là một hộp kiểm xác thực để ngăn chặn việc mua nhầm cùng một mặt hàng. Tùy chọn này có thể được chọn cho các trường hợp sử dụng cụ thể nơi có nhiều nguồn cho cùng một nguyên vật liệu, ví dụ như trong sản xuất.

## 4. Email đính kèm bản nháp PI (Email append-to tạo PI draft)

Trong quy trình mua hàng, khi bạn gửi email yêu cầu báo giá hoặc trao đổi với Nhà cung cấp, hệ thống cho phép tự động đính kèm hoặc tạo bản nháp Proforma Invoice (PI) dựa trên các thông tin đã trao đổi, giúp tối ưu hóa việc soạn thảo tài liệu giao dịch.

## 5. Các chủ đề liên quan
1. [Nhóm Nhà cung cấp](supplier-group.md)

{next}