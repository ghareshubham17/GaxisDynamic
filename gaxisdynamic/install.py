from gaxisdynamic.my_customization.setup import after_install as settinup_custom_fields
import frappe
import click

def after_install():
    try:
        print("Setting Up Custom Fields")
        settinup_custom_fields()

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
