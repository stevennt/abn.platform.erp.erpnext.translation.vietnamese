---
title: Trung tâm chi phí phân bổ
add_breadcrumbs: 1
show_sidebar: 0

metatags:
 description: Trung tâm chi phí phân bổ là một Trung tâm chi phí mà trong đó nhiều Trung tâm chi phí khác được gắn với một tỷ lệ phần trăm phù hợp.
 keywords: frappe, erpnext, accounting reports, Cost Center, GL Entry.
---

<!-- add-breadcrumbs -->
# Trung tâm chi phí phân bổ

**Trung tâm chi phí phân bổ là một Trung tâm chi phí mà trong đó nhiều Trung tâm chi phí khác được gắn với một tỷ lệ phần trăm phù hợp.**

Nếu một doanh nghiệp có một Trung tâm chi phí chính với các Trung tâm chi phí phụ thuộc. Trong mỗi giao dịch của Trung tâm chi phí chính, việc cập nhật ngân sách, lợi nhuận và thua lỗ cho từng Trung tâm chi phí phụ thuộc một cách thủ công theo tỷ lệ phân bổ của Trung tâm chi phí chính là rất khó khăn. Tính năng này giúp tự động hóa quá trình nhập liệu thủ công đó.

Ví dụ, trong doanh nghiệp của bạn, nếu Trung tâm chi phí 'B' và 'C' phụ thuộc vào Trung tâm chi phí 'A' với tỷ lệ lần lượt là 20% và 80%. Khi đó, bạn có thể thiết lập 'A' là một Trung tâm chi phí phân bổ. Điều này giúp phản ánh thu nhập, chi phí và ngân sách của 'A' vào 'B' và 'C' theo các tỷ lệ đã phân bổ.

Trong ERPNext, bạn có thể tạo Trung tâm chi phí phân bổ và sử dụng chúng trong các giao dịch và báo cáo.

## 1. Cách tạo Trung tâm chi phí phân bổ
1. Đi tới danh sách Trung tâm chi phí, nhấn vào Mới.
1. Nhập tên Trung tâm chi phí.
1. Chọn Trung tâm chi phí cha.
1. Tích vào ô **Enable Distributed Cost Center** (Cho phép Trung tâm chi phí phân bổ): Khi bật tùy chọn này, bảng trung tâm chi phí phân bổ sẽ hiển thị. Tại đây, hãy chọn các Trung tâm chi phí và phân bổ tỷ lệ phần trăm tương ứng.
1. Sau khi hoàn tất, nhấn Lưu.

  ![Distributed Cost Center](/docs/v13/assets/img/accounts/distributed-cost-centers.png)


Các báo cáo sau sẽ được cập nhật tự động khi bộ lọc Trung tâm chi phí được thêm vào:

  * [Báo cáo kế toán](/docs/v13/user/manual/en/accounts/accounting-reports)
    * Báo cáo tài chính
    * Biến động ngân sách
    * Sổ cái
  * [Phân tích khả năng sinh lời](/docs/v13/user/manual/en/accounts/articles/tracking-project-profitability-using-cost-center)

### 2. Các chủ đề liên quan
1. [Trung tâm chi phí](/docs/v13/user/manual/en/accounts/cost-center)

{next}