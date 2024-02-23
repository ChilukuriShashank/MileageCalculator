from django.shortcuts import render

def base(request):
    return render(request, 'base.html')


def vselection(request):
    return render(request, 'vselection.html')

def calculate(dis,m,pr):
    l=dis/m
    t=l*pr
    to=round(t,)
    return to

def output(request):
    vechile=request.POST.get('vehicleType')
    fuel=request.POST.get('fuelType')
    distance=int(request.POST.get('distance'))
    mileage=int(request.POST.get('mileage'))
    price=int(request.POST.get('pricePerLitre'))
    Total=calculate(distance,mileage,price)
    return render(request,'output.html',{'vechile':vechile,'fuel':fuel,'dis':distance,'pr':price,'tot':Total})
