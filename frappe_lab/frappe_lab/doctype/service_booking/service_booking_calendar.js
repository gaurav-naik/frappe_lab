frappe.views.calendar["Service Booking"] = {
	field_map: {
		"start": "starts_on",
		"end": "ends_on",
		"id": "name",
		"title": "title",
		"allDay": "all_day"
	},
	gantt: true,
	get_events_method: "frappe_lab.frappe_lab.doctype.service_booking.service_booking.get_bookings",
}