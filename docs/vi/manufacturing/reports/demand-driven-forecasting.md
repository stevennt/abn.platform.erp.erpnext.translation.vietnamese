<!-- add-breadcrumbs -->
# Dự báo dựa trên nhu cầu

Để truy cập Báo cáo Dự báo, hãy đi tới:

> Home > Manufacturing > Reports > Forecasting

<img class="screenshot" alt="Production Forecasting" src="https://docs.erpnext.com/docs/v13/assets/img/manufacturing/production-forecasting-using-sales-order.png">

Việc dự báo sẽ được tính toán bằng cách sử dụng phương pháp san bằng mũ (exponential smoothing) và dữ liệu Đơn bán hàng / Phiếu giao hàng / Báo giá trong quá khứ. Công thức phương pháp san bằng mũ như dưới đây:

<img class="screenshot" alt="Production Forecasting" src="https://docs.erpnext.com/docs/v13/assets/img/manufacturing/exponential-smoothing-formula.png">

Sử dụng phương pháp san bằng mũ, hệ thống sẽ dự đoán kết quả dự báo cho mỗi kỳ và dữ liệu dự báo tương tự sẽ được sử dụng để dự báo dữ liệu cho kỳ tiếp theo.

## Phương pháp san bằng mũ hoạt động như thế nào

<img class="screenshot" alt="Production Forecasting" src="https://docs.erpnext.com/docs/v13/assets/img/manufacturing/exponential-smoothing-formula-explain.png">

Đối với ví dụ trên, chúng tôi đã sử dụng dữ liệu đơn bán hàng hàng tháng trong vòng một năm. Dự báo tháng đầu tiên sẽ được tính toán dựa trên trung bình của tất cả tổng đơn hàng. Từ tháng thứ hai trở đi, chênh lệch giữa Tổng đơn hàng của tháng trước và Giá trị dự báo sẽ được nhân với Giá trị hằng số san bằng (nằm trong khoảng từ 0 đến 1). Giá trị mặc định của Hằng số san bằng là 0,3 giúp đưa ra dữ liệu dự báo hiệu quả. Chênh lệch giữa Tổng đơn hàng và Giá trị dự báo của tháng trước được gọi là sai số dự báo, và sai số này sẽ được cộng vào giá trị dự báo của cùng tháng đó để tính toán dự báo cho tháng tiếp theo.

## Các bộ lọc hoạt động như thế nào

1. **Company** :- người dùng có thể thực hiện dự báo cho một công ty cụ thể bằng cách áp dụng bộ lọc công ty.
1. **From Date và To Date** :- hệ thống sẽ thực hiện dự báo cho khoảng thời gian này, ngày bắt đầu mặc định là ngày hiện tại và ngày kết thúc sẽ là ngày cách ngày hiện tại một năm.
1. **Based On Document** :- theo mặc định, hệ thống sử dụng dữ liệu quá khứ của đơn bán hàng để dự báo. Người dùng có thể chọn các chứng từ khác như phiếu giao hàng / báo giá để dự báo dữ liệu.
1. **Based On** :- dựa trên số lượng / số tiền, hệ thống sẽ hiển thị dữ liệu dự báo.
1. **Based On Data ( tính theo năm )** :- việc dự báo yêu cầu dữ liệu trong quá khứ, bộ lọc này giúp hệ thống kiểm tra dữ liệu quá khứ trong số năm nhất định.
1. **Periodicity** :- dữ liệu dự báo có thể được xem theo cơ sở Hàng tháng / Hàng quý / Nửa năm / Hàng năm, dữ liệu dự báo cũ không thể hiển thị cho kỳ Hàng tháng để có cái nhìn tốt hơn.
1. **Smoothing Constant** - Hằng số san bằng sẽ được sử dụng để dự báo dữ liệu, giá trị phải nằm trong khoảng từ 0 đến 1.