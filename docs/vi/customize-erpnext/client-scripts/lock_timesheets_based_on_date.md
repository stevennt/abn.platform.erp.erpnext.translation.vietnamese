<!-- add-breadcrumbs -->
# Khóa Bảng chấm công dựa trên Ngày

Giả sử bạn muốn tất cả nhân viên phải hoàn thành bảng chấm công trước thứ Sáu hàng tuần. Và chỉ cho phép những người dùng có vai trò 'Projects Manager' mới được chỉnh sửa hoặc thêm bảng chấm công cho những ngày trước thứ Sáu gần nhất. Đoạn mã tùy chỉnh (custom script) dưới đây sẽ thực hiện tính năng này.

    frappe.ui.form.on("Timesheet", "validate", function(frm) {
        if (frappe.user_roles.indexOf("Projects Manager") == -1) {
            const t = new Date().getDate() + (6 - new Date().getDay() - 1) - 7;
            const lastFriday = new Date();
            lastFriday.setDate(t);

            let dd = lastFriday.getDate();
            let mm = lastFriday.getMonth() + 1;
            let yyyy = lastFriday.getFullYear();

            frm.doc.time_logs.forEach(log => {
                if (new Date(log.from_time) <= lastFriday) {
                    frappe.throw("Bạn không thể thêm bảng chấm công cho các ngày trước thứ Sáu vừa qua " + dd + "/" + mm + "/" + yyyy + ". Vui lòng liên hệ với Quản lý dự án của bạn.");
                }
            })
        }
    })

{next}