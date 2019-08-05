from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST
from db import query


# from grader.db import query


@require_GET
def create(request):
    query.create()
    return HttpResponse()


@require_GET
def edit_all(request):
    """Поменять first_name на uu1 у всех пользователей"""
    return HttpResponse(query.edit_all())


@require_GET
def edit_u1_u2(request):
    """Поменять first_name на uu1 у пользователей, у которых first_name u1 или u2"""
    return HttpResponse(query.edit_u1_u2())


@require_GET
def delete_u1(request):
    """Удалить пользователя с first_name u1"""
    return HttpResponse(query.delete_u1())


@require_GET
def unsubscribe_u2_from_blogs(request):
    """Отписать пользователя с first_name u2 от блогов"""
    return HttpResponse(query.unsubscribe_u2_from_blogs())


@require_GET
def get_topic_created_grated(request):
    """Найти топики у которых дата создания больше 2018-01-01"""
    query_set = query.get_topic_created_grated()
    q = query_set.query
    r = '\n'.join(map(str, [entity for entity in query_set]))
    html = f'<pre>' \
        f'Result: \n{r}\n\n' \
        f'Query: \n{q}\n</pre>'
    return HttpResponse(html)


@require_GET
def get_topic_title_ended(request):
    """Найти топик у которого title заканчивается на content"""
    query_set = query.get_topic_title_ended()
    q = query_set.query
    r = '\n'.join(map(str, [entity for entity in query_set]))
    html = f'<pre>' \
        f'Result: \n{r}\n\n' \
        f'Query: \n{q}\n</pre>'
    return HttpResponse(html)


@require_GET
def get_user_with_limit(request):
    """Получить 2х первых пользователей (сортировка в обратном порядке по id)"""
    query_set = query.get_user_with_limit()
    q = query_set.query
    r = '\n'.join(map(str, [entity for entity in query_set]))
    html = f'<pre>' \
        f'Result: \n{r}\n\n' \
        f'Query: \n{q}\n</pre>'
    return HttpResponse(html)


@require_GET
def get_topic_count(request):
    """Получить количество топиков в каждом блоге, назвать поле topic_count,
    отсортировать по topic_count по возрастанию"""
    query_set = query.get_topic_count()
    q = query_set.query
    r = '\n'.join(map(str, [entity for entity in query_set]))
    html = f'<pre>' \
        f'Result: \n{r}\n\n' \
        f'Query: \n{q}\n</pre>'
    return HttpResponse(html)


@require_GET
def get_avg_topic_count(request):
    """Получить среднее количество топиков в блоге"""
    query_set = query.get_avg_topic_count()
    # q = query_set.query
    r = '\n'.join(map(str, [entity for entity in query_set]))
    html = f'<pre>' \
        f'Result: \n{r}\n\n' \
        # f'Query: \n{q}\n</pre>'
    return HttpResponse(html)


@require_GET
def get_blog_that_have_more_than_one_topic(request):
    """Найти блоги, в которых топиков больше одного"""
    query_set = query.get_blog_that_have_more_than_one_topic()
    q = query_set.query
    r = '\n'.join(map(str, [entity for entity in query_set]))
    html = f'<pre>' \
        f'Result: \n{r}\n\n' \
        f'Query: \n{q}\n</pre>'
    return HttpResponse(html)


@require_GET
def get_topic_by_u1(request):
    """Получить все топики автора с first_name u1"""
    query_set = query.get_topic_by_u1()
    q = query_set.query
    r = '\n'.join(map(str, [entity for entity in query_set]))
    html = f'<pre>' \
        f'Result: \n{r}\n\n' \
        f'Query: \n{q}\n</pre>'
    return HttpResponse(html)


@require_GET
def get_user_that_dont_have_blog(request):
    """Найти пользователей, у которых нет блогов, отсортировать по возрастанию id"""
    query_set = query.get_user_that_dont_have_blog()
    q = query_set.query
    r = '\n'.join(map(str, [entity for entity in query_set]))
    html = f'<pre>' \
        f'Result: \n{r}\n\n' \
        f'Query: \n{q}\n</pre>'
    return HttpResponse(html)


@require_GET
def get_topic_that_like_all_users(request):
    """Найти топик, который лайкнули все пользователи"""
    query_set = query.get_topic_that_like_all_users()
    q = query_set.query
    r = '\n'.join(map(str, [entity for entity in query_set]))
    html = f'<pre>' \
        f'Result: \n{r}\n\n' \
        f'Query: \n{q}\n</pre>'
    return HttpResponse(html)


@require_GET
def get_topic_that_dont_have_like(request):
    """Найти топики, у которы нет лайков"""
    query_set = query.get_topic_that_dont_have_like()
    q = query_set.query
    r = '\n'.join(map(str, [entity for entity in query_set]))
    html = f'<pre>' \
        f'Result: \n{r}\n\n' \
        f'Query: \n{q}\n</pre>'
    return HttpResponse(html)


@require_GET
def delete_all(request):
    """Clean all tables"""
    query_set = query.delete_all()
    q = query_set.query
    r = '\n'.join(map(str, [entity for entity in query_set]))
    html = f'<pre>' \
        f'Result: \n{r}\n\n' \
        f'Query: \n{q}\n</pre>'
    return HttpResponse(html)
