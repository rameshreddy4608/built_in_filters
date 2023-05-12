from django.shortcuts import render

# Create your views here.

def built_in_filters(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'Hi I aM rAmesh welCOME TO djaNGO','dt':dt,'c':2,'b':1}
    return render(request,'built_in_filters.html',d)