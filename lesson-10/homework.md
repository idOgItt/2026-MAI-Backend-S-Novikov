# Домашнее задание к лекции №10

### Реализовать на стороне nginx Basic-авторизация для location secret, которая является дубликатом location public из второго домашнего задания.

### Реализовать OAuth2-авторизацию для одной из социальных сетей
Через любую социальную сеть/сервер ресурсов, используя библиотеку social-auth-app-django. Должна быть готова html-страница с кнопкой, по нажатию на которую произойдет механизм авторизации. Также для авторизованного пользователя должна отображаться кнопка logout.

Список доступных социальных сетей для OAuth2-авторизации можно посмотреть [тут](https://python-social-auth.readthedocs.io/en/latest/backends/).

### Написать middleware, проверяющий авторизацию при вызовах API
Написать middleware, проверяющий, что пользователь был авторизован в системе, иначе - редирект на страницу логина.
Предусмотреть, что могут быть view, которые останутся доступны без логина.

### Изменить запросы и код API
Изменить views так, чтобы в них учитывался текущий пользователь.
Допустим, у вас функция добавления фильма в избранное пользователем. Тогда Ваш код был например:


```python
def add_favorite(request, movie_id, user_id):
    movie = get_object_or_404(Movie, id=movie_id)
	user = get_object_or_404(User, id=user_id)
    user.favorites.add(movie)
    user.save()
	return JsonResponse(...)
```
тогда нужно у request проверять, что пользователь user неанонимный и использовать его.

или Вы должны проверить, что пользователь в запросе админ, чтобы добавлять кого-то в чат


```python
@login_required
def add_member(request, chat_id, user_id):
	chat = get_object_or_404(Chat, id=chat_id)
	user = get_object_or_404(User, id=user_id)

	if chat.admins.filter(id=request.user.id).exists(): # как вариант реализации хранения админов
		ChatMember.objects.create(chat=chat, user=user)
		return JsonResponse()
	return JsonResponse({'error': 'Only admin can add chat members'}, status=403)
```
