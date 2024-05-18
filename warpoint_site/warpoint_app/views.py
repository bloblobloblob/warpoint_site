from django.shortcuts import render
from .forms import ItemForm, RevForm
from .models import Item, Review
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.shortcuts import redirect
# from .models import PostModel


class UserProfileView(TemplateView):  
    template_name = 'profile_page.html'  

    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)  
        try:  
            user = get_object_or_404(User, username=self.kwargs.get('username'))  
        except User.DoesNotExist:  
            raise Http404("Пользователь не найден")  
        context['user_profile'] = user
        context['email'] = user.email 
        # context['user_posts'] = PostModel.post_manager.filter(author=user)[:5]  
        context['title'] = f'Профиль пользователя {user}'  
        return context

class CustomRegistrationView(CreateView):  
    form_class = RegistrationForm  
    template_name = 'signup.html'  
    extra_context = {'title': 'Регистрация на сайте'}  

    def get_success_url(self):  
        return reverse_lazy('login')  

    def form_valid(self, form):  
        user = form.save()  
        return super().form_valid(form)

class CustomLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'login.html'
    extra_context = {'title': 'Авторизация на сайте'}

    def get_success_url(self):
        return reverse_lazy('home')


def home_page(request):
    items = Item.objects.all()
    return render(request, 'index.html', { 'items': items })

def item_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    rev = Review.objects.filter(item_id=item_id)
    revForm = RevForm()
    if request.method == "POST":
        formset = RevForm(request.POST)
        if formset.is_valid():
            add_review = Review.objects.create(author=request.POST['author'], item_id=item_id, review=request.POST['review'])
            add_review.save()
            return redirect(f'/{item_id}/')
    return render(request, 'detail.html', { 'item': item, 'revForm': revForm, 'rev' : rev })

class ItemAdd(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'add.html'
    success_url = '/'
    extra_context = {
        'title': 'Добавление товара',
    }

class ItemEdit(UpdateView):
    model = Item
    fields = '__all__'
    template_name = 'edit.html'
    success_url = '/'
    extra_context = {
        'title': 'Редактирование товара',
    }