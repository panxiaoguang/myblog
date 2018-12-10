from django.shortcuts import render,redirect,reverse 




def tiaozhuan(request):
    return redirect("index",page=1)
