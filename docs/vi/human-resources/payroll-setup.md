<!-- add-breadcrumbs -->
# Thiết lập Bảng lương

Lương là một khoản tiền cố định hoặc thù lao được người sử dụng lao động trả cho nhân viên để đổi lấy công việc đã thực hiện.

Bảng lương là việc quản lý các hồ sơ tài chính về lương, tiền công, tiền thưởng, lương ròng và các khoản khấu trừ của nhân viên.

Để xử lý Bảng lương trong ERPNext,

1. Xác định [Kỳ tính lương](payroll-period.html.md) (tùy chọn)
1. Xác định [Bậc thuế thu nhập](income-tax-slab.html.md) (tùy chọn)
2. Tạo Cấu trúc lương với các Thành phần lương (Thu nhập và Khấu trừ)
3. Gán Cấu trúc lương cho từng Nhân viên thông qua Gán cấu trúc lương
4. Tạo Phiếu lương thông qua [Bút toán lương](payroll-entry.html.md).
5. Hạch toán Lương vào Tài khoản của bạn.
## Kỳ tính lương
[Kỳ tính lương](payroll-period.html.md) trong ERPNext là khoảng thời gian mà Nhân viên được trả lương cho công việc của họ tại Công ty. Kỳ tính lương giúp bạn xác định các bậc Thuế áp dụng cho kỳ đó, giúp việc quản lý các thay đổi về luật pháp trở nên dễ dàng hơn.

> Lưu ý: Việc cấu hình Kỳ tính lương là tùy chọn nếu bạn không có ý định sử dụng Phúc lợi linh hoạt hoặc các Bậc Thuế
## Thành phần Lương
Tài liệu này cho phép bạn định nghĩa từng thành phần Thu nhập và Khấu trừ, những thành phần này có thể được sử dụng để tạo Cấu trúc lương và sau đó tạo Phiếu lương hoặc Lương bổ sung. Bạn cũng có thể cấu hình loại, điều kiện và công thức cũng như các cài đặt khác được thảo luận dưới đây. Bạn có thể kích hoạt các tổ hợp khác nhau của các tùy chọn sau để cấu hình từng thành phần sao cho phù hợp với các chính sách của Công ty / Khu vực.

* Phụ thuộc vào Nghỉ không lương: Nghỉ không lương (LWP) xảy ra khi Nhân viên hết ngày nghỉ được phân bổ hoặc nghỉ mà không có sự phê duyệt (thông qua Đơn xin nghỉ phép). Nếu được kích hoạt, ERPNext sẽ tự động khấu trừ tiền lương theo tỷ lệ số ngày nghỉ không lương chia cho tổng số ngày làm việc trong tháng (dựa trên Danh sách ngày lễ).

	> Lưu ý: Nếu bạn không muốn ERPNext quản lý việc nghỉ không lương, đừng bật tùy chọn này trong bất kỳ Thành phần lương nào.

* Không bao gồm trong tổng số: Nếu tùy chọn này được kích hoạt, thành phần này sẽ không được cộng vào tổng Thu nhập hoặc Khấu trừ của Phiếu lương.

#### Thu nhập

<img class="screenshot" alt="Salary Component Earnings"
	src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/salary-component.png">

* Là Thành phần bổ sung: Tùy chọn này chỉ định rằng thành phần này chỉ có thể được thanh toán dưới dạng Lương bổ sung. Ví dụ về thành phần này có thể là Thưởng hiệu suất hoặc tiền lương nhận được khi đi công tác tại chỗ, v.v. Các thành phần như vậy không được coi là một phần của Cấu trúc lương thông thường. Thay vào đó, Lương bổ sung với các thành phần này có thể được Xác nhận khi cần thiết và sẽ được tự động thêm vào Phiếu lương.

* Có áp dụng Thuế: Nếu một thành phần cần được xem xét để tính Thuế theo Kỳ tính lương đã quy định, bạn có thể muốn kích hoạt tùy chọn này. Điều này yêu cầu bạn phải có Kỳ tính lương và Bậc thuế thu nhập được cấu hình với các Bậc thuế hợp lệ để xử lý bảng lương.

* Có thể thanh toán: Các thành phần như vậy có thể được hạch toán vào các tài khoản phải trả riêng biệt và các Tài khoản phải được cấu hình trong bảng Tài khoản.

