from django.views.generic import ListView,DetailView
from .models import Picture

class PictureListView(ListView):

    model = Picture
    template_name = 'pictures/picture_list.html'


class PictureDetailView(DetailView): 
    model = Picture
    template_name = 'pictures/picture_detail.html'
