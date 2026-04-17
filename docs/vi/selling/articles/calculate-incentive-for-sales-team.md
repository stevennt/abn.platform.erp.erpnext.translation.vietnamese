<!-- add-breadcrumbs -->
# Tính hoa hồng cho đội ngũ bán hàng

Bạn có thể Tính hoa hồng cho đội ngũ bán hàng bằng cách sử dụng các script tùy chỉnh.

Có thể được sử dụng trong bất kỳ Giao dịch bán hàng nào có bảng **Sales Team**:

    
    
    cur_frm.cscript.custom_validate = function(doc) {
        // calculate incentives for each person on the deal
        total_incentive = 0
        $.each(wn.model.get("Sales Team", {parent:doc.name}), function(i, d) {
    
            // calculate incentive
            var incentive_percent = 2;
            if(doc.grand_total > 400) incentive_percent = 4;
    
            // actual incentive
            d.incentives = flt(doc.grand_total) * incentive_percent / 100;
            total_incentive += flt(d.incentives)
        });
    
        doc.total_incentive = total_incentive;
    }