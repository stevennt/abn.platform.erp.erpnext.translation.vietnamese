<!-- add-breadcrumbs -->
# Nhập Séc hậu ngày

Séc hậu ngày là loại séc được ghi ngày vào một ngày trong tương lai. Đối tác thường đưa séc hậu ngày như một khoản thanh toán trước. Loại séc này sẽ chỉ được thanh toán khi đến ngày ghi trên séc.

Trong ERPNext, hãy tạo Bút toán thanh toán cho séc hậu ngày.

#### Bút toán thanh toán mới

Để mở một bút toán mới, hãy đi tới

`Explore > Accounting > Payment Entry > New`

#### Thiết lập Ngày hạch toán

Giả sử Ngày ghi trên séc của bạn là ngày 31 tháng 12 năm 2016 (hoặc bất kỳ ngày nào trong tương lai). Kết quả là, bút toán này trong sổ cái ngân hàng của bạn sẽ xuất hiện vào Ngày hạch toán được cập nhật.

![Posting Date in Payment Entry](/docs/v13/assets/img/articles/posting-date-in-payment-entry.png)

Lưu ý: Ngày tham chiếu của Bút toán thanh toán phải bằng hoặc nhỏ hơn Ngày hạch toán.

#### Bước 3: Lưu và Xác nhận

Sau khi nhập các chi tiết bắt buộc, hãy Lưu và Xác nhận Bút toán thanh toán.

#### Điều chỉnh Nhập Séc hậu ngày

Bạn có thể điều chỉnh Bút toán thanh toán hậu ngày đối với một hóa đơn thông qua [Công cụ Đối chiếu thanh toán](/docs/v13/user/manual/en/accounts/payment-reconciliation).

Khi séc được thanh toán, tức là vào ngày thực tế ghi trên séc, bạn có thể cập nhật Ngày thanh toán của nó thông qua [Công cụ Đối chiếu ngân hàng](/docs/v13/user/manual/en/accounts/bank-reconciliation).

Trong Hệ thống tài khoản, bạn có thể thấy giá trị của Bút toán thanh toán này đã được phản ánh đối với Tài khoản ngân hàng. Bạn nên kiểm tra **Báo cáo đối chiếu ngân hàng**, một báo cáo trong phân hệ kế toán để biết sự chênh lệch giữa số dư ngân hàng theo hệ thống và số dư thực tế trên sao kê của ngân hàng.
<!-- markdown -->

{next}