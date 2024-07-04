# Copyright (c) 2024, Muhammad Essam and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class Log(Document):
	pass




@frappe.whitelist()
def create_offer(source_name, target_doc=None, ignore_permissions=False):
	def postprocess(source, target):
		set_missing_values(source, target)

	def set_missing_values(source, target):
		target.flags.ignore_permissions = True
		target.run_method("set_missing_values")

	doclist = get_mapped_doc(
		"Log",
		source_name,
		{
			"Log": {
				"doctype": "Technical Offer",
				"field_map": {
				},
				"validation": {"docstatus": ["=", 1]},
			},
		},
		target_doc,
		postprocess,
		ignore_permissions=ignore_permissions,
	)
	doclist.set_onload("ignore_price_list", True)

	return doclist