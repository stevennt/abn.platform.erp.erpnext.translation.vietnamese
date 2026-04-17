<!-- add-breadcrumbs -->
# Thêm Nút Tùy chỉnh

	frappe.ui.form.on("Event", "refresh", function(frm) {
		frm.add_custom_button(__("Do Something"), function() {
			// Khi nút này được nhấp vào, thực hiện việc này
			
			var subject = frm.doc.subject;
			var event_type = frm.doc.event_type;
			
			// thực hiện điều gì đó với các giá trị này, ví dụ như một yêu cầu ajax 
			// hoặc gọi một hàm frappe phía máy chủ bằng cách sử dụng frappe.call
			$.ajax({
				url: "http://example.com/just-do-it",
				data: {
					"subject": subject,
					"event_type": event_type
				}
				
				// đọc thêm về cú pháp $.ajax tại http://api.jquery.com/jquery.ajax/
			
			});
		});
	});

{next}