<!-- add-breadcrumbs -->
# Cập nhật hàng loạt

**Cập nhật hàng loạt cho phép bạn cập nhật một trường cụ thể của một DocType cho tất cả các tài liệu.**

Để truy cập Cập nhật hàng loạt, hãy đi tới:
> Trang chủ > Cài đặt > Cập nhật hàng loạt

Giả sử bạn có 20 báo giá mà trong đó bạn đã chọn 'Tất cả khu vực' và bây giờ bạn muốn đổi Khu vực thành Pháp. Thay vì cập nhật từng báo giá một cách thủ công, bạn có thể sử dụng Cập nhật hàng loạt để cập nhật tất cả 20 Báo giá cùng một lúc.

Để thực hiện việc này,

1. Đi tới **Cập nhật hàng loạt**.
1. Chọn **DocType**, ví dụ như **Báo giá**.
1. Chọn **Trường** cần cập nhật, ví dụ như **Khu vực**.
1. Nhập giá trị mới **hợp lệ** cần được cập nhật.
1. Nhập bất kỳ điều kiện nào áp dụng, ví dụ: `status="Draft"` sẽ chỉ ảnh hưởng đến các tài liệu ở trạng thái Nháp.
1. Chọn giới hạn, tức là số lượng tài liệu (Báo giá) cần được cập nhật.
1. Nhấp vào **Cập nhật**.

    ![Bulk Update](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/bulk-update.png)

> [!IMPORTANT]
> Bạn chỉ có thể cập nhật các trường có thể được cập nhật bình thường trong một giai đoạn cụ thể. Ví dụ: Ngày có hiệu lực không thể được cập nhật đối với các Báo giá đã được **Xác nhận**.

### Các chủ đề liên quan
1. [Đổi tên hàng loạt](../user/manual/en/setting-up/settings/bulk-rename.md)