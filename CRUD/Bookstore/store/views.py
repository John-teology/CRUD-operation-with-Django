from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from django.urls import reverse 


# Create your views here.
from .models import Books
from .forms import *
def index(request):
    books = Books.objects.all()
    if request.method == 'POST':
        if request.POST.get('form'):
            form = BookForm(request.POST)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect(reverse('index'))
        if request.POST.get('delete'):
            book= Books.objects.get(pk = request.POST['delete'])
            book.delete()
            return HttpResponseRedirect(reverse('index'))
        if request.POST.get("reset"):
            Books.objects.all().delete()
            return HttpResponseRedirect(reverse('index')) 
        if request.POST.get('update'):
            book = Books.objects.get(pk = request.POST['update'])
            form = BookForm(initial={'title': book.title, 'author' :book.author,"price":book.price})
            return render(request, 'index.html', {
                'books': books,
                'forms' : form,
                'length' : len(books),
                'len': [(a+1) for a in range(len(books))],
                'msg': True,
                'bookid':book.id
            })
        if request.POST.get('save'):
            editform = BookForm(request.POST)
            book= Books.objects.get(pk = request.POST['save'])
            book.title = editform['title'].value()
            book.author = editform['author'].value()
            book.price = editform['price'].value()
            book.save()
            return HttpResponseRedirect(reverse('index'))              
    return render(request, 'index.html', {
        'books': books,
        'forms' : BookForm(),
        'length' : len(books),
        'len': [(a+1) for a in range(len(books))],
        'msg': False
        
    })