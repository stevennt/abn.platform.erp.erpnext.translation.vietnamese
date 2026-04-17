<!-- add-breadcrumbs -->
# Hệ thống tài khoản

**Hệ thống tài khoản là bản thiết kế các tài khoản trong tổ chức của bạn.**

Cấu trúc tổng thể của Hệ thống tài khoản dựa trên hệ thống kế toán bút toán kép, vốn đã trở thành tiêu chuẩn trên toàn thế giới để định lượng tình hình tài chính của một công ty.

Hệ thống tài khoản là một chế độ xem dạng cây của tên các Tài khoản (Sổ cái và Nhóm) mà một Công ty cần để quản lý sổ sách kế toán của mình. ERPNext thiết lập một hệ thống tài khoản đơn giản cho mỗi Công ty bạn tạo, nhưng bạn có thể sửa đổi nó theo nhu cầu và các yêu cầu pháp lý của mình.

Đối với mỗi công ty, Hệ thống tài khoản biểu thị cách phân loại các bút toán kế toán, chủ yếu dựa trên các yêu cầu theo quy định (thuế, tuân thủ các quy định của chính phủ).

![CoA Tree](https://docs.erpnext.com/docs/v13/assets/img/accounts/chart-of-accounts-tree.png)

Hệ thống tài khoản giúp bạn trả lời các câu hỏi như:

 * Tổ chức của bạn đáng giá bao nhiêu?
 * Bạn đã vay bao nhiêu nợ?
 * Bạn đang tạo ra bao nhiêu lợi nhuận (và từ đó đóng thuế bao nhiêu)?
 * Bạn đang bán được bao nhiêu?
 * Cơ cấu chi phí của bạn như thế nào?

Với tư cách là người quản lý doanh nghiệp, việc thấy được tình hình kinh doanh của mình đang diễn ra tốt như thế nào là rất có giá trị.

> **Mẹo**: Nếu bạn không thể đọc được Bảng cân đối kế toán, thì đây là một cơ hội tốt để bắt đầu tìm hiểu về nó. Việc này sẽ rất xứng đáng với công sức bỏ ra. Bạn cũng có thể nhờ sự trợ giúp của kế toán viên để thiết lập Hệ thống tài khoản của mình.

Để truy cập danh sách Hệ thống tài khoản, hãy đi tới:
> Home > Accounting > Accounting Masters > Chart of Accounts

## 1. Cách Tạo/Chỉnh sửa Tài khoản
ERPNext đi kèm với một bộ Hệ thống tài khoản tiêu chuẩn. Thay vì tạo/sửa đổi, bạn cũng có thể sử dụng công cụ [Chart of Accounts Importer](https://docs.erpnext.com/docs/v13/user/manual/en/setting-up/chart-of-accounts-importer). Lưu ý rằng Hệ thống tài khoản hiện tại sẽ bị ghi đè khi sử dụng công cụ này.

1. Đi tới danh sách Hệ thống tài khoản.

 Tại đây bạn có thể mở các tài khoản nhóm chứa các tài khoản khác. Có các tùy chọn để "Thêm con" (Add Child) trong một tài khoản, Chỉnh sửa hoặc Xóa tài khoản đó.

 <img class="screenshot" alt="Chart of Accounts" src="https://docs.erpnext.com/docs/v13/assets/img/accounts/chart-of-accounts-add.gif">

1. Tùy chọn để tạo tài khoản con sẽ chỉ xuất hiện nếu bạn nhấp vào loại Tài khoản là Nhóm (thư mục).
1. Nhập tên cho tài khoản.
1. Nhập mã số cho tài khoản.
1. Tích vào 'Is Group' nếu bạn muốn đây là một tài khoản nhóm có thể chứa các tài khoản khác.
1. Chọn Loại Tài khoản (Account Type). Việc chọn mục này rất quan trọng vì một số trường chỉ cho phép chọn các loại tài khoản cụ thể.
1. Thay đổi tiền tệ nếu tài khoản này sẽ được sử dụng cho các giao dịch với các loại tiền tệ khác nhau. Theo mặc định, đó là tiền tệ của Công ty. Để biết thêm, hãy truy cập trang [Multi Currency Accounting](multi-currency-accounting.md).
1. Nhấp vào **Create New**.

Thông thường, bạn có thể muốn tạo các Tài khoản cho:

 * Công tác phí, lương, điện thoại, v.v. trong mục **Expenses** (Chi phí).
 * Thuế giá trị gia tăng (VAT), Thuế doanh thu, Vốn chủ sở hữu, v.v. trong mục **Current Liabilities** (Nợ ngắn hạn).
 * Doanh thu bán sản phẩm, Doanh thu dịch vụ, v.v. trong mục **Income** (Thu nhập).
 * Nhà xưởng, máy móc, nội thất, v.v. trong mục **Fixed Assets** (Tài sản cố định).

![Chart of Accounts](https://docs.erpnext.com/docs/v13/assets/img/accounts/coa-root-accounts.png)

> Mẹo: Các Tài khoản với các loại tiền tệ khác nhau được tạo ra khi bạn nhận hoặc thực hiện thanh toán bằng các loại tiền tệ khác nhau. Ví dụ, nếu bạn ở Ấn Độ và giao dịch với Hoa Kỳ, bạn có thể cần tạo các tài khoản như 'Debtors US', 'Creditors US', v.v.

Hãy cùng tìm hiểu các nhóm chính của Hệ thống tài khoản.

## 2. Loại Tài khoản
Các loại tài khoản chủ yếu được phân loại là thu nhập, chi phí, tài sản hoặc nợ phải trả.

### 2.1 Tài khoản Bảng cân đối kế toán

Các tài khoản Bảng cân đối kế toán là 'Nguồn sử dụng vốn (Tài sản)' và 'Nguồn hình thành vốn (Nợ phải trả)' biểu thị giá trị tài sản ròng của công ty bạn tại bất kỳ thời điểm nào.
Khi bạn bắt đầu hoặc kết thúc một kỳ tài chính, tất cả Tài sản sẽ bằng với Nợ phải trả.

> **Ghi chú về Kế toán**: Nếu bạn mới làm quen với kế toán, bạn có thể thắc mắc, làm sao Tài sản có thể bằng Nợ phải trả? Điều đó có nghĩa là công ty không có gì của riêng mình. Đúng vậy! Tất cả các "khoản đầu tư" được thực hiện vào công ty để mua tài sản (như đất đai, nội thất, máy móc) đều do các chủ sở hữu thực hiện. Các chủ sở hữu là một khoản nợ đối với công ty vì lợi nhuận thuộc về các chủ sở hữu.

> Nếu một công ty đóng cửa, họ sẽ cần bán tất cả tài sản và trả lại tất cả các khoản nợ phải trả (bao gồm cả lợi nhuận) cho các chủ sở hữu, khiến bản thân công ty không còn lại gì.

Tất cả các tài khoản trong mục Tài khoản Bảng cân đối kế toán đại diện cho một tài sản thuộc sở hữu của công ty như "Tài khoản Ngân hàng", "Đất đai và Bất động sản", "Nội thất" hoặc một khoản nợ phải trả (số tiền mà công ty nợ người khác) như "Vốn chủ sở hữu", "Nợ" v.v.

Hai tài khoản đặc biệt cần lưu ý ở đây là Phải thu khách hàng (Accounts Receivable - tiền bạn phải thu từ Khách hàng) và Phải trả người bán (Accounts Payable - tiền bạn phải trả cho Nhà cung cấp) tương ứng nằm trong mục Tài sản và Nợ phải trả.


### 2.2 Tài khoản Báo cáo Kết quả kinh doanh

Báo cáo Kết quả kinh doanh là nhóm các tài khoản 'Thu nhập' và 'Chi phí' đại diện cho các giao dịch kế toán của bạn trong một kỳ.

Khác với các tài khoản Bảng cân đối kế toán, các tài khoản Báo cáo Kết quả kinh doanh (hoặc tài khoản P&L) không đại diện cho giá trị tài sản ròng (Tài sản), mà đại diện cho số tiền đã chi và thu được trong quá trình phục vụ khách hàng trong kỳ. Do đó, vào đầu và cuối Năm tài chính, chúng sẽ trở về bằng không.

Trong ERPNext, việc theo dõi Báo cáo Kết quả kinh doanh rất dễ dàng thông qua biểu đồ Lợi nhuận và Thua lỗ.

![Profit and Loss Report](https://docs.erpnext.com/docs/v13/assets/img/accounts/profit-and-loss-report.png)


Lưu ý rằng, vào ngày đầu tiên của năm, bạn chưa tạo ra bất kỳ lợi nhuận hay thua lỗ nào, nhưng bạn vẫn có tài sản, do đó các tài khoản bảng cân đối kế toán không bao giờ trở về bằng không vào đầu hoặc cuối một kỳ.

### 2.3 Nhóm và Sổ cái

Có hai loại Tài khoản chính trong ERPNext - Nhóm (Group) và Sổ cái (Ledger). Nhóm có thể có các nhóm con và sổ cái bên trong, trong khi sổ cái là các nút cuối cùng của sơ đồ và không thể chứa thêm các tài khoản khác bên trong.

Các Giao dịch kế toán chỉ có thể được thực hiện đối với các Tài khoản Sổ cái.