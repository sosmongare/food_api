from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Food
from .serializers import FoodSerializer

# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def food_list(request):
    if request.method == 'GET':
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            food = serializer.save()
            # Customize the response for a successful creation
            response_data = {
                'message': 'Food item created successfully!',
                'data': serializer.data,
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def food_detail(request, pk):
    try:
        food = Food.objects.get(pk=pk)
    except Food.DoesNotExist:
        # Customize the response for a food item not found
        return Response({'Error': 'Food not found'}, status=404)

    if request.method == 'GET':
        serializer = FoodSerializer(food)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FoodSerializer(food, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Customize the response for a successful update
            response_data = {
                'message': 'Food item updated successfully!',
                'data': serializer.data,
            }
            return Response(response_data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        food.delete()
        # Customize the response for a successful deletion
        return Response({'message': 'Food item deleted successfully!'}, status=204)
