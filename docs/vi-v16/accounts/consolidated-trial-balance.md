# Bảng cân đối thử hợp nhất (Consolidated Trial Balance)

Bảng cân đối thử hợp nhất cung cấp cái nhìn tổng thể về tình hình tài chính của toàn bộ tập đoàn hoặc nhóm công ty bằng cách tổng hợp dữ liệu từ nhiều công ty khác nhau trong cùng một hệ thống ERPNext.

## 1. Giới thiệu tính năng <span style="color: #2ecc71;">(Mới trong v16)</span>

Trong phiên bản v16, tính năng **Bảng cân đối thử hợp nhất** đã được nâng cấp mạnh mẽ để hỗ trợ các mô hình kinh doanh đa quốc gia và đa công ty. 

*   **Hợp nhất đa công ty:** Tự động thu thập dữ liệu từ tất cả các công ty con được thiết lập trong hệ thống.
*   **Tự động quy đổi tiền tệ:** Hệ thống tự động lấy tỷ giá hối đoái tại thời điểm báo cáo để quy đổi các tài khoản có ngoại tệ về đồng tiền báo cáo chung của tập đoàn.
*   **Phân tích theo đơn vị:** Cho phép người dùng lọc và so sánh dữ liệu giữa công ty mẹ và các công ty con một cách linh hoạt.

## 2. Điều kiện tiên quyết

Để sử dụng báo cáo này một cách chính xác, bạn cần đảm bảo các điều kiện sau:
*   Hệ thống đã được thiết lập cấu trúc **Multi-company** (Đa công ty).
*   Các tài khoản kế toán đã được thiết lập đầy đủ và chính xác.
*   Các giao dịch ngoại tệ đã được cập nhật tỷ giá hối đoái trong hệ thống.
*   Người dùng có quyền truy cập vào báo cáo tài chính của tất cả các công ty liên quan.

## 3. Hướng dẫn từng bước

Để xem Bảng cân đối thử hợp nhất, hãy thực hiện theo các bước sau:

1.  Truy cập vào thanh tìm kiếm và nhập **"Consolidated Trial Balance"**.
2.  Chọn báo cáo **Bảng cân đối thử hợp nhất** từ danh sách kết quả.
3.  **Thiết lập bộ lọc:**
    *   **Company:** Chọn công ty mẹ hoặc chọn tất cả các công ty để xem báo cáo hợp nhất.
    *   **Fiscal Year:** Chọn năm tài chính cần báo cáo.
    *   **Period:** Chọn khoảng thời gian cụ thể (từ ngày... đến ngày...).
4.  **Chọn chế độ quy đổi tiền tệ:** Tại mục *Target Currency*, chọn đồng tiền mà bạn muốn quy đổi toàn bộ dữ liệu về để xem báo cáo tổng quát.
5.  Nhấn nút **Show Report** để hệ thống tính toán và hiển thị dữ liệu.

## 4. Ảnh minh họa

![Bảng cân đối thử hợp nhất](../../screenshots/reports/trial-balance.png)

## 5. Các tùy chọn/cài đặt liên quan

Khi tùy chỉnh báo cáo, bạn có thể sử dụng các tùy chọn sau:

| Tùy chọn | Mô tả |
| :--- | :--- |
| **Company** | Cho phép chọn một công ty cụ thể hoặc chọn nhiều công ty con để hợp nhất. |
| **Target Currency** | Đồng tiền mục tiêu để quy đổi các tài khoản ngoại tệ về. |
| **Include Child Companies** | Nếu tích chọn, báo cáo sẽ bao gồm cả dữ liệu từ các công ty con trực thuộc công ty đã chọn. |
| **Account Filter** | Lọc báo cáo theo các nhóm tài khoản hoặc tài khoản cụ thể. |

## 6. Lưu ý quan trọng

*   **Kiểm tra tỷ giá:** Đảm bảo rằng tỷ giá hối đoái (Exchange Rate) đã được cập nhật đầy đủ cho các ngày giao dịch để tránh sai lệch khi quy đổi tiền tệ trong báo cáo hợp nhất.
*   **Bút toán loại trừ:** Khi thực hiện hợp nhất, hãy lưu ý các **Bút toán (JE)** loại trừ các giao dịch nội bộ giữa các công ty con để tránh tình trạng trùng lặp doanh thu hoặc tài sản.
*   **Đồng nhất danh mục:** Để báo cáo hợp nhất có ý nghĩa, các công ty con nên sử dụng chung một **Chart of Accounts** (Hệ thống tài khoản) hoặc có sự ánh xạ (mapping) tài khoản tương đương chính xác.

## 7. Liên kết đến trang liên quan

*   [Bảng cân đối thử (Trial Balance)](trial-balance.md)
*   [Quản lý đa công ty (Multi-company Setup)](multi-company-setup.md)
*   [Hướng dẫn Bút toán (Journal Entry)](journal-entry.md)
*   [Quản lý Tiền tệ (Currency Setup)](currency-setup.md)