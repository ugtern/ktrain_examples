в начале необходимо развернуть виртуальное окружение со всеми зависимостями из файла requirements.txt, в моем случае я использую venv сним будет выглядеть так, но лучше использовать anaconda:
1) python3.7 -m venv ./venv
2) source venv/bin/activate
3) pip install -r requirements.txt
4) запустить генератор тестового csv файла python data_generator.py
5) запустить файл генерирующий модель python main.py
6) визуализацию сделал через юпитер лаб ибо там удобнее смотреть на данные и словари, по этому запускаем jupyter lab
7) в открывшемся окне в браузере смотрим что получилось)
