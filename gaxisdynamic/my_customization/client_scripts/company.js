frappe.ui.form.on('Company', {
	refresh: function(frm) {
	  // GAxis Dynamic Logic
	  gaxis_dynamic(frm);
	},
});

var gaxis_dynamic = function(frm, bool=true) {
	if(!frappe.user_roles.includes("Administrator")) {
		// Set Read Only property
		frm.set_df_property("create_chart_of_accounts_based_on", "read_only", bool);
		frm.set_df_property("chart_of_accounts", "read_only", bool);
		frm.set_df_property("existing_company", "read_only", bool);

		frm.set_df_property("default_bank_account", "read_only", bool);
		frm.set_df_property("default_cash_account", "read_only", bool);
		frm.set_df_property("default_receivable_account", "read_only", bool);
		frm.set_df_property("round_off_account", "read_only", bool);
		frm.set_df_property("round_off_cost_center", "read_only", bool);
		frm.set_df_property("write_off_account", "read_only", bool);
		frm.set_df_property("exchange_gain_loss_account", "read_only", bool);
		frm.set_df_property("unrealized_exchange_gain_loss_account", "read_only", bool);
		frm.set_df_property("unrealized_profit_loss_account", "read_only", bool);

		frm.set_df_property("allow_account_creation_against_child_company", "read_only", bool);
		frm.set_df_property("default_payable_account", "read_only", bool);
		frm.set_df_property("default_expense_account", "read_only", bool);
		frm.set_df_property("default_income_account", "read_only", bool);
		frm.set_df_property("default_deferred_revenue_account", "read_only", bool);
		frm.set_df_property("default_deferred_expense_account", "read_only", bool);
		frm.set_df_property("default_discount_account", "read_only", bool);

		frm.set_df_property("cost_center", "read_only", bool);
		frm.set_df_property("default_finance_book", "read_only", bool);

		frm.set_df_property("accumulated_depreciation_account", "read_only", bool);
		frm.set_df_property("depreciation_expense_account", "read_only", bool);
		frm.set_df_property("series_for_depreciation_entry", "read_only", bool);
		frm.set_df_property("expenses_included_in_asset_valuation", "read_only", bool);
		frm.set_df_property("disposal_account", "read_only", bool);
		frm.set_df_property("depreciation_cost_center", "read_only", bool);
		frm.set_df_property("capital_work_in_progress_account", "read_only", bool);
		frm.set_df_property("asset_received_but_not_billed", "read_only", bool);

		frm.set_df_property("sales_monthly_history", "read_only", bool);
		frm.set_df_property("monthly_sales_target", "read_only", bool);
		frm.set_df_property("total_monthly_sales", "read_only", bool);

		frm.set_df_property("credit_limit", "read_only", bool);
		frm.set_df_property("transactions_annual_history", "read_only", bool);

		frm.set_df_property("exception_budget_approver_role", "read_only", bool);

		frm.set_df_property("enable_perpetual_inventory", "read_only", bool);
		frm.set_df_property("enable_provisional_accounting_for_non_stock_items", "read_only", bool);
		frm.set_df_property("default_inventory_account", "read_only", bool);
		frm.set_df_property("stock_adjustment_account", "read_only", bool);
		frm.set_df_property("stock_received_but_not_billed", "read_only", bool);
		frm.set_df_property("default_provisional_account", "read_only", bool);
		frm.set_df_property("expenses_included_in_valuation", "read_only", bool);

		// Set Hidden property
		frm.set_df_property("create_chart_of_accounts_based_on", "hidden", bool);
		frm.set_df_property("chart_of_accounts", "hidden", bool);
		frm.set_df_property("existing_company", "hidden", bool);

		frm.set_df_property("default_bank_account", "hidden", bool);
		frm.set_df_property("default_cash_account", "hidden", bool);
		frm.set_df_property("default_receivable_account", "hidden", bool);
		frm.set_df_property("round_off_account", "hidden", bool);
		frm.set_df_property("round_off_cost_center", "hidden", bool);
		frm.set_df_property("write_off_account", "hidden", bool);
		frm.set_df_property("exchange_gain_loss_account", "hidden", bool);
		frm.set_df_property("unrealized_exchange_gain_loss_account", "hidden", bool);
		frm.set_df_property("unrealized_profit_loss_account", "hidden", bool);

		frm.set_df_property("allow_account_creation_against_child_company", "hidden", bool);
		frm.set_df_property("default_payable_account", "hidden", bool);
		frm.set_df_property("default_expense_account", "hidden", bool);
		frm.set_df_property("default_income_account", "hidden", bool);
		frm.set_df_property("default_deferred_revenue_account", "hidden", bool);
		frm.set_df_property("default_deferred_expense_account", "hidden", bool);
		frm.set_df_property("default_discount_account", "hidden", bool);

		frm.set_df_property("cost_center", "hidden", bool);
		frm.set_df_property("default_finance_book", "hidden", bool);

		frm.set_df_property("accumulated_depreciation_account", "hidden", bool);
		frm.set_df_property("depreciation_expense_account", "hidden", bool);
		frm.set_df_property("series_for_depreciation_entry", "hidden", bool);
		frm.set_df_property("expenses_included_in_asset_valuation", "hidden", bool);
		frm.set_df_property("disposal_account", "hidden", bool);
		frm.set_df_property("depreciation_cost_center", "hidden", bool);
		frm.set_df_property("capital_work_in_progress_account", "hidden", bool);
		frm.set_df_property("asset_received_but_not_billed", "hidden", bool);

		frm.set_df_property("sales_monthly_history", "hidden", bool);
		frm.set_df_property("monthly_sales_target", "hidden", bool);
		frm.set_df_property("total_monthly_sales", "hidden", bool);

		frm.set_df_property("credit_limit", "hidden", bool);
		frm.set_df_property("transactions_annual_history", "hidden", bool);

		frm.set_df_property("exception_budget_approver_role", "hidden", bool);

		frm.set_df_property("enable_perpetual_inventory", "hidden", bool);
		frm.set_df_property("enable_provisional_accounting_for_non_stock_items", "hidden", bool);
		frm.set_df_property("default_inventory_account", "hidden", bool);
		frm.set_df_property("stock_adjustment_account", "hidden", bool);
		frm.set_df_property("stock_received_but_not_billed", "hidden", bool);
		frm.set_df_property("default_provisional_account", "hidden", bool);
		frm.set_df_property("expenses_included_in_valuation", "hidden", bool);
	}
}