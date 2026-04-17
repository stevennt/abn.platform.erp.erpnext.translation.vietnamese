<!-- add-breadcrumbs -->
# Thiết lập Khấu trừ Thuế thu nhập

Việc tính toán các khoản khấu trừ thuế cho nhân viên hàng tháng là một hoạt động tốn thời gian đối với hầu hết các doanh nghiệp, đặc biệt là đối với các doanh nghiệp lớn. Nếu được thiết lập đúng cách, ERPNext sẽ đơn giản hóa hầu hết các tính toán liên quan đến thuế bằng cách tự động tính toán các khoản khấu trừ thuế trong khi lập Phiếu lương. Dưới đây là cách bạn có thể cấu hình ERPNext để giúp quá trình xử lý bảng lương trở nên dễ dàng hơn.

# Miễn thuế thu nhập

Ở nhiều quốc gia, các quy định cho phép miễn một phần (hoặc toàn bộ) một số loại chi tiêu của cá nhân để không bị cộng vào thu nhập chịu thuế hàng năm của họ. Ví dụ về các loại chi tiêu này có thể là đóng góp cho các tổ chức từ thiện, số tiền chi cho giáo dục con cái, các khoản đầu tư cụ thể, v.v. Để được hưởng mức miễn trừ từ thu nhập chịu thuế, các cá nhân được yêu cầu nộp bằng chứng cho các khoản chi tiêu đó.

ERPNext cho phép bạn cấu hình các Bậc thuế thu nhập và thuế được tính toán dựa trên thu nhập dự kiến hàng năm của nhân viên. Vì lý do này, nhân viên được yêu cầu khai báo số tiền miễn trừ mà họ dự định yêu cầu vào đầu năm tài chính để các khoản khấu trừ thuế trong bảng lương sẽ được tính toán dựa trên thu nhập dự kiến hàng năm trừ đi khoản miễn trừ. Nhân viên có thể khai báo điều này thông qua [Khai báo miễn thuế cho nhân viên](../human-resources/employee-tax-exemption-declaration).

Nếu nhân viên không nộp bản khai báo, các khoản khấu trừ hàng tháng sẽ được tính toán mà không có bất kỳ khoản miễn trừ nào từ thu nhập hàng năm của nhân viên. Tuy nhiên, nếu nhân viên nộp bản khai báo trong giữa kỳ lương, khoản miễn thuế sẽ được áp dụng từ kỳ lương tiếp theo trở đi. Bất kỳ khoản thuế bổ sung nào đã thu trong các kỳ lương trước sẽ được điều chỉnh vào kỳ lương cuối cùng hoặc khi sử dụng tùy chọn *Deduct Tax For Unsubmitted Tax Exemption Proof* trong Bút toán lương hoặc Phiếu lương.

Ngoài ra, vào cuối năm, nhân viên nộp bằng chứng thực tế về các khoản chi tiêu để kê khai thông qua [Nộp bằng chứng miễn thuế cho nhân viên](../human-resources/employee-tax-exemption-proof-submission). Trong kỳ lương cuối cùng của Kỳ lương, ERPNext sẽ kiểm tra việc nộp bằng chứng của nhân viên, và nếu không tìm thấy, thuế cho phần thu nhập được miễn sẽ được cộng vào thành phần khấu trừ tiêu chuẩn.

### Danh mục miễn thuế cho nhân viên
Các khoản miễn trừ từ lương chịu thuế thường bị giới hạn trong các danh mục chi tiêu cụ thể do chính phủ hoặc các cơ quan quản lý quyết định. ERPNext cho phép bạn cấu hình các danh mục khác nhau được phép miễn trừ.

Bạn có thể cấu hình Danh mục miễn thuế cho nhân viên bằng cách đi tới:
> Human resources > Payroll Setup > Employee Tax Exemption Category > New Employee Tax Exemption Category

