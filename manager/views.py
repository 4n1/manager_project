from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.views import login
from django.contrib.auth import authenticate

from manager.models import Person, Worker


class WorkerListView(TemplateView):
    template_name = 'worker_list.html'

    def get(self, request, *args, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        # DBからオブジェクトを取得する。
#        workers = Worker.objects.all().selected_related('person')
        workers = Worker.objects.filter(person__sex=Person.MAN) \
                                .select_related('person')
        # 入れ物に入れる。
        context['workers'] = workers

        return render(self.request, self.template_name, context)


class CustomLoginView(TemplateView):
    template_name = 'login.html'

    def get(self, _, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.get_next_redirect_url())
        else:
            kwargs = {'template_name': 'login.html'}
            return login(self.request, *args, **kwargs)

    def post(self, _, *args, **kwargs):
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            return redirect(self.get_next_redirect_url())
        else:
            kwargs = {'template_name', 'login.html'}
            return login(self.request, *args, **kwargs)

    def get_next_redirect_url(self):
        redirect_url = self.request.GET.get('next')

        if not redirect_url or redirect_url == '/':
            redirect_url = '/worker_list/'

        return redirect_url


def logout_view(request):
    logout(request)

    return redirect('/login/')
