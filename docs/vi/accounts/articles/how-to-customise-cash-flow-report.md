<!-- add-breadcrumbs -->
# Cách Tùy Chỉnh Báo Cáo Lưu Chuyển Tiền Tệ

Khi hệ thống tài khoản của bạn bắt đầu trở nên phức tạp hơn và các tiêu chuẩn báo cáo thay đổi và phát triển, báo cáo lưu chuyển tiền tệ mặc định có thể không còn đáp ứng đủ nhu cầu. Điều này là do ERPNext có thể không thể dự đoán chính xác phân loại và mục đích của tất cả các tài khoản trong hệ thống tài khoản. Một vấn đề khác mà bạn có thể gặp phải là không thể điều chỉnh định dạng báo cáo để phù hợp với nhu cầu của mình.

Điều này sẽ không còn là vấn đề nữa vì ERPNext hiện cho phép người dùng tùy chỉnh báo cáo lưu chuyển tiền tệ.


## Tổng quan kỹ thuật
Việc tùy chỉnh được thực hiện nhờ việc giới thiệu hai DocType mới - Cash Flow Mapper và Cash Flow Mapping. Cả hai DocType đều chứa thông tin cần thiết để tạo báo cáo lưu chuyển tiền tệ.

Cash Flow Mapping hiển thị cách các tài khoản trong hệ thống tài khoản của bạn ánh xạ tới một dòng trong báo cáo lưu chuyển tiền tệ, trong khi Cash Flow Mapper sẽ lấy tất cả các Cash Flow Mapping liên quan đến ba phần của một báo cáo lưu chuyển tiền tệ.

Với điều này, bạn có thể tạo các báo cáo lưu chuyển tiền tệ chi tiết theo yêu cầu của mình. Điều này nghe có vẻ chưa hợp lý lắm nhưng nó sẽ trở nên dễ hiểu sau khi chúng ta đi qua một ví dụ.

## Ví dụ
### Thông tin nền
Giả sử chúng ta có một công ty giả định mà chúng ta muốn tạo báo cáo lưu chuyển tiền tệ.
Đây là hình ảnh báo cáo lưu chuyển tiền tệ hiện tại:

