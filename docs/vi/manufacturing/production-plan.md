<!-- add breadcrumbs -->
# Kế hoạch sản xuất

**Kế hoạch sản xuất giúp lập kế hoạch sản xuất và vật tư cho các Mặt hàng dự kiến sản xuất. Các mặt hàng sản xuất này có thể được cam kết thông qua Đơn bán hàng (cho Khách hàng) hoặc Yêu cầu vật tư (nội bộ).**

Kế hoạch sản xuất giúp người dùng lập kế hoạch sản xuất dựa trên nhiều Đơn bán hàng hoặc Yêu cầu vật tư. Ngoài ra, nó còn giúp lập kế hoạch mua sắm vật tư cho các mặt hàng nguyên vật liệu, dựa trên số lượng thành phẩm cần sản xuất.

Để truy cập danh sách Kế hoạch sản xuất, hãy đi tới:

> Home > Manufacturing > Production > Production Plan

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Kế hoạch sản xuất, bạn nên tạo các mục sau trước:

* [Mặt hàng](../stock/item.md)
* [Yêu cầu vật tư](../stock/material-request.md)
* [Đơn bán hàng](../selling/sales-order.md)
* [Định mức nguyên vật liệu](manufacturing/bill-of-materials)
* [Định tuyến](routing.md)

## 2. Cách tạo Kế hoạch sản xuất
Như đã đề cập trước đó, Kế hoạch sản xuất có thể được sử dụng để lập kế hoạch sản xuất các Mặt hàng dựa trên Đơn bán hàng hoặc Yêu cầu vật tư.

Các bước thông thường là:

1. Đi tới danh sách Kế hoạch sản xuất, nhấn vào Mới.
1. Chọn lấy mặt hàng từ [Đơn bán hàng](../selling/sales-order.md) hay [Yêu cầu vật tư](../stock/material-request.md).

Kế hoạch sản xuất cũng có thể được tạo thủ công, nơi bạn có thể chọn các Mặt hàng cần sản xuất.

### 2.1 Sản xuất theo Đơn bán hàng

1. Chọn tùy chọn Sales Order từ danh sách thả xuống 'Get Items From'. Hệ thống sẽ hiển thị các bộ lọc, sử dụng bộ lọc đó bạn có thể lấy các Đơn bán hàng để sản xuất. Bạn không cần sử dụng tất cả các bộ lọc này nếu chỉ có một vài Đơn bán hàng trong một khoảng thời gian cụ thể.

  ![Production Plan fetch items](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/pp_fetch_from.png)

1. Nhấp vào Get Sales Orders để lấy các đơn bán hàng dựa trên các bộ lọc trên.

  ![Sales Order Filters](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/sales_order_filter.png)

1. Nhấp vào 'Get Items for Work Order' để lấy các mặt hàng từ các Đơn bán hàng trên. Chỉ những mặt hàng có Định mức nguyên vật liệu mới được lấy ra.
  ![Get items for Production Plan](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/get_items_wo.png)

1. Khi mở rộng một dòng trong bảng Mặt hàng cần sản xuất (Items to Manufacture), bạn sẽ thấy tùy chọn 'Include Exploded Items'. Khi tích vào đây, các nguyên vật liệu của các mặt hàng lắp ráp phụ sẽ được bao gồm trong quy trình sản xuất.

### 2.2 Sản xuất theo Yêu cầu vật tư

1. Chọn tùy chọn Material Request từ danh sách thả xuống Get Items From. Hệ thống sẽ hiển thị các bộ lọc, sử dụng bộ lọc đó chúng ta có thể lấy các Yêu cầu vật tư để sản xuất.

  <img class="screenshot" alt="Material Request Filters" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/material_request_filter.png">

1. Nhấp vào 'Get Material Request' để lấy các yêu cầu vật tư dựa trên các bộ lọc trên.

  <img class="screenshot" alt="Material Requests" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/material_requests.png">

1. Nhấp vào Get Items for Work Order để lấy các mặt hàng từ các yêu cầu vật tư trên.

  <img class="screenshot" alt="Material Request Item" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/material_request_items.png">

### 2.3 Lập kế hoạch cho Yêu cầu vật tư

Nhấp vào nút 'Get Raw Materials for Production' sẽ lấy các Mặt hàng nguyên vật liệu cần thiết vào bảng Kế hoạch yêu cầu vật tư (Material Request Plan). Ví dụ, để sản xuất 200 cây nhựa, bạn cần 100 thanh nhựa nguyên liệu nhưng chỉ có 20 trong Kho của mình, khi đó nhấp vào nút này sẽ thêm một dòng với số lượng 80 trong cột Số lượng yêu cầu (Required Quantity).

<img class="screenshot" alt="Material Request Plan" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/material_request_plan.png">

Sử dụng các hộp kiểm sau để thực hiện các hành động nhất định:

  * <b>Include Non Stock Items</b>: Để bao gồm các mặt hàng không lưu kho trong việc lập kế hoạch yêu cầu vật tư. Tức là các Mặt hàng mà ô 'Maintain Stock' không được tích. Tham khảo [trang Mặt hàng](../stock/item.md#12-options-when-creating-an-item) để biết thêm chi tiết.
  * <b>Include Subcontracted Items</b>: Để thêm nguyên vật liệu của các Mặt hàng gia công ngoài nếu tùy chọn include exploded items bị tắt.
  * <b>Ignore Existing Projected Quantity</b>: Nếu được bật, hệ thống sẽ tạo Yêu cầu vật tư ngay cả khi người dùng đã đặt hàng hoặc yêu cầu các mặt hàng tương ứng. Ví dụ, nếu bạn cần 100 số lượng nguyên vật liệu A và ngay cả khi bạn đã có 150, việc bật hộp kiểm này sẽ thêm một yêu cầu cho 100 số lượng nguyên vật liệu đó.
  * <b>For Warehouse</b>: Người dùng có thể thiết lập Kho mà họ muốn tạo yêu cầu vật tư. Khi tạo Phiếu kho trong quá trình sản xuất, hệ thống sẽ tìm kiếm tồn kho nguyên vật liệu trong Kho này.
  * <b>Download Materials Required</b>:- Khi hộp kiểm này được tích, Người dùng sẽ nhận được bảng tính Excel với các nguyên vật liệu cần thiết để hoàn thành Kế hoạch sản xuất này. Người dùng có thể chọn Kho để kiểm tra số lượng hiện có trong Kho tương ứng. Nếu Người dùng để trống trường 'For Warehouse' thì hệ thống sẽ cung cấp bảng tính Excel với các nguyên vật liệu và số lượng hiện có theo từng Kho của các nguyên vật liệu tương ứng. Bảng tính Excel sẽ trông giống như sau:

 <img class="screenshot" alt="Material Request Plan" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/material_request_excel.png">

### 2.4 Sau khi Xác nhận

Sau khi Kế hoạch sản xuất được Xác nhận, Người dùng có tùy chọn tạo Lệnh sản xuất cho các mặt hàng sản xuất và Yêu cầu vật tư cho các nguyên vật liệu. Người dùng cũng có thể thiết lập Trạng thái là **Closed** trong Kế hoạch sản xuất.

<img class="screenshot" alt="Make PO or MR" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/make_prod_mr_wo.png">

#### 2.4.1 Đóng một Kế hoạch sản xuất

Có thể xảy ra trường hợp một Kế hoạch sản xuất được