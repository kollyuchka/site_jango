from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import Form_one


class FormsView(View):

    def get(self,request):
        form = Form_one()
        return render(request,'form.html',{'form':form})


    def post(self,request):
        form = Form_one(request.POST,request.FILES)
        if form.is_valid():


            context = form.cleaned_data

            return HttpResponseRedirect('/form/')

        else:
            return render(request,'error.html',{"error":form.errors})
