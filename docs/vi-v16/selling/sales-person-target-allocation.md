<!-- add-breadcrumbs -->
# Phân bổ Chỉ tiêu Nhân viên bán hàng

**Đây là việc chỉ định Nhân viên bán hàng cho một mặt hàng hoặc một khu vực.**

Cùng với việc quản lý Nhân viên bán hàng, ERPNext cũng cho phép bạn chỉ định chỉ tiêu cho Nhân viên bán hàng dựa trên Nhóm mặt hàng và Khu vực. Dựa trên chỉ tiêu được phân bổ và doanh số thực tế được ghi nhận bởi Nhân viên bán hàng, bạn sẽ nhận được Báo cáo Chênh lệch Chỉ tiêu của Nhân viên bán hàng.

## 1. Phân bổ Chỉ tiêu theo Nhóm mặt hàng cho Nhân viên bán hàng

### 1.1 Mở Danh mục Nhân viên bán hàng

Để phân bổ chỉ tiêu, bạn cần mở danh mục Nhân viên bán hàng cụ thể.

**Bán hàng > Đối tác bán hàng và Khu vực > Nhân viên bán hàng > Sửa**

### 1.2 Phân bổ Chỉ tiêu theo Nhóm mặt hàng

Trong danh mục Nhân viên bán hàng, bạn sẽ thấy một bảng gọi là Chỉ tiêu Nhân viên bán hàng.

<img class="screenshot" alt="Sales person target" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/sales-person-target-item-group.png">

Trong bảng này, bạn nên chọn Nhóm mặt hàng, Năm tài chính, Số lượng chỉ tiêu, Số tiền chỉ tiêu và Phân bổ chỉ tiêu.

Bạn có thể đưa ra chỉ tiêu theo số tiền hoặc số lượng, hoặc cả hai. Nhóm mặt hàng cũng có thể để trống. Trong trường hợp này, hệ thống sẽ tính toán chỉ tiêu dựa trên Tất cả các Nhóm mặt hàng.

**Phân bổ chỉ tiêu**

Bạn có thể chia nhỏ chỉ tiêu theo các tháng. Để làm việc này, hãy tạo một phân bổ hàng tháng mới, bạn có thể thấy tùy chọn này khi nhấp vào trường Phân bổ chỉ tiêu trong bảng Chỉ tiêu. Ví dụ, chỉ tiêu bán được 1.000 đơn vị cho quý đầu tiên của Năm tài chính 2024-2025 như được hiển thị trong ảnh chụp màn hình trước đó.

<img class="screenshot" alt="Target Distribution" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/sales-person-target-distribution.png">

### 1.3 Báo cáo - Chênh lệch Chỉ tiêu Nhân viên bán hàng theo Nhóm mặt hàng

Để kiểm tra báo cáo này, hãy đi tới:

**Bán hàng > Các báo cáo khác > Chênh lệch Chỉ tiêu Nhân viên bán hàng theo Nhóm mặt hàng**

Báo cáo này sẽ cung cấp cho bạn sự chênh lệch giữa chỉ tiêu và kết quả thực tế của Nhân viên bán hàng. Báo cáo này dựa trên báo cáo Đơn bán hàng.

Tại đây, theo báo cáo, chỉ tiêu được phân bổ cho Nhân viên bán hàng là khoảng 83 về số lượng trong một tháng, nhưng anh ấy đã đạt được chỉ tiêu là 80 khi xem báo cáo, do đó báo cáo chênh lệch được hiển thị tương ứng.

<img class="screenshot" alt="Target Item Group" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/sales-person-item-group-report.png">

**Lưu ý:** Để báo cáo phản ánh chi tiết chính xác, bạn cần liên kết Nhân viên bán hàng với một Đơn bán hàng, tùy chọn này nằm trong phần Đội ngũ bán hàng của Đơn bán hàng. Đơn bán hàng cũng phải ở trạng thái đã Xác nhận.

---

## 2. Phân bổ Chỉ tiêu theo Khu vực cho Nhân viên bán hàng

Để phân bổ chỉ tiêu theo Khu vực cho Nhân viên bán hàng, hãy chọn Nhân viên bán hàng cụ thể trong danh mục Khu vực. Nhân viên bán hàng này được nhập chỉ để tham chiếu. Chi tiết Nhân viên bán hàng không được cập nhật trong báo cáo chênh lệch của Phân bổ Chỉ tiêu theo Khu vực.

### 2.1 Đi tới danh mục Khu vực

**Bán hàng > Thiết lập > Khu vực > (Sửa một Khu vực cụ thể)**

Trong Khu vực được chọn, bạn sẽ tìm thấy một trường để chọn Quản lý khu vực. Trường này được liên kết với danh mục "Nhân viên bán hàng".

<img class="screenshot" alt="Sales Person Territory Manager" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/sales-person-territory-manager.png">

### 2.2 Phân bổ Chỉ tiêu

Việc Phân bổ Chỉ tiêu trong danh mục Khu vực tương tự như trong danh mục Nhân viên bán hàng. Bạn có thể làm theo các bước tương tự đã nêu trong phần _1.2 Phân bổ Chỉ tiêu theo Nhóm mặt hàng_ để chỉ định chỉ tiêu trong danh mục Khu vực.

### 2.3 Báo cáo - Chênh lệch Chỉ tiêu Khu vực theo Nhóm mặt hàng

Báo cáo này sẽ cung cấp cho bạn sự chênh lệch giữa chỉ tiêu và kết quả doanh số thực tế tại một khu vực cụ thể. Báo cáo này dựa trên báo cáo Đơn bán hàng. Mặc dù Nhân viên bán hàng được xác định trong danh mục Khu vực, nhưng chi tiết của họ không được đưa vào báo cáo.

**Lưu ý** rằng Khu vực của Khách hàng phải được thiết lập tương ứng để báo cáo này hoạt động. Ví dụ, trong ảnh chụp màn hình sau, chỉ tiêu là khoảng tám đơn vị và đã đạt được năm đơn vị, do đó mức chênh lệch là ba.

<img class="screenshot" alt="Sales Person Territory Report" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/sales-person-territory-report.png">

---

## 3. Phân bổ chỉ tiêu

Để tạo một Phân bổ hàng tháng mới, hãy đi tới:
**Kế toán > Phân bổ hàng tháng**

Chứng từ Phân bổ chỉ tiêu cho phép bạn chia nhỏ các chỉ tiêu đã phân bổ qua nhiều tháng. Nếu sản phẩm và dịch vụ của của bạn có tính mùa vụ, bạn có thể phân bổ chỉ tiêu bán hàng tương ứng. Ví dụ, nếu bạn kinh doanh ô (dù), thì chỉ tiêu được phân bổ trong mùa mưa sẽ cao hơn các tháng khác.

<img class="screenshot" alt="Target Distribution" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/target-distribution.png">

Bạn có thể liên kết Phân bổ hàng tháng khi đang phân bổ chỉ tiêu trong danh mục Nhân viên bán hàng và danh mục Khu vực.

### 4. Các chủ đề liên quan
1. [Nhân viên bán hàng trong các Giao dịch bán hàng](articles/sales-persons-in-the-sales-transactions.md)
1. [Sử dụng Nhân viên bán hàng trong các giao dịch](articles/sales-persons-in-the-sales-transactions.md)

{next}