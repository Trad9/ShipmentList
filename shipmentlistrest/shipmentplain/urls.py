
from django.conf.urls import url
from .views import ShipmentListView
from .views import ShipmentItemView
from .views import ShipmentItemCreateView
from .views import ShipmentItemUpdate

urlpatterns = [
    url(r'^create/$', ShipmentItemCreateView.as_view()),
    url(r'^update/(?P<pk>\d+)/$', ShipmentItemUpdate.as_view()),
    url(r'^retrieve/(?P<pk>\d+)/$', ShipmentItemView.as_view()),
    url(r'^list/$', ShipmentListView.as_view()),
]
