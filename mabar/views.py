from django.shortcuts import render
from .models import Mabar, BonusSkin, RequestHero

# View untuk menampilkan daftar Mabar Record
def mabar_list(request):
    records = Mabar.objects.all().order_by('date_created')
    records_show_all_except_done = records.filter(is_done=False)
    records_filter_by_status_prepare = records.filter(status='prepare', is_done=False)
    records_show_all_done = records.filter(is_done=True)
    
    context = {
        'records_all': records,
        'records_except_done': records_show_all_except_done,
        'prepare_records': records_filter_by_status_prepare,
        'done_records': records_show_all_done
    }
    return render(request, 'public/mabar_list.html', context)

# View untuk menampilkan daftar Bonus Skin
def bonus_skin_list(request):
    skins = BonusSkin.objects.all().order_by('date_created')
    return render(request, 'public/bonus_skin_list.html', {'skins': skins})

# View untuk menampilkan daftar Request Hero
def request_hero_list(request):
    requests = RequestHero.objects.all().order_by('date_created')
    return render(request, 'public/request_hero_list.html', {'requests': requests})
