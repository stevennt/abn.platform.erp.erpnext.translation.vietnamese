<!-- add-breadcrumbs -->
# Mục đích của Phiếu kho

Phiếu kho là một giao dịch kho, có thể được sử dụng cho nhiều mục đích khác nhau. Hãy cùng tìm hiểu về từng Mục đích của Phiếu kho dưới đây.

#### 1. Mục đích: Xuất vật tư (Material Issue)

Phiếu Xuất vật tư được tạo để xuất (các) mặt hàng từ một kho. Khi Xác nhận Phiếu Xuất vật tư, số lượng tồn kho của mặt hàng sẽ được trừ khỏi Kho nguồn.

Xuất vật tư thường được thực hiện cho các mặt hàng tiêu hao có giá trị thấp như văn phòng phẩm, vật tư tiêu hao sản xuất, v.v. Ngoài ra, bạn có thể tạo Phiếu Xuất vật tư để đối chiếu tồn kho của các mặt hàng theo số serial và theo lô.

<img alt="Material Issue" class="screenshot" src="{{docs_base_url}}/v13/assets/img/articles/stock-entry-issue.png">

#### 2. Mục đích: Nhập vật tư (Material Receipt)

Phiếu Nhập vật tư được tạo để nhập kho (các) mặt hàng vào một kho. Loại phiếu kho này có thể được tạo để cập nhật số dư đầu kỳ của các mặt hàng theo số serial và theo lô. Ngoài ra, các mặt hàng được mua mà không có Đơn mua hàng cũng có thể được nhập kho từ phiếu Nhập vật tư.

Vì mục đích tính giá tồn kho, trường Giá trị tính giá mặt hàng (Item Valuation) trở thành trường bắt buộc trong phiếu Nhập vật tư.

<img alt="Material Receipt" class="screenshot" src="{{docs_base_url}}/v13/assets/img/articles/stock-entry-receipt.png">

#### 3. Mục đích: Chuyển vật tư (Material Transfer)

Phiếu Chuyển vật tư được tạo để thực hiện việc Chuyển vật tư giữa các kho với nhau.

<img alt="Material Transfer" class="screenshot" src="{{docs_base_url}}/v13/assets/img/articles/stock-entry-transfer.png">

#### 4. Mục đích: Chuyển vật tư để Sản xuất (Material Transfer for Manufacture)

Trong quy trình sản xuất, nguyên vật liệu được xuất từ kho vật tư sang bộ phận sản xuất (thường là kho bán thành phẩm - WIP). Phiếu Chuyển vật tư này được tạo từ Lệnh sản xuất. Các mặt hàng trong phiếu này được lấy từ Định mức nguyên vật liệu của mặt hàng sản xuất đã được chọn trong Lệnh sản xuất.

<img alt="Transfer for Manufacture" class="screenshot" src="{{docs_base_url}}/v13/assets/img/articles/stock-entry-manufacture-transfer.gif">

#### 4. Mục đích: Sản xuất (Manufacture)

Phiếu Sản xuất được tạo từ Lệnh sản xuất. Trong phiếu này, cả mặt hàng nguyên vật liệu cũng như mặt hàng sản xuất đều được lấy từ Định mức nguyên vật liệu đã chọn trong Lệnh sản xuất. Đối với các mặt hàng nguyên vật liệu, chỉ có Kho nguồn (thường là kho bán thành phẩm - WIP) được đề cập. Đối với mặt hàng sản xuất, chỉ có kho đích như đã nêu trong Lệnh sản xuất được cập nhật. Khi Xác nhận, số lượng tồn kho của các mặt hàng nguyên vật liệu sẽ bị trừ khỏi Kho nguồn, cho thấy các mặt hàng nguyên vật liệu đã được tiêu thụ trong quá trình sản xuất. Mặt hàng sản xuất sẽ được thêm vào Kho đích, đánh dấu việc hoàn thành chu kỳ sản xuất.

<img alt="Manufacture" class="screenshot" src="{{docs_base_url}}/v13/assets/img/articles/stock-entry-manufacture.gif">

#### 5. Mục đích: Đóng gói lại (Repack)

Phiếu Đóng gói lại được tạo khi các mặt hàng mua số lượng lớn được đóng gói lại thành các gói nhỏ hơn. [Xem trang này để biết thêm về phiếu Đóng gói lại.](/docs/v13/user/manual/en/stock/articles/repack-entry.html)

#### 6. Mục đích: Gia công (Subcontract)

Giao dịch gia công bao gồm việc công ty chuyển các mặt hàng nguyên vật liệu sang kho của bên gia công. Việc này cũng yêu cầu phải thêm một kho cho bên gia công. Phiếu Gia công sẽ chuyển kho từ kho của công ty sang kho của bên gia công. [Xem trang này để biết thêm về Gia công](/docs/v13/user/manual/en/manufacturing/subcontracting.html).

<img alt="Subcontract" class="screenshot" src="{{docs_base_url}}/v13/assets/img/articles/stock-entry-subcontract.gif">

<!-- markdown -->