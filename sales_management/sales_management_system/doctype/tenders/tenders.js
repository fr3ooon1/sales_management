// Copyright (c) 2024, Muhammad Essam and contributors
// For license information, please see license.txt

frappe.ui.form.on('Tenders', {
	refresh: function(frm) {
		
		let doc_status = frm.doc.doc_status ;
		if(doc_status == 'Approved'){
			frm.add_custom_button(__("Log"),
				function() {
					create_log();
				},
				__("Create")
			);
		}
		
	},
	doc_status: function(frm){
		let doc_status = frm.doc.doc_status ;
		if (doc_status == 'Rejected'){
			frm.set_df_property('doc_reason', 'reqd', 1);
		}else{
			frm.set_df_property('doc_reason', 'reqd', 0);
		}
	}
});

function create_log(){
	msgprint("hi");
}