from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView,DetailView
from .models import Picture

class PictureListView(LoginRequiredMixin,ListView):

    model = Picture
    template_name = 'pictures/picture_list.html'
    login_url = 'account_login'


class PictureDetailView(LoginRequiredMixin,DetailView): 
    model = Picture
    template_name = 'pictures/picture_detail.html'
    login_url = 'account_login'
    # permission_required = 'pictures.special_status'#new


class SearchResultsListView(ListView): # new
    model = Picture

    template_name = 'pictures/search_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Picture.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )

