<!-- add-breadcrumbs -->
# Thành phần Lương

**Lương được các tổ chức chi trả cho nhân viên để đổi lấy các dịch vụ mà họ cung cấp. Các thành phần khác nhau tạo nên Cơ cấu Lương được gọi là Thành phần Lương.**

Tiền lương trả cho nhân viên bao gồm nhiều thành phần khác nhau, chẳng hạn như lương cơ bản, phụ cấp, lương truy lĩnh, v.v. ERPNext cho phép bạn định nghĩa các Thành phần Lương này và cũng chỉ định các thuộc tính khác nhau của chúng.

Để truy cập Thành phần Lương, hãy đi đến:
> Home > Human Resources > Payroll > Salary Component

## 1. Cách tạo Thành phần Lương

Để tạo một Thành phần Lương mới:

1. Đi đến danh sách Thành phần Lương, nhấp vào Mới.
2. Nhập Tên và Viết tắt.
3. Nhập Mô tả của Thành phần Lương (tùy chọn).
4. Nhập tên Công ty và Tài khoản mặc định của Thành phần Lương trong bảng Tài khoản.
5. Lưu.

 <img class="screenshot" alt="Salary Component" src="https://docs.erpnext.com/docs/v16/assets/img/human-resources/salary-component1.png">

## 2. Các tính năng

Ngoài các trường bắt buộc nêu trên, một số tính năng bổ sung của Thành phần Lương được đưa ra dưới đây:

### 2.1 Điều kiện và Công thức

Trong phần này, Điều kiện và Công thức cần thiết để tính toán Thành phần Lương có thể được chỉ định. Để chỉ định công thức, hãy bật hộp kiểm 'Amount based on formula' (Số tiền dựa trên công thức).

<img class="screenshot" alt="Salary Component" src="https://docs.erpnext.com/docs/v16/assets/img/human-resources/salary-component2.png">

Trong trường hợp Thành phần Lương dựa trên một số tiền đã được xác định trước, ERPNext cho phép bạn nhập trực tiếp số tiền vào trường Số tiền (tắt hộp kiểm 'Amount based on formula').

> **Lưu ý:** Thiết lập trên là tùy chọn. Bạn cũng có thể định nghĩa Số tiền và Công thức/Điều kiện cho một Thành phần Lương trực tiếp trong Cơ cấu Lương. Nếu chúng được chỉ định trong chính tài liệu Thành phần Lương, thông tin sẽ được lấy trực tiếp vào Cơ cấu Lương khi Thành phần được chọn.

### 2.2 Các thuộc tính bổ sung

Một số thuộc tính bổ sung của Thành phần Lương có thể được bật bằng cách sử dụng các hộp kiểm như sau:

