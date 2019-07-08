﻿# MD5-light
BostonGene Test Task

Способ сборки довольно прост: необходимо сначала запустить server.py (подходящим для Вас способом, то есть python3 server.py на Linux подобных системах или же python server.py на Windows в командной строке).
Адрес для подключения будет вида "http://" + <ваш localhost> + ":8000".

После этого можно начинать curl'ить запросы к нашему серверу. Заметим, что server.py поддерживает только два типа запросов:
1)  создает новую задачу по адресу /submit (результатом такого запроса будет выведенный id задачи);
2)  возвращает текущее состояние задачи по адресу /check (результатом будет MD5 - хеш сумма или же статус задачи, если сумма еще
не посчитана или её невозможно посчитатать).

Все запросы будут направляться к остальным двум файлам - application.py и settings.py. Таким образом, будет поддерживаться автономность работы запросов.

В качестве аналога базы данных для наших запросов я использовал создание json файлов для каждого запроса. Файлы помещаются в директорию, в которой производится сборка сервера. Имена файлов имеют вид <id нашей задачи>.json.
БостонДжин - калл :)