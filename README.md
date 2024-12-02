# Учебный проект Skypro.

## Создание виджета для банковских операций.

### Разработка серверной части виджета банковских операций.

#### __Директории и модули:__

### ***__src/masks.py__***
_Модуль для маскировки номера карты и/или номера счета._\
_Формат маскировки номера карты: XXXX XX** **** XXXX, где X - цифры номера счета._\
_Формат маскировки номера счета: **XXXX, где XXXX - последние 4 цифры номера счета._

__Функции:__
* get_mask_card_number(card_number) - возвращает маску введенного номера карты.\
Где (card_number) - 16-ти значный номер карты.
* get_mask_account(account_number) - возвращает маску введенного номера счета.\
Где (account_number) - 20-ти значный номер счета.

### ***__tests/test_masks.py__***
_Модуль для тестирования функций из модуля src/masks.py._

__Функции:__
* test_get_mask_card_number(card_number, expected) - тесты для проверки работоспособности функции.\
Где (card_number, expected) - передаваемые данные и ожидаемый результат.
* test_get_mask_account(account_number, expected) - тесты для проверки работоспособности функции.\
Где (account_number, expected) - передаваемые данные и ожидаемый результат.

***widget.py***\
Описание в разработке

***processing.py***\
Описание в разработке
