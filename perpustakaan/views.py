from django.shortcuts import render, redirect
from perpustakaan.models import Buku
# from django.http import HttpResponse
from perpustakaan.forms import FormBuku
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    # return HttpResponse('Halaman buku')
    # titles = ['Belajar Python', 'Belajar Django', 'Belajar Flask']
    books = Buku.objects.all()
    # books = Buku.objects.filter(jumlah=80)
    # books = Buku.objects.filter(kelompok_id__nama='Fabel')
    # books = Buku.objects.filter(kelompok_id__nama='Fabel')[:2]
    context = {
        # 'titles': titles,
        # 'writer': 'divakrishnam'
        'books': books
    }
    return render(request, 'buku.html', context)

@login_required(login_url=settings.LOGIN_URL)
def penerbit(request):
    # return HttpResponse('<H1>Halaman Penerbit</H1>')
    return render(request, 'penerbit.html')

@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()
            form = FormBuku()
            message = "Data berhasil disimpan"
            context = {
                'form': form,
                'message': message,
            }
            return render(request, 'tambah-buku.html', context)
    else:
        form = FormBuku()
        context = {
            'form': form,
        }
        return render(request, 'tambah-buku.html', context)

@login_required(login_url=settings.LOGIN_URL)
def ubah_buku(request, id_buku):
    book = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    if request.POST:
        form = FormBuku(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui")
            return redirect('ubah_buku', id_buku=id_buku)
    else:
        form = FormBuku(instance=book)
        context = {
            'form': form,
            'book': book
        }
    return render(request, template, context)

@login_required(login_url=settings.LOGIN_URL)
def hapus_buku(request, id_buku):
    book = Buku.objects.filter(id=id_buku)
    book.delete()
    messages.success(request, 'Data berhasil dihapus')
    return redirect('buku')