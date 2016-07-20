from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, View
import json


class Index(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'HelloDjangoApp/index.html')


class ModifyTextView(View):
    SOURCE_TEXT = 'Django was modified this: {}'

    def get(self, request):
        text = request.GET.get('data')
        response_dict = {'modifyData': self.SOURCE_TEXT.format(text)}
        return HttpResponse(json.dumps(response_dict), content_type='application/json')
