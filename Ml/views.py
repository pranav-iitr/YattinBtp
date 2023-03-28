from django.shortcuts import render
from .utils.summer import predict_summer , getHeat
from .utils.winter import predict_winter


def Summer(request):
    args = {"output": 0,"heat":0}
    if request.method == 'POST':
        d1 = int(request.POST["d1"])
        d2 = int(request.POST["d2"])
        d3 = int(request.POST["d3"])
        data = [[d1, d2, d3]]
        output = predict_summer(data)
        args["output"] = output
        args["heat"]=getHeat(d3,output)
    args["type"]="summer"
    args["rec"]="Heat rejection will be"
    return render(request, r'base.html', args)

def Winter(request):
    args = {"output": 0,"heat":0}
    if request.method == 'POST':
        d1 = int(request.POST["d1"])
        d2 = int(request.POST["d2"])
        d3 = int(request.POST["d3"])
        data = [[d1, d2, d3]]
        output = predict_winter(data)
        args["output"] = output
        args["heat"]=getHeat(d3,output)
    args["type"]="winter"
    args["rec"]="Heat extraction will be"
    return render(request, r'base.html', args)