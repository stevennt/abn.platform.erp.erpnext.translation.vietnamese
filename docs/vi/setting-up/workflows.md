<!-- add-breadcrumbs -->
# Quy trình công việc (Workflows)

**Với Quy trình công việc, bạn có thể thiết lập lại cách một quy trình/luồng công việc cụ thể được phê duyệt trong ERPNext.**

Bạn có thể thiết lập nhiều cấp độ phê duyệt cho một Quy trình công việc trong ERPNext. Để cho phép nhiều người thực hiện nhiều yêu cầu, hoặc để nhiều người dùng phê duyệt, ERPNext yêu cầu bạn phải điền các Điều kiện Quy trình công việc (Workflow conditions).
ERPNext sẽ theo dõi các quyền hạn khác nhau trước khi Xác nhận.

Hãy xem xét một kịch bản, nơi cần có nhiều cấp độ phê duyệt cho một Báo giá. Một nhân viên bán hàng (người dùng có vai trò 'Sales User') sẽ tạo một báo giá. Sau đó, nó sẽ được phê duyệt hoặc từ chối bởi một trưởng nhóm bán hàng (người dùng có vai trò 'Sales Manager'). Nếu được trưởng nhóm bán hàng phê duyệt, nó sẽ tiếp tục được phê duyệt hoặc từ chối bởi quản lý khu vực (người dùng có vai trò 'Regional Manager').

Để tạo một Quy trình công việc và các quy tắc chuyển đổi, hãy đi tới:

> Home > Settings > Workflow

Sau khi một Quy trình công việc được tạo, bạn có thể thực hiện các hành động trên đó thông qua [Workflow Actions](/docs/v13/user/manual/en/setting-up/workflow-actions).

## 1. Điều kiện tiên quyết
Trước khi tạo một Quy trình công việc, bạn nên tạo các thành phần này trước:

* [Workflow Actions](/docs/v13/user/manual/en/setting-up/workflow-actions)
* Các Trạng thái Quy trình công việc (Workflow States) như Đã phê duyệt (Approved), Đã hủy (Canceled), v.v.

