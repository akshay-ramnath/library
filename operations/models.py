from pynamodb.models import Model
from pynamodb.attributes import *
from datetime import datetime

class library_item (Model):
    class Meta:
        read_capacity_units = 1
        write_capacity_units = 1
        table_name = "library_table"
        host = "http://localhost:3000"
    title = UnicodeAttribute(null=False)
    author = UnicodeAttribute(null=False)
    isbn = UnicodeAttribute(null=False)
    url = UnicodeAttribute()
    image_url = UnicodeAttribute()
    create_date = UTCDateTimeAttribute(null=True,default=datetime.utcnow())
    modified_date = UTCDateTimeAttribute(null=True,default=datetime.utcnow())
    created_ts = NumberAttribute(null=True)
    modified_ts = NumberAttribute(null=True)
    uid = UnicodeAttribute(hash_key=True,attr_name="id")
    active = UnicodeAttribute() #What is the significance of this field?
    department = UnicodeAttribute(range_key=True)