![Default Cash Flow Report](https://docs.erpnext.com/docs/v13/assets/img/articles/default-cash-flow-report.png)

Chúng ta không thích báo cáo này vì những lý do sau:
- Định dạng báo cáo quá sơ sài.
- Số liệu 'Net Cash From Operations' (Lưu chuyển tiền thuần từ hoạt động kinh doanh) bị sai.

### Quy trình tùy chỉnh

Chúng ta muốn Báo cáo Lưu chuyển tiền tệ có định dạng tương tự như các hình ảnh dưới đây:

![Custom Cash Flow Format](https://docs.erpnext.com/docs/v13/assets/img/articles/format-1.png)

![Custom Cash Flow Format](https://docs.erpnext.com/docs/v13/assets/img/articles/format-2.png)

#### Kích hoạt Báo cáo Lưu chuyển tiền tệ tùy chỉnh
Thực hiện việc này trong Cài đặt Kế toán (Accounts Settings) bằng cách tích vào ô 'Use Custom Cash Flow Format'. Việc này sẽ khiến ERPNext chỉ sử dụng định dạng tùy chỉnh của bạn cho các báo cáo lưu chuyển tiền tệ.

![Enable Custom Cash Flow Report](https://docs.erpnext.com/docs/v13/assets/img/articles/enable-custom-cash-flow.png)

Chuyển sang phần tiếp theo để xây dựng báo cáo.

#### Tạo Cash Flow Mappings
Đối với mỗi dòng, chúng ta cần tạo một tài liệu Cash Flow Mapping để đại diện cho nó.

![New Cash Flow Mapping](https://docs.erpnext.com/docs/v13/assets/img/articles/new-cash-flow-mapping.png)

Bạn có thể coi Cash Flow Mapping là sự đại diện cho mỗi dòng trong báo cáo lưu chuyển tiền tệ. Một Cash Flow Mapping là con của một Cash Flow Mapper, điều này sẽ được giải thích sau.

Hãy bắt đầu bằng cách tạo các Cash Flow Mappings đại diện cho việc cộng ngược lại các chi phí không bằng tiền mặt đã được ghi nhận trong báo cáo Kết quả hoạt động kinh doanh (Profit or Loss). Chúng ta muốn chúng xuất hiện trên báo cáo lưu chuyển tiền tệ dưới dạng:
- Thuế thu nhập đã ghi nhận trong báo cáo kết quả hoạt động kinh doanh
- Chi phí tài chính đã ghi nhận trong báo cáo kết quả hoạt động kinh doanh
- Khấu hao tài sản cố định

Bắt đầu bằng cách mở một biểu mẫu Cash Flow Mapping mới.

Các trường trong DocType Cash Flow Mapping bao gồm:
- **Name**: Đây là thông tin để định danh tài liệu này. Hãy đặt tên liên quan đến nhãn (label).
- **Label**: Đây là nội dung sẽ hiển thị trong báo cáo lưu chuyển tiền tệ.
- **Accounts**: Bảng này chứa tất cả các tài khoản liên quan đến dòng này.

Với thông tin này, hãy tiến hành tạo tài liệu Cash Flow Mapping cho dòng 'Income taxes recognised in profit or loss' (Thuế thu nhập đã ghi nhận trong báo cáo kết quả hoạt động kinh doanh).

![Cash Flow Mapping for Income Tax Expense](https://docs.erpnext.com/docs/v13/assets/img/articles/cash-flow-mapping-for-income-tax.png)

Tôi đã đặt tên nó là 'Income Tax Charge' và đặt nhãn là 'Income taxes recognised in profit or loss'. Chúng ta muốn dòng này phản ánh các khoản thuế thu nhập từ báo cáo kết quả hoạt động kinh doanh của mình. Tài khoản nơi điều này xảy ra trong hệ thống tài khoản của chúng ta được đặt tên là 'Income Taxes' (một loại chi phí), vì vậy tôi đã thêm 'Income Taxes' vào bảng tài khoản. Nếu bạn có nhiều tài khoản đại diện cho chi phí thuế thu nhập hơn, bạn nên thêm tất cả chúng vào đây.

Vì chi phí Thuế thu nhập cần được điều chỉnh thêm trong báo cáo lưu chuyển tiền tệ, hãy tích vào ô 'Is Income Tax Expense'. Điều này sẽ giúp ERPNext tính toán chính xác các khoản điều chỉnh cần thực hiện.

*Để có kết quả tốt nhất, hãy để các tài khoản cha có các tài khoản con có cùng cách xử lý cho mục đích báo cáo lưu chuyển tiền tệ, vì ERPNext sẽ tính toán thay đổi thuần của tất cả các tài khoản con trong trường hợp tài khoản được chọn là tài khoản cha.*

Tương tự như vậy, tôi đã tạo cho hai mapping còn lại.

![Cash Flow Mapping for Finance Cost](https://docs.erpnext.com/docs/v13/assets/img/articles/cash-flow-mapping-for-finance-cost.png)

Chi phí tài chính cũng cần được điều chỉnh, vì vậy hãy đảm bảo tích vào ô 'Is Finance Cost'.

![Cash Flow Mapping for Depreciation](https://docs.erpnext.com/docs/v13/assets/img/articles/cash-flow-mapping-for-depreciation.png)

Tiếp theo, hãy thêm Cash Flow Mapping cho các mục hiển thị sự thay đổi trong vốn lưu động:

- Tăng/(giảm) các khoản nợ phải trả khác
- (Tăng)/giảm các khoản phải thu khách hàng và phải thu khác
- Tăng/(giảm) các khoản phải trả người bán và phải trả khác
- Thuế GTGT phải nộp
- (Tăng)/giảm hàng tồn kho

![Cash Flow Mapping for Other Liabilities](https://docs.erpnext.com/docs/v13/assets/img/articles/cash-flow-mapping-for-other-liabilities.png)

![Cash Flow Mapping for Receivables](https://docs.erpnext.com/docs/v13/assets/img/articles/cash-flow-mapping-for-receivables.png)

![Cash Flow Mapping for Payables](https://docs.erpnext.com/docs/v13/assets/img/articles/cash-flow-mapping-for-payables.png)

![Cash Flow Mapping for Duties and Taxes](https://docs.erpnext.com/docs/v13/assets/img/articles/cash-flow-mapping-for-taxes-payables.png)

![Cash Flow Mapping for Inventory](https://docs.erpnext.com/docs/v13/assets/img/articles/cash-flow-mapping-inventory.png)

Đừng quên cho ERPNext biết rằng các mapping này đại diện cho sự thay đổi trong vốn lưu động bằng cách tích vào ô 'Is Working Capital'.

Tại thời điểm này, chúng ta đã tạo tất cả các mapping cần thiết cho phần Hoạt động kinh doanh (Operating Activities) trong báo cáo lưu chuyển tiền tệ của mình. Tuy nhiên, ERPNext vẫn chưa biết điều đó cho đến khi chúng ta tạo các tài liệu Cash Flow Mapper. Chúng ta sẽ tạo các tài liệu Cash Flow Mapper tiếp theo.


#### Tạo Cash Flow Mappers
Cash Flow Mappers đại diện cho các phần của t