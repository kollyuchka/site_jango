from django.http import HttpResponseRedirect, HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import Form_one
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os


class FormsView(View):

    def get(self,request):
        form = Form_one()

        return render(request,'form.html',{'form':form})


    def post(self,request):
        form = Form_one(request.POST,request.FILES)
        if form.is_valid():
            file1 = request.FILES['file_1']
            file2 = request.FILES['file_2']
            file3 = request.FILES['file_3']
            file4 = request.FILES['file_4']


            fs = FileSystemStorage()
            filename_1 = fs.save(file1.name, file1)
            filename_2 = fs.save(file2.name, file2)
            filename_3 = fs.save(file3.name, file3)
            filename_4 = fs.save(file4.name, file4)

            if not os.path.isdir("file_storage"):
               os.mkdir("file_storage")
            os.replace(filename_1, "file_storage/file_1")
            os.replace(filename_2, "file_storage/file_2")
            os.replace(filename_3, "file_storage/file_3")
            os.replace(filename_4, "file_storage/file_4")


            storage = {}
            storage['STACK_HEIGT']= form.cleaned_data['stack_height']
            storage['BOTTOM_SOLID_LAYER'] = form.cleaned_data['botton_solid_layer']
            storage['TOP_SOLID_LAYER']= form.cleaned_data['top_solid_layer']
            storage['TOP_RAFT_LAYER']=form.cleaned_data['top_raft_layer']
            storage['TOP_BRIDGE_LAYER']= form.cleaned_data['top_bridge_layer']

            with open('file_storage/conf', 'w') as f:
                for item in storage:
                    f.write(item+'='+str(storage[item]) +'\n')

            return HttpResponseRedirect('/form/')

        else:
            return render(request,'error.html',{"error":form.errors})
