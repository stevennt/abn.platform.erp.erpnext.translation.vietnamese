<!-- add-breadcrumbs -->
# Đơn vị tính (UoM)

**UoM là đơn vị được sử dụng để đo lường một Mặt hàng.**

Theo mặc định, có nhiều UoM đã được tạo sẵn trong ERPNext. Tuy nhiên, bạn có thể thêm nhiều UoM khác tùy thuộc vào trường hợp sử dụng trong doanh nghiệp của mình.

Trong UoM có một tùy chọn 'Must be Whole Number' (Phải là số nguyên). Nếu tùy chọn này được chọn, bạn không thể sử dụng các số phân số trong UoM này. Để biết thêm về phân số và UoM, hãy xem [trang này](articles/managing-fractions-in-uom.md).

Bản thân danh sách UoM chỉ lưu trữ tên. Các tỷ lệ chuyển đổi thực tế được lưu trữ trong một tài liệu gọi là 'UoM Conversion Factor' (Hệ số chuyển đổi UoM). Nếu bạn thêm các UoM mới và có kế hoạch sử dụng chúng trong các giao dịch mà chúng sẽ được chuyển đổi sang các UoM khác, bạn nên thêm chúng vào danh sách này.

Ví dụ, ở đây 1 Kg xấp xỉ bằng 2.2 Pounds và hệ số chuyển đổi chính xác được lưu trữ như sau:

![UoM conversion factor](https://docs.erpnext.com/docs/v16/assets/img/stock/uom_convert.png)

---

### Các tính năng mới trong phiên bản v16 liên quan đến Quản lý Tồn kho

Trong phiên bản v16, hệ thống quản lý Tồn kho đã được nâng cấp mạnh mẽ để hỗ trợ các nghiệp vụ phức tạp hơn:

*   **Hệ thống Giữ hàng (Stock Reservation System):** Cho phép giữ trước lượng tồn kho cho các Đơn bán hàng (SO) hoặc các yêu cầu khác, giúp đảm bảo hàng hóa luôn sẵn sàng cho các đơn hàng ưu tiên.
*   **Báo cáo Truy xuất nguồn gốc Số sê-ri/Lô hàng (Serial/Batch Traceability Report):** Cung cấp khả năng theo dõi chi tiết lịch sử di chuyển của từng Lô hàng (Batch) hoặc Số sê-ri từ khi nhập kho (PR) cho đến khi xuất kho, giúp kiểm soát chất lượng (QI) tốt hơn.
*   **Chi phí cập bến cho Phiếu kho (Landed Cost cho Stock Entry):** Cho phép phân bổ các chi phí mua hàng (như vận chuyển, thuế, phí bốc xếp) trực tiếp vào giá trị của Mặt hàng khi thực hiện các giao dịch nhập kho, giúp phản ánh chính xác giá trị tồn kho.
*   **Kế toán tồn kho theo cấp độ Mặt hàng (Item-Level Stock Accounting):** Tăng cường độ chính xác trong việc hạch toán Bút toán (JE) bằng cách cho phép theo dõi giá trị tồn kho chi tiết đến từng Mặt hàng cụ thể.
*   **Xem trước Sổ cái (Ledger Preview):** Cho phép người dùng xem nhanh các bút toán liên quan trực tiếp từ giao dịch kho, giúp việc đối soát giữa kho và kế toán trở nên dễ dàng hơn.