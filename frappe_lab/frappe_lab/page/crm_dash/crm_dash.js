frappe.pages['crm-dash'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'CRM Dash',
		single_column: true
	});

	frappe.crmd = new frappe.CRMDash(wrapper);
}

frappe.CRMDash = Class.extend({
	init: function(wrapper) {
		this.page = wrapper.page;
		this.make();
	},
	make: function() {
		var me = this;

		me.page.add_field({
			fieldtype: "Date",
			fieldname: "from_date",
			label: __("From Date"),
			reqd: 1,
			default: frappe.datetime.get_today(),
			input_css: {"z-index": 1},
			change: function() {
				me.get_data();
			},
		});

		me.page.add_field({
			fieldtype: "Date",
			fieldname: "to_date",
			label: __("To Date"),
			reqd: 1,
			default: frappe.datetime.get_today(),
			input_css: {"z-index": 1},
			change: function() {
				me.get_data();
			},
		});	

		me.page.add_field({
			fieldtype: "Link",
			fieldname: "campaign",
			label: __("Campaign"),
			options: "Campaign",
			input_css: {"z-index": 1},
			change: function() {
				me.get_data();
			},
		});

		me.get_data()	
	},
	get_data: function() {
		var me = this;

		if (!me.page.fields_dict["from_date"].get_value() || !me.page.fields_dict["to_date"].get_value()) return

		frappe.call({
			method: "frappe_lab.frappe_lab.page.crm_dash.crm_dash.get_crm_dash_data",
			args: {
				"from_date": me.page.fields_dict["from_date"].get_value(),
				"to_date": me.page.fields_dict["to_date"].get_value(),
				"campaign": (me.page.fields_dict["campaign"].get_value() || "")
			}
		}).done((r) => {
			console.log("Reloaded")
			me.page.wrapper.find('.crm-dashboard').remove()
			me.page.main.append(r.message)
		}).fail(() => {
			frappe.show_alert("Could not load data.");
		})
	}
})

