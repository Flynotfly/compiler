
<br />
<div align="center">
  <h3 align="center">Compiler</h3>

  <p align="center">
    Компилятор C-подобного проприетарного языка
    <br />
  </p>
</div>


Этот проект представляет собой базовый компилятор для небольшого, C-подобного языка программирования, разработанный с использованием Python и библиотеки `ply`. Он обрабатывает исходный код в несколько этапов: лексический анализ, синтаксический анализ, семантический анализ и генерация промежуточного кода.

---
## Возможности

* **Лексический анализ**: Разбивает исходный код на поток токенов.
* **Синтаксический анализ**: Разбирает поток токенов для построения абстрактного синтаксического дерева (AST) в соответствии с грамматикой языка.
* **Семантический анализ**:
    * Управляет **таблицей символов** для отслеживания объявлений переменных.
    * Выполняет **проверку типов** для присваиваний и выражений.
    * Сообщает о семантических ошибках, таких как использование необъявленных переменных или несоответствие типов.
* **Генерация промежуточного кода**: Создает список **квадруполей** (форма трехадресного кода), представляющих операции программы.

---
## Поддерживаемые конструкции языка

* **Типы данных**: `int`, `double`, `string`, `bool`.
* **Объявления переменных**: `int x;`
* **Присваивания**: `x = 10;`
* **Арифметические выражения**: Поддерживаются `+`, `-`, `*`, `/`.
* **Операторы вывода**: `Print("Hello World");`
* **Комментарии**: Поддерживаются как однострочные (`// ...`), так и многострочные (`/* ... */`) комментарии.

---
## Зависимости

* Python 3.9
* PLY (`pip install ply`)
