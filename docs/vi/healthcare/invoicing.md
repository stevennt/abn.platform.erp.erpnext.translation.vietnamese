<!-- add-breadcrumbs -->
# Lập hóa đơn

Lập hóa đơn là một phần không thể thiếu của bất kỳ hoạt động kinh doanh nào và ERPNext Healthcare thực hiện điều này bằng cách sử dụng tài liệu `Sales Invoice` trong phân hệ Kế toán của ERPNext.

Phân hệ Y tế liên kết tài liệu Bệnh nhân với `Customer` và tất cả các dịch vụ có thể tính phí như Xét nghiệm, Thủ thuật lâm sàng, Phí tư vấn, v.v. với tài liệu `Item` _(với tùy chọn Maintain Stock được đặt thành false)_. Bạn cũng có thể thiết lập các liên kết này một cách thủ công.

`Sales Invoice` đã có sẵn nút `Get Items` giúp Người dùng lấy danh sách các Mặt hàng từ các tài liệu liên quan khác. ERPNext Healthcare mang đến thêm hai tùy chọn nữa tại đây để lấy tất cả các dịch vụ chưa được lập hóa đơn cho Bệnh nhân cũng như các loại thuốc được kê đơn từ Patient Encounter. Bằng cách này, người lập hóa đơn có thể lấy tất cả các dịch vụ có thể tính phí cũng như thuốc mà không cần phải có quyền truy cập vào Patient Encounter hay chính phân hệ Y tế.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v13/assets/img/healthcare/get_items.png">

> Lưu ý: Tất cả các giao dịch của một Bệnh nhân được ghi nhận cho `Customer` mà bệnh nhân đó được liên kết. Bạn có thể muốn tra cứu các Báo cáo Kế toán khác nhau có sẵn trong phân hệ Kế toán của ERPNext (như Phải thu khách hàng) bằng cách sử dụng liên kết Khách hàng này.

{next}