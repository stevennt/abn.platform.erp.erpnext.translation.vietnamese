<!-- add-breadcrumbs -->
# Lỗi Cấp độ Quyền (Perm Level) trong Permission Manager

Trong khi tùy chỉnh các quy tắc trong [Permission Manager](/docs/v13/user/manual/en/setting-up/users-and-permissions/role-based-permissions), bạn có thể nhận được thông báo lỗi như sau:

> For System Manager _(or any other role)_ at level 2 _(or another level)_ in Customer _(or any other document)_ in row 8: Permission at level 0 must be set before higher levels are set.
> (Dịch: Đối với System Manager _(hoặc bất kỳ vai trò nào khác)_ ở cấp độ 2 _(hoặc cấp độ khác)_ trong Customer _(hoặc bất kỳ tài liệu nào khác)_ tại dòng 8: Quyền ở cấp độ 0 phải được thiết lập trước khi thiết lập các cấp độ cao hơn.)

Thông báo lỗi cho thấy vấn đề nằm ở thiết lập quyền hiện có cho tài liệu này.

Đối với bất kỳ vai trò nào, trước khi gán quyền ở Cấp độ Quyền (Perm Level) 1 hoặc 2 (và các cấp độ tiếp theo), quyền ở Cấp độ Quyền 0 phải được gán trước. Thông báo lỗi cho biết System Manager đã được gán quyền ở Cấp độ Quyền 1 và 2, nhưng chưa được gán ở cấp độ 0. Bạn nên khắc phục quyền cho vai trò System Manager trước bằng cách:

- Gán quyền cho System Manager ở cấp độ 0.

    Hoặc

- Xóa bỏ quyền ở cấp độ 1 và 2.

Sau khi thực hiện một trong các bước trên, bạn sẽ có thể thêm thành công các quy tắc quyền mới trong Role Permission Manager.

{next}

<!-- markdown -->