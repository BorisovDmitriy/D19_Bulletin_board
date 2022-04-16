from .models import Ad, Category, Response, Author
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import AdForm


class AdList(ListView):
    model = Ad
    template_name = 'board/ad_list.html'
    context_object_name = 'ads'
    queryset = Ad.objects.order_by('-create_time')
    paginate_by = 5


class AdDetail(DetailView):
    model = Ad
    template_name = 'board/ad.html'
    context_object_name = 'ad'


class AdSearchList(ListView):
    pass


class AdCreate(CreateView):
    template_name = 'board/ad_create.html'
    form_class = AdForm

    def get_initial(self):
        initial = super().get_initial()
        initial['author'] = self.request.user
        return initial


class AdUpdate(UpdateView):
    template_name = 'board/ad_update.html'
    form_class = AdForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Ad.objects.get(pk=id)


class AdDelete(DeleteView):
    template_name = 'board/ad_delete.html'
    queryset = Ad.objects.all()
    success_url = '/board/'


class ResponseList(ListView):
    pass


class ResponseDetail(DetailView):
    pass


class ResponseSearchList(ListView):
    pass


class ResponseCreate(CreateView):
    pass


class ResponseUpdate(UpdateView):
    pass


class ResponseDelete(DeleteView):
    pass
