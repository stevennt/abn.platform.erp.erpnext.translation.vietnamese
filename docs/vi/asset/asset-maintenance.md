<!-- add-breadcrumbs -->
# Bảo trì Tài sản

**Bảo trì Tài sản đề cập đến bất kỳ hoạt động nào được thực hiện trên Tài sản để duy trì hiệu suất hoặc tình trạng của chúng.**

ERPNext cung cấp các tính năng để theo dõi chi tiết các tác vụ bảo trì/hiệu chuẩn riêng lẻ cho một tài sản theo ngày, người chịu trách nhiệm bảo trì và ngày đến hạn bảo trì trong tương lai.

Để thực hiện Bảo trì Tài sản trong ERPNext:

1. Bật 'Maintenance Required' từ danh mục Tài sản.
2. Tạo Nhóm Bảo trì Tài sản.
3. Tạo Bảo trì Tài sản.
4. Một Nhật ký Bảo trì Tài sản sẽ được tạo.
5. Tạo Nhật ký Sửa chữa Tài sản.

Để truy cập danh sách Bảo trì Tài sản, hãy đi đến:
> Home > Assets > Maintenance > Asset Maintenance

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Bảo trì Tài sản, bạn nên tạo các mục sau trước:


* [Asset](asset.md) với mục 'Maintenance Required' đã được chọn.

    <img class="screenshot" alt="Asset" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/asset/maintenance-required.png">

* [Asset Maintenance Team](asset-maintenance-team.md)

## 2. Cách tạo Bảo trì Tài sản
Đối với mỗi tài sản, hãy tạo một bản ghi Bảo trì Tài sản liệt kê tất cả các tác vụ bảo trì liên quan, loại bảo trì (Bảo trì phòng ngừa hoặc Hiệu chuẩn), tính định kỳ, người được giao, ngày bắt đầu và ngày kết thúc bảo trì. Dựa trên ngày bắt đầu và tính định kỳ, ngày đến hạn tiếp theo sẽ được tự động tính toán và một ToDo sẽ được tạo cho Người được giao.

1. Đi đến danh sách Bảo trì Tài sản, nhấn vào Mới.
1. Chọn Tài sản.
1. Chọn Nhóm Bảo trì Tài sản.
1. Thêm các Tác vụ Bảo trì vào bảng.
  1. Thiết lập Trạng thái Bảo trì là 'Planned' (Đã lập kế hoạch), 'Overdue' (Quá hạn), hoặc 'Canceled' (Đã hủy).
  1. Chọn tính định kỳ mà tác vụ cần được thực hiện. Ngày đến hạn tiếp theo sẽ được tính toán.
1. Lưu.
1. Sau khi lưu, bạn có thể giao tác vụ cho một người dùng.

<img class="screenshot" alt="Asset" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/asset/asset-maintenance.png">

Nếu Mặt hàng có số serial, bạn có thể nhập Số serial.

## 3. Các tính năng
### 3.1 Tác vụ Bảo trì

* **Maintenance Type (Loại bảo trì)**: Đây là hoạt động bảo trì 'Preventive' (Phòng ngừa) hay 'Calibration' (Hiệu chuẩn) để khôi phục chức năng chính xác.
* **Start and End Date (Ngày bắt đầu và Ngày kết thúc)**: Thiết lập ngày bắt đầu và ngày kết thúc khi việc bảo trì dự kiến bắt đầu và kết thúc.
* **Last Completion Date (Ngày hoàn thành cuối cùng)**: Nếu việc bảo trì không được thực hiện vào hoặc trước ngày đã lên lịch, ngày bảo trì thực tế có thể được ghi lại tại đây.

### 3.2 Bảo trì Tài sản trong ToDo

Khi giao việc bảo trì cho một người dùng, nó sẽ xuất hiện trong danh sách ToDo của người dùng đó.

<img class="screenshot" alt="Asset" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/asset/asset-maintenance.png">

## 4. Các chủ đề liên quan
1. [Asset Value Adjustment](asset-value-adjustment.md)
1. [Asset Depreciation](asset-depreciation.md)
1. [Scrapping an Asset](scrapping-an-asset.md)

{next}