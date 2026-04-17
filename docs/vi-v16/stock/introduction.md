<!-- add-breadcrumbs -->
# Giới thiệu

Các doanh nghiệp thường đầu tư một phần lớn nguồn lực tài chính vào các mặt hàng tồn kho mà họ kinh doanh. Với ERPNext, bạn luôn có thể có cái nhìn tổng quan về tình trạng tồn kho, việc bổ sung hàng, thu mua, bán hàng và nhiều hoạt động khác.

## 1. Các giao dịch Kho cốt lõi

Có ba loại bút toán **chính**:

* **Phiếu nhập hàng (PR)**: Các mặt hàng nhận được từ Nhà cung cấp dựa trên Đơn mua hàng.
* **Phiếu kho (SE)**: Các mặt hàng được chuyển từ Kho này sang Kho khác.
* **Phiếu giao hàng (DN)**: Các mặt hàng được giao cho Khách hàng.

Ngoài các giao dịch cốt lõi này, còn có các chứng từ khác có sẵn trong mô-đun Tồn kho của ERPNext để quản lý Đối chiếu tồn kho, Giá mặt hàng, quản lý Số lô (Batch), Số Serial, Kiểm tra chất lượng (QI), hàng trả lại, v.v.

### Các tính năng mới trong phiên bản v16

ERPNext v16 mang đến những cải tiến mạnh mẽ để tối ưu hóa quản lý chuỗi cung ứng và kế toán kho:

* **Hệ thống Giữ hàng (Stock Reservation System)**: Cho phép giữ trước các mặt hàng trong kho cho các Đơn bán hàng (SO) hoặc các yêu cầu cụ thể, giúp lập kế hoạch cung ứng chính xác hơn.
* **Báo cáo Truy xuất nguồn gốc Số Serial/Lô hàng (Serial/Batch Traceability Report)**: Cung cấp khả năng theo dõi toàn diện lịch sử di chuyển của từng lô hàng hoặc số serial từ khi nhập kho đến khi xuất kho.
* **Chi phí vận chuyển tính vào giá trị hàng nhập (Landed Cost cho Stock Entry)**: Cho phép phân bổ các chi phí liên quan (vận chuyển, thuế, phí bốc xếp...) trực tiếp vào giá trị của mặt hàng khi thực hiện Phiếu nhập hàng, giúp phản ánh chính xác giá trị tồn kho.
* **Kế toán tồn kho theo từng mặt hàng (Item-Level Stock Accounting)**: Tăng cường độ chính xác trong việc hạch toán các bút toán (JE) liên quan đến giá trị tồn kho cho từng mặt hàng cụ thể.
* **Xem trước Sổ cái (Ledger Preview)**: Cho phép người dùng xem nhanh các bút toán liên quan ngay tại giao diện quản lý kho mà không cần chuyển đổi quá nhiều màn hình.

Dưới đây là chế độ xem Tóm tắt tồn kho mặt hàng trong ERPNext.

<img class="screenshot" alt="ERPNext Stock" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/stock-hero.png">

## 2. Một Nhà phân phối chia sẻ về việc triển khai ERPNext

Khi công ty khởi nghiệp dịch vụ an ninh Neural Integrated Services của Tarun Gupta bắt đầu phát triển, hệ thống ERP của ông đã không thể theo kịp và đầy lỗi mặc dù đã chi rất nhiều tiền. Đó là lúc Tarun quyết định chuyển sang một giải pháp tốt hơn và khám phá ra ERPNext.

<div>
    <div class='embed-container'>
        <iframe src='https://www.youtube.com/embed/7tPifRTfbGo' frameborder='0' allowfullscreen>
        </iframe>
    </div>
</div>