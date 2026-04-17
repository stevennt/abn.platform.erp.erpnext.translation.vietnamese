<!-- add-breadcrumbs -->
# Quy tắc trợ cấp thôi việc

> Tính năng này được giới thiệu trong Phiên bản 13, sẽ là một phần của Phân hệ Bảng lương riêng biệt.

**Quy tắc trợ cấp thôi việc là tập hợp các quy tắc được quy định bởi Trung ương hoặc Tiểu bang được sử dụng trong quá trình tính toán Số tiền trợ cấp thôi việc**

Trong ERPNext, bạn có thể xác định các Quy tắc trợ cấp thôi việc khác nhau dựa trên các Khu vực khác nhau.

Để truy cập Quy tắc trợ cấp thôi việc, hãy đi đến:

> Home > Payroll > Gratuity Rule

## 1. Điều kiện tiên quyết

Trước khi tạo Quy tắc trợ cấp thôi việc, bạn nên tạo các mục sau:

1. [Employee](/docs/v13/user/manual/en/human-resources/employee)
1. [Salary Component](/docs/v13/user/manual/en/human-resources/salary-component)

## 2. Cách tạo Quy tắc trợ cấp thôi việc

1. Đi đến Gratuity Rule > New
1. Chọn các Thành phần áp dụng (Applicable Components). Các Thành phần lương này sẽ đóng góp vào quá trình Tính toán trợ cấp thôi việc.
1. Chọn "Calculate Gratuity Amount based on" (Tính Số tiền trợ cấp thôi việc dựa trên)
1. Xác định Quy tắc trợ cấp thôi việc
1. Lưu

<img class="screenshot" alt="Gratuity Rule" src="https://docs.erpnext.com/docs/v13/assets/img/human-resources/gratuity-rule.png">

## 3. Các thuộc tính bổ sung

Một số thuộc tính bổ sung được sử dụng trong khi tính toán trợ cấp thôi việc được xác định dưới đây.

### 3.1 Phương pháp tính Kinh nghiệm làm việc:
ERPNext cung cấp hai phương pháp khác nhau để tính toán Kinh nghiệm làm việc.

1. Phương pháp làm tròn Kinh nghiệm làm việc (Round off Work Experience): Làm tròn kinh nghiệm hiện tại của bạn. Ví dụ: nếu nhân viên có tổng kinh nghiệm là 3 năm 6 tháng sẽ được tính là 4 năm kinh nghiệm.
1. Lấy số năm hoàn thành chính xác (Take Exact Completed Year).


### 3.2 Tính Số tiền trợ cấp thôi việc dựa trên:

Hãy xem xét ví dụ sau để hiểu cách tính toán.

<img class="screenshot" alt="gratuity-rule-example" src="https://docs.erpnext.com/docs/v13/assets/img/human-resources/gratuity-rule-example.png">

1. **Mức hiện tại (Current slab):** Nếu việc tính Số tiền trợ cấp thôi việc dựa trên Mức hiện tại, thì số tiền sẽ là tích của Kinh nghiệm làm việc (tính theo năm), Tỷ lệ của Thu nhập áp dụng và tổng các Thành phần thu nhập áp dụng. Dựa trên các Quy tắc/mức trợ cấp thôi việc ở trên, nếu một nhân viên có 5 năm kinh nghiệm, thì họ sẽ thuộc mức thứ ba. Việc tính Số tiền trợ cấp thôi việc sẽ như sau:

> Số tiền trợ cấp thôi việc = 5 * 0.467 * (Arrear + Basic)

2. **Tổng của tất cả các mức trước đó (Sum of all previous slabs):** Nếu việc tính Số tiền trợ cấp thôi việc dựa trên Tổng của tất cả các mức trước đó, thì số tiền sẽ là tổng của tích các mức riêng lẻ cho đến năm kinh nghiệm và tổng các Thành phần thu nhập áp dụng. Dựa trên các Quy tắc/mức trợ cấp thôi việc ở trên, nếu một nhân viên có 5 năm kinh nghiệm, thì việc tính Số tiền trợ cấp thôi việc sẽ như sau:


> Số tiền trợ cấp thôi việc = [(1 * 0) + (2 * 0.233) + (2 * 0.467)]*(Arrear + Basic)