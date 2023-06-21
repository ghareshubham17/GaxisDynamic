import frappe

def removing_fields():
    # Sales Order Item
    hide_child_table_field('Sales Order Item','page_break')
    hide_child_table_field('Sales Order Item','shopping_cart_section')

    # Sales Invoice Item
    hide_child_table_field('Sales Invoice Item','page_break')
    hide_child_table_field('Sales Invoice Item','barcode')
    hide_child_table_field('Sales Invoice Item','accounting')
    hide_child_table_field('Sales Invoice Item','deferred_revenue') 
    hide_child_table_field('Sales Invoice Item','accounting_dimensions_section')

    #Quotation Item
    hide_child_table_field('Quotation Item','is_alternative')
    hide_child_table_field('Quotation Item','is_free_item')
    hide_child_table_field('Quotation Item','against_blanket_order') 
    hide_child_table_field('Quotation Item','shopping_cart_section')
    hide_child_table_field('Quotation Item','page_break')

    #Supplier Quotation Item
    hide_child_table_field('Supplier Quotation Item','page_break')

@frappe.whitelist()
def hide_child_table_field(doctype_name, fieldname):
    doctype = frappe.get_doc("DocType", doctype_name)
    for field in doctype.fields:
        if field.fieldname == fieldname:
            field.hidden = 1
            break
    doctype.save()
    