# 639-py-async

Репозиторий задания "Знакомство с асинхронным вводом/выводом на питоне (async/await) (LEARNING_CENTER-639)"

Сравнение скорости выполнения:

|                               | Синхронный вариант | Асинхронный вариант |
|-------------------------------|--------------------|---------------------|
| Время (сек) с задержкой 0.001 | 11.55              | 1.66                |
| Время (сек) без задержки      | 0.003              | 0.42                |

*Если сравнивать результаты между синхронным и аснихронным вариантами*:

При наличии задержки в виде вызова `sleep()` синхронный вариант работает дольше, 
поскольку все команды выполняются последовательно и задержка накапливается,
тогда как в асинхронном варианте, во время задержки одной задачи, другие продолжают работу.

При отсутствии задержки асинхронный вариант наоборот работает дольше синхронного. 
Это можно объяснить затратами на создание задач и их управление.

*Если сравнивать результаты между наличием и отсутствием задержки*:

В синхронной версии различия по времени намного значительнее (в ~4000 раз), чем в асинхронной (в ~4 раза),
поскольку б**о**льшая часть времени в синхронной тратится на простаивание.