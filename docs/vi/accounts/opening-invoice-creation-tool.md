<!-- add-breadcrumbs -->
# Công cụ tạo Hóa đơn đầu kỳ

Công cụ tạo Hóa đơn đầu kỳ cho phép nhập dữ liệu của các Hóa đơn mua hàng hoặc Hóa đơn bán hàng còn tồn đọng vào ERPNext. Công cụ cụ thể này được sử dụng thay thế cho Công cụ Nhập dữ liệu (Data Import Tool) trong các trường hợp dữ liệu Mặt hàng không liên quan và cần nhập các số dư còn tồn đọng đối với Khách hàng/Nhà cung cấp vào ERPNext.

Để truy cập Công cụ tạo Hóa đơn đầu kỳ, hãy đi đến:

> Trang chủ > Kế toán > Đầu kỳ và Kết kỳ > Công cụ tạo Hóa đơn đầu kỳ

## 1: Cách nhập Hóa đơn đầu kỳ

1. Chọn Công ty mà bạn muốn nhập số dư đầu kỳ.

2. Chọn Loại hóa đơn. Việc chọn Bán hàng hoặc Mua hàng sẽ lần lượt tạo ra các Hóa đơn bán hàng hoặc Hóa đơn mua hàng.

3. Đánh dấu vào ô "Create Missing Party" sẽ tự động tạo khách hàng hoặc nhà cung cấp nếu chưa có dựa trên tên được cung cấp trong cột Đối tác (Party).

    <img class="screenshot" alt="Opening Invoice Creation Tool" src="https://docs.erpnext.com/docs/v13/assets/img/setup/opening-invoice-creation-tool.png">

4. Điền vào bảng Hóa đơn. Bảng bao gồm các trường sau:
    - **Party (Đối tác)**: Bạn có thể chọn Khách hàng/Nhà cung cấp hiện có hoặc nhập tên của một đối tác mới, đối tác này sẽ được tự động tạo.
    - **Posting Date (Ngày hạch toán)**: Ngày mà hóa đơn sẽ được hạch toán.
    - **Due Date (Hạn thanh toán)**: Ngày mà sau đó hóa đơn sẽ bị quá hạn.
    - **Item Name (Tên mặt hàng)**: (Tùy chọn) Tên mặt hàng được nhập ở đây sẽ được hiển thị trong bảng mặt hàng của hóa đơn.
    - **Outstanding Amount (Số tiền còn nợ)**: Số tiền còn tồn đọng của hóa đơn.

> **Mẹo**: Bạn có thể nhấp vào nút tải xuống để tải một bảng tính excel giúp bạn điền dữ liệu phù hợp một cách dễ dàng. Nếu bạn đã tải bảng tính excel, hãy sử dụng nút Tải lên (Upload) để tải nó lên. Sau khi bạn tải bảng lên, bảng sẽ được điền đầy đủ các dòng dữ liệu phù hợp.