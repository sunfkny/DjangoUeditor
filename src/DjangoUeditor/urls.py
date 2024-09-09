from .views import get_ueditor_controller

try:
    from django.urls import re_path as url
except ImportError:
    from django.conf.urls import url
urlpatterns = [url(r"^controller/$", get_ueditor_controller)]
