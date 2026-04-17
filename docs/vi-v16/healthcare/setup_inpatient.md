<!-- add-breadcrumbs -->
# Thiết lập Cơ sở Điều trị Nội trú

ERPNext Healthcare cho phép bạn dễ dàng cấu hình cơ sở Điều trị Nội trú, Nhập viện, Xuất viện và Chuyển viện (ADT) cho bệnh nhân, cũng như lập Hóa đơn cho bệnh nhân đối với các dịch vụ chăm sóc đã thực hiện. Dưới đây là cách bạn có thể thiết lập việc này.

Bạn có thể thiết lập cơ sở hạ tầng của mình (phòng bệnh, giường bệnh, v.v.) trong ERPNext bằng cách sử dụng tài liệu [Healthcare Service Unit](../user/manual/en/healthcare/healthcare_service_unit.html).

### Healthcare Service Unit Type
Bạn có thể xác định các thuộc tính tiêu chuẩn của các `Healthcare Service Units` mà bạn tạo bằng cách sử dụng Healthcare Service Unit Type. Bằng cách cấu hình các loại đơn vị dịch vụ khác nhau trong cơ sở của bạn với các đơn giá và các thuộc tính khác tương ứng, bạn có thể dễ dàng tạo nhiều Healthcare Service Units chỉ bằng cách chọn loại. Bạn có thể cấu hình các loại khác nhau bằng cách đi tới,

`Healthcare > Setup > Healthcare Service Unit Type > New Healthcare Service Unit Type`

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v16/assets/img/healthcare/healthcare_service_unit_type.png">

ERPNext sẽ tự động tạo một Mặt hàng với các chi tiết mà bạn cung cấp tại đây để chức năng lập hóa đơn có thể hoạt động.

Bạn cũng có thể tạo các Healthcare Service Units để thiết lập các phòng khám và các khu vực khác nơi có thể lập lịch hẹn bằng cách tích vào tùy chọn `Allow Appointments`. Các đơn vị dịch vụ như vậy không được liên kết với danh mục Mặt hàng vì việc lập hóa đơn sẽ sử dụng Mặt hàng được chọn trong danh mục [Healthcare Practitioner](../user/manual/en/healthcare/healthcare_practitioner.html) hoặc các mặt hàng được cấu hình trong [Healthcare Settings](../user/manual/en/healthcare/healthcare_settings)

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v16/assets/img/healthcare/healthcare_service_unit_type_1.png">

Lưu ý rằng việc bật `Allow Overlap` sẽ cho phép các lịch hẹn chồng lấn nhau đối với Healthcare Practitioner có mặt tại đơn vị dịch vụ. Điều này sẽ hữu ích khi bạn tạo các đơn vị dịch vụ nơi nhiều Bệnh nhân có thể được điều trị cùng một lúc, ví dụ như trung tâm yoga hoặc phòng vật lý trị liệu.

{next}