* **Is Payable (Có thể thanh toán):** Chọn mục này nếu Thành phần Lương có thể thanh toán.
* **Depends on Payment Days (Phụ thuộc vào số ngày thanh toán):** Nếu hộp kiểm này được bật, Thành phần Lương sẽ được tính toán dựa trên số ngày làm việc.
* **Is Tax Applicable (Có áp dụng thuế):** Hộp kiểm này áp dụng cho các Thành phần Thu nhập. Việc chọn hộp kiểm này cho phép áp dụng thuế cho Thành phần Lương này.
* **Deduct Full Tax on Selected Payroll Date (Khấu trừ toàn bộ thuế vào ngày tính lương đã chọn):** Nếu được chọn và thành phần được sử dụng trong Lương bổ sung, số tiền thuế áp dụng cho số tiền bổ sung sẽ được khấu trừ vào tháng tính lương cụ thể đó. Nếu không được chọn, thuế sẽ được phân bổ cho các tháng còn lại của kỳ tính lương. Ví dụ: nếu một khoản tiền thưởng được đưa ra trong một tháng cụ thể bằng cách sử dụng Lương bổ sung, thì bạn có thể khấu trừ toàn bộ số tiền thuế chỉ trong tháng đó.
* **Round to the Nearest Integer (Làm tròn đến số nguyên gần nhất):** Chọn hộp kiểm này cho phép bạn làm tròn số tiền của Thành phần Lương này đến số nguyên gần nhất.
* **Statistical Component (Thành phần thống kê):** Nếu được chọn, giá trị được chỉ định hoặc tính toán trong thành phần này sẽ không đóng góp vào thu nhập hoặc các khoản khấu trừ. Tuy nhiên, giá trị của nó có thể được tham chiếu bởi các thành phần khác có thể được cộng vào hoặc trừ đi. Nếu bạn đặt một Thành phần Lương là thành phần Thống kê, bạn sẽ không cần phải thiết lập Tài khoản mặc định cho nó. Ngoài ra, bạn cũng sẽ không thể đặt thành phần này làm Phúc lợi linh hoạt.
* **Do Not Include in Total (Không bao gồm trong Tổng):** Chọn hộp kiểm này đảm bảo rằng Thành phần Lương không được bao gồm trong Tổng Lương. Nó được sử dụng để định nghĩa thành phần là một phần của CTC nhưng không được thanh toán (ví dụ: Sử dụng xe công ty).
* **Variable Based On Taxable Salary (Biến đổi dựa trên Lương chịu thuế):** Thành phần được tính toán tự động dựa trên thu nhập chịu thuế theo Bậc thuế thu nhập áp dụng (ví dụ: TDS hoặc Thuế thu nhập).
* **Exempted from Income Tax (Miễn thuế thu nhập):** Nếu được chọn, toàn bộ số tiền sẽ được khấu trừ khỏi thu nhập chịu thuế trước khi tính thuế thu nhập mà không cần bất kỳ [khai báo](/docs/v16/user/manual/en/human-resources/employee-tax-exemption-declaration) hoặc [nộp chứng từ](/docs/v16/user/manual/en/human-resources/employee-tax-exemption-proof-submission) nào. Ví dụ: Thuế chuyên nghiệp ở Ấn Độ được khấu trừ khỏi thu nhập chịu thuế trước khi tính thuế thu nhập.
* **Disabled (Vô hiệu hóa):** Hộp kiểm này có thể được chọn để vô hiệu hóa Thành phần Lương này. Một Thành phần Lương bị vô hiệu hóa không thể được sử dụng trong Cơ cấu Lương.

### 2.3 Phúc lợi linh hoạt

Phần này được hiển thị nếu Thành phần Lương là một Thành phần Thu nhập. Các kế hoạch Phúc lợi linh hoạt cho phép nhân viên hưởng các phúc lợi mà họ muốn hoặc cần từ một gói chương trình do người sử dụng lao động cung cấp. Chúng có thể bao gồm bảo hiểm y tế, kế hoạch hưu trí, chi phí điện thoại, v.v. Để thiết lập một Thành phần Lương là Phúc lợi linh hoạt, hãy tích vào hộp kiểm 'Is Flexible Benefit'.

<img class="screenshot" alt="Flexible Benefit" src="https://docs.erpnext.com/docs/v16/assets/img/human-resources/flexible-ben.png">

Nhập số tiền tối đa hàng năm cho phúc lợi linh hoạt này vào trường 'Max Benefit Amount (Yearly)' (Số tiền phúc lợi tối đa hàng năm). Một số thuộc tính bổ sung của Phúc lợi linh hoạt có thể được bật bằng cách sử dụng các hộp kiểm như sau:

* **Pay Against Benefit Claim (Thanh toán theo yêu cầu phúc lợi):** Bật hộp kiểm này nếu bạn muốn thanh toán phúc lợi này thông qua [Yêu cầu phúc lợi của nhân viên](/docs/v16/user/manual/en/human-resources/employee-benefit-claim).
* **Only Tax Impact (Cannot Claim But Part of Taxable Income) (Chỉ ảnh hưởng thuế - Không thể yêu cầu nhưng là một phần của thu nhập chịu thuế):** Nếu được thiết lập, phúc lợi này sẽ không được thanh toán trực tiếp cho nhân viên nhưng sẽ được tính vào thu nhập chịu thuế của họ.