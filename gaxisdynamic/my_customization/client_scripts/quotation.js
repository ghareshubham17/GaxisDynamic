frappe.ui.form.on('Quotation', {
	refresh: function(frm) {
	    // GAxis Dynamic Logic
		gaxis_dynamic(frm);
	},
});

var gaxis_dynamic = function(frm, bool=true) {
	if(!frappe.user_roles.includes("Administrator")) {	
		// Set Read Only property
		frm.set_df_property("additional_info_section", "read_only", bool);
		frm.set_df_property("print_settings", "read_only", bool);

		// Set Hidden property
		frm.set_df_property("print_settings", "hidden", bool);
		frm.set_df_property("additional_info_section", "hidden", bool);

		//Hidden Child Quotation item fields
		// is_alternative
		// is_free_item
		// against_blanket_order
		// shopping_cart_section
		// page_break
	}
}
