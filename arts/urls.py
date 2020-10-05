from django.urls import path
from .views import PictureListView,PictureDetailView

urlpatterns = [
path('', PictureListView.as_view(), name='picture_list'),
path('<uuid:pk>', PictureDetailView.as_view(), name='picture_detail'),
]