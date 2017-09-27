#from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

# Create your views here.
class Index(View):
    def get(self, request):
        params = {}
        params["name"] = "Roy"
        return render(request, "base.html", params)
        #return HttpResponse('I am called from a get Request')
    # def post(self, request):
    #     return HttpResponse('I am called from a post Request')

# def index(request):
#     if request.method == 'GET':
#         return HttpResponse('I am called from a get Request')
#     elif request.method == 'POST':
#         return HttpResponse('I am called from a post Request')
