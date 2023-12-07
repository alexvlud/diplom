В проекте 2 тестовых сценария:

  test_smoke_rostelecom.py - тестирует Web UI элементы главной страницы сайта авторизации в личном кабинете Ростелеком ID (https://b2c.passport.rt.ru/)
  test_auth_page.py - тестирует процесс авторизации зарегистрированного пользователя в системе Ростелеком ID (https://b2c.passport.rt.ru/)

Файлы:
    auth_data.py - данные пользователя для авторизации
    auth_page.py - содержит вспомогательный класс для тестирования страницы авторизации
    pages/base.py - содержит реализацию  PageObject pattern на Python. 
    pages/elements.py - содержит вспомогательный класс для определения web elements на web pages.
    rostelecom.py - содержит вспомогательный класс для тестирования Web UI элементов главной страницы сайта. 
    conftest.py - содержит необходимый код для отлавливания ошибок и создания скриншотов в упавших тестах.

Запуск:
  
  1. Установить все элементы:
      pip3 install -r requirements

  2. Скачать совместимую с браузером версию Selenium WebDriver с ресурса https://chromedriver.chromium.org/downloads

  3. Запустить тесты:
      python -m pytest -v --driver Chrome --driver-path path_to_webdriver Path_to_test\test_smoke_rostelecom.py
      python -m pytest -v --driver Chrome --driver-path path_to_webdriver Path_to_test\test_auth_page.py
