<!-- add-breadcrumbs -->
# Thiết lập Bảng lương

Lương là một khoản tiền cố định hoặc thù lao được người sử dụng lao động trả cho nhân viên để đổi lấy công việc đã thực hiện.

Bảng lương là việc quản lý các hồ sơ tài chính về lương, tiền công, tiền thưởng, lương ròng và các khoản khấu trừ của nhân viên.

Để xử lý Bảng lương trong ERPNext,

1. Xác định [Kỳ tính lương](/docs/v16/user/manual/vi/human-resources/payroll-period.html) (tùy chọn)
1. Xác định [Bậc thuế thu nhập](/docs/v16/user/manual/vi/human-resources/income-tax-slab.html) (tùy chọn)
2. Tạo Cấu trúc lương với các Thành phần lương (Thu nhập và Khấu trừ)
3. Gán Cấu trúc lương cho từng Nhân viên thông qua Gán cấu trúc lương
4. Tạo Phiếu lương thông qua [Bút toán lương](/docs/v16/user/manual/vi/human-resources/payroll-entry.html).
5. Hạch toán Lương vào Tài khoản của bạn.

## Kỳ tính lương
[Kỳ tính lương](/docs/v16/user/manual/vi/human-resources/payroll-period.html) trong ERPNext là khoảng thời gian mà Nhân viên được trả lương cho công việc của họ tại Công ty. Kỳ tính lương giúp bạn xác định các bậc Thuế áp dụng cho kỳ đó, giúp việc quản lý các thay đổi về luật pháp trở nên dễ dàng hơn.

> Lưu ý: Việc cấu hình Kỳ tính lương là tùy chọn nếu bạn không có ý định sử dụng Phúc lợi linh hoạt hoặc các Bậc Thuế.

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

* Phúc lợi linh hoạt: Phúc lợi linh hoạt là các thành phần thu nhập mà Nhân viên có thể chọn nhận theo tỷ lệ hoặc hàng năm khi họ yêu cầu. Những khoản này hầu hết được miễn thuế, trừ khi Nhân viên không nộp yêu cầu kèm theo đầy đủ hóa đơn / chứng từ. Nếu được bật, bạn có thể chỉ định mức phúc lợi tối đa cho phép cho một nhân viên trong một năm. Nhân viên có thể tạo [Đơn xin phúc lợi nhân viên](/docs/v16/user/manual/vi/human-resources/employee-benefit-application.html) với những mục mà họ chọn.

	> Lưu ý: Đơn xin phúc lợi nhân viên sẽ chỉ cho phép Nhân viên chọn từ các thành phần linh hoạt có trong Cấu trúc lương được gán cho Nhân viên đó.

	- Thanh toán theo Yêu cầu phúc lợi: Nhân viên có thể chọn nhận phúc lợi linh hoạt hàng năm thông qua Yêu cầu phúc lợi nhân viên hoặc cùng với lương hàng tháng của họ. Nếu bạn kích hoạt tùy chọn này, số tiền được phân bổ cho thành phần sẽ được thanh toán khi Nhân viên nộp [Yêu cầu phúc lợi nhân viên](/docs/v16/user/manual/vi/human-resources/employee-benefit-claim.html). Nếu không, số tiền sẽ được chi trả như một phần lương của Nhân viên theo tỷ lệ.

 - Chỉ ảnh hưởng đến Thuế (Không thể yêu cầu nhưng là một phần của Thu nhập chịu thuế): Đây là những thành phần mà công ty đã thanh toán cho Nhân viên bằng tiền mặt hoặc bằng hình thức khác, ví dụ như một chiếc xe hơi được mua để Nhân viên sử dụng. Nhân viên không thể yêu cầu thanh toán lại nhưng có nghĩa vụ phải nộp thuế. Số tiền được phân bổ cho thành phần này sẽ được xem xét khi tính thu nhập chịu thuế của Nhân viên.

 - Tạo Bút toán thanh toán riêng cho Yêu cầu phúc lợi: Một số phúc lợi linh hoạt có thể được yêu cầu về mặt pháp lý là phải thanh toán thông qua các chứng từ riêng biệt. Nếu bạn kích hoạt tùy chọn này, khi hạch toán bút toán ngân hàng, số tiền thanh toán cho các thành phần đó sẽ được hạch toán thành một bút toán riêng cho mỗi Nhân viên.

	<img class="screenshot" alt="Flexible Salary Component"
	src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/salary-component-1.png">

	> Lưu ý: Việc tính Thuế thông thường không bao gồm Phúc lợi linh hoạt vì trong hầu hết các trường hợp, các khoản này được miễn Thuế. Để tính thuế cho các thành phần này bất kỳ lúc nào trước kỳ lương cuối cùng, hãy sử dụng "Khấu trừ thuế cho phúc lợi nhân viên chưa yêu cầu" trong Bút toán lương / Phiếu lương khi đang xử lý Lương.

#### Khấu trừ

<img class="screenshot" alt="Salary Component Deduction"
	src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/salary-component-2.png">

* Biến đổi dựa trên Lương chịu thuế: Nếu bạn kích hoạt tùy chọn này...