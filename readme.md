# Приложение для определения расстояния между людьми на видео
На вход программа принимает видео и фокусное расстояние камеры. Нейронная сеть обнаруживает людей на видео, при помощи алгоритма вычисляется расстояние между всеми присутствующими на кадре людьми. На выходе транслируется видео с отмеченными людьми и расстоянием между ними в метрах.

## Перед запуском
Необходимо установить зависимости из requirements.txt
```
pip install -r requirements.txt
```

## Запуск
Запустить нужно файл main_window.py перед этим подгрузить нужные модули из requirements.txt
После запуска приложения для тестирования можно взять video.mp4 в папке data, либо можете использовать свои видео с расширением .mp4 

## Выполнено
1) Обучена нейронная сеть https://github.com/AlexeyAB/darknet, веса и cfg-файл хранятся в папке detection: yolo-obj_final.weights и yolo-obj.cfg

mean average precision = 0.809892. Есть некоторая погрешность в определении людей

2) Написан алгоритм нахождения расстояния между людьми на видео video/distanse.py
Средний рост человека взят 170 см, поэтому есть некоторая погрешность в вычислениях.

Кратко идея алгоритма:
Наш мир трехмерный, а следовательно у каждого человека в пространстве должно быть 3 оси координат (x, y, z). Изображение (1 кадр видео) является двумерной проекцией трехмерного пространства. Расстояние между двумя людьми мы можем получить по оси x (в пикселях), ось y нам здесь не важна (предполагаем, что люди на одной линии по оси y). Нам не хватает знаний о глубине (ось z). Использовала данные о камере (нашла расстояние от человека до камеры) и центра изображения (расстояние от камеры до центра), чтобы найти z. Затем по теореме Пифагора находим реальное расстояние между людьми.

3) Написано приложение на PyQT для демонстрации работы алгоритма. Реализована возможность устанавливать фокусное расстояние камеры и загружать свои видео (первое окно). После загрузки запускается окно проигрывателя, реализована возможность ставить на паузу видео и вернуться назад.

В detection/detection.py с помощью opencv обнаруживаем людей на видео, опираясь на веса и cfg-файл из первого пункта

В video/video.py реализована загрузка видео, отрисовка расстояний и боксов(найденые люди помечаются)

В main_window.py собственно объединение всего, работа с PyQt (в папке ui два окна приложения)


