from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from .models import MarkedPlaces
from .forms import MarkForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    marked_places = MarkedPlaces.objects.all().order_by('-id')[:3]
    datas = []

    for i in marked_places:
        temp_data = {
            "name": i.name,
            "lat": i.location.coords[1],
            "long": i.location.coords[0]
        }
        datas.append(temp_data)

    context = {
        'datas': datas
    }

    return render(request, 'index.html', context)


def marked_datasets(request):
    marked_datas = serialize('geojson', MarkedPlaces.objects.all())
    return HttpResponse(marked_datas, content_type='json')


def kayit_ekle(request):
    if request.method == 'POST':
        form = MarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            messages.warning(request, 'Lütfen haritadan yer seçiniz!')
            return redirect('kayit_ekle')
    else:
        form = MarkForm()

    context = {
        'form': form
    }

    return render(request, 'kayit_ekle.html', context)


def kayitlar(request):

    my_model = MarkedPlaces.objects.all().order_by('id')
    datas = []

    for i in my_model:
        temp_data = {
            "id": i.id,
            "name": i.name,
            "lat": i.location.coords[1],
            "long": i.location.coords[0]
        }

        datas.append(temp_data)

    number_of_item = 5

    paginatorr = Paginator(datas, number_of_item)

    first_page = paginatorr.page(1).object_list

    page_range = paginatorr.page_range

    if request.method == 'POST':
        page_n = request.POST.get('page_n', None)
        results = list(paginatorr.page(page_n))
        return JsonResponse({"results": results})

    context = {
        'paginatorr': paginatorr,
        'first_page': first_page,
        'page_range': page_range,
        'kayitlar': my_model,
        'datas': datas
    }

    return render(request, 'kayitlar.html', context)


def kayitguncelle(request, id):
    kayitlar = get_object_or_404(MarkedPlaces, id=id)
    form = MarkForm(instance=kayitlar)
    location = {'lat': kayitlar.location.coords[1],
                'long': kayitlar.location.coords[0]}

    if request.method == 'POST':
        form = MarkForm(request.POST, instance=kayitlar)

        if form.is_valid():
            form.save()
            messages.success(request, 'Kayıt başarıyla güncellendi!')
            return redirect('/kayitlar')

    return render(request, 'kayit_duzenle.html', {'form': form, 'kayit': location})


def kayitsil(request, id):
    kayit = get_object_or_404(MarkedPlaces, id=id)
    kayit.delete()
    messages.success(request, 'Kayıt başarıyla silindi.')
    return redirect('/kayitlar')
