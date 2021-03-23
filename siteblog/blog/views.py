from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView

from .forms import EmailSubscriptionForm
from .models import Post, Category, Tag, EmailSubscriptions
from django.db.models import F

from .service import send_email
from .tasks import send_subscribe_email


class Home(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.filter(fixed=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Classic Blog Design'
        return context

class PostsByCategory(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class GetPosts(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EmailSubscriptionForm
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context

class PostsByTag(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Posts by tag: ' + str(Tag.objects.get(slug=self.kwargs['slug']))
        return context


class Search(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Search result'
        context["s"] = f"s={self.request.GET.get('s')}&"
        return context


class CreateSubscription(CreateView):
    form_class = EmailSubscriptionForm

    def get_success_url(self):
        return reverse_lazy('post', kwargs={'slug': self.kwargs.get('post_slug')})

    def form_valid(self, form):
        form.save()
        send_subscribe_email.delay(form.instance.email)
        messages.success(self.request, f'You subscribed successfully. Check you mail {form.instance.email}')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, f'Subscription for mail {form.instance.email} already exists')
        print('!!!!')
        print(self.kwargs)
        return redirect('post', slug=self.kwargs.get('post_slug'))

