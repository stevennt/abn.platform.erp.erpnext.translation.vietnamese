# Loại nghỉ phép

**Loại nghỉ phép đề cập đến các loại nghỉ phép được phân bổ cho Nhân viên mà họ có thể sử dụng khi thực hiện Đơn xin nghỉ phép.**


Bạn có thể tạo bất kỳ số lượng Loại nghỉ phép nào dựa trên yêu cầu của công ty mình.

Để truy cập Loại nghỉ phép, hãy đi tới:

> Home > Human Resources > Leaves > Leave Type

## 1. Cách tạo Loại nghỉ phép

1. Đi tới danh sách Loại nghỉ phép, nhấn vào Mới.
1. Nhập Tên Loại nghỉ phép.
1. Nhập Số ngày nghỉ tối đa cho phép, Áp dụng sau (Ngày làm việc), Số ngày tối đa liên tục có thể áp dụng (tùy chọn).
1. Lưu.

    <img class="screenshot" alt="New Leave Type"
    src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/new-leave-type.png">

Dưới đây là giải thích chi tiết về tất cả các trường và ô kiểm trong Loại nghỉ phép.

* **Max Leaves Allowed (Số ngày nghỉ tối đa cho phép):** Trường này cho phép bạn thiết lập số lượng tối đa của phân bổ hàng năm cho Loại nghỉ phép này khi tạo Chính sách nghỉ phép.

* **Applicable After (Working Days) (Áp dụng sau (Ngày làm việc)):** Nhập số ngày làm việc tối thiểu tại đây. Chỉ những nhân viên đã làm việc đủ số ngày này trở lên mới được phép đăng ký loại nghỉ phép cụ thể này. Bất kỳ loại nghỉ phép nào khác (như Nghỉ phép thông thường, Nghỉ ốm, v.v.) mà Nhân viên đã sử dụng sau ngày gia nhập cũng sẽ được xem xét khi tính toán số ngày làm việc của Nhân viên.

* **Maximum Continuous Days Applicable (Số ngày tối đa liên tục có thể áp dụng):** Đề cập đến số ngày tối đa mà Loại nghỉ phép cụ thể này có thể được sử dụng liên tục. Nếu một nhân viên vượt quá số ngày tối đa, kỳ nghỉ kéo dài của họ sẽ được coi là 'Nghỉ không lương'.

* **Is Carry Forward (Có chuyển sang kỳ sau):** Nếu được chọn, số ngày nghỉ còn lại của Loại nghỉ phép này sẽ được chuyển sang kỳ phân bổ tiếp theo.

* **Is Leave Without Pay (Là nghỉ không lương):** Điều này đảm bảo rằng Loại nghỉ phép sẽ được xử lý là nghỉ không lương và lương sẽ bị khấu trừ cho Loại nghỉ phép này.

* **Is Optional (Là tùy chọn):** Nghỉ phép tùy chọn là những ngày nghỉ mà Nhân viên có thể chọn sử dụng từ danh sách các ngày nghỉ do công ty công bố. Danh sách ngày nghỉ cho Nghỉ phép tùy chọn có thể có bất kỳ số lượng ngày nghỉ nào, nhưng bạn có thể giới hạn số lượng nghỉ phép đó bằng cách thiết lập trường Max Days Leave Allowed.

* **Allow Negative Balance (Cho phép số dư âm):** Nếu được chọn, hệ thống sẽ luôn cho phép đăng ký và phê duyệt [Leave Applications](leave-application.md) cho Loại nghỉ phép, ngay cả khi không còn số dư ngày nghỉ.

* **Include holidays within leaves as leaves (Tính ngày lễ trong kỳ nghỉ là ngày nghỉ):** Chọn tùy chọn này nếu bạn muốn tính các ngày lễ nằm trong kỳ nghỉ là một 'ngày nghỉ'. Ví dụ: nếu một Nhân viên xin nghỉ vào Thứ Sáu và Thứ Hai, trong khi Thứ Bảy và Chủ Nhật là ngày nghỉ hàng tuần, nếu ô 'Include holidays within leaves as leaves' của Loại nghỉ phép được chọn, hệ thống sẽ coi Thứ Bảy và Chủ Nhật cũng là ngày nghỉ. Những ngày lễ như vậy sẽ được khấu trừ vào tổng số ngày nghỉ.

