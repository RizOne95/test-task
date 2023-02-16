Задание 2.1
Создать 2 WEB сервера с выводом страницы «Hello Word! \n Server 1» (аналогично для второго Server 2). Сделать балансировку нагрузки (HA + keepalived), чтобы при обновлении страницы мы попадали на любой из WEB серверов(Для балансировки можно сделать 2 отдельных сервера, в сумме 4).
Будет плюсом использование Docker.

Для выполнения задания развернул 4 виртуальных сервера (2 web сервера и 2 сервера с Haproxy+Keepalived) с балансировкой roundrobin. Развернул только один кластер, т.к. не хватило ресурсов системы.

 
 ![1](https://user-images.githubusercontent.com/86364025/219378914-4361eb57-07b1-4efe-bb9b-67a61875ed1a.png)

![2](https://user-images.githubusercontent.com/86364025/219379066-b604324f-ac94-4eb8-846c-67a065fa6436.png)


Далее развернул два кластера в Docker. 
 
![3_1](https://user-images.githubusercontent.com/86364025/219379133-5953db7e-d7fb-466e-bb21-b981a4ceb44e.png)
![3_2](https://user-images.githubusercontent.com/86364025/219379156-143ed0ec-b544-48a1-bf40-265cbd6475d8.png)
