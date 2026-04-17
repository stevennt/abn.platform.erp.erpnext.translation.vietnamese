<!-- add-breadcrumbs -->
#Nhập số dư tồn kho đầu kỳ cho Mặt hàng theo Số serial và Lô hàng

Đối với các mặt hàng có quản lý Số serial và Số lô, việc nhập số dư tồn kho đầu kỳ cho chúng được cập nhật thông qua Phiếu kho. [Nhấp vào đây để tìm hiểu cách quản lý tồn kho theo số serial trong ERPNext](../serial-no.html.md).

**Câu hỏi:** Tại sao việc nhập Số dư đầu kỳ cho Mặt hàng theo Số serial và Lô hàng không thể cập nhật thông qua Đối chiếu tồn kho?

Trong ERPNext, mức tồn kho của một mặt hàng theo số serial được tính toán dựa trên số lượng Số serial của mặt hàng đó. Do đó, trừ khi các Số serial được tạo cho mặt hàng theo số serial, mức tồn kho của nó sẽ không được cập nhật. Trong Công cụ Đối chiếu tồn kho, bạn chỉ có thể cập nhật số lượng đầu kỳ của một mặt hàng, chứ không thể cập nhật Số serial và Số lô.

### Số dư đầu kỳ cho Mặt hàng theo Số serial

Dưới đây là các bước để tạo phiếu nhập số dư tồn kho đầu kỳ cho Mặt hàng theo Số serial và Lô hàng.

#### Bước 1: Phiếu kho mới

`Kho > Phiếu kho > Mới`

#### Bước 2: Chọn Mục đích

Mục đích Phiếu kho nên được cập nhật là `Nhập vật tư`.

#### Bước 3: Cập nhật Ngày hạch toán

Ngày hạch toán phải là ngày mà bạn muốn cập nhật số dư đầu kỳ cho một mặt hàng.

#### Bước 4: Cập nhật Kho đích

Kho đích sẽ là kho mà số dư đầu kỳ của mặt hàng sẽ được cập nhật vào.

#### Bước 5: Chọn Mặt hàng

Chọn các Mặt hàng cần cập nhật số dư đầu kỳ.

#### Bước 6: Cập nhật Số lượng đầu kỳ

Đối với mặt hàng theo số serial, hãy cập nhật số lượng tương ứng với số lượng Số serial đang có.

Đối với mặt hàng theo số serial, hãy ghi các Số serial tương đương với Số lượng của nó. Hoặc nếu các Số serial được cấu hình để tạo dựa trên Tiền tố, thì không cần phải nhập Số serial một cách thủ công. Nhấp [tại đây](serial-no-naming.html.md) để tìm hiểu thêm về cách đặt tên Số serial.

Đối với mặt hàng theo lô, hãy cung cấp ID Lô mà số dư đầu kỳ sẽ được cập nhật. Hãy chuẩn bị sẵn danh mục lô và cập nhật nó cho Mặt hàng theo lô. Để tạo Lô mới, hãy vào:

`Kho > Thiết lập > Lô hàng > Mới`

[Nhấp vào đây để tìm hiểu cách quản lý tồn kho theo lô trong ERPNext.](managing-batch-wise-inventory.html.md)

#### Bước 7: Cập nhật Giá trị tính giá mặt hàng

Cập nhật giá trị tính giá, đây sẽ là giá trị trên mỗi đơn vị của mặt hàng. Nếu các đơn vị khác nhau của cùng một mặt hàng có giá trị tính giá khác nhau, chúng nên được cập nhật ở một dòng riêng biệt, với các Giá trị tính giá khác nhau.

#### Bước 8: Tài khoản chênh lệch

Theo hệ thống tính giá tồn kho thường xuyên, bút toán kế toán được tạo cho mọi giao dịch kho. Hệ thống kế toán bút toán kép yêu cầu Tổng Nợ phải khớp với Tổng Có trong một bút toán. Khi Xác nhận Phiếu kho, hệ thống sẽ ghi Nợ tài khoản Kho bằng tổng giá trị của các mặt hàng. Để cân bằng điều này, chúng ta sử dụng tài khoản Mở đầu Tạm thời làm Tài khoản chênh lệch.

<img alt="Difference Account" class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/articles/difference-account-1.png">

#### Bước 9: Lưu và Xác nhận Phiếu kho

Khi Xác nhận Phiếu kho, bút toán sổ cái kho sẽ được ghi nhận, và số dư đầu kỳ sẽ được cập nhật cho các mặt hàng vào một Ngày hạch toán nhất định.


<div>
    <div class="embed-container">
        <iframe src="https://www.youtube.com/embed/nlHX0ZZ84Lw?start=120" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
        </iframe>
    </div]
</div]

<!-- markdown -->