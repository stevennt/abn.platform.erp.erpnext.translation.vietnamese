<!-- add-breadcrumbs -->
# Mặt hàng do Khách hàng cung cấp

Trong Sản xuất gia công, trong một số trường hợp, Khách hàng sẽ cung cấp các mặt hàng cụ thể đóng vai trò là một hoặc một vài thành phần trong BOM. Những mặt hàng này không thể được nhập kho bằng 'Chu trình mua hàng' (Buying Cycle) vì điều đó đồng nghĩa với việc biến Khách hàng thành Nhà cung cấp tại cùng một thời điểm. Nó cũng sẽ phải đi qua từng DocType trong chu trình đó.

Với tính năng này, Mặt hàng do Khách hàng cung cấp sẽ được nhập kho thông qua 'Phiếu kho' (Stock Entry) với loại 'Nhập vật tư' (Material Receipt) từ một 'Yêu cầu vật tư' (Material Request) có loại là 'Khách hàng cung cấp' (Customer provided). Tính năng này được sử dụng khi có bên nào đó thuê ngoài quy trình sản xuất của bạn và cung cấp nguyên vật liệu cho bạn.

<img alt="Customer Provided Material Request" class="screenshot" src="../assets/img/articles/material-request-customer-provided.png">

Dưới đây là các bước để thiết lập một mặt hàng 'Khách hàng cung cấp'.

1.  Đi tới [Mặt hàng](../stock.md) và thêm một mặt hàng 'Khách hàng cung cấp' mới.

    > Home > Kho > Mặt hàng và Giá > Mặt hàng

2.  Trong phần 'Purchase, Replenishment Details', tích chọn 'Is Customer Provided' và thiết lập Khách hàng mặc định. Lưu ý rằng cần phải bỏ tích 'Is Purchase Item' để sử dụng tính năng này.

    <img alt="Item Purchase Details" class="screenshot" src="../assets/img/articles/item-customer-provided.png">

Làm thế nào để nhập một Mặt hàng 'Khách hàng cung cấp'?

1.  Nếu sử dụng 'Kế hoạch sản xuất' (Production Plan), 'Yêu cầu vật tư' cho mặt hàng này có thể được tự động tạo. Nghĩa là, mặt hàng cần sản xuất sẽ được lấy thông tin trước thông qua Đơn bán hàng hoặc Yêu cầu vật tư, các Mặt hàng sẽ được lấy cho Lệnh sản xuất bằng nút 'Get Items for Work Order', sau đó nhấp vào nút 'Get Raw Materials for Production'.

    <img alt="Material Request in Production Plan" class="screenshot" src="../assets/img/articles/material-request-production-plan.png">

2.  Khi một thành phần trong BOM được thiết lập là 'Khách hàng cung cấp' và 'Yêu cầu vật tư' được tạo từ 'Kế hoạch sản xuất', nó sẽ tạo ra cả 'Yêu cầu vật tư' loại 'Mua hàng' (Purchase) và 'Khách hàng cung cấp' (Customer Provided). Từ đó, một 'Phiếu kho' với mục đích 'Nhập vật tư' (Material Receipt) có thể được tạo ra.

   <img alt="Stock Entry from Material Request" class="screenshot" src="../assets/img/articles/create-mr-from-production-plan.png">

3.  Một 'Yêu cầu vật tư' có thể có nhiều 'Phiếu kho' - Nhập vật tư. Trạng thái sẽ phản ánh điều này.

4.  Khách hàng sẽ có thể theo dõi các 'Yêu cầu vật tư' của họ trong Cổng thông tin Web tại mục 'Material Requests'. Cổng thông tin được lọc để chỉ hiển thị các 'Yêu cầu vật tư' của chính khách hàng đó.