from datetime import datetime

from django.db.models import Q, Count, Avg
from pytz import UTC

from db.models import User, Blog, Topic


def create():
    # Создать пользователя first_name = u1, last_name = u1.
    user1 = User()
    user1.first_name, user1.last_name = "u1", "u1"
    user1.save()

    # Создать пользователя first_name = u2, last_name = u2.
    user2 = User()
    user2.first_name, user2.last_name = "u2", "u2"
    user2.save()

    # Создать пользователя first_name = u3, last_name = u3.
    user3 = User(first_name="u3", last_name="u3")
    user3.save()

    # Создать блог title = blog1, author = u1.
    blog1 = Blog()
    blog1.title = "blog1"
    blog1.author = user1
    blog1.save()

    # Создать блог title = blog2, author = u1.
    blog2 = Blog.objects.create(title="blog2", author=user1)

    # Подписать пользователей u1 u2 на blog1, u2 на blog2.
    u1u2s = User.objects.filter(Q(first_name='u1') | Q(first_name='u2'))
    b1s = Blog.objects.filter(title='blog1')
    # b2 = Blog.objects.filter(title='blog2')
    # u2s = User.objects.filter(first_name='u2')

    for user in u1u2s:
        for b1 in b1s:
            b1.subscribers.add(user)

    blog2.subscribers.add(user2)

    # Создать топик title = topic1, blog = blog1, author = u1.
    topic1 = Topic.objects.create(title='topic1', blog=blog1, author=user1)

    # Создать топик title = topic2_content, blog = blog1, author = u3, created = 2017-01-01.
    topic2 = Topic.objects.create(title='topic2_content', blog=blog1, author=user3, created='2017-01-01')

    # Лайкнуть topic1 пользователями u1, u2, u3.
    topic1.likes.add(user1, user2, user3)


def edit_all():
    """Поменять first_name на uu1 у всех пользователей"""
    all_users = User.objects.all()
    for user in all_users:
        user.first_name = "uu1"
        user.save()

    return all_users.query


def edit_u1_u2():
    """Поменять first_name на uu1 у пользователей, у которых first_name u1 или u2"""
    users_with_first_name_u1_or_u2 = User.objects.filter(Q(first_name='u1') | Q(first_name='u2'))
    for user in users_with_first_name_u1_or_u2:
        user.first_name = 'uu1'
        user.save()

    return users_with_first_name_u1_or_u2.query


def delete_u1():
    """Удалить пользователя с first_name u1"""
    deleted = User.objects.filter(first_name='u1').delete()
    return deleted


def unsubscribe_u2_from_blogs():
    """Отписать пользователя с first_name u2 от блогов"""
    users = User.objects.filter(first_name="u2")

    return [[blog.subscribers.remove(user) for user in users] for blog in Blog.objects.all()]

    # for user in users:
    #     user.blog_set.all().delete()
    #     user.blog_set.clear()

    # Blog.subscribers.through.objects.filter(user__first_name='u2').delete()

    """
    Removes the specified model objects from the related object set:
    b = Blog.objects.get(id=1)
    e = Entry.objects.get(id=234)
    b.entry_set.remove(e) # Disassociates Entry e from Blog b.
    
    Removes all objects from the related object set:
    b = Blog.objects.get(id=1)
    b.entry_set.clear()
    """


def get_topic_created_grated():
    """Найти топики у которых дата создания больше 2018-01-01"""
    utc_dt = datetime(2018, 1, 1, 0, 0, 0, tzinfo=UTC)
    topics = Topic.objects.filter(created__gte=utc_dt)
    # Topic.objects.filter(created__gt=datetime(year=2018, month=1, day=1, tzinfo=UTC))
    return topics


def get_topic_title_ended():
    """Найти топик у которого title заканчивается на content"""
    return Topic.objects.filter(title__endswith="content")


def get_user_with_limit():
    """Получить 2х первых пользователей (сортировка в обратном порядке по id)"""
    return User.objects.all().order_by('-id')[:2]


def get_topic_count():
    """Получить количество топиков в каждом блоге, назвать поле topic_count,
    отсортировать по topic_count по возрастанию"""
    return Blog.objects.annotate(topic_count=Count('topic')).order_by('topic_count')


def get_avg_topic_count():
    """Получить среднее количество топиков в блоге"""
    return Blog.objects.annotate(topic_count=Count('topic')).aggregate(avg=Avg('topic_count'))


def get_blog_that_have_more_than_one_topic():
    """Найти блоги, в которых топиков больше одного"""
    # return Blog.objects.annotate(topic_count=Count('topic')).filter(topic_count__gt=1)
    return Blog.objects.annotate(topic_count=Count('topic')).filter(topic_count__gt=1)

def get_topic_by_u1():
    """Получить все топики автора с first_name u1"""
    return Topic.author.objects.filter(first_name="u1")


def get_user_that_dont_have_blog():
    """Найти пользователей, у которых нет блогов, отсортировать по возрастанию id"""
    return User.blog_set.objects.order_by(id)


def get_topic_that_like_all_users():
    """Найти топик, который лайкнули все пользователи"""
    pass


def get_topic_that_dont_have_like():
    """Найти топики, у которы нет лайков"""
    pass


def delete_all():
    blog_deletion_log = 'blog_deletion_log:\t' + str(Blog.objects.all().delete()) + '\t\n'
    topic_deletion_log = 'topic_deletion_log:\t' + str(Topic.objects.all().delete()) + '\t\n'
    user_deletion_log = 'user_deletion_log:\t' + str(User.objects.all().delete()) + '\t\n'
    return blog_deletion_log + topic_deletion_log + user_deletion_log
