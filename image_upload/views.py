from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import  Uploaddatafromcsv
from . models import  UploadCsv, Csvdata
import pandas as pd
import csv

# Create your views here.

# Applying filter and showing data to screen between the two selected dates
def Datefilter(request):
    data = Csvdata.objects.all().values_list('dateadd', flat=True).distinct()
    data=data.order_by('dateadd')
    form = Uploaddatafromcsv()
    if request.method=='POST':
        date1= request.POST.get('date1')
        date2= request.POST.get('date2')
        detectedobj=Csvdata.objects.filter(dateadd__gte=date1, dateadd__lte=date2) 
    else:
        detectedobj={}
    context={'form':form, 'data':data, 'detectedobj':detectedobj}
    return render(request, 'csv.html', context)


# View for add the csv file and read data using pandas and saving the data to the database
def Readcsv(request):
    if request.method=='POST':
        data=Uploaddatafromcsv(request.POST, request.FILES)
        if data.is_valid():
            data.save()
            csvdata= UploadCsv.objects.latest('id')
            pddata= pd.read_csv(csvdata.Fileupload)
            iter_data = pddata.iterrows()
            for i in iter_data:
                Csvdata.objects.create(name=i[1][0], detected=i[1][1],dateadd=i[1][2], image=i[1][0])
            return redirect('/')


def Generate_csv(request):
    if request.method=='POST':
        data= request.POST.get('data_to_export')
# Getting all the id of data fetched for the two dates
        data = data.split(',')
        data.pop()
        rex=[]
        for i in data:
            detects=Csvdata.objects.get(id=int(i))
    # Spliting and converting the detected objects into list 
            detects_list=detects.detected.split(',')
            for p in detects_list:
                rex.append(p)
# Counting the number of repetation of values
        my_dict = {i:rex.count(i) for i in rex}
        
        response= HttpResponse(content_type='text/csv')
        response['Content-Disposition']='attachment; filename=Detections.csv'
        writer=csv.writer(response)
# Adding the report data to our output.csv file
        writer.writerow(['Objects', 'Frequence'])
        for key in my_dict:
            writer.writerow([key, my_dict[key]])
    return response
