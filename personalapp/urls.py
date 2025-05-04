from django.urls import path
from .views import index, innerpage
from .views import page_not_found


handler404 = page_not_found


urlpatterns = [
    path('', index, name='index'),
    path('inner-page/', innerpage, name='inner-page')
]