* Phúc lợi linh hoạt: Phúc lợi linh hoạt là các thành phần thu nhập mà Nhân viên có thể chọn nhận theo tỷ lệ hoặc hàng năm khi họ yêu cầu. Những khoản này hầu hết được miễn thuế, trừ khi Nhân viên không nộp yêu cầu kèm theo đầy đủ hóa đơn / chứng từ. Nếu được bật, bạn có thể chỉ định mức phúc lợi tối đa cho phép cho một nhân viên trong một năm. Nhân viên có thể tạo [Đơn xin phúc lợi nhân viên](employee-benefit-application.md) với những mục mà họ chọn.

	> Lưu ý: Đơn xin phúc lợi nhân viên sẽ chỉ cho phép Nhân viên chọn từ các thành phần linh hoạt có trong Cấu trúc lương được gán cho Nhân viên đó.

	- Thanh toán theo Yêu cầu phúc lợi: Nhân viên có thể chọn nhận phúc lợi linh hoạt hàng năm thông qua Yêu cầu phúc lợi nhân viên hoặc cùng với lương hàng tháng của họ. Nếu bạn kích hoạt tùy chọn này, số tiền được phân bổ cho thành phần sẽ được thanh toán khi Nhân viên nộp [Yêu cầu phúc lợi nhân viên](employee-benefit-claim.html.md). Nếu không, số tiền sẽ được chi trả như một phần lương của Nhân viên theo tỷ lệ.

 - Chỉ ảnh hưởng đến Thuế (Không thể yêu cầu nhưng là một phần của Thu nhập chịu thuế): Đây là những thành phần mà công ty đã thanh toán cho Nhân viên bằng tiền mặt hoặc bằng hình thức khác, ví dụ như một chiếc xe hơi được mua để Nhân viên sử dụng. Nhân viên không thể yêu cầu thanh toán lại nhưng có nghĩa vụ phải nộp thuế. Số tiền được phân bổ cho thành phần này sẽ được xem xét khi tính thu nhập chịu thuế của Nhân viên.

 - Tạo Bút toán thanh toán riêng cho Yêu cầu phúc lợi: Một số phúc lợi linh hoạt có thể được yêu cầu về mặt pháp lý là phải thanh toán thông qua các chứng từ riêng biệt. Nếu bạn kích hoạt tùy chọn này, khi hạch toán bút toán ngân hàng, số tiền thanh toán cho các thành phần đó sẽ được hạch toán thành một bút toán riêng cho mỗi Nhân viên.

	<img class="screenshot" alt="Flexible Salary Component"
	src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/salary-component-1.png">

	> Lưu ý: Việc tính Thuế thông thường không bao gồm Phúc lợi linh hoạt vì trong hầu hết các trường hợp, các khoản này được miễn Thuế. Để tính thuế cho các thành phần này bất kỳ lúc nào trước kỳ lương cuối cùng, hãy sử dụng "Khấu trừ thuế cho phúc lợi nhân viên chưa yêu cầu" trong Bút toán lương / Phiếu lương khi đang xử lý Lương.

#### Khấu trừ

<img class="screenshot" alt="Salary Component Deduction"
	src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/salary-component-2.png">

* Biến đổi dựa trên Lương chịu thuế: Nếu bạn kích hoạt tùy chọn này, thành phần sẽ được coi là thành phần Khấu trừ thuế tiêu chuẩn. Thuế sẽ được tính dựa trên Bậc thuế thu nhập được liên kết với nhân viên.
## Cơ cấu Lương

Cơ cấu Lương (Salary Structure) thể hiện cách thức Lương được cấu trúc và tính toán dựa trên các Khoản thu nhập (Earnings) và Khoản khấu trừ (Deductions). Cơ cấu lương được sử dụng để giúp các tổ chức:

1. Duy trì mức lương cạnh tranh với thị trường lao động bên ngoài,
2. Duy trì mối quan hệ lương nội bộ giữa các vị trí công việc,
3. Ghi nhận và khen thưởng sự khác biệt về mức độ trách nhiệm, kỹ năng và hiệu suất, cũng như quản lý các chi phí lương.

Các thành phần thông thường của một cơ cấu lương (tại Ấn Độ) bao gồm:

* Lương cơ bản (Basic Salary): Đây là thu nhập chịu thuế và thường không quá 40% CTC.

