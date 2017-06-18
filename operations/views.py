from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .models import library_item
from .serializers import item_serializer
import json

@csrf_exempt
@api_view(['GET','POST'])
def table_operation(request):

    if request.method == 'GET':             # retrieves data from table
        result = library_item.objects.all()
        result_serializer = item_serializer(result,many=True)
        return JsonResponse(result_serializer.data,safe=False)

    elif request.method == 'POST':          # inserts an item into the table
        print("RESULT is "+str(request.data))
        result= JSONParser().parse(request.data)
        result_serializer= item_serializer(data=result)

        if result_serializer.is_valid():
            result_serializer.save()
            return JsonResponse(result.data,status=201)

        return JsonResponse(result.errors,status=400)


@csrf_exempt
@api_view(['GET'])
def book_operation(request,book_title):


    try:
        result = library_item.get(title=book_title)
    except library_item.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        result_serializer =item_serializer(result)
        return JsonResponse(result_serializer.data)


@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def id_operation(request,id):
    try:
        result = library_item.get(pk=id)
    except library_item.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        result_serializer = item_serializer(result)
        return JsonResponse(result_serializer.data)

    if request.method == 'PUT':
        update_result = JSONParser().parse(request)        # the result to be updated
        result_serializer = item_serializer(result,data=update_result)

        if result_serializer.is_valid():
            return JsonResponse(result_serializer.data,status=201)
        return JsonResponse(result_serializer,status=400)

    elif request.method == 'DELETE':
        result.delete()
        return HttpResponse(status=204)