## 2. Cách tạo một Quy trình công việc
1. Đi tới danh sách Workflow, nhấn vào New.
1. Nhập tên cho **Workflow** và chọn DocType mà quy trình sẽ được áp dụng.
1. Nhập các trạng thái khác nhau của Quy trình công việc. Nhập Trạng thái tài liệu (Doc Status) cho chúng, chọn trường nào sẽ được cập nhật từ cột Update Field, và nhập giá trị sẽ được cập nhật tại mục Update Value.

    Các Trạng thái Quy trình công việc có thể có màu sắc khác nhau tùy theo trạng thái. Ví dụ: Màu xanh lá cây cho thành công. Trạng thái tài liệu: Saved = 0, Submitted = 1, Cancelled = 2.

    ![Workflow](https://docs.erpnext.com/docs/v13/assets/img/setup/workflow.png)

1. Nhập các Quy tắc chuyển đổi (Transition Rules).

    ![Workflow Transition Rules](https://docs.erpnext.com/docs/v13/assets/img/setup/workflow-transition-rules.png)

### 2.2 Những điều cần lưu ý khi tạo Quy trình công việc

* Việc tạo một Quy trình công việc trong ERPNext về cơ bản sẽ ghi đè lên quy trình Lưu (Save) và Xác nhận (Submit) thông thường. Do đó, tài liệu sẽ hoạt động dựa trên Quy trình công việc của bạn chứ không dựa trên quy trình mã nguồn được thiết lập sẵn. Vì vậy, có thể sẽ không có nút hoặc tùy chọn Xác nhận (Submit) nếu bạn không chỉ định nó trong Quy trình công việc mà bạn tạo.

    Nếu bạn không áp dụng Quy trình công việc cho một tài liệu, và tài liệu đó có thể Xác nhận (submittable), thì nó sẽ có quy trình mặc định với các trạng thái: Nháp (Draft) - Đã Xác nhận (Submitted) - Đã Hủy (Cancelled). Nếu bạn đang áp dụng một Quy trình công việc cho một tài liệu có thể Xác nhận, thì những trạng thái mặc định đó phải được người dùng xử lý.

* Một tài liệu không thể bị hủy trừ khi nó đã được Xác nhận.

* Nếu bạn muốn cung cấp tùy chọn để hủy, bạn sẽ phải viết một bước chuyển đổi quy trình (workflow transition step) cho phép từ trạng thái đã Xác nhận (submitted) có thể Hủy (cancel).

* Nếu các trường trong cột Update Field không được cập nhật, một trường tùy chỉnh mới sẽ được tạo với tên mà bạn đã thiết lập trong trường 'Workflow State Field'.

### 2.3 Các tùy chọn khác cho Quy trình công việc
1. Is Active: Khi tích vào đây, tất cả các Quy trình công việc khác cho DocType đã chọn sẽ trở nên không hoạt động.
1. Don't Override Status: Trạng thái của Quy trình công việc này sẽ không ghi đè lên trạng thái của tài liệu (Báo giá) trong danh sách xem.
1. Send Email Alerts: Email sẽ được gửi đến người dùng với các hành động quy trình công việc tiếp theo có thể thực hiện.

## 3. Các tính năng

### 3.1 Bật/Tắt Trạng thái Quy trình công việc không bắt buộc (Optional Workflow State)

> Được giới thiệu trong Phiên bản 12

Trong phần Trạng thái (States), trạng thái Quy trình công việc không bắt buộc có nghĩa là trạng thái đó có thể không phải là một phần của quá trình phê duyệt cuối cùng.

Ví dụ: các trạng thái như Đã hủy (Canceled) hoặc Từ chối (Rejected) có thể là không bắt buộc.
![Optional State](https://docs.erpnext.com/docs/v13/assets/img/setup/workflow-optional-state.png)

**Lưu ý:** Các Workflow Actions không được tạo cho các trạng thái không bắt buộc.

### 3.2 Điều kiện (Conditions)


Bạn cũng có thể thêm một điều kiện để Quy tắc chuyển đổi (Transition) có hiệu lực. Ví dụ, trong trường hợp này, nếu nhân viên kinh doanh tạo một báo giá với tổng cộng (grand total) từ $100,000 trở lên, một vai trò cụ thể phải phê duyệt. Để điều này xảy ra trong bước chuyển đổi cụ thể, bạn có thể thiết lập thuộc tính cho **Condition**:

```
doc.grand_total <= 100000
```
Ở đây, `grand_total` là tên trường của trường 'Grand Total' trong Báo giá. Để xem tên trường của một trường, hãy đi tới Menu > Customize.

Điều này có thể mở rộng cho bất kỳ thuộc tính nào của tài liệu.

> Được giới thiệu trong Phiên bản 13

Trong Phiên bản 13, bạn có thể sử dụng các hàm ngày/giờ (date/time), session, get_value và get_list trong các biểu thức điều kiện của mình.

Các hàm được cho phép:

* frappe.db.get_value
* frappe.db.get_list
* frappe.session
* frappe.utils.now_datetime
* frappe.utils.get_datetime
* frappe.utils.add_to_date
* frappe.utils.now

Ví dụ:

```
doc.creation > frappe.utils.add_to_date(frappe.utils.now_datetime(), days=-5, as_string=True, as_datetime=True)
```

## 4. Ví dụ về Quy trình phê duyệt Báo giá

Khi một báo giá được lưu bởi nhân viên bán hàng, trạng thái của tài liệu sẽ chuyển sang "Nháp" (Draft) và khi nhấn vào Xác nhận (submit), trạng thái sẽ chuyển sang 'Chờ Quản lý bán hàng phê duyệt' (Approval Pending By Sales Manager):

![Workflow State in Transaction](https://docs.erpnext.com/docs/v13/assets/img/setup/workflow-status-in-transaction.png)

Khi Quản lý bán hàng đăng nhập, họ có thể Phê duyệt (Approve) hoặc Từ chối (Reject). Nếu được phê duyệt, trạng thái của tài liệu sẽ chuyển sang "Chờ Quản lý khu vực phê duyệt" (Approval Pending By Regional Manager).

![Workflow Action Options](https://docs.erpnext.com/docs/v13/assets/img/setup/workflow-action-options.png)

Khi Quản lý khu vực mở báo giá, họ có thể thực hiện bước cuối cùng là "Phê duyệt" (Approve) hoặc "Từ chối" (Reject) nó.

![Workflow Action Options](https://docs.erpnext.com/docs/v13/assets/img/setup/workflow-action-options-2.png)

## 5. Video
<div>
    <div class="embed-container">
        <iframe src="https://www.youtube.com/embed/yObJUg9FxFs?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
        </iframe>
    </div>
</div>

### 6. Các chủ đề liên quan
1. [Workflow Actions](/docs/v13/user/manual/en/setting-up/workflow-actions)
1. [Assignment Rule](/docs/v13/user/manual/en/automation/assignment-rule)