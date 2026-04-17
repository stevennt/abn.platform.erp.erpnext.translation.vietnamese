# Tính toán Nghỉ phép trong Phiếu lương

Có hai loại nghỉ phép mà người dùng có thể đăng ký.

* **Nghỉ phép có lương** (Nghỉ ốm, Nghỉ phép năm, Nghỉ phép đột xuất, v.v.)
* **Nghỉ không lương**

Nghỉ phép có lương trước tiên sẽ được Quản lý nhân sự phân bổ. Khi Nhân viên tạo Đơn xin nghỉ phép, số ngày nghỉ được phân bổ cho họ sẽ bị trừ đi. Những ngày nghỉ này không ảnh hưởng đến Phiếu lương của nhân viên.

Khi Nhân viên hết ngày nghỉ phép có lương, họ sẽ tạo Đơn xin nghỉ phép cho việc nghỉ không lương. Thuật ngữ được sử dụng cho nghỉ không lương trong ERPNext là Leave Without Pay (LWP). Những ngày nghỉ này có ảnh hưởng đến Phiếu lương của Nhân viên.

<div class="well">
Việc chỉ đánh dấu Vắng mặt trong bản ghi Chấm công sẽ không ảnh hưởng đến việc tính lương của Nhân viên, vì sự vắng mặt đó có thể là do nghỉ phép có lương. Do đó, cần phải tạo Đơn xin nghỉ phép trong trường hợp vắng mặt. Hãy xem xét một kịch bản để hiểu cách các ngày nghỉ ảnh hưởng đến Phiếu lương của nhân viên.
</div>

### Kịch bản thiết lập

1. **Thiết lập Nhân viên:** Tạo hồ sơ nhân viên trong hệ thống.
2. **Phân bổ nghỉ phép:** Phân bổ các ngày nghỉ phép có lương cho nhân viên đó.
3. **Cấu trúc lương:** Tạo Cấu trúc lương cho Nhân viên đó. Trong bảng Thu nhập và Khấu trừ, hãy chọn thành phần lương nào sẽ bị ảnh hưởng nếu Nhân viên nghỉ LWP.
4. **Danh sách ngày nghỉ:** Tạo Danh sách ngày nghỉ (nếu có), và liên kết nó với hồ sơ Nhân viên.

**Ngày làm việc:** Ngày làm việc trong Phiếu lương được tính dựa trên số ngày đã chọn ở trên. Nếu bạn không muốn tính ngày lễ vào Ngày làm việc, bạn nên thực hiện cài đặt sau:

> Human Resource > Setup > HR Setting

Bỏ chọn trường **"Include Holidays in Total No. of Working Days"**

Ngày lễ được tính dựa trên Danh sách ngày nghỉ được đính kèm với hồ sơ Nhân viên.

**Nghỉ không lương:** Nghỉ không lương được cập nhật dựa trên Đơn xin nghỉ phép được tạo cho Nhân viên này, trong tháng mà Phiếu lương được tạo, và có Loại nghỉ phép là "Leave Without Pay".

**Ngày thanh toán:** Dưới đây là cách tính Ngày thanh toán:

$$\text{Ngày thanh toán} = \text{Ngày làm việc} - \text{Nghỉ không lương}$$

Nếu bạn đã tích chọn LWP cho Thành phần lương, Số tiền sẽ bị giảm dựa trên số ngày LWP của Nhân viên trong tháng đó.