<!-- add-breadcrumbs -->
# Khái niệm và Thuật ngữ

Trước khi bạn bắt đầu triển khai, hãy làm quen với các thuật ngữ được sử dụng và một số khái niệm cơ bản trong ERPNext v16.

* * *

### Khái niệm Cơ bản

#### Công ty

Phần này đại diện cho các hồ sơ Công ty mà ERPNext được thiết lập. Với cùng một thiết lập này, bạn có thể tạo nhiều hồ sơ Công ty, mỗi hồ sơ đại diện cho một pháp nhân khác nhau. Việc hạch toán cho mỗi Công ty sẽ khác nhau, nhưng chúng sẽ dùng chung các hồ sơ Khách hàng, Nhà cung cấp và Mặt hàng.

> Setup > Company

#### Khách hàng

Đại diện cho một khách hàng. Một Khách hàng có thể là một cá nhân hoặc một tổ chức. Bạn có thể tạo nhiều Liên hệ và Địa chỉ cho mỗi Khách hàng.

> Selling > Customer

#### Nhà cung cấp

Đại diện cho một nhà cung cấp hàng hóa hoặc dịch vụ. Công ty điện thoại của bạn là một Nhà cung cấp, và nhà cung cấp nguyên vật liệu của bạn cũng vậy. Tương tự, một Nhà cung cấp có thể là một cá nhân hoặc một tổ chức và có nhiều Liên hệ cũng như Địa chỉ.

> Buying > Supplier

#### Mặt hàng

Một Sản phẩm, bán thành phẩm hoặc Dịch vụ được mua, bán hoặc sản xuất và được định danh duy nhất.

> Stock > Item

#### Tài khoản

Tài khoản là một tiêu đề mà dưới đó các giao dịch tài chính và kinh doanh được thực hiện. Ví dụ, "Chi phí đi lại" là một tài khoản, "Khách hàng Zoe", "Nhà cung cấp Mae" là các tài khoản. ERPNext tự động tạo các tài khoản cho Khách hàng và Nhà cung cấp.

> Accounting > Chart of Accounts

#### Địa chỉ

Địa chỉ đại diện cho chi tiết vị trí của một Khách hàng hoặc Nhà cung cấp. Những địa chỉ này có thể là các địa điểm khác nhau như Trụ sở chính, Nhà máy, Kho, Cửa hàng, v.v.

> Selling > Address

#### Liên hệ

Một Liên hệ cá nhân thuộc về một Khách hàng hoặc Nhà cung cấp hoặc chỉ là một liên hệ độc lập. Một Liên hệ có tên và thông tin liên lạc như email và số điện thoại.

> Selling > Contact

#### Liên lạc

Danh sách tất cả các Liên lạc với một Liên hệ hoặc Khách hàng tiềm năng. Tất cả email được gửi từ hệ thống đều được thêm vào bảng Liên lạc.

> Support > Communication

#### Bảng giá

Bảng giá là nơi có thể lưu trữ các kế hoạch đơn giá khác nhau. Đó là tên bạn đặt cho một tập hợp các Giá Mặt hàng được lưu trữ dưới một Danh sách cụ thể.

> Selling > Price List


> Buying > Price List


* * *

### Kế toán

#### Năm tài chính

Đại diện cho một Năm tài chính hoặc Năm kế toán. Bạn có thể vận hành nhiều Năm tài chính cùng một lúc. Mỗi Năm tài chính có ngày bắt đầu và ngày kết thúc, và các giao dịch chỉ có thể được ghi lại trong giai đoạn này. Khi bạn "đóng" một năm tài chính, số dư của nó sẽ được chuyển thành số dư "đầu kỳ" cho năm tài chính tiếp theo.

> Setup > Company > Fiscal Year

#### Trung tâm chi phí

Trung tâm chi phí giống như một Tài khoản, nhưng điểm khác biệt duy nhất là cấu trúc của nó đại diện cho hoạt động kinh doanh của bạn sát sao hơn so với các Tài khoản.
Ví dụ, trong Hệ thống tài khoản, bạn có thể phân loại chi phí theo loại (ví dụ: đi lại, tiếp thị, v.v.). Trong Hệ thống trung tâm chi phí, bạn có thể phân loại chúng theo dòng sản phẩm hoặc nhóm kinh doanh (ví dụ: bán hàng trực tuyến, bán lẻ, v.v.).

