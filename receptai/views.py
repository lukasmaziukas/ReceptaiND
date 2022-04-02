from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Receptas

from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class AllUserLists(ListView, LoginRequiredMixin):
    model = Receptas
    template_name = 'base.html'

    def get_queryset(self):
        return Receptas.objects.filter(user=self.request.user)


def list(request, id):
    list = Receptas.objects.get(id=id)
    if request.method == "POST":
        if request.POST.get('save'):
            checked = request.POST.getlist('checkbox')
            for item in list.produktas_set.all():
                if str(item.id) in checked:
                    item.isCompleted = True
                else:
                    item.isCompleted = False
                item.save()
        elif request.POST.get('add'):
            text = request.POST.get('new')
            if len(text) > 2:
                list.produktas_set.create(text=text, isCompleted=False)
            else:
                print("produkto pavadinimas per trumpas")
        elif request.POST.get('delete'):
            id_to_delete = request.POST.get('delete')
            for item in list.produktas_set.all():
                if str(item.id) == id_to_delete:
                    item.delete()
        return redirect('list', id=id)
    else:
        context = {"title":f"{list.title}","items": list.produktas_set.all() }
        return render(request, 'list.html', context=context)