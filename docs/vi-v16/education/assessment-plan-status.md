# Trạng thái Kế hoạch Đánh giá (Assessment Plan Status)

Kế hoạch Đánh giá (Assessment Plan) được sử dụng để quản lý các quy trình kiểm tra chất lượng (QI) và đánh giá các tiêu chuẩn sản phẩm hoặc quy trình trong hệ thống ERPNext. Trạng thái của Kế hoạch Đánh giá giúp theo dõi tiến độ từ khi lập kế hoạch đến khi hoàn tất việc kiểm tra.

## Các trạng thái của Kế hoạch Đánh giá

| Trạng thái | Mô tả |
| :--- | :--- |
| **Draft (Nháp)** | Kế hoạch đang được soạn thảo. Bạn có thể chỉnh sửa các thông tin về **Mặt hàng (Item)**, **Lô hàng (Batch)** hoặc các tiêu chí kiểm tra. |
| **Submitted (Đã xác nhận)** | Kế hoạch đã được **Xác nhận (Submit)**. Tại thời điểm này, các thông tin trong kế hoạch sẽ được khóa để đảm bảo tính toàn vẹn dữ liệu. Bạn không thể chỉnh sửa trừ khi thực hiện **Hủy (Cancel)**. |
| **Cancelled (Đã hủy)** | Kế hoạch đã bị **Hủy (Cancel)**. Các bản ghi liên quan đến kế hoạch này sẽ không còn hiệu lực trong các báo cáo kiểm tra chất lượng. |

## Quy trình làm việc (Workflow)

1.  **Tạo mới:** Người dùng tạo một bản ghi mới và nhập các thông tin cần thiết (ví dụ: liên kết với **Lô hàng (Batch)** hoặc **Mặt hàng (Item)** cụ thể). Trạng thái mặc định là **Draft**.
2.  **Lưu (Save):** Nhấn **Lưu (Save)** để lưu lại các thay đổi tạm thời.
3.  **Xác nhận (Submit):** Sau khi kiểm tra kỹ các tiêu chí **Kiểm tra chất lượng (QI)**, nhấn **Xác nhận (Submit)** để chính thức hóa kế hoạch.
4.  **Thực hiện:** Dựa trên kế hoạch đã xác nhận, nhân viên QC sẽ tiến hành kiểm tra thực tế tại **Kho (Warehouse)**.
5.  **Hủy (Cancel):** Nếu có sai sót về thông tin hoặc kế hoạch không còn phù hợp, người dùng có quyền **Hủy (Cancel)** kế hoạch (chỉ áp dụng khi kế hoạch đã được **Xác nhận**).

## Lưu ý quan trọng

*   **Liên kết dữ liệu:** Một Kế hoạch Đánh giá đã được **Xác nhận (Submit)** có thể liên kết trực tiếp với các phiếu **Kiểm tra chất lượng (QI)** và ảnh hưởng đến trạng thái của **Lô hàng (Batch)** trong hệ thống **Tồn kho (Stock)**.
*   **Phân quyền:** Chỉ những người dùng có quyền quản lý chất lượng mới có thể **Xác nhận (Submit)** hoặc **Hủy (Cancel)** kế hoạch.

---
[Quay lại trang chủ](../index.md) | [Tài liệu ERPNext v16](../index.md)