from django.conf.urls import url
from .views import ModifyTextView

urlpatterns = [
    url(r'^modify/', ModifyTextView.as_view(), name='modify text view'),
]