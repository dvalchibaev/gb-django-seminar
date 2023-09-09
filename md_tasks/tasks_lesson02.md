## Задача 1

- [x] Создайте модель для запоминания бросков монеты: орёл или
решка.

- [x] Также запоминайте время броска

- [x] Добавьте статический метод для статистики по n последним
броскам монеты.
- [ ] Метод должен возвращать словарь с парой ключейзначений, для орла и для решки.

## Задача 2

- [x] Создайте модель Автор. Модель должна содержать
следующие поля:

    - [x] имя до 100 символов
    - [x] фамилия до 100 символов
    - [x] почта
    - [x] биография
    - [x] день рождения

- [x] Дополнительно создай пользовательское поле “полное
    имя”, которое возвращает имя и фамилию.


- [x] Создайте модель Статья (публикация). Авторы из прошлой задачи могут
писать статьи. У статьи может быть только один автор. У статьи должны быть
следующие обязательные поля:

  - [x] заголовок статьи с максимальной длиной 200 символов
  - [x] содержание статьи
  - [x] дата публикации статьи
  - [x] автор статьи с удалением связанных объектов при удалении автора
  - [x] категория статьи с максимальной длиной 100 символов
  - [x] количество просмотров статьи со значением по умолчанию 0
  - [x] флаг, указывающий, опубликована ли статья со значением по умолчанию
  False


- [x] Создай четыре функции для реализации CRUD в модели Django Article (статья). 
*Используйте Django команды для вызова функций.


- [x] Создайте модель Комментарий.
- [x] Авторы могут добавлять комментарии к своим и чужим
статьям. Т.е. у комментария может быть один автор. И комментарий относится к одной статье. 

У модели должны быть следующие поля
  - [x] автор
  - [x] статья
  - [x] комментарий
  - [x] дата создания
  - [x] дата изменения