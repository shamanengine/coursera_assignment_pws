# from django.http import HttpResponse
# # from django.shortcuts import render
# from django.views.decorators.http import require_GET, require_POST
#
#
# def simple_route(request):
#     """Формирует http ответ с пустым телом со статусом 200 на запрос GET
#     (если запросы отличные от GET - возвращать 405) по /routing/simple_route/
#     """
#     if request.method == 'GET':
#         return HttpResponse(status=200)
#     else:
#         return HttpResponse(status=405)
#
#
# @require_GET
# def slug_route(request, slug):
#     """Принимает slug и отдает его в теле ответа.
#     В slug допустимы символы: 0-9, a-z, -, _ .
#     Минимальная длина 1 символ, максимальная длина 16.
#     """
#     return HttpResponse(slug)
#
#
# # @require_GET
# def sum_route(request, n, m):
#     """Принимает 2 числа и их суммирует, например /routing/sum_route/1/2/"""
#     html = str(int(n) + int(m))
#     return HttpResponse(html)
#
#
# @require_GET
# def sum_get_method(request):
#     """Принимает 2 числа из GET параметров a и b и суммирует их.
#     Допускается только метод GET. Например /routing/sum_get_method/?а=1&b=2
#     """
#     try:
#         a, b = request.GET.get('a'), request.GET.get('b')
#         html = str(int(a) + int(b))
#         return HttpResponse(html)
#     except:
#         return HttpResponse(status=400)
#
#
# @require_POST
# def sum_post_method(request):
#     """Принимает 2 числа из POST параметров a и b и суммирует их.
#     Допускается только метод POST. Например /routing/sum_post_method/
#     """
#     try:
#         a, b = request.POST['a'], request.POST['b']
#         html = str(int(a) + int(b))
#         return HttpResponse(html)
#     except Exception as e:
#         return HttpResponse(e, status=400)


from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST


@require_GET
def simple_route(request):
    return HttpResponse()


def slug_route(request, slug):
    return HttpResponse(slug)


def sum_route(request, a, b):
    try:
        a = int(a)
        b = int(b)
    except (ValueError, TypeError):
        return HttpResponse(status=400)

    return HttpResponse(a + b)


@require_GET
def sum_get_method(request):
    try:
        a = int(request.GET.get('a'))
        b = int(request.GET.get('b'))
    except (ValueError, TypeError):
        return HttpResponse(status=400)

    return HttpResponse(a + b)


@require_POST
def sum_post_method(request):
    try:
        a = int(request.POST.get('a'))
        b = int(request.POST.get('b'))
    except (ValueError, TypeError):
        return HttpResponse(status=400)

    return HttpResponse(a + b)