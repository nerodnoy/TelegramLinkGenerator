# [Тестим](https://telegram-converter.onrender.com)

Создать:

I. Таблица учеников

1) При создании группы, при вводе ссылки, надо сделать, чтобы список учеников сразу помещался в таблицу + группа сама формировала название по результатам парсига страницы
- Если этого сделать не получится, то сделать поле для вставки html-кода, чтобы его парсить

2) Создать таблицу для учеников в SQL, которая состоит из:

а) Имя ученика

б) Заметки по первому занятию

в) Заметки по второму занятию

г) Присутствовал ли на уроке (система галочек)

3) Добавить возможность удалять ученика из группы

4) По результатам проставленных галочек, выводить на экран: "ссылка на группу, ждём на занятии"
- если группа стартует в понедельник - один куратор, в четверг - другой.

5) Каждый ученик обладает своей гиперссылкой, которую попробуем взять из страницы группы

При переходе по имени ученика:

- В идеале: мы сразу имеем его имя, имя родителя, телефон
- Не в идеале: ничего не имеем, кроме имени, которое мы возьмем из таблицы учеников

* В идеале: нажимаем "Создать обратную связь" и начинаем сразу с вопросом по существу
* Не в идеале: нажимаем "Создать обратную связь" и начинаем с самого начала

*** По результатам составления обратной связи выводится итоговый результат

- В идеале: два результата (для голоса и для таблички); с этим позже разберемся 

Придумать:

I. Логику для заполнения таблицы

1) Автоматический перенос текста в таблицу Excel
- Перенос имен в таблицу
- Перенос обратной связи в таблицу