* Phụ cấp thuê nhà (House Rent Allowance): HRA chiếm từ 40 đến 50% lương cơ bản.

* Phụ cấp đặc biệt (Special Allowances): Chiếm phần còn lại của lương, thường nhỏ hơn lương cơ bản và phải chịu thuế hoàn toàn.

* Phụ cấp đi lại khi nghỉ phép (Leave Travel Allowance): Khoản tiền không chịu thuế mà người sử dụng lao động trả cho nhân viên để đi nghỉ mát/du lịch cùng gia đình trong phạm vi Ấn Độ.

* Trợ cấp thôi việc (Gratuity): Về cơ bản là một khoản tiền trọn gói mà người sử dụng lao động trả khi nhân viên thôi việc hoặc nghỉ hưu.

* PF: Quỹ được thu thập trong trường hợp khẩn cấp hoặc khi về già. 12% lương cơ bản sẽ tự động được khấu trừ và đưa vào quỹ dự phòng của nhân viên.

* Phụ cấp y tế (Medical Allowance): Người sử dụng lao động trả cho nhân viên các chi phí y tế phát sinh. Khoản này được miễn thuế lên đến 15.000 Rs.

* Thưởng (Bonus): Phần chịu thuế của CTC, thường là một khoản tiền trọn gói mỗi năm một lần, được trao cho nhân viên dựa trên hiệu suất của cá nhân cũng như của tổ chức trong năm.

* Quyền chọn cổ phiếu cho nhân viên (Employee Stock Options): ESOPS là cổ phiếu miễn phí/chiết khấu được công ty trao cho nhân viên. Điều này được thực hiện chủ yếu để tăng tỷ lệ giữ chân nhân viên.

<img class="screenshot" alt="Submitted Salary Structure" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/salary-structure.png">
Một Cơ cấu Lương đã được Xác nhận

### Tạo Cơ cấu Lương mới
Để tạo một Cơ cấu Lương mới, hãy đi tới:

> Human Resources > Payroll Setup > Salary Structure > New Salary Structure

Trong Cơ cấu Lương mới,

1. Đặt tên cho Cơ cấu lương và thiết lập công ty, tiêu đề thư (letterhead) để in Phiếu lương (Salary Slip) và tần suất tính lương, v.v.
2. Thiết lập ngày bắt đầu có hiệu lực (Lưu ý: Chỉ có thể có một Cơ cấu lương duy nhất ở trạng thái "Active" cho một Nhân viên trong bất kỳ khoảng thời gian nào).
3. Cấu hình Số tiền quy đổi ngày nghỉ (Leave Encashment Amount) mỗi ngày, đây sẽ là số tiền phải trả cho Nhân viên khi có yêu cầu quy đổi ngày nghỉ thành tiền.
4. Số tiền phúc lợi tối đa (Max Benefits amount) là số tiền tối đa mà nhân viên đủ điều kiện nhận dưới dạng các Thành phần linh hoạt (Flexible Components).

#### Phiếu lương dựa trên Bảng chấm công (Timesheet)

Phiếu lương dựa trên Bảng chấm công áp dụng nếu bạn có hệ thống tính lương dựa trên bảng chấm công.

1. Tích chọn "Salary Slip Based on Timesheet"
2. Chọn thành phần lương và nhập Đơn giá giờ (Lưu ý: Thành phần lương này sẽ được cộng vào các khoản thu nhập trong Phiếu lương)

<img class="screenshot" alt="Salary Slip based on Timesheet" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/salary-timesheet.png">

#### Các Khoản thu nhập và Khoản khấu trừ trong Cơ cấu Lương

Trong các bảng “Earnings” (Thu nhập) và “Deductions” (Khấu trừ), bạn có thể chọn các thành phần thu nhập và khấu trừ. Điều kiện và công thức được cấu hình trong Thành phần lương (Salary Component) sẽ được sao chép theo mặc định, nhưng bạn có thể thay đổi nếu cần. Bạn cũng có thể muốn chọn Thành phần cơ sở (Base component) trong bảng Thu nhập. Lưu ý rằng số tiền đủ điều kiện cho mỗi nhân viên nên được cấu hình trong Phân bổ Cơ cấu lương (Salary Structure Assignment).

