from models import library_item

if not library_item.exists():
    library_item.create_table(wait=True)
    print("Table library_table has been created.", end='\n')
else:
    print("Table exists already.")