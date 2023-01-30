from django.contrib import messages
from django.views.generic import TemplateView, DetailView, FormView

from .forms import PostForm
from .models import Post

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # For more information regarding get_context_data go to ccbv.co.uk
        context['posts'] = Post.objects.all().order_by('-id') # Outputted on Home.html.
        return context

class PostDetailView(DetailView): # Inherit from Django’s generic detail view
    template_name = 'detail.html'
    model = Post

class AddPostView(FormView): # Remember to read docs at ccbv.co.uk
    template_name = "new_post.html"
    form_class = PostForm
    success_url = "/"

    def dispatch(self, request, *args, **kwargs): # From docs at ccbv.co.uk
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # print(form.cleaned_data['text'])
        # print(form.cleaned_data['image'])

        # Create a new post
        new_object = Post.objects.create(
            text = form.cleaned_data['text'],
            image = form.cleaned_data['image']
        )
        messages.add_message(self.request, messages.SUCCESS, 'Your post was successful!')
        return super().form_valid(form)


