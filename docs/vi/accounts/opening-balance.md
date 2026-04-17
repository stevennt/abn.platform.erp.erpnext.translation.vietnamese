<!-- add-breadcrumbs -->
# Số dư đầu kỳ trong Kế toán

**Số dư đầu kỳ là số dư được chuyển sang vào đầu một kỳ kế toán từ cuối kỳ kế toán trước đó hoặc khi mới bắt đầu hoạt động.**

Điều này cũng áp dụng khi bắt đầu một Công ty mới và bạn muốn cập nhật các số dư ngoại tuyến của mình vào ERPNext.

## 1. Giới thiệu

Nếu bạn là một công ty mới, bạn sẽ có rất ít số dư đầu kỳ cần nhập. Tuy nhiên, nếu bạn đang chuyển đổi từ một hệ thống kế toán cũ như Tally hoặc phần mềm dựa trên Fox Pro, bạn sẽ có một lượng dữ liệu đáng kể cần được nhập dưới dạng số dư đầu kỳ.

Chúng tôi khuyên bạn nên bắt đầu sử dụng ERPNext cho kế toán từ một năm tài chính mới, nhưng bạn cũng có thể bắt đầu vào giữa kỳ. Để thiết lập các tài khoản của mình, bạn sẽ cần những thứ sau cho "ngày" bạn bắt đầu sử dụng kế toán trong ERPNext:

### Tài sản
1. Tài sản tồn kho (hàng tồn kho trong tay).
1. Tài sản cố định như nội thất, máy tính, v.v.
1. Khoản phải thu (AR) tức là các hóa đơn chưa thanh toán mà bạn đã gửi cho Khách hàng.
1. Tài sản lưu động như số dư ngân hàng, tiền mặt tại quỹ, tiền gửi, v.v.

### Nợ phải trả

1. Tài khoản vốn như vốn của cổ đông (hoặc chủ sở hữu)
1. Nợ ngắn hạn như các khoản vay, lương phải trả, v.v.
1. Khoản phải trả (AP) tức là các hóa đơn chưa thanh toán mà Nhà cung cấp đã gửi cho bạn


Nếu trước đây bạn đã sử dụng phần mềm kế toán khác, bạn nên **đóng** các báo cáo tài chính trong phần mềm đó trước. Số dư cuối kỳ của các tài khoản nên được cập nhật làm số dư đầu kỳ trong ERPNext. Trước khi bắt đầu cập nhật số dư đầu kỳ, hãy đảm bảo rằng [Hệ thống tài khoản](chart-of-accounts.md) của bạn đã có đầy đủ các Tài khoản cần thiết.

Các bút toán đầu kỳ có thể được tạo bằng Công cụ tạo Hóa đơn đầu kỳ trong ERPNext.

> Bút toán đầu kỳ chỉ dành cho các tài khoản Bảng cân đối kế toán và không dành cho các tài khoản Báo cáo kết quả hoạt động kinh doanh.

## 2. Số dư đầu kỳ của Tài sản

2.1 [Tài sản cố định](opening-balance/fixed_assets.md)

2.2 [Tài sản tồn kho](../stock/opening-stock.md)

2.3 [Khoản phải thu](opening-balance/accounts_receivable.md)

2.4 [Tài sản lưu động](opening-balance/current_assets.md)

## 3. Số dư đầu kỳ của Nợ phải trả

3.1 [Tài khoản vốn](opening-balance/capital_accounts.md)

3.2 [Nợ ngắn hạn](opening-balance/current_liabilities.md)

3.3 [Khoản phải trả](opening-balance/accounts_payable.md)

## 4. Xác minh Số dư đầu kỳ

Sau khi tất cả tài sản và nợ phải trả đã được nhập, số dư của sổ cái **Số dư tạm thời** phải bằng không.

## 5. Video
<div>
  <div class='embed-container'>
    <iframe src='https://www.youtube.com/embed//U5wPIvEn-0c' frameborder='0' allowfullscreen>
    </iframe>
  </div>
</div>

### 6. Các chủ đề liên quan
1. [Hệ thống tài khoản](chart-of-accounts.md)
1. [Bút toán](journal-entry.md)
1. [Bút toán thanh toán](payment-entry.md)
1. [Đối chiếu thanh toán](payment-reconciliation.md)

{next}