import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render
from lasotuvi.DiaBan import diaBan
from lasotuvi.ThienBan import lapThienBan

from lasotuvi_django.utils import lapDiaBan


def api(request):
    now = datetime.datetime.now()
    hoTen = (request.GET.get('hoten'))
    ngaySinh = int(request.GET.get('ngaysinh', now.day))
    thangSinh = int(request.GET.get('thangsinh', now.month))
    namSinh = int(request.GET.get('namsinh', now.year))
    gioiTinh = 1 if request.GET.get('gioitinh') == 'nam' else -1
    gioSinh = int(request.GET.get('giosinh', 1))
    timeZone = int(request.GET.get('muigio', 7))
    duongLich = False if request.GET.get('amlich') == 'on' else True
    db = lapDiaBan(diaBan, ngaySinh, thangSinh, namSinh, gioSinh,
                   gioiTinh, duongLich, timeZone)
    thienBan = lapThienBan(ngaySinh, thangSinh, namSinh,
                           gioSinh, gioiTinh, hoTen, db)
    laso = {
        'thienBan': thienBan,
        'thapNhiCung': db.thapNhiCung
    }
    my_return = (json.dumps(laso, default=lambda o: o.__dict__))
    return HttpResponse(my_return, content_type="application/json")


def lasotuvi_django_index(request):
    return render(request, 'index.html')
