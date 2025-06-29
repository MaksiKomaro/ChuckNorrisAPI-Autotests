# Описание
Демонстрационные автотесты https://api.chucknorris.io/ с использованием pytest,
asyncio, allure и других инструментов.
Цель - продемонстрировать разницу в асинхронном выполнении 16 тестов относительно
синхронного, показать умении в составлении простых pipeline, работу с Allure. 

# Запуск
Запуск тестов производится командой python -m pytest tests
Для генерации отчета Allure добавить флаг --alluredir allure-results

Для создания и запуска отчета выполнить команду allure serve allure-results

При коммите и ручном запуске происходит автотестирование кода с помощью GitHub Actions,
при этом автоматически создается и загружается в Github Pages allure-отчет.

# Немного о сравнении продолжительности асинхронных тестов
Как показывает тестирование, асинхронное выполнение 16 запросов по категориям
выполняется в ~9-10 раз быстрее (linux, mac), чем последовательное.
Однозначно, при росте числа запросов эта разница может стать еще весомее.

Для просмотра времени тестирования можно перейти на страницу Actions репозитория, 
выбрать слева в workflow "pages-build-deployment" и перейти в этот раздел. Внутри
будет небольшая схема с элементом "deploy" и ссылкой на Allure отчет. Изучив отчет,
можно увидеть, что среднее время 1-го из 16-ти последовательных запросов около 450мс,
тогда как 16 асинхронных запросов выполняются примерно за 800-900мс. И это еще без
модуля xdist для параллельного запуска тестов!

# Немного фактов о Чаке Норрисе
«Чак Норрис может проводить модульное тестирование целых приложений с помощью одного assert».
«Если Чак Норрис пишет код с ошибками, ошибки исправляются сами собой».
«Чаку Норрису не нужен sudo, он просто вводит "Chuck Norris" перед своими командами».
«Чак Норрис делает бесконечные циклы за 4 секунды».
«Google не будет искать Чака Норриса, потому что знает, что не вы находите Чака Норриса, а он находит вас».
«Чак Норрис может получить доступ к закрытым методам».
