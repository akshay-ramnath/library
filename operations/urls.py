from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^$',csrf_exempt(views.table_operation)),
    url(r'^(?P<id>[a-z0-9-]+)$',csrf_exempt(views.id_operation)),
    url(r'^(?P<book_title>[A-Za-z\s]+)$',csrf_exempt(views.book_operation))

]