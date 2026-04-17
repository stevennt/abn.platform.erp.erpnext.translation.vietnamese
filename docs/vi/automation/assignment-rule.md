<!-- add-breadcrumbs -->

# Quy tắc phân công

> Được giới thiệu trong Phiên bản 12

**Quy tắc phân công cho phép bạn thiết lập việc tự động phân công các chứng từ cho Người dùng.**

Để phân công các phiếu hỗ trợ (support tickets) một cách tự động giữa các nhân viên làm việc tại bộ phận hỗ trợ, bạn có thể sử dụng Quy tắc phân công.

Để truy cập Quy tắc phân công, hãy đi tới:
> Home > Settings > Assignment Rule

## 1. Cách tạo Quy tắc phân công
Để thiết lập việc phân công tự động:

1. Đi tới danh sách Quy tắc phân công, nhấn vào Mới.
1. Chọn DocType mà bạn muốn phân công tự động (ví dụ: **Issue**).
1. Viết "Description" (Mô tả) sẽ được thêm vào To Do.
1. Chọn điều kiện để phân công.
    Bạn có thể viết các biểu thức Python đơn giản để phân công tự động trong `Assign Rule`, `Close Rule` và `Unassign Rule`. Bạn sẽ có quyền truy cập vào tất cả các thuộc tính của chứng từ và có thể sử dụng các toán tử như >, <, ==, v.v. cũng như nhiều điều kiện như `and` và `or`.

    Ví dụ:

    - `status == "Open"`
    - `issue_type == "Technical" and priority=="High" and status == "Open"`

1. Chọn quy tắc phân công.

    ![Assignment Rule](https://docs.erpnext.com/docs/v13/assets/img/automation/assignment-rule-select.png)

    * **Round Robin**: Phân công mỗi chứng từ cho một Người dùng theo thứ tự tuần tự.
    * **Load Balancing**: Phân công các chứng từ mới cho Người dùng có số lượng công việc được phân công ít nhất.

        Chọn danh sách Người dùng mà Quy tắc phân công này sẽ áp dụng:
        ![Users in Assignment Rule](https://docs.erpnext.com/docs/v13/assets/img/automation/auto-assign-2.png)

    * **Based on Field**: Được giới thiệu trong v13, quy tắc này có thể được sử dụng để phân công một chứng từ cho Người dùng được thiết lập trong trường đã cấu hình.

        Chọn trường liên kết Người dùng (User link field) để xác định Quy tắc phân công này sẽ áp dụng cho ai:
        ![Field Assign](https://docs.erpnext.com/docs/v13/assets/img/automation/field-auto-assign.png)


1. Lưu.

Bạn có thể sử dụng các thuộc tính của chứng từ trong trường Description để trở thành một phần của nội dung phân công. Các Quy tắc phân công có 'Priority' (Độ ưu tiên) cao hơn sẽ được áp dụng trước.

Ví dụ:

Issue có độ ưu tiên cao *File Upload not working* đã được phân công cho bạn.

### 1.1 Nhiều Quy tắc phân công

Bạn cũng có thể thiết lập nhiều quy tắc phân công tự động cho mỗi DocType, quy tắc nào có Priority cao nhất sẽ được áp dụng trước.

![Assignment Rule with Higher Priority](https://docs.erpnext.com/docs/v13/assets/img/automation/assignment-rule-with-higher-priority.png)


assignment-rule-with-higher-priority

### 1.2 Thiết lập Hạn chót cho việc phân công

Bạn có thể tự động thiết lập hạn chót cho các việc được phân công dựa trên trường ngày tháng trong chứng từ tham chiếu.

Ví dụ:

Nếu bạn muốn thiết lập hạn chót cho việc phân công Issue dựa trên ngày "Resolution By" của Issue đó, bạn có thể thực hiện bằng cách chọn trường "Resolution By" trong tùy chọn `Due Date Based On` trong Quy tắc phân công.

![Due Date Based On](https://docs.erpnext.com/docs/v13/assets/img/automation/assignment-rule-due-date-based-on.png)

**Lưu ý:**

- Tùy chọn "Due Date Based On" sẽ không khả dụng nếu "Document Type" chưa được chọn hoặc nếu DocType được chọn không có bất kỳ trường "Date" hoặc "Datetime" nào.
- Hạn chót (Due Date) trong việc phân công/ToDo sẽ được cập nhật bất cứ khi nào giá trị của trường "Due Date Based On" được cập nhật trong chứng từ tham chiếu.

### 2. Các chủ đề liên quan

1. [Workflows](/docs/v13/user/manual/en/setting-up/workflows)
1. [Workflow Actions](/docs/v13/user/manual/en/setting-up/workflow-actions)

{next}