from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from manager.models import Person, Manager, Worker


class WorkerListView(TemplateView):
    template_name = 'worker_list.html'

    def get(self, request, *args, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        # DBからオブジェクトを取得する。
#        workers = Worker.objects.all()
        workers = Worker.objects.filter(person__sex=Person.MAN)
        # 入れ物に入れる。
        context['workers'] = workers

        return render(self.request, self.template_name, context)
