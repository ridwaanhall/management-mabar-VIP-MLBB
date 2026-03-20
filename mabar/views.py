
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Mabar, BonusSkin, RequestHero
from .forms import MabarForm

# View untuk menampilkan daftar Mabar Record
def mabar_list(request):
    records = Mabar.objects.all().order_by('date_created')
    records_show_all_except_done_and_except_prepare = records.filter(is_done=False, status__in=['antri', 'antri_scrim', 'in_mabar', 'salah_id', 'kurang', 'done'])
    records_filter_by_status_prepare = records.filter(status='prepare', is_done=False)
    records_show_all_done = records.filter(is_done=True)

    context = {
        'records_all': records,
        'records_except_done': records_show_all_except_done_and_except_prepare,
        'prepare_records': records_filter_by_status_prepare,
        'done_records': records_show_all_done
    }
    return render(request, 'public/mabar_list.html', context)

# CRUD views for Mabar (only for authenticated users)
@login_required
def mabar_create(request):
    if request.method == 'POST':
        form = MabarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mabar_list')
    else:
        form = MabarForm()
    return render(request, 'public/mabar_form.html', {'form': form, 'action': 'Tambah'})

@login_required
def mabar_update(request, pk):
    mabar = get_object_or_404(Mabar, pk=pk)
    if request.method == 'POST':
        form = MabarForm(request.POST, instance=mabar)
        if form.is_valid():
            form.save()
            return redirect('mabar_list')
    else:
        form = MabarForm(instance=mabar)
    return render(request, 'public/mabar_form.html', {'form': form, 'action': 'Edit'})

@login_required
def mabar_delete(request, pk):
    mabar = get_object_or_404(Mabar, pk=pk)
    if request.method == 'POST':
        mabar.delete()
        return redirect('mabar_list')
    return render(request, 'public/mabar_confirm_delete.html', {'mabar': mabar})

# View untuk menampilkan daftar Bonus Skin
def bonus_skin_list(request):
    skins = BonusSkin.objects.all().order_by('date_created')
    return render(request, 'public/bonus_skin_list.html', {'skins': skins})

# View untuk menampilkan daftar Request Hero
def request_hero_list(request):
    requests = RequestHero.objects.all().order_by('date_created')
    return render(request, 'public/request_hero_list.html', {'requests': requests})
