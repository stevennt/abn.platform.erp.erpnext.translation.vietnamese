Do bạn chưa cung cấp nội dung cụ thể của các trang tài liệu cần chuyển đổi từ v13 lên v16, tôi sẽ thiết lập **khung cấu trúc chuẩn** và **quy tắc định dạng** dựa trên các thuật ngữ bạn đã cung cấp. 

Khi bạn gửi nội dung chi tiết, tôi sẽ áp dụng đúng bộ quy tắc này để viết lại.

---

# Khung mẫu tài liệu ERPNext v16 (Tiếng Việt)

```markdown
---
title: [Tên tài liệu - Ví dụ: Quản lý Bán hàng]
parent: Articles
route: Articles/[tên-tài-liệu]
---

# [Tên tài liệu]

[Mô tả tổng quan về module hoặc quy trình trong phiên bản v16]

## Quy trình thực hiện

Để hoàn tất quy trình, vui lòng thực hiện theo các bước sau:

1. **Tạo mới**: Truy cập vào module, chọn **Mới** và nhập thông tin.
2. **Lưu**: Nhấn nút **Lưu** để hệ thống ghi nhận dữ liệu tạm thời.
3. **Xác nhận**: Sau khi kiểm tra thông tin chính xác, nhấn **Xác nhận** để hoàn tất giao dịch (hệ thống sẽ không cho phép sửa đổi sau bước này).
4. **Hủy**: Nếu có sai sót, bạn có thể chọn **Hủy** để đóng giao dịch.

## Các thuật ngữ chính trong module

| Thuật ngữ gốc (EN) | Thuật ngữ tiếng Việt (v16) | Mô tả |
| :--- | :--- | :--- |
| Customer | Khách hàng | Đối tượng mua hàng |
| Item | Mặt hàng | Sản phẩm hoặc dịch vụ |
| Sales Order (SO) | Đơn bán hàng | Đơn đặt hàng từ khách hàng |
| Invoice | Hóa đơn | Chứng từ yêu cầu thanh toán |
| Payment | Thanh toán | Ghi nhận dòng tiền |

## Hướng dẫn chi tiết

### 1. Quản lý [Tên đối tượng]
[Nội dung hướng dẫn sử dụng...]

> **Lưu ý:** Hãy đảm bảo đã kiểm tra **Tồn kho** tại **Kho** trước khi tạo **Đơn bán hàng**.

### 2. Quản lý [Tên đối tượng khác]
[Nội dung hướng dẫn sử dụng...]

---
[Link liên quan](./tên-file-liên-quan.md)
```

---

### ⚠️ Quy tắc chuyển đổi tôi sẽ áp dụng cho bạn:

1.  **Cập nhật thuật ngữ (Bắt buộc):**
    *   `Submit` $\rightarrow$ **Xác nhận**
    *   `Save` $\rightarrow$ **Lưu**
    *   `Cancel` $\rightarrow$ **Hủy**
    *   `Customer` $\rightarrow$ **Khách hàng**
    *   `Supplier` $\rightarrow$ **Nhà cung cấp**
    *   `Item` $\rightarrow$ **Mặt hàng**
    *   `PO` $\rightarrow$ **Đơn mua hàng**
    *   `SO` $\rightarrow$ **Đơn bán hàng**
    *   `Invoice` $\rightarrow$ **Hóa đơn**
    *   `Payment` $\rightarrow$ **Thanh toán**
    *   `Stock` $\rightarrow$ **Tồn kho**
    *   `Warehouse` $\rightarrow$ **Kho**
    *   `Batch` $\rightarrow$ **Lô hàng**
    *   `DN` $\rightarrow$ **Phiếu giao hàng**
    *   `PR` $\rightarrow$ **Phiếu nhập hàng**
    *   `JE` $\rightarrow$ **Bút toán**
    *   `MR` $\rightarrow$ **Yêu cầu vật tư**
    *   `SE` $\rightarrow$ **Phiếu kho**
    *   `QI` $\rightarrow$ **Kiểm tra chất lượng**

2.  **Định dạng:**
    *   Giữ nguyên cấu trúc Markdown.
    *   Sử dụng đường dẫn tương đối: `[Tên tài liệu](./file.md)`.
    *   Chỉ trả về nội dung Markdown, không giải thích thêm.

**Mời bạn gửi nội dung tài liệu v13 cần chuyển đổi.**