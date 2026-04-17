# Bảng cân đối thử hợp nhất (Consolidated Trial Balance)

Bảng cân đối thử hợp nhất cung cấp cái nhìn tổng thể về tình hình tài chính của toàn bộ tập đoàn hoặc nhóm công ty bằng cách tổng hợp dữ liệu từ nhiều công ty khác nhau trong cùng một hệ thống ERPNext.

## 1. Giới thiệu tính năng <span style="color: #2ecc71;">(Mới trong v16)</span>

Trong phiên bản v16, tính năng **Bảng cân đối thử hợp nhất** đã được nâng cấp mạnh mẽ để hỗ trợ các doanh nghiệp đa quốc gia và đa công ty. 

*   **Hợp nhất đa công ty:** Tự động cộng dồn số dư từ các công ty con vào một báo cáo duy nhất.
*   **Tự động quy đổi tiền tệ:** Hệ thống tự động lấy tỷ giá hối đoái tại thời điểm báo cáo để quy đổi tất cả các loại tiền tệ của các công ty con về một loại tiền tệ báo cáo chung (Reporting Currency).
*   **Phân tích đa chiều:** Cho phép lọc và xem dữ liệu theo từng công ty con hoặc xem tổng thể toàn tập đoàn.

## 2. Điều kiện tiên quyết

Để sử dụng báo cáo này một cách chính xác, bạn cần đảm bảo:
*   Hệ thống đã được thiết lập cấu trúc **Multi-company** (Đa công ty).
*   Các công ty con đã được liên kết trong cùng một nhóm doanh nghiệp (nếu có).
*   Các giao dịch tài chính (Bút toán - JE) đã được **Xác nhận (Submit)**.
*   Đã thiết lập tỷ giá hối đoảng trong hệ thống để phục vụ việc quy đổi tiền tệ tự động.

## 3. Hướng dẫn từng bước

Để truy cập và chạy báo cáo Bảng cân đối thử hợp nhất, hãy làm theo các bước sau:

1.  Truy cập vào module **Kế toán (Accounting)**.
2.  Trong mục **Báo cáo (Reports)**, tìm và chọn **Bảng cân đối thử hợp nhất (Consolidated Trial Balance)**.
3.  **Thiết lập bộ lọc:**
    *   **Company:** Chọn công ty mẹ hoặc chọn nhiều công ty con muốn hợp nhất.
    *   **Fiscal Year:** Chọn năm tài chính tương ứng.
    *   **Accounting View:** Chọn chế độ xem theo tài khoản hoặc theo nhóm tài khoản.
    *   **Reporting Currency:** Chọn loại tiền tệ bạn muốn quy đổi tất cả số dư về (ví dụ: VND).
4.  Nhấn nút **Tạo báo cáo (Show Report)**.
5.  Hệ thống sẽ hiển thị bảng tổng hợp bao gồm: Tên tài khoản, số dư nợ, số dư có của từng công ty và cột tổng hợp cuối cùng sau khi đã quy đổi tiền tệ.

## 4. Ảnh minh họa

![Bảng cân đối thử hợp nhất](../../screenshots/reports/trial-balance.png)

## 5. Các tùy chọn/cài đặt liên quan

*   **Include Child Companies:** Nếu được tích chọn, báo cáo sẽ tự động bao gồm dữ liệu từ tất cả các công ty con trực thuộc công ty chính đã chọn.
*   **Exchange Rate Date:** Chọn ngày để hệ thống lấy tỷ giá hối đoái dùng cho việc quy đổi tiền tệ.
*   **Filter by Dimension:** Cho phép lọc báo cáo theo các chiều dữ liệu khác như Trung tâm chi phí (Cost Center) nếu đã được cấu hình.

## 6. Lưu ý quan trọng

*   **Kiểm tra Bút toán (JE):** Đảm bảo tất cả các **Bút toán (JE)** liên quan đến các giao dịch liên công ty đã được **Xác nhận (Submit)** để tránh sai lệch số liệu hợp nhất.
*   **Đồng nhất tài khoản:** Để báo cáo hợp nhất có ý nghĩa, các công ty con nên sử dụng cùng một **Sơ đồ tài khoản (Chart of Accounts)** hoặc có sự ánh xạ tài khoản tương ứng.
*   **Tỷ giá quy đổi:** Nếu số dư tài khoản bằng ngoại tệ quá lớn, hãy kiểm tra lại bảng tỷ giá để đảm bảo giá trị quy đổi sang tiền tệ báo cáo là chính xác.

## 7. Liên kết đến trang liên quan

*   [Bảng cân đối thử (Trial Balance)](trial-balance.md)
*   [Sơ đồ tài khoản (Chart of Accounts)](chart-of-accounts.md)
*   [Quản lý đa công ty (Multi-company Setup)](multi-company-setup.md)
*   [Bút toán (Journal Entry)](journal-entry.md)