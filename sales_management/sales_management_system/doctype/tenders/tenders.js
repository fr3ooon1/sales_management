// Copyright (c) 2024, Muhammad Essam and contributors
// For license information, please see license.txt

frappe.ui.form.on('Tenders', {
	refresh: function(frm) {
		
		let doc_status = frm.doc.doc_status ;
		if(doc_status == 'Approved'){
			frm.add_custom_button(__("Log"),
				function() {
					make_log(frm);
				},
				__("Create")
			);
		}
		
	},
});

function make_log(frm){
	frappe.model.open_mapped_doc({
		method: "sales_management.sales_management_system.doctype.tenders.tenders.make_log",
		frm: frm
	})
}