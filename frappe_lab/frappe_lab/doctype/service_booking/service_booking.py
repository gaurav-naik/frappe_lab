# -*- coding: utf-8 -*-
# Copyright (c) 2017, Gaurav Naik and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.desk.reportview import get_filters_cond

class ServiceBooking(Document):
	pass

@frappe.whitelist()
def get_bookings(start, end, filters=None):
	for x in xrange(1,5):
		print("Start", start)
		print("End", end)
		print("Filters", filters)

	return frappe.get_all("Service Booking")
	# return frappe.db.sql("""
	# 	SELECT name, title, starts_on, ends_on, all_day
	# 	FROM `tabService Booking`
	# 	WHERE date(starts_on) >= date('{start}') AND date(ends_on) <= date('{end}')
	# 	{filter_condition};
	# """.format(
	# 	start=start,
	# 	end=end,
	# 	filter_condition=get_filters_cond("Service Booking", filters, [])
	# ))
