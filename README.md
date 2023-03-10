### HW_28 Тестирование веб-интерфейсов сайта Ростелеком https://b2c.passport.rt.ru/ .
---
- Проект представляет собой автоматизированые тесты, написанные на Python, и осуществляющие проверку основных функциональностей страницы авторизации и регистрации пользователя на сайте компании Ростелеком.
- Тесты написаны с помощью библиотек Pytest и Selenium v4.0.   
- В тестах использованы позитивные и негативные сценарии проверок, техники тест-дизайна: 
   - Исследовательское тестирование, Предположение об ошибках. 
   - Тестирование с помощью сценариев использования (прохождение в тестах процесса авторизации/регистрации, перехода по ссылкам и ожидание определенного результата в        конце).
   - Эквивалентное разделение и анализ граничных значений (при тестирование полей ввода, где есть конкретный диапазон количества вводимых символов).
   - Таблица альтернатив (при заполнении форм регистрации и авторизации разными комбинациями входных данных). 
- Для реализации в автотестах техник эквивалентного разделения, граничных значений, таблицы альтернатив использована фикстура @pytest.mark.parametrize .
- Тест-кейсы и баг-репорты : https://docs.google.com/spreadsheets/d/1VT-B0rjrZ9yTvK4bkm_YoQ8O0YUAn5wHZ85ikgxaH1k/edit?usp=sharing
---
### Структура проекта.
- В корневой директории расположены файлы:

        chromedriver.exe - Chromedriver
        settings.py - данные для выполнения тестов (email, пароли, имена пользователей и т.п.)
        
 - В директории /pages расположены файлы:
         
         locators.py - список локаторов
         base_page.py - базовая страница, от которой унаследованы все остальные классы         
         auth_page.py - содержит класс для страницы "Авторизация"
         registr_page.py - содержит класс для страницы "Регистрация"
         
- В директории /tests расположены файлы с тестами: 

        test_auth_page.py - автотесты для страницы "Авторизация"
        test_registr_page.py - автотесты для страницы "Регистрация"
---
### Команды для запуска тестов.
- Для запуска всех тестов:

        python -m pytest -v --driver Chrome --driver-path chromedriver.exe
        
- Для запуска тестов для страницы "Авторизация":

        python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_auth_page.py
        
- Для запуска тестов для страницы "Регистрация":

        python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_registr_page.py
        
-  Описанные команды работают на компьютере с установленными Python3 , PyTest , Selenium v4.0 , браузером Chrome.       
---
### Сценарии проверок автотестами.
- Каждый тест внутри проекта содержит описание своего назначения.
- Тестовые сценарии страницы "Авторизация" (test_auth_page.py):
    - Проверка различных элементов страницы на их наличие и название согласно Требованию.
    - Проверка табов меню "Авторизация".
    - При переходе по ссылкам "Забыл пороль" и  "Зарегистрироваться" открываются соответствующие страницы.
    - Проверка аутентификации пользователя с валидными и невалидными данными.
- Тестовые сценарии страницы "Регистрация" (test_registr_page.py):
    - Проверка различных элементов страницы на их наличие и название согласно Требованию.
    - Сценарии регистрации пользователя с валидными данными двух типов ("Имя" и "Фамилия" - буквы кириллицы либо тире).
    - Сценарии регистрации пользователя с данными, которы были использованы ранее.
    - Проверки полей ввода валидными и невалидными данными. 
