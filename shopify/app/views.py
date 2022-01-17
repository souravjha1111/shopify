from django.http import response
from .serializers import inventoryserializer
from .models import inventorymodel
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import never_cache
from django.http import HttpResponse
from rest_framework.response import Response
from .forms import myform


from django.http import HttpResponse
import csv



def export(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=itemss.csv'
	writer = csv.writer(response)
	itemss = inventorymodel.objects.all()
	writer.writerow(['id','identifier', 'itemname', 'descriptiom', 'unitprice', 'instockquantity', 'reorderlevel', 'reorderdays', 'ordered', 'discontinued'])
	for items in itemss:
		writer.writerow([items.id, items.identifier, items.itemname, items.descriptiom, items.unitprice, items.instockquantity, items.reorderlevel, items.reorderdays, items.ordered, items.discontinued])

	return response


@api_view(['GET', 'POST'])
@never_cache
def getitems(request):
    if request.method == 'GET':
        orders = inventorymodel.objects.all()
        serializer = inventoryserializer(orders,many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer  = inventoryserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('http://127.0.0.1:8080/')
        else:
            return HttpResponse('entered data is not valid')

def deleteitem(request, pk):
    inventorymodel.objects.get(pk=pk).delete()
    return redirect('http://127.0.0.1:8080/')


def home(request):
    data = inventorymodel.objects.values()
    context = {
        "data": data
    }
    return render(request, 'app/home.html', context)


def additempage(request):
    return render(request, 'app/additem.html')



def edititem(request, pk): 
    instance = get_object_or_404(inventorymodel, pk=pk)
    form = myform(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('http://127.0.0.1:8080/')
    return render(request, 'app/update.html', {'form': form})