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
		this.service_info = {};
		this.page.incoming_call_info = {};
		this.make();
	},
	make: function() {
		var me = this;

		me.page.add_field({
			fieldtype: "Date",
			fieldname: "from_date",
			label: __("From Date"),
			reqd: 1,
			input_css: {"z-index": 1},
			change: function() {
				if (this && this.$input && this.$input.is(":focus")) {						
					me.get_data();
				}
			},
		});

		me.page.add_field({
			fieldtype: "Date",
			fieldname: "to_date",
			label: __("To Date"),
			reqd: 1,
			input_css: {"z-index": 1},
			change: function() {
				if (this && this.$input && this.$input.is(":focus")) {						
					me.get_data();
				}
			},
		});	

		me.get_data()	
	},
	get_data: function() {
		var me = this;

		console.log("Getting data");

		frappe.call({
			method: "frappe_lab.frappe_lab.page.crm_dash.crm_dash.get_crm_dash_data",
			args: {
				"from_date": frappe.datetime.get_today(),
				"to_date": frappe.datetime.get_today()
			}
		}).done((r) => {
			console.log(r);
			me.page.main.append(r.message)
		}).fail(() => {
			console.log("Data could not be loaded.");
		})
	}
})