<img class="screenshot" alt="Employee Tax Exemption Category" src="https://docs.erpnext.com/docs/v16/assets/img/human-resources/employee-tax-exemption-category.png">

### Danh mục phụ miễn thuế cho nhân viên
Dưới mỗi danh mục, có thể có nhiều mục mà các khoản miễn trừ được cho phép. Ví dụ, dưới danh mục 80C có thể là Phí bảo hiểm nhân thọ.

Bạn có thể cấu hình Danh mục phụ miễn thuế cho nhân viên bằng cách đi tới:
> Human resources > Payroll Setup > Employee Tax Exemption Sub Category > New Employee Tax Sub Exemption Category

<img class="screenshot" alt="Employee Tax Exemption Sub Category" src="https://docs.erpnext.com/docs/v16/assets/img/human-resources/employee-tax-exemption-subcategory.png">

### Miễn thuế HRA
Đối với một số khu vực và quy định cụ thể, khoản miễn thuế Phụ cấp thuê nhà (HRA) từ thu nhập chịu thuế được tính dựa trên các mức thấp nhất trong các mức sau:
 * Số tiền thực tế được người sử dụng lao động phân bổ làm HRA.
 * Tiền thuê nhà thực tế trả trừ đi 10% lương cơ bản.
 * 50% lương cơ bản, nếu nhân viên đang ở tại một thành phố lớn (40% đối với thành phố không phải là thành phố lớn).

 Là một phần của Khai báo miễn thuế cho nhân viên, nhân viên cũng sẽ điền thông tin Miễn thuế HRA. ERPNext sẽ tính toán mức miễn trừ đủ điều kiện cho HRA và miễn trừ nó khi tính toán thu nhập chịu thuế.

 > Lưu ý: Thành phần lương Cơ bản và HRA phải được cấu hình trong Công ty để việc miễn thuế HRA hoạt động chính xác.

### Các tùy chọn trong Bút toán lương và Phiếu lương
ERPNext đơn giản hóa quá trình xử lý lương bằng cách tự động xử lý lương hàng loạt thông qua [Bút toán lương](../human-resources/payroll-entry).

* **Deduct Tax For Unclaimed Employee Benefits**: Các phúc lợi linh hoạt (các Thành phần lương được đánh dấu là *Is Flexible Benefit*) không được bao gồm trong thu nhập chịu thuế của nhân viên. Tuy nhiên, số tiền nhận được cho các thành phần này sẽ được bao gồm trong thu nhập chịu thuế của nhân viên nếu nhân viên không nộp [Yêu cầu phúc lợi nhân viên](../human-resources/employee-benefit-claim) khi tính thuế trong kỳ lương cuối cùng của Kỳ lương.

Nếu bạn muốn thu thuế cho các phúc lợi trước kỳ lương cuối cùng, hãy chọn tùy chọn này và ERPNext sẽ tính toán lại thuế và cộng thêm thuế cho tất cả các phúc lợi chưa bị đánh thuế khi lập Phiếu lương.

* **Deduct Tax For Unsubmitted Tax Exemption Proof**: Tùy chọn này cho phép bạn khấu trừ thuế cho các khoản thu nhập đã được miễn trong các kỳ lương trước như đã khai báo trong [Khai báo miễn thuế cho nhân viên](../human-resources/employee-tax-exemption-declaration) nhưng nhân viên chưa nộp đủ bằng chứng thông qua [Nộp bằng chứng miễn thuế cho nhân viên](../human-resources/employee-tax-exemption-proof-submission). Cần lưu ý rằng nếu tùy chọn này được chọn, ERPNext sẽ không xem xét Bản khai báo miễn thuế của nhân viên mà sẽ chỉ tính đến việc *Nộp bằng chứng miễn thuế cho nhân viên* khi tính toán khoản miễn trừ từ thu nhập hàng năm của nhân viên.

> Lưu ý: Nếu cần, bạn vẫn có thể điều chỉnh thủ công các khoản thuế này trong Phiếu lương.