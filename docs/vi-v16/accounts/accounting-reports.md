<!-- add-breadcrumbs -->
# Báo cáo Kế toán

Một số báo cáo kế toán chính bao gồm:

## 1. Công ty và Tài khoản
### Sổ cái
Đi đến: **Accounts > Company and Accounts > General Ledger**.

Sổ cái là một báo cáo chi tiết cho tất cả các giao dịch được ghi vào từng tài khoản và đối với mỗi giao dịch đều có một tài khoản Nợ và tài khoản Có, vì vậy nó liệt kê tất cả chúng.

Báo cáo dựa trên bảng GL Entry và có thể được lọc bằng nhiều bộ lọc được định nghĩa trước như Tài khoản, Trung tâm chi phí, Đối tác, Dự án và Kỳ kế toán, v.v. Điều này giúp bạn có được bản cập nhật đầy đủ cho tất cả các bút toán được ghi trong một kỳ đối với bất kỳ tài khoản nào. Kết quả có thể được nhóm theo Tài khoản, Chứng từ/Giao dịch và Đối tác với số dư đầu kỳ và cuối kỳ cho mỗi nhóm. Trong trường hợp kế toán đa tiền tệ, cũng có tùy chọn để kiểm tra số tiền bằng bất kỳ loại tiền tệ nào khác ngoài tiền tệ cơ sở của công ty.

 ![General Ledger](https://docs.erpnext.com/docs/v13/assets/img/accounts/general-ledger.png)

## 2. Báo cáo Tài chính
### 2.1 Phải thu Khách hàng và Phải trả Nhà cung cấp (AR / AP)
Đi đến: **Accounts > Accounting Statements > Accounts Receivable**.

Các báo cáo này giúp bạn theo dõi số tiền còn nợ của Khách hàng và Nhà cung cấp. Nó cũng cung cấp phân tích tuổi nợ, tức là phân tách số tiền còn nợ dựa trên khoảng thời gian mà số tiền đó chưa được thanh toán.

![Accounts Receivable](https://docs.erpnext.com/docs/v13/assets/img/accounts/accounts-receivable.png)

#### 2.1.1 Phải thu Khách hàng dựa trên Điều khoản thanh toán
Bạn cũng có thể xem Phải thu Khách hàng dựa trên [Payment Terms](payment-terms.md).

Báo cáo Phải thu Khách hàng dựa trên điều khoản thanh toán có thể được xem bằng cách tích vào ô 'Based On Payment Terms' như trong ảnh chụp màn hình sau.

 ![Accounts Receivable Based on Payment Terms](https://docs.erpnext.com/docs/v13/assets/img/accounts/accounts-receivable-based-on-payment-terms.png)


Số tiền còn nợ đối với mỗi điều khoản thanh toán có thể được xem. **Invoiced Amount** hiển thị số tiền của từng điều khoản thanh toán và **Paid Amount** hiển thị số tiền đã thanh toán đối với từng điều khoản thanh toán. Việc thanh toán cho mỗi điều khoản được phân bổ theo thứ tự FIFO.

<img alt="Accounts Receivable" class="screenshot"
    src="https://docs.erpnext.com/docs/v13/assets/img/accounts/reports/accounts-receivable-2.png">

    ![](https://docs.erpnext.com/docs/v13/assets/img/accounts/)


### 2.2 Bảng cân đối thử
Đi đến: **Accounts > Accounting Statements > Trial Balance**.

Bảng cân đối thử là một báo cáo kế toán liệt kê số dư tài khoản cho tất cả các Tài khoản của bạn (“Ledger” và “Group”) cho bất kỳ kỳ báo cáo nào. Một công ty lập bảng cân đối thử định kỳ, thường là vào cuối mỗi kỳ báo cáo. Mục đích chung của việc lập bảng cân đối thử là để đảm bảo các bút toán trong hệ thống ghi chép sổ sách của công ty là chính xác về mặt toán học. Tổng cột Nợ và cột Có phải giống nhau cho bất kỳ kỳ nào để đảm bảo các bút toán là chính xác. Trong ERPNext, báo cáo hiển thị các cột sau:

  * Opening (Dr): Số dư Nợ đầu kỳ tại Ngày bắt đầu
  * Opening (Cr): Số dư Có đầu kỳ tại Ngày bắt đầu
  * Debit: Tổng số tiền Nợ đối với tài khoản trong khoảng thời gian được chọn
  * Credit: Tổng số tiền Có đối với tài khoản trong khoảng thời gian được chọn
  * Closing (Dr): Số dư Nợ cuối kỳ tại Ngày kết thúc
  * Closing (Cr): Số dư Có cuối kỳ tại Ngày kết thúc

Cũng có một số tùy chọn khác để bao gồm hoặc loại trừ các Bút toán khóa sổ kỳ, hiển thị / ẩn các tài khoản có số dư bằng không và hiển thị số dư P&L (Thu nhập & Chi phí) chưa đóng của năm tài chính trước. Tất cả các số liệu trong báo cáo được hiển thị bằng tiền tệ cơ sở của công ty.

 ![Trial Balance](https://docs.erpnext.com/docs/v13/assets/img/accounts/trial-balance.png)

### 2.3 Bảng cân đối kế toán
Đi đến: **Accounts > Accounting Statements > Balance Sheet**.

Bảng cân đối kế toán là báo cáo tài chính của một công ty trình bày tài sản, nợ phải trả và vốn chủ sở hữu tại một thời điểm nhất định.

Bảng cân đối kế toán trong ERPNext mang lại cho bạn nhiều sự linh hoạt hơn để phân tích tình hình tài chính của mình. Bạn có thể chạy báo cáo qua nhiều năm để so sánh các giá trị. Bạn có thể kiểm tra giá trị cho một Sổ tài chính hoặc Trung tâm chi phí cụ thể. Bạn cũng có thể chọn bất kỳ loại tiền tệ nào khác để hiển thị số dư.

 ![Balance Sheet](https://docs.erpnext.com/docs/v13/assets/img/accounts/balance-sheet-report.png)

### 2.4 Báo cáo Lưu chuyển tiền tệ
Đi đến: **Accounts > Accounting Statements > Cash Flow**.

Lưu chuyển tiền tệ là một báo cáo tài chính cho thấy dòng tiền vào và dòng tiền ra của tiền mặt hoặc các khoản tương đương tiền của một công ty. Nó được sử dụng để phân tích khả năng thanh khoản của công ty.

 ![Cash Flow](https://docs.erpnext.com/docs/v13/assets/img/accounts/cash-flow-report.png)

### 2.5 Báo cáo Kết quả hoạt động kinh doanh
Đi đến: **Accounts > Accounting Statements > Profit and Loss Statement**.

Báo cáo Kết quả hoạt động kinh doanh là một báo cáo tài chính tóm tắt tất cả doanh thu và chi phí trong một kỳ nhất định. Báo cáo này còn được gọi là Báo cáo P&L.

Trong ERPNext, bạn có thể chạy báo cáo qua nhiều năm / kỳ để so sánh các giá trị. Bạn cũng có thể kiểm tra giá trị cho một Sổ tài chính, Dự án hoặc Trung tâm chi phí cụ thể. Bạn cũng có thể chọn bất kỳ loại tiền tệ nào khác để hiển thị số dư. Nếu bạn đang chạy báo cáo để xem số dư hàng quý / hàng tháng, bạn có thể chọn muốn hiển thị số dư lũy kế hoặc chỉ cho từng kỳ.

 ![Profit and Loss Report](https://docs.erpnext.com/docs/v13/assets/img/accounts/profit-and-loss-report.png)

### 2.6 Báo cáo Tài chính hợp nhất
Đi đến: **Accounts > Accounting Statements > Consolidated Financial Statement**.

Báo cáo hiển thị cái nhìn hợp nhất về Bảng cân đối kế toán, Báo cáo Kết quả hoạt động kinh doanh và Lưu chuyển tiền tệ cho một tập đoàn, bằng cách hợp nhất các báo cáo tài chính của tất cả các công ty con. Nó hiển thị số dư cho tất cả các công ty riêng lẻ cũng như số dư lũy kế cho một công ty tập đoàn.

![Consolidated Financial Statements](https://docs.erpnext.com/docs/v13/assets/img/accounts/consolidated-financial-statement.png)

## 3. Thuế
### 3.1 Sổ nhật ký Bán hàng và Mua hàng
Đi đến: **Accounts > Taxes > Sales Register *hoặc* Purchase Register**.

Báo cáo Sổ nhật ký Bán hàng và Mua hàng hiển thị tất cả các giao dịch Bán hàng và Mua hàng cho một kỳ nhất định với số tiền hóa đơn và chi tiết thuế.