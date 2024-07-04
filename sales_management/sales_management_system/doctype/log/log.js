// Copyright (c) 2024, Muhammad Essam and contributors
// For license information, please see license.txt

frappe.ui.form.on('Log', {
	refresh: function(frm) {
		let status = frm.doc.docstatus ;
		if(status == 1){
			frm.add_custom_button(__("Technical Offer"),
				function() {
					create_offer(frm);
				},
				__("Create")
			);
		}
		
	},
});

function create_offer(frm){
	frappe.model.open_mapped_doc({
		method: "sales_management.sales_management_system.doctype.log.log.create_offer",
		frm: frm
	})
}