from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Post
# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class ImageListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "list_image.html"
    login_url = 'account_login'


class ImageDetailView(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = "post_detail"
    template_name = "detail_image.html"
    login_url = 'account_login'


class ImagePremiumView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Post
    context_object_name = "premium_post"
    template_name = "premium_image.html"
    permission_required = "post.special_status"
