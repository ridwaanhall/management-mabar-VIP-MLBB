
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Mabar, BonusSkin, RequestHero
from .forms import MabarForm, BonusSkinForm, RequestHeroForm

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

# CRUD views for BonusSkin
@login_required
def bonus_skin_create(request):
    if request.method == 'POST':
        form = BonusSkinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bonus_skin_list')
    else:
        form = BonusSkinForm()
    return render(request, 'public/bonus_skin_form.html', {'form': form, 'action': 'Tambah'})

@login_required
def bonus_skin_update(request, pk):
    skin = get_object_or_404(BonusSkin, pk=pk)
    if request.method == 'POST':
        form = BonusSkinForm(request.POST, instance=skin)
        if form.is_valid():
            form.save()
            return redirect('bonus_skin_list')
    else:
        form = BonusSkinForm(instance=skin)
    return render(request, 'public/bonus_skin_form.html', {'form': form, 'action': 'Edit'})

@login_required
def bonus_skin_delete(request, pk):
    skin = get_object_or_404(BonusSkin, pk=pk)
    if request.method == 'POST':
        skin.delete()
        return redirect('bonus_skin_list')
    return render(request, 'public/bonus_skin_confirm_delete.html', {'skin': skin})

# View untuk menampilkan daftar Request Hero

def request_hero_list(request):
    requests = RequestHero.objects.all().order_by('date_created')
    return render(request, 'public/request_hero_list.html', {'requests': requests})

# CRUD views for RequestHero
@login_required
def request_hero_create(request):
    if request.method == 'POST':
        form = RequestHeroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request_hero_list')
    else:
        form = RequestHeroForm()
    return render(request, 'public/request_hero_form.html', {'form': form, 'action': 'Tambah'})

@login_required
def request_hero_update(request, pk):
    req = get_object_or_404(RequestHero, pk=pk)
    if request.method == 'POST':
        form = RequestHeroForm(request.POST, instance=req)
        if form.is_valid():
            form.save()
            return redirect('request_hero_list')
    else:
        form = RequestHeroForm(instance=req)
    return render(request, 'public/request_hero_form.html', {'form': form, 'action': 'Edit'})

@login_required
def request_hero_delete(request, pk):
    req = get_object_or_404(RequestHero, pk=pk)
    if request.method == 'POST':
        req.delete()
        return redirect('request_hero_list')
    return render(request, 'public/request_hero_confirm_delete.html', {'req': req})