Nếu điều kiện và công thức cho bất kỳ khoản thu nhập hoặc khấu trừ nào chưa được cấu hình trong Thành phần lương, bạn có thể tính toán giá trị của các Thành phần lương dựa trên:

#### Điều kiện và Công thức

<img class="screenshot" alt="Condition and Formula" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/condition-formula.png">

#### Điều kiện và Số tiền

<img class="screenshot" alt="Condition and Amount" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/condition-amount.png">


Trong các điều kiện và công thức,

  * Sử dụng trường "base" để sử dụng lương cơ bản của Nhân viên
  * Sử dụng các chữ viết tắt của Thành phần lương. Ví dụ: BS cho Lương cơ bản (Basic Salary)
  * Sử dụng tên trường cho chi tiết nhân viên. Ví dụ: Employment Type cho employment_type

#### Chi tiết Tài khoản

<img class="screenshot" alt="Salary Structure Account" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/salary-structure-account.png">

  * Chọn Phương thức thanh toán (Mode of Payment) và Tài khoản thanh toán (Payment Account) cho các Phiếu lương sẽ được tạo bằng Cơ cấu lương này

Cuối cùng, nhấn *Lưu* Cơ cấu lương.

### Nghỉ không lương (LWP)

Nghỉ không lương (Leave Without Pay - LWP) xảy ra khi một Nhân viên hết số ngày nghỉ được phân bổ hoặc nghỉ mà không có sự phê duyệt (thông qua Đơn xin nghỉ phép). Nếu bạn muốn ERPNext tự động khấu trừ lương trong trường hợp LWP, bạn phải tích vào cột “Apply LWP” trong các danh mục Loại thu nhập (Earning Type) và Loại khấu trừ (Deduction Type). Số tiền bị trừ lương là tỷ lệ giữa số ngày LWP chia cho tổng số ngày làm việc trong tháng (dựa trên Danh sách ngày lễ).

Nếu bạn không muốn ERPNext quản lý LWP, hãy để trống mục LWP trong tất cả các Loại thu nhập và Loại khấu trừ.
## Gán Cấu trúc Lương

Gán Cấu trúc Lương cho phép bạn gán cấu trúc lương và chỉ định mức lương cơ bản đủ điều kiện cho mỗi nhân viên. Điều quan trọng là bạn phải thiết lập mức lương cơ bản cho mỗi lần gán vì đây sẽ là mức lương cơ bản được sử dụng để tính toán theo Cấu trúc Lương.

Để tạo một Gán Cấu trúc Lương mới, hãy đi tới:

> Nhân sự > Bảng lương > Gán Cấu trúc Lương > Gán Cấu trúc Lương mới

<img class="screenshot" alt="Salary Structure Assignment" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/salary-structure-assignment.png">

* * *

#Xử lý Bảng lương
Bạn có thể xử lý bảng lương hàng loạt cho Nhân viên thuộc một phòng ban, chi nhánh hoặc chức danh, hoặc xử lý bảng lương riêng lẻ bằng cách tạo Phiếu lương cho từng nhân viên.
## Xử lý Bảng lương bằng Bút toán thanh toán lương (Payroll Entry)
Bạn cũng có thể tạo phiếu lương cho nhiều nhân viên cùng lúc bằng cách sử dụng Payroll Entry:

> Human Resources > Payroll > Payroll Entry > New Payroll Entry

#### Payroll Entry

<img class="screenshot" alt="Payroll Entry" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/payroll-entry.png">

Trong Payroll Entry,

