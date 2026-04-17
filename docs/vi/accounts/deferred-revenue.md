<!-- add-breadcrumbs -->
# Doanh thu chưa thực hiện

**Doanh thu chưa thực hiện đề cập đến các khoản thanh toán trước mà Công ty nhận được cho các sản phẩm hoặc dịch vụ sẽ được giao hoặc thực hiện trong tương lai.**

Nó còn được gọi là doanh thu chưa kiếm được.

Công ty nhận tiền trả trước sẽ ghi nhận số tiền đó là Doanh thu chưa thực hiện trên bảng cân đối kế toán của họ dưới dạng một khoản nợ phải trả. Doanh thu chưa thực hiện là một khoản nợ phải trả vì nó đề cập đến doanh thu chưa được thực hiện và đại diện cho các sản phẩm hoặc dịch vụ đang nợ Khách hàng. Khi sản phẩm hoặc dịch vụ được giao theo thời gian, nó sẽ được ghi nhận là doanh thu trên báo cáo kết quả hoạt động kinh doanh.

## 1. Cấu hình Kế toán trả sau

> Được giới thiệu trong Phiên bản 13

Trước khi bạn bắt đầu sử dụng kế toán trả sau, bạn nên lưu ý các cài đặt dưới đây để có thể kiểm soát tốt hơn cách bạn quản lý kế toán trả sau của mình.

![Deferred Accounting Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/deferred-accounting-settings.png)

1. **Automatically Process Deferred Accounting Entry (Tự động xử lý bút toán kế toán trả sau):** Cài đặt này được bật theo mặc định. Trong trường hợp bạn không muốn các bút toán kế toán trả sau được ghi sổ tự động, bạn có thể tắt cài đặt này. Nếu cài đặt này bị tắt, kế toán trả sau sẽ phải được xử lý thủ công bằng cách sử dụng [Process Deferred Accounting](process-deferred-accounting.md)

1. **Book Deferred Entries Based On (Ghi nhận bút toán trả sau dựa trên):** Số tiền doanh thu chưa thực hiện có thể được ghi nhận dựa trên hai tiêu chí. Tùy chọn mặc định ở đây là "Days" (Ngày). Nếu "Days" được chọn, số tiền doanh thu chưa thực hiện sẽ được ghi nhận dựa trên số ngày trong mỗi tháng và nếu "Months" (Tháng) được chọn, thì nó sẽ được ghi nhận dựa trên số tháng. **Ví dụ:** Nếu "Days" được chọn và doanh thu $12,000 phải được trả sau trong khoảng thời gian 12 tháng, thì $986.30 sẽ dành cho tháng có 30 ngày và $1,019.17 sẽ được ghi nhận cho tháng có 31 ngày. Nếu "Months" được chọn, $1,000 doanh thu chưa thực hiện sẽ được ghi nhận mỗi tháng bất kể số ngày trong tháng là bao nhiêu.

1. **Book Deferred Entries Via Journal Entry (Ghi nhận bút toán trả sau qua Bút toán):** Theo mặc định, các Bút toán Sổ cái được ghi trực tiếp để ghi nhận doanh thu chưa thực hiện đối với một hóa đơn. Để ghi nhận số tiền trả sau này thông qua Bút toán, tùy chọn này có thể được bật.

1. **Submit Journal Entries (Xác nhận Bút toán):** Tùy chọn này chỉ áp dụng nếu các bút toán kế toán trả sau được ghi thông qua Bút toán. Theo mặc định, các Bút toán cho việc ghi nhận trả sau được giữ ở trạng thái Nháp và người dùng phải kiểm tra các bút toán đó và xác nhận chúng một cách thủ công. Nếu tùy chọn này được bật, các Bút toán sẽ được tự động xác nhận mà không cần sự can thiệp của người dùng.

## 2. Cách sử dụng Doanh thu chưa thực hiện

Các nhà cung cấp dịch vụ internet và truyền hình cung cấp các gói đăng ký theo quý hoặc theo năm. Họ nhận toàn bộ khoản thanh toán trước từ Khách hàng cho vài tháng, nhưng ghi nhận thu nhập hàng tháng trong sổ sách kế toán của họ. Đây là Doanh thu chưa thực hiện đối với Nhà cung cấp và [Deferred Expense](deferred-expense.md) đối với Khách hàng. Dưới đây là cách họ nên cấu hình kế toán Doanh thu chưa thực hiện trong ERPNext để tự động hóa quy trình.

### 2.1 Mặt hàng

Trong danh mục Mặt hàng được tạo cho gói đăng ký, tại phần Doanh thu chưa thực hiện, hãy tích vào trường **Enable Deferred Revenue**. Bạn cũng có thể chọn một tài khoản Doanh thu chưa thực hiện cho mặt hàng cụ thể này và số tháng.

![Item With Deferred Revenue](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/deferred-item.png)

### 2.2 Hóa đơn bán hàng

Khi tạo Hóa đơn bán hàng cho Mặt hàng Doanh thu chưa thực hiện, thay vì ghi vào Tài khoản thu nhập, tài khoản Doanh thu chưa thực hiện sẽ được ghi Có bằng số tiền bán hàng. Nếu bạn đã thiết lập tài khoản và thời hạn trong Mặt hàng, thì tài khoản và ngày bắt đầu, ngày kết thúc dịch vụ sẽ được lấy tự động.

![Invoice With Deferred Revenue](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/deferred-invoice.gif)

### 2.3 Bút toán

Dựa trên Ngày bắt đầu và Ngày kết thúc được thiết lập trong bảng Mặt hàng của Hóa đơn bán hàng, các Bút toán sẽ được tạo tự động vào cuối mỗi tháng. Nó ghi Nợ giá trị từ tài khoản Doanh thu chưa thực hiện và ghi Có vào Tài khoản thu nhập đã chọn cho một Mặt hàng trong Hóa đơn bán hàng.

Dưới đây là một ví dụ về Thu nhập cho Mặt hàng Doanh thu chưa thực hiện được ghi nhận thông qua nhiều Bút toán.

![Deferred Revenue GL](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/deferred-revenue-gl.png)

## 3. Video

<div class="embed-container">
  <iframe src="https://www.youtube.com/embed/j6mx-EHU4aY" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
  </iframe>
</div>

### 4. Các chủ đề liên quan
1. [Sales Invoice](sales-invoice.md)
1. [Journal Entry](journal-entry.md)
1. [Chart Of Accounts](chart-of-accounts.md)

{next}