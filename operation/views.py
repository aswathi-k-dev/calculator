from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from json import loads

# Create your views here.
@method_decorator(csrf_exempt,name = "dispatch")
class AdditionView(View):
    def post(self,request):
        form_data = loads(request.body)
        n1 = int(form_data.get("num1"))
        n2 = int(form_data.get("num2"))
        result = n1+n2

        response_data = {
            "message":f"addition result of {n1},{n2}={result}"
        }
        return JsonResponse(response_data)

@method_decorator(csrf_exempt,name ="dispatch")
class SubtractionView(View):
    def post(self,request):
        form_data = loads(request.body)
        n1 = int(form_data.get("num1"))
        n2 = int(form_data.get("num2"))
        result = n1 - n2

        response_data = {
            "message":f"subtraction result of {n1},{n2} = {result}"
        }
        return JsonResponse(response_data)

@method_decorator(csrf_exempt,name="dispatch")
class MultiplicationView(View):
    def post(self,request):
        form_data = loads(request.body)
        n1 = int(form_data.get("num1"))
        n2 = int(form_data.get("num2"))
        result = n1 * n2

        response_data = {
            "message":f"product of {n1},{n2} = {result}"
        }
        return JsonResponse(response_data)
    
@method_decorator(csrf_exempt,name = "dispatch")
class DivisionView(View):
    def post(self,request):
        form_data = loads(request.body)
        n1 = int(form_data.get("num1"))
        n2 = int(form_data.get("num2"))
        result = n1/n2

        response_data = {
            "message":f"ddivision result of {n1},{n2} = {result}"
        }
        return JsonResponse(response_data)

@method_decorator(csrf_exempt,name = "dispatch")
class FactorialView(View):
    def post(self,request):
        form_data = loads(request.body)
        n = int(form_data.get("num")) 
        result = 1
        for i in range(1,n+1):
            result = result * i

        response_data = {
            "message":f"factorial of {n} = {result}"
        }      
        return JsonResponse(response_data)

@method_decorator(csrf_exempt,name = "dispatch")
class PrimeNumberView(View):
    def post(self,request):
        form_data = loads(request.body)
        num = int(form_data.get("num"))
        for i in range(2,num):
            if num % i == 0:
                is_prime = False
                break
        else:
            is_prime = True

        response_data = {
            "message":f"{num} is {is_prime}"
        }
        return JsonResponse(response_data)

@method_decorator(csrf_exempt,name = "dispatch")
class PerfectNumberView(View):
    def post(self,request):
        form_data = loads(request.body)
        num = int(form_data.get("num"))
        total = 0
        for i in range(1,num):
            if num % i == 0:
                total+= i
        if total == num:
            is_perfect = True
        else:
            is_perfect = False

        response_data = {
            "message":f"{num} is {is_perfect}"
        }
        return JsonResponse(response_data)


