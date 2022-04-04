from django.shortcuts import render, redirect
from .models import Bee
from .forms import BeeForm


def list_bees(request):
    bees = Bee.objects.all()
    return render(request, 'bees.html', {'bees': bees})


def create_bee(request):
    form = BeeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_bees')

    return render(request, 'bees-form.html', {'form': form})


def update_bee(request, id):
    bee = Bee.objects.get(id=id)
    form = BeeForm(request.POST or None, instance=bee)

    if form.is_valid():
        form.save()
        return redirect('list_bees')

    return render(request, 'bees-form.html', {'form': form, 'bee': bee})


def delete_bee(request, id):
    bee = Bee.objects.get(id=id)

    if request.method == 'POST':
        bee.delete()
        return redirect('list_bees')

    return render(request, 'bee-delete-confirm.html', {'bee': bee})
