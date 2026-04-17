<!-- add-breadcrumbs -->
# Tồn kho đầu kỳ

**Tồn kho đầu kỳ là số lượng và giá trị của các mặt hàng mà một công ty có sẵn để bán hoặc sử dụng tại thời điểm bắt đầu một kỳ kế toán.**

Tồn kho cuối kỳ của kỳ kế toán trước sẽ trở thành tồn kho đầu kỳ của kỳ kế toán hiện tại. Trong phiên bản v16, việc quản lý tồn kho đầu kỳ được tối ưu hóa với hệ thống Dự trữ tồn kho (Stock Reservation) và Kế toán tồn kho theo từng mặt hàng (Item-Level Stock Accounting).

## 1. Điều kiện tiên quyết

* Tạo [Kho](warehouse.md).
* Liên kết Kho với các sổ cái kế toán phù hợp.
* Thiết lập các [Mặt hàng](item.md) với phương pháp tính giá trị tồn kho chính xác.

## 2. Tồn kho đầu kỳ cho các Mặt hàng không theo số serial

Để hạch toán tồn kho đầu kỳ cho các mặt hàng thông thường, hãy truy cập trang [Đối chiếu tồn kho](stock-reconciliation.md).

## 3. Tồn kho đầu kỳ cho các Mặt hàng theo số serial và theo Lô hàng

Để đảm bảo tính truy xuất nguồn gốc (Traceability), bạn cần tạo các bản ghi [Lô hàng](batch.md) và [Số serial](serial-no.md) trước. 

Để hạch toán tồn kho đầu kỳ cho các mặt hàng theo số serial và theo lô hàng:

1. Đi đến **Kho > Giao dịch kho > [Phiếu kho](stock-entry.md) > Mới**.
2. Chọn 'Material Receipt' trong 'Loại phiếu kho'.
3. Chọn Kho trong 'Kho đích mặc định'.
4. Trong bảng Mặt hàng, chọn Mã mặt hàng, Số lượng và Đơn giá cơ bản.
5. Đối với các mặt hàng theo lô, chọn [Lô hàng](batch.md).
6. Đối với các mặt hàng theo số serial, chọn Số serial.
7. [Lưu](save.md) và [Xác nhận](submit.md).

*Lưu ý: Với các mặt hàng có quản lý theo lô/serial, bạn có thể sử dụng [Báo cáo truy xuất nguồn gốc lô/serial](serial-batch-traceability-report.md) để kiểm tra tính chính xác sau khi nhập kho.*

## 4. Các tính năng mới trong v16 liên quan đến Tồn kho

* **Hệ thống Dự trữ tồn kho (Stock Reservation System):** Cho phép giữ chỗ số lượng tồn kho cho các Đơn bán hàng (SO) hoặc lệnh sản xuất, giúp việc tính toán tồn kho đầu kỳ và tồn kho khả dụng chính xác hơn.
* **Chi phí thu mua (Landed Cost) cho Phiếu kho:** Cho phép phân bổ các chi phí liên quan (vận chuyển, thuế...) vào giá trị tồn kho ngay khi thực hiện [Phiếu nhập hàng](pr.md) hoặc [Phiếu kho](stock-entry.md).
* **Kế toán tồn kho theo từng Mặt hàng (Item-Level Stock Accounting):** Cung cấp cái nhìn chi tiết về giá trị sổ cái cho từng mặt hàng cụ thể.
* **Xem trước Sổ cái (Ledger Preview):** Kiểm tra nhanh các [Bút toán](je.md) liên quan đến giá trị tồn kho ngay tại giao diện kho.

## 5. Video
<div>
    <div class="embed-container">
        <iframe src="https://www.youtube.com/embed/nlHX0ZZ84Lw?end=120" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
        </iframe>
    </div>
</div>

### 6. Các chủ đề liên quan
1. [Kế toán tồn kho](accounting-of-inventory-stock.md)
2. [Phiếu kho](stock-entry.md)
3. [Đối chiếu tồn kho](stock-reconciliation.md)
4. [Lô hàng](batch.md)

{next}