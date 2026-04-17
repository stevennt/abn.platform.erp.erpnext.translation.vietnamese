<!-- add-breadcrumbs -->
# Bậc thuế thu nhập

**Bậc thuế thu nhập là một tài liệu để xác định các mức thuế thu nhập dựa trên các bậc thu nhập chịu thuế khác nhau.**

Ở nhiều quốc gia, thuế thu nhập được đánh vào cá nhân nộp thuế dựa trên hệ thống bậc thuế, trong đó các mức thuế khác nhau được quy định cho các bậc khác nhau và các mức thuế này sẽ tăng dần theo sự gia tăng của bậc thu nhập. Trong ERPNext, bạn có thể xác định nhiều Bậc thuế thu nhập và liên kết chúng với cấu trúc lương của từng nhân viên thông qua Phân bổ cấu trúc lương.

Để truy cập Bậc thuế thu nhập, hãy đi tới:
> Home > Human Resources > Payroll > Income Tax Slab

## 1. Cách tạo Bậc thuế thu nhập

Để tạo một Bậc thuế thu nhập mới:

1. Nhập Tên cho Bậc thuế thu nhập, Công ty và ngày mà nó sẽ có Hiệu lực từ.
1. Bật hộp kiểm 'Allow Tax Exemption' nếu có thể áp dụng.
1. Lưu và Xác nhận.

## 2. Các tính năng

### 2.1 Các bậc thuế

Trong bảng Bậc thuế, bạn có thể xác định mức thuế cho các bậc thu nhập khác nhau. Để xác định bậc thuế, cần nhập Số tiền từ (From Amount) và Số tiền đến (To Amount). Đối với bậc đầu tiên, Số tiền từ là tùy chọn và đối với bậc cuối cùng, Số tiền đến là tùy chọn. Cả hai số tiền đều được bao gồm khi tính toán thuế dựa trên thu nhập chịu thuế.


<img class="screenshot" alt="Income Tax Slab" src="../assets/img/human-resources/income-tax-slab.png">

Bậc thuế có thể được áp dụng dựa trên các điều kiện cụ thể. Các điều kiện có thể được viết bằng cách sử dụng tất cả tên trường của các tài liệu Nhân viên, Cấu trúc lương, Phân bổ cấu trúc lương và Phiếu lương.

Ví dụ:

```python
// Áp dụng thuế nếu nhân viên sinh trong khoảng từ 31-12-1937 đến 01-01-1958 (Nhân viên từ 60 đến 80 tuổi)
date_of_birth > date(1937, 12, 31) and date_of_birth < date(1958, 01, 01)

// Áp dụng thuế theo giới tính nhân viên
gender == "Male"

// Áp dụng thuế theo Thành phần lương
base > 10000

// Thu nhập chịu thuế hàng năm lớn hơn 5 lakh
annual_taxable_earning > 500000
```

### 2.2 Các loại thuế và phí khác trên Thuế thu nhập

Nếu các loại thuế khác được áp dụng trên thuế thu nhập đã tính, bạn có thể nhập chúng bằng bảng này. Bạn cũng có thể xác định số tiền chịu thuế tối thiểu và tối đa mà loại thuế này sẽ được áp dụng.
Ví dụ, Phụ phí Y tế và Giáo dục được áp dụng bổ sung trên thuế thu nhập cho tất cả mọi người ở Ấn Độ.

<img class="screenshot" alt="Other Charged on Income Tax" src="../assets/img/human-resources/other-taxes-on-income-tax.png">


### 2.3 Các thuộc tính khác

- **Allow Tax Exemptions:** Miễn thuế có thể được cho phép đối với một Bậc thuế thu nhập cụ thể. Nếu được bật, khi tính toán thuế dựa trên bậc thuế này, Khai báo miễn thuế của nhân viên và Nộp minh chứng sẽ được xem xét để tính toán thu nhập chịu thuế.
- **Standard Tax Exemption Amount:** Nếu việc miễn thuế được cho phép, Số tiền miễn thuế tiêu chuẩn do chính phủ quy định có thể được thêm vào đây. Khoản miễn thuế này thường không cần bất kỳ loại minh chứng tài liệu nào và áp dụng cho tất cả nhân viên được liên kết với bậc thuế thu nhập này.

## 3. Các chủ đề liên quan

1. [Thành phần lương](../human-resources/salary-component)
1. [Cấu trúc lương](../human-resources/salary-structure)
1. [Phân bổ cấu trúc lương](../human-resources/salary-structure-assignment)
1. [Bút toán lương](../human-resources/payroll-entry)
1. [Khai báo miễn thuế của nhân viên](../human-resources/employee-tax-exemption-declaration)
1. [Nộp minh chứng miễn thuế của nhân viên](../human-resources/employee-tax-exemption-proof-submission)