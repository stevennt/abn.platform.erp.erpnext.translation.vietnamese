<!-- add-breadcrumbs -->
# Lệnh sản xuất

**Lệnh sản xuất là một chứng từ được Người lập kế hoạch sản xuất đưa cho xưởng sản xuất để làm tín hiệu sản xuất một số lượng nhất định của một Mặt hàng nhất định.**

<img class="screenshot" alt="Work Order" src="https://docs.erpnext.com/docs/v16/assets/img/manufacturing/manufacturing-flow-wo.png">

Lệnh sản xuất cũng giúp tạo ra các yêu cầu vật tư (Phiếu kho) cho Mặt hàng cần sản xuất từ **Định mức nguyên vật liệu** của nó.

**Lệnh sản xuất** có thể được tạo từ [Kế hoạch sản xuất](../manufacturing/production-plan) dựa trên các Đơn bán hàng.

Để truy cập danh sách Lệnh sản xuất, hãy đi tới:

> Home > Manufacturing > Production > Work Order

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Lệnh sản xuất, bạn nên tạo các mục sau trước:

* [Định mức nguyên vật liệu](../manufacturing/bill-of-materials)
* [Công đoạn](../manufacturing/operation)
* [Máy/Trạm làm việc](../manufacturing/workstation)

## 2. Cách tạo Lệnh sản xuất
1. Đi tới danh sách Lệnh sản xuất, nhấn vào Mới.
1. Chọn Mặt hàng cần sản xuất.
1. Định mức nguyên vật liệu mặc định cho mặt hàng đó sẽ được hệ thống tự động lấy ra. Bạn cũng có thể thay đổi Định mức nguyên vật liệu.
1. Nhập số lượng cần sản xuất. Các Mặt hàng nguyên vật liệu sẽ chỉ được lấy ra khi số lượng này được thiết lập.
1. Nếu Định mức nguyên vật liệu được chọn có đề cập đến các Công đoạn, hệ thống sẽ lấy tất cả các Công đoạn từ Định mức nguyên vật liệu, các giá trị này có thể được thay đổi. Tham khảo [mục 3.2](../manufacturing/work-order#32-operations-table) để biết thêm chi tiết.
1. Thiết lập Ngày bắt đầu dự kiến (Ngày ước tính mà bạn muốn việc Sản xuất bắt đầu).
  <img class="screenshot" alt="Work Order" src="https://docs.erpnext.com/docs/v16/assets/img/manufacturing/work-order.png">
1. **Sử dụng Định mức nguyên vật liệu đa cấp**: Tính năng này được bật theo mặc định. Nếu bạn muốn lập kế hoạch vật tư cho các cụm lắp ráp phụ của Mặt hàng bạn đang sản xuất, hãy để tùy chọn này được bật. Nếu bạn lập kế hoạch và sản xuất các cụm lắp ráp phụ riêng biệt, bạn có thể tắt tùy chọn này. Để biết thêm, hãy truy cập [trang này](../manufacturing/articles/managing-multi-level-bom).
1. Chọn Kho:
  1. **Kho nguồn**: Chọn Kho này tại dòng Mặt hàng. Đây là kho nơi bạn lưu trữ nguyên vật liệu của mình. Mỗi mặt hàng yêu cầu có thể có một kho nguồn riêng biệt. Kho nhóm cũng có thể được chọn làm kho nguồn. Khi Xác nhận Lệnh sản xuất, nguyên vật liệu sẽ được giữ tại các kho này để phục vụ sản xuất.
  2. **Kho bán thành phẩm (WIP)**: Kho nơi các Mặt hàng của bạn sẽ được chuyển đến khi bạn bắt đầu sản xuất. Kho nhóm cũng có thể được chọn làm kho bán thành phẩm.
  3. **Kho đích**: Kho nơi bạn lưu trữ các Mặt hàng thành phẩm trước khi chúng được xuất đi.
  4. **Kho phế liệu**: Nếu Định mức nguyên vật liệu tạo ra phế liệu, cần phải chọn Kho phế liệu.
1. **Mặt hàng yêu cầu**: Tất cả các mặt hàng yêu cầu (nguyên vật liệu) sẽ được lấy từ Định mức nguyên vật liệu và hiển thị trong bảng này. Tại đây bạn cũng có thể thay đổi Kho nguồn cho bất kỳ mặt hàng nào. Và trong quá trình sản xuất, bạn có thể theo dõi các nguyên vật liệu đã được chuyển đi từ bảng này.

> Lưu ý: Bạn có thể Lưu một Lệnh sản xuất mà không cần chọn Kho, nhưng việc chọn Kho là bắt buộc để Xác nhận Lệnh sản xuất.

Một Lệnh sản xuất cũng có thể được tạo trực tiếp từ [Đơn bán hàng](../selling/sales-order#214-after-submitting).

### 2.1 Các tùy chọn bổ sung khi tạo Lệnh sản xuất

* **Đơn bán hàng**: Nếu bạn tạo Lệnh sản xuất từ một Đơn bán hàng, nó sẽ được lấy vào đây. Bạn cũng có thể liên kết một Đơn bán hàng hiện có có chứa Mặt hàng cần sản xuất với Lệnh sản xuất này.
* **Dự án**: Liên kết Lệnh sản xuất với một Dự án để theo dõi tiến độ trong các trường hợp như sản xuất theo yêu cầu kỹ thuật của khách hàng.
* **Cho phép mặt hàng thay thế**: Đôi khi khi sản xuất thành phẩm, các vật liệu cụ thể có thể không có sẵn. Ví dụ, sử dụng hạt nhựa thay vì tinh thể nhựa. Bản thân thành phẩm cũng có thể khác đi. Việc tích vào ô này sẽ cho phép bạn chọn một Mặt hàng thay thế. Để biết thêm, hãy truy cập [trang này](../manufacturing/item-alternative).
* **Bỏ qua chuyển vật tư vào Kho bán thành phẩm**: Thông thường, một Phiếu kho sẽ được tạo khi nguyên vật liệu được chuyển vào Kho bán thành phẩm. Trong trường hợp này, nguyên vật liệu được coi là đã tiêu hao nên bước tạo Phiếu kho sẽ được bỏ qua. Tùy chọn tiếp theo sẽ được hiển thị nếu bạn tích vào ô này.
* **Backflush nguyên vật liệu từ Kho bán thành phẩm**: Tích vào ô này sẽ tự động tạo một Phiếu kho với loại là 'Sản xuất'. Điều này có nghĩa là nguyên vật liệu đã được tiêu hao từ Kho nguồn, được sử dụng để sản xuất thành phẩm và một Phiếu kho khác đã được tạo cho Kho đích của bạn.
  ![Options when creating WO](https://docs.erpnext.com/docs/v16/assets/img/manufacturing/work-order-options.png)

## 3. Các tính năng
### 3.1 Thời gian
Ngày bắt đầu dự kiến và Ngày giao hàng dự kiến có thể được thiết lập tại đây. Mặc định cho Ngày bắt đầu dự kiến là ngày và giờ hiện tại tại thời điểm tạo Lệnh sản xuất.

### 3.2 Bảng Mặt hàng yêu cầu
Kho nguồn có thể được thay đổi cho các mặt hàng nguyên vật liệu được sử dụng ở đây. Kho mặc định có thể được thiết lập ở cấp độ Mặt hàng trong danh mục [Mặt hàng](../stock/item#28-item-defaults) hoặc thiết lập toàn cầu trong [Cài đặt kho](../stock/stock-settings#23-default-warehouse).

* **Số lượng yêu cầu**: Số lượng này sẽ được tính toán tự động dựa trên [Định mức nguyên vật liệu](../manufacturing/bill-of-materials).
* **Số lượng đã chuyển**: Khi Lệnh sản xuất bắt đầu và các Thẻ công việc (Job Cards) được thực hiện, các mặt hàng sẽ được chuyển từ Kho nguồn sang Kho bán thành phẩm. Trường này hiển thị số lượng đang có trong Kho bán thành phẩm.