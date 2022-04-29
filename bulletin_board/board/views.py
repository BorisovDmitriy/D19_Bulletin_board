from .models import Ad, Category, Response, Author
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .forms import AdForm, ResponseForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from .filters import NewsFilterByAd


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

    def get_context_data(self, **kwargs):
        context = super(AdDetail, self).get_context_data(**kwargs)
        context['responses'] = Response.objects.filter(ads=self.kwargs["pk"]).filter(response_state=True)
        if self.request.user in User.objects.all():
            context['is_author'] = Ad.objects.filter(pk=self.kwargs["pk"], author__user=self.request.user).exists()
        return context


class AdCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = 'board.add_ad'
    template_name = 'board/ad_create.html'
    form_class = AdForm

    # def get_initial(self):
    #     initial = super().get_initial()
    #     initial['author'] = self.request.user
    #     return initial

    def get_initial(self):
        initial = super().get_initial()
        user = self.request.user
        author = Author.objects.get(user=user)
        initial['author'] = author
        return initial


class AdUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = 'board.change_ad'
    template_name = 'board/ad_update.html'
    form_class = AdForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Ad.objects.get(pk=id)


class AdDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = 'board.delete_ad'
    template_name = 'board/ad_delete.html'
    queryset = Ad.objects.all()
    success_url = '/board/'


class ResponseList(LoginRequiredMixin, ListView):
    model = Response
    template_name = 'response/profile.html'
    context_object_name = 'responses'
    queryset = Response.objects.order_by('-create_time')
    paginate_by = 5


    def get_queryset(self, **kwargs):
        if not self.request.user.is_authenticated:
            qs = Response.objects.none()
        else:
            user = User.objects.get(username=self.request.user)
            qs = Response.objects.filter(ads__author__user=user.pk).order_by('-create_time')
        return qs


    # def get_context_data(self, **kwargs):
    #     context = super(ResponseList, self).get_context_data()
    #
    #     filtered = NewsFilterByAd(self.request.GET, request=self.get_queryset())
    #
    #     if self.request.user.is_authenticated:
    #         user = User.objects.get(username=self.request.user)
    #         ad_qs = Ad.objects.filter(author__user=user)
    #         filtered.qs.filter(ads__in=ad_qs)
    #     context['filter'] = filtered


class ResponseCreate(LoginRequiredMixin, CreateView):
    template_name = 'response/response_create.html'
    form_class = ResponseForm
    success_url = reverse_lazy('reaction_to_response')

    def get_initial(self):
        initial = super().get_initial()
        ads = get_object_or_404(Ad, id=self.kwargs['pk'])
        initial['user'] = self.request.user
        initial['ads'] = ads
        return initial


class ReactionView(TemplateView):
    template_name = 'response/reaction_to_response.html'


class ResponseDelete(LoginRequiredMixin, DeleteView):
    template_name = 'response/response_delete.html'
    queryset = Response.objects.all()
    success_url = reverse_lazy('profile')


class CategoryView(ListView):
    context_object_name = 'category_ads'
    template_name = 'board/category_ads.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['cat'])
        return Ad.objects.filter(categories=self.category).order_by('-create_time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


def accept_response(request, pk):
    response = Response.objects.get(id=pk)
    response.response_state = 'True'
    response.save()
    return redirect('profile')