> Accounting > Chart of Cost Centers

#### Bút toán

Một chứng từ chứa các bút toán Sổ cái (GL) và tổng số tiền Nợ và Có của các bút toán đó là bằng nhau. Trong ERPNext, bạn có thể cập nhật các Thanh toán, Trả hàng, v.v., bằng cách sử dụng các Bút toán.

> Accounting > Journal Entry

#### Hóa đơn bán hàng

Một hóa đơn được gửi cho Khách hàng khi giao các Mặt hàng (hàng hóa hoặc dịch vụ).

> Accounting > Sales Invoice

#### Hóa đơn mua hàng

Một hóa đơn được gửi bởi Nhà cung cấp khi giao các Mặt hàng (hàng hóa hoặc dịch vụ).

> Accounting > Purchase Invoice

#### Tiền tệ

ERPNext cho phép bạn ghi chép các giao dịch bằng nhiều loại tiền tệ khác nhau. Tuy nhiên, chỉ có một loại tiền tệ duy nhất cho sổ sách kế toán của bạn. Khi hạch toán các Hóa đơn với các thanh toán bằng các loại tiền tệ khác nhau, số tiền sẽ được chuyển đổi sang tiền tệ mặc định theo tỷ giá hối đoái đã chỉ định.

> Setup > Currency

* * *

### Bán hàng

#### Nhóm khách hàng

Một cách phân loại Khách hàng, thường dựa trên phân khúc thị trường.

> Selling > Setup > Customer Group

#### Khách hàng tiềm năng

Một người có thể là nguồn kinh doanh trong tương lai. Một Khách hàng tiềm năng có thể tạo ra các Cơ hội.

> CRM > Lead

#### Cơ hội

Một giao dịch bán hàng tiềm năng.

> CRM > Opportunity

#### Báo giá

Yêu cầu của Khách hàng về việc báo giá một mặt hàng hoặc dịch vụ.

> Selling > Quotation

#### Đơn bán hàng

Một ghi chú xác nhận các điều khoản giao hàng và giá của một Mặt hàng (sản phẩm hoặc dịch vụ) bởi Khách hàng. Việc giao hàng, Lệnh sản xuất và Hóa đơn được thực hiện dựa trên Đơn bán hàng.

> Selling > Sales Order

#### Khu vực

Một phân loại khu vực địa lý để quản lý bán hàng. Bạn có thể thiết lập mục tiêu cho các Khu vực và mỗi giao dịch bán hàng đều được liên kết với một Khu vực.

> Selling > Setup > Territory

#### Đối tác bán hàng

Một bên thứ ba phân phối / đại lý / liên kết / đại lý hoa hồng, người bán các sản phẩm của công ty thường để nhận hoa hồng.

> Selling > Setup > Sales Partner

#### Nhân viên bán hàng

Người chào hàng cho Khách hàng và chốt giao dịch. Bạn có thể thiết lập mục tiêu cho Nhân viên bán hàng và gắn họ vào các giao dịch.

> Selling > Setup > Sales Person

* * *

### Mua hàng

#### Đơn mua hàng

Một hợp đồng được đưa cho Nhà cung cấp để giao các Mặt hàng đã chỉ định với chi phí, số lượng, ngày tháng và các điều khoản khác đã chỉ định.

> Buying > Purchase Order

#### Yêu cầu vật tư

Một yêu cầu được thực hiện bởi Người dùng hệ thống, hoặc được tạo tự động bởi ERPNext dựa trên mức đặt hàng lại hoặc số lượng dự kiến trong Kế hoạch sản xuất để mua một bộ các Mặt hàng.

> Buying > Material Request

* * *

### Kho (Tồn kho)

#### Kho

Một Kho logic dùng để thực hiện các phiếu kho.

> Stock > Warehouse

#### Phiếu kho

Chuyển vật tư từ một Kho, đến một Kho hoặc từ Kho này sang Kho khác.

> Stock > Stock Entry