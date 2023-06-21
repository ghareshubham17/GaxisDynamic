frappe.ui.form.on('Sales Invoice', {
	refresh: function(frm) {
	    // GAxis Dynamic Logic
		gaxis_dynamic(frm);
	},
});

var gaxis_dynamic = function(frm, bool=true) {
	if(!frappe.user_roles.includes("Administrator")) {
		// Remove the field if form is new and show on edit

		// Set Read Only property
		frm.set_df_property("set_posting_time", "read_only", bool);
		frm.set_df_property("accounting_dimensions_section", "read_only", bool);
		frm.set_df_property("scan_barcode", "read_only", bool);
		frm.set_df_property("update_stock", "read_only", bool);
		frm.set_df_property("disable_rounded_total", "read_only", bool);

		// Set Hidden property
		frm.set_df_property("set_posting_time", "hidden", bool);
		frm.set_df_property("accounting_dimensions_section", "hidden", bool);
		frm.set_df_property("scan_barcode", "hidden", bool);
		frm.set_df_property("update_stock", "hidden", bool);
		frm.set_df_property("disable_rounded_total", "hidden", bool);
		frm.set_df_property("more_information", "hidden", bool);
		frm.set_df_property("more_info", "hidden", bool);
		frm.set_df_property("edit_printing_settings", "hidden", bool);

		//Child table hide fields
		// barcode
		// accounting
		// deferred_revenue
		// accounting_dimensions_section
		// page_break
	}
}