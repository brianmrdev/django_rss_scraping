from django.shortcuts import render
from django.views.generic import View, DetailView
from .scraper import get_main_news
from django.http import JsonResponse


class Index(View):
    def get(self, request):
        
        context_data = {
            'title': 'RSS Reader',
        }
        return render(request, 'index.html', context_data)
    
    def post(self, request):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            res = None
            url = request.POST['url']
            data = get_main_news(url)
            if len(data) > 0:                
                res = data
            else:
                res = 'No se han encontrado resultados para su búsqueda o la url proporcionada no es RSS válida'
            return JsonResponse({'data': res})
        return JsonResponse({})