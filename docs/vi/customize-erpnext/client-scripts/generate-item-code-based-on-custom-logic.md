<!-- add-breadcrumbs -->
# Tạo Mã Mặt hàng Dựa trên Logic Tùy chỉnh

Thêm Custom Script này vào phần script của **Mặt hàng**, để Mã Mặt hàng mới được
tạo ra ngay trước khi Mặt hàng được Lưu.



    cur_frm.cscript.custom_validate = function(doc) {
        // xóa item_code (tên được lấy từ item_code)
        doc.item_code = "";

        // 2 ký tự đầu tiên dựa trên item_group
        switch(doc.item_group) {
            case "Test A":
                doc.item_code = "TA";
                break;
            case "Test B":
                doc.item_code = "TB";
                break;
            default:
                doc.item_code = "XX";
        }

        // thêm 2 ký tự tiếp theo dựa trên brand
        switch(doc.brand) {
            case "Brand A":
                doc.item_code += "BA";
                break;
            case "Brand B":
                doc.item_code += "BB";
                break;
            default:
                doc.item_code += "BX";
        }
    }


{next}