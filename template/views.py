from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

#
# def echo0(request):
#     """Принимает request и возвращает HttpResponse всегда со статусом 200,
#     а также она должна возвращать эхо, переданных в запросе,
#     параметров и значение заголовка X-Print-Statement.
#     View должна быть доступна по пути /template/echo/
#     """
#     t = loader.get_template('templates/echo.html')
#     context = {'foo': 'bar'}
#     return HttpResponse(t.render(context, request))
#     # html =
#     # return HttpResponse(content=html, status=200)
#
#
# # render
# def echo1(request):
#     """Принимает request и возвращает HttpResponse всегда со статусом 200,
#     а также она должна возвращать эхо, переданных в запросе,
#     параметров и значение заголовка X-Print-Statement.
#     View должна быть доступна по пути /template/echo/
#     """
#     # View code
#     if request.method == "GET":
#         method = "GET"
#         params = request.GET.dict()
#     elif request.method == "POST":
#         method = "POST"
#         params = request.POST.dict()
#     else:
#         return HttpResponse(status=400)
#
#     statement = request.META.get('HTTP_X_PRINT_STATEMENT', 'empty')
#
#     return render(request, 'echo.html', context={
#         'method': method, 'params': params, 'statement': statement})


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })


def echo(request):
    context = {
        "GET": request.GET,
        "POST": request.POST,
        "statement": request.META.get("HTTP_X_PRINT_STATEMENT", "empty"),
        "META": request.META
    }
    return render(request, 'echo.html', context=context)
