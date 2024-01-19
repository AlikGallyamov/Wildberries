<h1 align="center">Проект по тестированию интернет-магазина <a href="https://www.wildberries.ru/"> Wildberries </a> </h1>



### Стек: Python, Selene, Pytest, Jenkins, Selenoid, Allure-report
<p align="left">
<img align="center" src="logo/python.svg" width="50"/>
<img align="center"  src="logo/selene.png" width="50"/>
<img align="center"  src="logo/pytest-original.svg" width="50"/>
<img align="center"  src="logo/Jenkins.svg" width="50"/>
<img align="center"  src="logo/Selenoid.svg" width="50"/>
<img align="center"  src="logo/Allure_new.png" width="50"/>
</p>

---

### Автотестами проверяется:

- Добавление товара в корзину  
- Удаление товара из корзины
- Поиск товара по названию  
- Поиск товара по артикулу  
- Поиск несуществующего товара  

Пример выполнения теста


<img src="readme_files/add_to_cart.gif" width="600"/>  

---

Отчёт о прохождении будет сгенерирован в allure-report с подробными шагами, скриншотами, видео.
Также, при необходимости можно подключить уведомления в Telegram, skype, discord, slack  


<img align="left" src="readme_files/allure_report.png" width="600" height="300"/>  
<img align="center" src="readme_files/tg_screen.png" width="200" height="300"/>.

---


### Как запустить

###### Удаленно

1. Открыть <a href="https://jenkins.autotests.cloud/job/009-JenkiLi-wildberries/"> jenkins-control  </a>
2. Нажать Build now
3. Дождаться завершения 
4. Перейти в allure отчет

<img src="readme_files/jenkins_control.png" width="400" height="200"/>  

###### Локально

1. Клонируйте репозиторий
```ruby
git clone https://github.com/AlikGallyamov/Wildberries.git
```
2. Создайте и активируйте виртуальное окружение
  ```ruby
  cd Wildberries
  python -m venv .venv
  .venv/Scripts/activate
  ```
3. Установите зависимости с помощью pip
  ```ruby
  pip install -r requirements.txt
  ```
3. Установите  <a href="https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.26.0/allure-commandline-2.26.0.zip"> Allure </a>. Распакуйте архив в папку с проектом. Распакованную папку переименуйте в "allure"
4. Запустите автотесты 
  ```ruby
  pytest tests
  ```
5. Получите отчёт allure
```ruby
allure serve allure-results
``` 




