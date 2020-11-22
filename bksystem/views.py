from django.shortcuts import render
from django.http import HttpResponse
from bksystem.models import books

# Create your views here.

def index(request):
    # return HttpResponse("Hello Django")   #直接伺服器回復
    book_list=books.objects.all()
    #bkname=request.session.get('title','')
    return render(request,"index.html",{"books":book_list})    #指向要求的網頁

def search_title(request):
    #username=request.session.get('user','')
    search_name=request.GET.get("title","")
    book_list=books.objects.filter(title__contains=search_name)
    return render(request,"index.html",{"books":book_list}) #抓取cookie值
