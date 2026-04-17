<!-- add-breadcrumbs -->
# Nhập số dư tồn kho đầu kỳ cho Mặt hàng theo Số serial và Lô hàng

Đối với các mặt hàng có quản lý Số serial và Lô hàng, việc nhập số dư tồn kho đầu kỳ được thực hiện thông qua Phiếu kho. [Nhấp vào đây để tìm hiểu cách quản lý tồn kho theo số serial trong ERPNext](../serial-no.html.md).

**Câu hỏi:** Tại sao việc nhập Số dư đầu kỳ cho Mặt hàng theo Số serial và Lô hàng không thể cập nhật thông qua Đối chiếu tồn kho?

Trong ERPNext, mức tồn kho của một mặt hàng theo số serial được tính toán dựa trên số lượng Số serial cụ thể của mặt hàng đó. Do đó, trừ khi các Số serial được tạo cho mặt hàng, mức tồn kho sẽ không được cập nhật chính xác. Trong Công cụ Đối chiếu tồn kho, bạn chỉ có thể điều chỉnh số lượng tổng quát của một mặt hàng mà không thể quản lý chi tiết từng Số serial hoặc Lô hàng.

### Số dư đầu kỳ cho Mặt hàng theo Số serial và Lô hàng

Dưới đây là các bước để tạo Phiếu kho nhập số dư tồn kho đầu kỳ cho Mặt hàng theo Số serial và Lô hàng.

#### Bước 1: Tạo Phiếu kho mới

`Kho > Phiếu kho > Mới`

#### Bước 2: Chọn Mục đích

Mục đích của Phiếu kho phải được chọn là `Nhập vật tư`.

#### Bước 3: Cập nhật Ngày hạch toán

Ngày hạch toán phải là ngày bạn muốn ghi nhận số dư đầu kỳ cho mặt hàng vào sổ cái và sổ kho.

#### Bước 4: Cập nhật Kho

Chọn Kho nơi số dư đầu kỳ của mặt hàng sẽ được ghi nhận.

#### Bước 5: Chọn Mặt hàng

Chọn các Mặt hàng cần cập nhật số dư đầu kỳ.

#### Bước 6: Cập nhật Số lượng và Chi tiết Số serial/Lô hàng

*   **Đối với mặt hàng theo Số serial:** Nhập số lượng tương ứng với số lượng Số serial đang có trong kho. Bạn cần nhập chi tiết các Số serial tương ứng. Nếu các Số serial được cấu hình để tự động tạo theo Tiền tố, bạn có thể không cần nhập thủ công. Nhấp [tại đây](serial-no-naming.html.md) để tìm hiểu thêm về cách đặt tên Số serial.
*   **Đối với mặt hàng theo Lô hàng:** Cung cấp ID Lô hàng mà số dư đầu kỳ sẽ được cập nhật vào. Hãy đảm bảo bạn đã chuẩn bị sẵn danh mục lô. Để tạo Lô hàng mới, hãy vào:
    `Kho > Thiết lập > Lô hàng > Mới`

    [Nhấp vào đây để tìm hiểu cách quản lý tồn kho theo lô trong ERPNext.](managing-batch-wise-inventory.html.md)

#### Bước 7: Cập nhật Giá trị tính giá mặt hàng

Cập nhật giá trị tính giá (giá trị trên mỗi đơn vị) của mặt hàng. Nếu các lô hàng hoặc các đơn vị khác nhau của cùng một mặt hàng có giá trị tính giá khác nhau, bạn nên tách chúng thành các dòng riêng biệt để đảm bảo chính xác cho việc tính giá tồn kho.

#### Bước 8: Tài khoản chênh lệch

Theo hệ thống tính giá tồn kho thường xuyên, mọi giao dịch kho đều tạo ra Bút toán kế toán. Hệ thống kế toán kép yêu cầu Tổng Nợ phải khớp với Tổng Có. Khi Xác nhận Phiếu kho, hệ thống sẽ ghi Nợ tài khoản Kho bằng tổng giá trị của các mặt hàng. Để cân bằng bút toán này, bạn cần chọn một tài khoản phù hợp (thường là tài khoản Tài sản hoặc tài khoản Mở đầu) làm Tài khoản chênh lệch.

<img alt="Difference Account" class="screenshot" src="https://docs.erpnext.com/docs/v16/assets/img/articles/difference-account-1.png">

#### Bước 9: Lưu và Xác nhận Phiếu kho

Sau khi kiểm tra kỹ các thông tin, nhấn **Lưu** và sau đó nhấn **Xác nhận**. Khi Phiếu kho được Xác nhận, Bút toán sẽ được ghi nhận vào sổ cái, số lượng tồn kho và giá trị tồn kho sẽ được cập nhật vào Ngày hạch toán đã chọn.

<div>
    <div class="embed-container">
        <iframe src="https://www.youtube.com/embed/nlHX0ZZ84Lw?start=120" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
        </iframe>
    </div>
</div>