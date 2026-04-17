# Tính hoa hồng cho đội ngũ bán hàng

Bạn có thể tính hoa hồng cho đội ngũ bán hàng bằng cách sử dụng các script tùy chỉnh.

Tính năng này có thể được sử dụng trong bất kỳ Giao dịch bán hàng nào có bảng **Đội ngũ bán hàng (Sales Team)**.

```javascript
cur_frm.cscript.custom_validate = function(doc) {
    // Tính toán tiền hoa hồng cho từng người trong giao dịch
    total_incentive = 0
    $.each(wn.model.get("Sales Team", {parent:doc.name}), function(i, d) {

        // Tính tỷ lệ hoa hồng
        var incentive_percent = 2;
        if(doc.grand_total > 400) incentive_percent = 4;

        // Số tiền hoa hồng thực tế
        d.incentives = flt(doc.grand_total) * incentive_percent / 100;
        total_incentive += flt(d.incentives)
    });

    doc.total_incentive = total_incentive;
}
```

---

### Các cập nhật mới trong phiên bản v16

Trong phiên bản ERPNext v16, quy trình quản lý bán hàng và kho đã được tối ưu hóa với các tính năng sau:

#### 1. Ngày chốt (Cutoff date) cho Phiếu giao hàng (DN) từ Đơn bán hàng (SO)
Khi tạo **Phiếu giao hàng (DN)** từ **Đơn bán hàng (SO)**, hệ thống hiện đã hỗ trợ thiết lập **Ngày chốt (Cutoff date)**. Điều này giúp bộ phận kho kiểm soát chính xác thời điểm xuất hàng, tránh việc xuất các mặt hàng nằm ngoài kế hoạch hoặc ngoài kỳ kế toán đã định.

#### 2. Nút bấm SO/Quotation trên biểu mẫu Khách hàng
Để tăng tốc độ quy trình bán hàng, tại biểu mẫu **Khách hàng (Customer)**, các nút bấm nhanh **Đơn bán hàng (SO)** và **Báo giá (Quotation)** đã được thêm vào. Bạn có thể tạo nhanh các tài liệu bán hàng trực tiếp từ thông tin khách hàng mà không cần phải chuyển đổi qua lại giữa các màn hình.

#### 3. Giữ chỗ tồn kho (Stock Reservation)
Tính năng **Giữ chỗ tồn kho (Stock Reservation)** cho phép bạn giữ trước một lượng **Mặt hàng (Item)** nhất định trong **Kho (Warehouse)** cho một **Đơn bán hàng (SO)** cụ thể. Điều này đảm bảo rằng các mặt hàng đã được cam kết với khách hàng sẽ không bị xuất nhầm cho các đơn hàng khác, giúp quản lý **Tồn kho (Stock)** chính xác hơn.