<!-- add-breadcrumbs -->
# Tùy chỉnh hiển thị Module

**ERPNext là một hệ thống có thể được sử dụng bởi nhiều doanh nghiệp ở mọi quy mô, trong đó Sản xuất, Giáo dục, Bán lẻ là một số lĩnh vực được hưởng lợi nhiều nhất từ khả năng sử dụng của hệ thống.**

Để đáp ứng nhu cầu của mọi loại chủ doanh nghiệp, khả năng sử dụng của hệ thống cho các loại hình kinh doanh khác nhau đã được phân chia thành các 'Module' khác nhau, được hiển thị dưới dạng các 'Thẻ' (Cards) trong hệ thống. Tương tự, các module cốt lõi trong hệ thống như Nhân sự, Kế toán, CRM, v.v. cũng được hiển thị bằng các thẻ khác nhau trên Trang tổng quan.

Mọi chủ tài khoản ERPNext đều có tùy chọn tùy chỉnh hiển thị của các module khác nhau dựa trên mô hình kinh doanh của họ.

*Trong Phiên bản 12, bạn có thể đi tới Show / Hide Modules ở góc trên bên phải của màn hình chính để kiểm tra hiển thị của các module.**

<img alt="Module Visibility" class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/customize/customize-module-visibility-2.png">

<img alt="Module Visibility" class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/customize/customize-module-visibility.gif">

> Lưu ý: Các Module sẽ tự động bị ẩn đối với những người dùng không có quyền đối với các tài liệu trong module đó. Ví dụ: nếu một Người dùng không có quyền đối với Đơn mua hàng, Yêu cầu mua hàng, Nhà cung cấp, thì module “Buying” sẽ tự động bị ẩn đối với Người dùng đó.

Nếu bạn có quyền đối với một module cụ thể nhưng nó vẫn không hiển thị, dưới đây có thể là các lý do khả thi.

Hãy xem xét một tình huống là người dùng có quyền đối với module Website nhưng không thể truy cập được.

Như một yêu cầu cơ bản, hãy đảm bảo rằng vai trò "Website Manager" đã được gán cho người dùng đó. Đây là một Vai trò tiêu chuẩn cấp quyền cho module Website. Nếu các quyền đã được tùy chỉnh trong tài khoản của bạn, hãy kiểm tra Role Permission Manager để biết Vai trò nào có quyền đối với Website, sau đó kiểm tra xem Vai trò đó đã được gán cho Người dùng hay chưa.

<img alt="Module Visibility" class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/customize/customize-module-visibility-4.png">

Ngoài ra, bạn cũng nên kiểm tra xem trong phần cài đặt, tại mục 'Allow Modules', module cần thiết đã được bật cho người dùng hay chưa.

<img alt="Module Visibility" class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/customize/customize-module-visibility-1.png">

Tải lại (Reload) tab tài khoản ERPNext của bạn, các thay đổi đã thực hiện sẽ được áp dụng và hiển thị trong hệ thống.

{next}