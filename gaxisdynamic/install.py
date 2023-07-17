from gaxisdynamic.my_customization.setup import after_install as settinup_custom_fields
import frappe
import click

def after_install():
    try:
        print("Setting Up Custom Fields")
        settinup_custom_fields()
        delete_workspace()

    except Exception as e:
        click.secho(
            (
                "Installation for GaxisDynamic failed due to an error."
                " Please try re-installing the app or"
                f" report the issue on  if not resolved."
            ),
            fg="bright_red",
        )
        raise e

    click.secho("Thank you for installing GaxisDynamic!", fg="green")


def delete_workspace():
    frappe.delete_doc("Workspace", "support", force=True)
    frappe.delete_doc("Workspace", "Loans", force=True)
    frappe.delete_doc("Workspace", "crm",force=True)
    frappe.delete_doc("Workspace", "Projects", force=True)
    frappe.delete_doc("Workspace", "Assets", force=True)
    frappe.delete_doc("Workspace", "GST India", force=True)
    frappe.delete_doc("Workspace", "Accounting", force=True)
    frappe.delete_doc("Workspace", "Buying", force=True)
    frappe.delete_doc("Workspace", "Stock", force=True)
    frappe.delete_doc("Workspace", "Selling", force=True)
    
