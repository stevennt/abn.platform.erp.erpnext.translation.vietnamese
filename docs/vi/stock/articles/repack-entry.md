<!-- add-breadcrumbs -->
# Phiếu đóng gói lại

Phiếu đóng gói lại được tạo cho các mặt hàng được mua với số lượng lớn, sau đó được đóng gói thành các gói nhỏ hơn. Ví dụ, mặt hàng mua theo tấn có thể được đóng gói lại thành Kg.

Lưu ý:
1. Mặt hàng mua vào và mặt hàng đóng gói lại sẽ có Mã mặt hàng khác nhau.
2. Phiếu đóng gói lại có thể được thực hiện có hoặc không có BOM (Định mức nguyên vật liệu).

Trong một Phiếu đóng gói lại, có thể có một hoặc nhiều mặt hàng đóng gói lại. Hãy xem kịch bản dưới đây để hiểu rõ hơn.

Giả sử chúng ta đang mua các hộp sơn xịt với các màu cụ thể (Xanh lá, Xanh dương, v.v.). Và sau đó đóng gói lại để tạo ra các gói có nhiều màu sơn xịt khác nhau (Xanh dương-Xanh lá, Xanh lá-Vàng, v.v.) bên trong.

#### 1. Tạo Phiếu kho mới

`Kho > Chứng từ > Phiếu kho > Phiếu kho mới`

#### 2. Nhập các mặt hàng

Chọn Mục đích là 'Repack Entry'.

Đối với mặt hàng nguyên liệu/đầu vào, chỉ có Kho Nguồn được cung cấp.

Đối với các mặt hàng được đóng gói lại/đầu ra, chỉ có Kho Đích được cung cấp. Bạn sẽ phải cung cấp giá trị tính giá cho các mặt hàng đóng gói lại.

<img alt="Repack Entry" class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/articles/repack-1.png">

Cập nhật Số lượng cho tất cả các mặt hàng đã chọn.

#### 3. Xác nhận Phiếu kho

Khi Xác nhận Phiếu kho, tồn kho của mặt hàng đầu vào sẽ bị giảm ở Kho Nguồn, và tồn kho của mặt hàng đóng gói lại/đầu ra sẽ được thêm vào Kho Đích.

<img alt="Repack Stock Entry" class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/articles/repack-2.png">

<!-- markdown -->