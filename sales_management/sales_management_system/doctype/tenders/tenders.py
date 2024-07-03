# Copyright (c) 2024, Muhammad Essam and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class Tenders(Document):
	def on_change(self):
		self.reason_doc()


	def reason_doc(self):
		if not self.doc_reason and self.doc_status == 'Rejected':
			frappe.throw(_("Please Enter the Reason"))

