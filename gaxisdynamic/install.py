from gaxisdynamic.my_customization.setup import removing_fields

def after_install():
    print("--------------------HIDEING FIELDS------------------")
    removing_fields()
    
    