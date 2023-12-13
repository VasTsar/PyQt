"Текстовая новелла"

Описание: 
Эта игра заставит Вас пройти весь жизненный путь и осмыслить то, что думают о Вас окружающие. Решайте задачи в школе, делайте первые шаги в карьере ученого, выбирайте лучший способ решения проблем, с которыми столкнетесь, двигаясь к величию.
Насколько Ваши решения изменят жизнь окружающих и насколько жизнь окружающих изменит Ваши решения? Готовьтесь философствовать и рефлексировать.
Игровая новелла с элементами пазла и разветвлением сюжета. Сделана при помощи Qt Designer. Решение графических, логических и философских задач.
История должна заставить игрока задуматься над своей ролью в этом мире. 

Технологии:
В игре используются диалоговые окна, в которых возникают различные задания. Необходимо сделать выбор из двух пунктов, в зависимости от выбора возникает следующее задание. Есть две концовки.

База данных с несколькими таблицами (Choices, Screens, Answers, Statistics):
В первых двух записаны айди окна, текст выбора (на кнопке), номер сюжетной линии и текст окна.
В таблицу Answers записаны правильные ответы на задачи, в которых требуется ввод с клавиатуры.
В Statistics вносятся порядковый номер игрока, время, которое он думал над финальным вопросом и концовка. 
Между собой таблицы связаны айди.

Функции в PyCharm:
draw_screen собирает диалоговое окно в PyQt
get_result получает нужные данные из таблицы
write записывает данные (найденные в предыдущей функции) в диалоговое окно
correct_answer проверяет ответы, введенные с клавиатуры на правильность
В зависимости от финального выбора игрок увидит иллюстрацию, показывающую его дальнейшее существование (в качестве зрелищной концовки)

В проекте использованы Python, PyQt, SQLite.