1. Chọn Công ty mà bạn muốn tạo Phiếu lương. Bạn cũng có thể chọn các trường khác như Chi nhánh, Phòng ban, Chức danh hoặc Dự án để cụ thể hơn.
2. Tích chọn _Salary Slip based on Timesheet_ nếu bạn muốn xử lý các Phiếu lương dựa trên bảng chấm công.
3. Chọn Ngày hạch toán (Posting Date) và kỳ hạn lương mà bạn muốn tạo Phiếu lương.
4. Nhấp vào "Get Employee Details" để lấy danh sách Nhân viên mà Phiếu lương sẽ được tạo dựa trên các tiêu chí đã chọn.
5. Nhập ngày Bắt đầu và Kết thúc cho kỳ lương.
6. Bạn có thể tích chọn _Deduct Tax For Unclaimed Employee Benefits_ nếu bạn muốn khấu trừ thuế cho tất cả các khoản phúc lợi (các Thành phần lương được đánh dấu là _Is Flexible Benefit_) đã trả cho nhân viên cho đến kỳ lương hiện tại.
7. Tương tự, _Deduct Tax For Unsubmitted Tax Exemption Proof_ cho phép bạn khấu trừ thuế đối với các khoản thu nhập đã được miễn thuế trong các kỳ lương trước như đã khai báo trong [Employee Tax Exemption Declaration](employee-tax-exemption-declaration.md) nhưng Nhân viên vẫn chưa nộp đủ chứng từ [Employee Tax Exemption Proof Submission](employee-tax-exemption-proof-submission.md).
8. Chọn Trung tâm chi phí và Tài khoản thanh toán.
9. Lưu biểu mẫu và Xác nhận để tạo các bản ghi Phiếu lương cho mỗi Nhân viên đang hoạt động trong khoảng thời gian đã chọn. Nếu các Phiếu lương đã được tạo trước đó, hệ thống sẽ không tạo thêm bất kỳ Phiếu lương nào nữa. Bạn cũng có thể chỉ lưu biểu mẫu dưới dạng Nháp và tạo Phiếu lương sau.

<img class="screenshot" alt="Submitted Payroll Entry" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/created-payroll.png">

Sau khi tất cả Phiếu lương đã được tạo, bạn có thể sử dụng _View Salary Slips_ để kiểm tra xem chúng có được tạo chính xác hay không hoặc chỉnh sửa nếu bạn muốn khấu trừ Nghỉ không lương (LWP).

Sau khi kiểm tra, bạn có thể "Xác nhận" tất cả cùng một lúc bằng cách nhấp vào "Submit Salary Slip".

>Lưu ý: Việc Xác nhận Phiếu lương cũng sẽ hạch toán vào tài khoản Phải trả lương mặc định để ghi nhận chi phí lương trích trước.

#### Hạch toán Lương vào Tài khoản

Bước cuối cùng là hạch toán Lương vào Hệ thống tài khoản của bạn.

Lương trong các doanh nghiệp thường được xử lý với sự bảo mật cực kỳ cao. Trong hầu hết các trường hợp, công ty thực hiện một lệnh thanh toán duy nhất tới ngân hàng bao gồm tất cả các khoản lương, và ngân hàng sẽ phân phối lương vào tài khoản lương của từng nhân viên. Bằng cách này, chỉ có một bút toán thanh toán duy nhất trong sổ sách kế toán của công ty và bất kỳ ai có quyền truy cập vào tài khoản của công ty cũng sẽ không thể xem được mức lương của từng cá nhân.

Bút toán thanh toán lương là một Bút toán (Journal Entry) ghi nợ tổng các thành phần lương thuộc loại thu nhập và ghi có tổng các thành phần lương thuộc loại khấu trừ của tất cả Nhân viên vào tài khoản mặc định được thiết lập ở cấp độ Thành phần lương cho từng thành phần.

Để tạo chứng từ thanh toán lương từ Payroll Entry, hãy nhấp vào -
> Make > Bank Entry

<img class="screenshot" alt="Payroll Make Entry" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/payroll-make-bank-entry.png">

Payroll Entry sẽ dẫn bạn đến Bút toán (Journal Entry) với các bộ lọc liên quan để xem các Phiếu bút toán Nháp đã được tạo. Bạn nên thiết lập số tham chiếu và ngày cho các giao dịch và Xác nhận các Bút toán đó.

>Lưu ý: Đối với các Thành phần lương là Phúc lợi linh hoạt và có tích chọn _Create Separate Payment Entry Against Benefit Claim_, ERPNext sẽ hạch toán các Bút toán Nháp riêng biệt.

<img class="screenshot" alt="Payroll Entry" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/payroll-journal-entry.png">
## Tạo Phiếu lương Thủ công

Sau khi Cấu trúc lương được tạo và được gán cho nhân viên thông qua Gán cấu trúc lương, bạn có thể tạo Phiếu lương riêng lẻ. Đi tới:

> Nhân sự > Bảng lương > Phiếu lương > Phiếu lương mới

#### Phiếu lương

<img class="screenshot" alt="Salary Slip" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/salary-slip.png">

{next}