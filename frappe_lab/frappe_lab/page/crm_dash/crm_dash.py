import frappe
from collections import OrderedDict

@frappe.whitelist()
def get_crm_dash_data(from_date, to_date, campaign=None):
	data =  {
		"leads": [
			OrderedDict([
				("status", "New"),
				("count", 20),
				("percent", "20%"),
			]),
			OrderedDict([
				("status", "Lost"),
				("count", 50),
				("percent", "50%"),
			]),
			OrderedDict([
				("status", "Converted"),
				("count", 30),
				("percent", "30%"),
			])
		],
		"opportunities": [
			OrderedDict([
				("rank", "Colonel"),
				("status", "Quotation"),
				("count", 35),
				("percent", "35%"),
				("foo", "bar"),
			]),
			OrderedDict([
				("rank", "Major"),
				("status", "Lost"),
				("count", 35),
				("percent", "35%"),
				("foo", "bar"),
			]),
			OrderedDict([
				("rank", "Sergeant Major"),
				("status", "Converted"),
				("count", 35),
				("percent", "35%"),
				("foo", "bar"),
			]),
			OrderedDict([
				("rank", "Lance Corporal"),
				("status", "Passive"),
				("count", 30),
				("percent", "30%"),
				("foo", "bar"),
			])
		]
	}

	html = ""

	try:
		html = frappe.render_template("frappe_lab/frappe_lab/page/crm_dash/crm_dashboard.html", {"data": data})
	except Exception as e:
		frappe.throw("Could not create data output. Reason: {0}".format(e))

	return html