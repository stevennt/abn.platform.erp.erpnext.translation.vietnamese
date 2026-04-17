<!-- add-breadcrumbs -->
# Rút Lương từ Tài khoản Vốn chủ sở hữu

### Câu hỏi

Sau khi họp với kế toán của tôi tại Hoa Kỳ, tôi được thông báo rằng vì công ty của tôi là công ty một thành viên, tôi không nên trả lương cho chính mình theo cách ghi nhận vào tài khoản chi phí trực tiếp, mà thay vào đó nên thực hiện một khoản "rút vốn" (draw) ghi nhận vào bảng cân đối kế toán chứ không phải chi phí. Bạn có thể vui lòng hướng dẫn tôi cách thiết lập việc này trong ERPNext được không?

### Trả lời

1. Tạo một tài khoản cho **Vốn chủ sở hữu** (Owner's Equity) dưới mục Nợ phải trả nếu bạn chưa có. Tài khoản này sẽ là khoản đầu tư của bạn vào doanh nghiệp và lợi nhuận (hoặc lỗ) tích lũy. Nó sẽ có số dư bên "Có" (Credit).
2. Trong phiên bản 5, Vốn chủ sở hữu sẽ là một mục lớn mới (không nằm dưới Nợ phải trả). (Trong cả hai trường hợp, Tài sản = Vốn chủ sở hữu + Nợ phải trả, vì vậy bảng cân đối kế toán của bạn vẫn sẽ chính xác [Tìm hiểu thêm về tài khoản vốn chủ sở hữu](http://www.accountingcoach.com/blog/what-is-owners-equity)).
3. Tạo một tài khoản cho **Rút vốn của chủ sở hữu** (Owner's Draws) dưới mục **Vốn chủ sở hữu**.
4. Lưu ý rằng số dư của tài khoản **Rút vốn của chủ sở hữu** sẽ luôn là số âm vì bạn đang làm giảm số tiền từ tổng vốn chủ sở hữu / lợi nhuận của mình.

### Ví dụ

Ví dụ về bút toán (sử dụng Bút toán trong ERPNext) cho một khoản rút tiền $1000 sẽ là:

1. Có **Tiền mặt** $1000
2. Nợ **Rút vốn của chủ sở hữu** $1000

<!-- markdown -->

{next}