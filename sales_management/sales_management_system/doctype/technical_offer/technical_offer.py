# Copyright (c) 2024, Muhammad Essam and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class TechnicalOffer(Document):
	def validate(self):
		self.document_name = self.name
