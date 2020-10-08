from django.urls import path
from .views import PictureListView,PictureDetailView,SearchResultsListView

urlpatterns = [
path('', PictureListView.as_view(), name='picture_list'),
path('<uuid:pk>', PictureDetailView.as_view(), name='picture_detail'),
path('search/', SearchResultsListView.as_view(), name='search_results'),
]