* **Is Compensatory (Là nghỉ bù):** Nghỉ bù là các ngày nghỉ được cấp khi làm việc tăng ca hoặc vào ngày lễ, thông thường được bù đắp dưới dạng nghỉ phép có thể quy đổi thành tiền. Bạn có thể chọn tùy chọn này để đánh dấu Loại nghỉ phép là nghỉ bù. Nhân viên có thể yêu cầu nghỉ bù bằng cách sử dụng [Compensatory Leave Request](compensatory-leave-request.md).

> Được giới thiệu trong phiên bản 13

* **Is Partially Paid Leaves (Là nghỉ có hưởng một phần lương):** Ô kiểm này đảm bảo rằng Loại nghỉ phép sẽ được xử lý là nghỉ có hưởng một phần lương và một phần thu nhập hàng ngày sẽ được thanh toán thông qua phiếu lương. Nếu ô kiểm này được bật, trường "Fraction of Daily Salary Per Leave" (Tỷ lệ lương hàng ngày mỗi ngày nghỉ) sẽ xuất hiện, nơi bạn có thể xác định tỷ lệ lương hàng ngày được trả cho ngày nghỉ một phần đó.

    <img class="screenshot" alt="New Leave Type"
    src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/is-partially-paid-leaves.png">

> **Lưu ý:** Loại nghỉ phép có thể là Nghỉ không lương hoặc Nghỉ có hưởng một phần lương.

## 2. Các tính năng

### 2.1 Quy đổi nghỉ phép thành tiền

Có khả năng Nhân viên có thể nhận tiền mặt từ Người sử dụng lao động cho những ngày nghỉ chưa sử dụng được cấp cho họ trong một Kỳ nghỉ phép. Không phải tất cả các Loại nghỉ phép đều cần được quy đổi thành tiền, vì vậy, bạn chỉ nên thiết lập "Allow Encashment" (Cho phép quy đổi thành tiền) cho những Loại nghỉ phép nào có thể quy đổi.

> **Lưu ý:** Việc quy đổi nghỉ phép thành tiền chỉ được phép thực hiện vào tháng cuối cùng của Kỳ nghỉ phép.

<img class="screenshot" alt="Leave Encashment"
        src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/leave-encashment.png">

**Encashment Threshold Days (Số ngày ngưỡng quy đổi):** Trường này cho biết số ngày nghỉ mà Nhân viên sẽ không thể quy đổi thành tiền. Trên số ngày đã nêu, Nhân viên đủ điều kiện để quy đổi ngày nghỉ thành tiền.

Ví dụ: nếu có 10 ngày nghỉ của một Loại nghỉ phép cụ thể có thể quy đổi, và Nhân viên còn lại 8 ngày nghỉ. Nếu Encashment Threshold Days = 5, Nhân viên chỉ được quy đổi 8 - 5 = 3 ngày nghỉ.

**Earning Component (Thành phần thu nhập):** Trường này cho phép bạn chỉ định Thành phần Lương sẽ được quy đổi cho Nhân viên như một phần của Lương trong Phiếu lương.

> **Lưu ý:** Khi Xác nhận [Leave Encashment](leave-encashment.md) cho một Nhân viên, ERPNext sẽ tự động tạo một [Additional Salary](additional-salary.md) (Lương bổ sung) để được cộng vào Phiếu lương của Nhân viên khi xử lý bảng lương tiếp theo.

### 2.2 Nghỉ phép hưởng lương (Earned Leave)

Nghỉ phép hưởng lương là những ngày nghỉ mà Nhân viên tích lũy được sau khi làm việc cho công ty trong một khoảng thời gian nhất định. Việc chọn "Is Earned Leave" sẽ phân bổ ngày nghỉ theo tỷ lệ bằng cách tự động cập nhật Phân bổ nghỉ phép cho các loại nghỉ này theo các khoảng thời gian được thiết lập bởi 'Earned Leave Frequency'.


Ví dụ: Một Nhân viên được phân bổ 24 ngày Nghỉ phép đặc biệt trong một năm, trong đó Nghỉ phép đặc biệt được thiết lập là Nghỉ phép hưởng lương với phân bổ hàng tháng. Trong trường hợp này, Nhân viên sẽ được hưởng 2 (24 ngày/12 tháng) ngày Nghỉ phép đặc biệt vào cuối mỗi tháng. Quy trình phân bổ nghỉ phép (tác vụ chạy ngầm) sẽ chỉ phân bổ ngày nghỉ dựa trên số ngày nghỉ tối đa cho loại nghỉ phép đó và sẽ làm tròn theo 'Rounding' đối với các phần lẻ.

<img class="screenshot" alt="Earned Leave"
        src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/earned-leave.png">

> **Lưu ý:** Việc phân bổ ban đầu của th