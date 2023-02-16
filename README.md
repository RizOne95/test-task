Задание 2.1
Создать 2 WEB сервера с выводом страницы «Hello Word! \n Server 1» (аналогично для второго Server 2). Сделать балансировку нагрузки (HA + keepalived), чтобы при обновлении страницы мы попадали на любой из WEB серверов(Для балансировки можно сделать 2 отдельных сервера, в сумме 4).
Будет плюсом использование Docker.

Для выполнения задания развернул 4 виртуальных сервера (2 web сервера и 2 сервера с Haproxy+Keepalived) с балансировкой roundrobin. Развернул только один кластер, т.к. не хватило ресурсов системы. Конфиги в директории VM_config.

 
 ![1](https://user-images.githubusercontent.com/86364025/219378914-4361eb57-07b1-4efe-bb9b-67a61875ed1a.png)

![2](https://user-images.githubusercontent.com/86364025/219379066-b604324f-ac94-4eb8-846c-67a065fa6436.png)


Далее развернул два кластера в Docker. 

1. Создал Dockerfile используя образ alpine в качестве основного.
2. Написал docker-compose.yml с описанием  2-х хоста мастера и 2-х зависимых хостов
3. Далее написал конфиги для keepalived и haproxy
4. Затем создал 4 веб-страницы, две для Master и две для Backup
5. Сконфигурировал два конфига для haproxy.
6. Написал сценарий для entrypoint.sh
7. Все конфиги выложил в папку /Docker в корень проекта.
![3_3](https://user-images.githubusercontent.com/86364025/219385200-b3554420-69e3-43a2-ac0c-a00280a6604c.png)
![3_1](https://user-images.githubusercontent.com/86364025/219379133-5953db7e-d7fb-466e-bb21-b981a4ceb44e.png)
![3_2](https://user-images.githubusercontent.com/86364025/219379156-143ed0ec-b544-48a1-bf40-265cbd6475d8.png)

Задание 2.2(усложненное)
Написать роль на Ansible по развёртыванию стенда из Задание 2.1.(4 виртуальных сервера (2 web сервера и 2 сервера с Haproxy+Keepalived) с балансировкой roundrobin) Должен быть описан файл инвентори.

Написал 3 роли (Nginx, Haproxy, Keepalived), конфиги оформил в jinja2, переменные вывел в отдельный в group_vars, роли расписал в каталоге roles
