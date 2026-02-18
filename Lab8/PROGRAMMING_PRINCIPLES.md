# Дотримання принципів програмування в проекті

## 1. Single Responsibility Principle (SRP)
Кожен клас відповідає за одну задачу. `Bank` класу в `bank.py` лише керує балансом через `deposit()`, `withdraw()`, `get_balance()`.  
`Validators` в `validators.py` містять лише функції перевірки: `validate_email()`, `validate_year()`, `validate_age()` - винесено окремо від бізнес-логіки.  
Клас `Privileges` в `admin_module.py` лише показує список прав через `show_privileges()`, а `Admin(User)` делегує йому цю задачу.

## 2. Open/Closed Principle (OCP)  
Код відкритий для розширення через наслідування. Базовий `Dog` в `pets.py` має `bark()`, а підкласи `Labrador`, `GermanShepherd`, `Husky` додають `fetch()`, `guard()`, `howl()` без змін `Dog`.  
`Discount(Shop)` в `shop.py` розширює магазин методом `get_discount_products()` без модифікації `Shop`.  
`Pets.add()` приймає будь-яку породу через поліморфізм в `info()`.

## 4. DRY (Don't Repeat Yourself)
Валідація винесена в `validators.py`: `validate_string_no_digits()` використовується в `Car.make/model`, `Dog.name/breed`; `validate_age()` - для всіх собак.  
Константи з `config.py` (`DOG_MAX_AGE=30`, `CAR_MIN_YEAR=1886`, `BUFFER_SIZE=5`) застосовуються всюди замість хардкоду.  
Римська конвертація в `roman.py` - єдине місце з перевіркою коректності.

## 5. KISS (Keep It Simple, Stupid)
Методи короткі та прямі: `Coin.toss()` - один `random.choice()`; `Bank.deposit()` - валідація + додавання; `Car.accelerate()` - `+= CAR_SPEED_STEP`.  
`Buffer.add()` в `buffer.py` - проста логіка FIFO без складних патернів.  
Логіка в `task1()`-`task9()` - лінійні приклади без зайвих абстракцій.

## 6. Інкапсуляція
Приватні атрибути: `Bank.__balance`, `Car.__speed`, `Coin.__sideup` - доступ лише через методи (`get_balance()`, `get_speed()`, `toss()`).  
Валідація на вході: `validate_email()` з regex, `validate_name()` з перевіркою довжини/літер захищає об'єкти від некоректних даних.  
`Privileges.privileges` прихований, доступний лише через `show_privileges()`.

## 7. Defensive Programming
Кожен конструктор валідує параметри: `Shop.__init__()` - непорожні рядки; `User.__init__()` - email, ім'я, нікнейм; `DecimalToRoman` - діапазон 1-3999.  
Окремі винятки: `NameTooShortError` для семантичних помилок, `ValueError` з контекстом ("Недостатньо: 120").  
Перевірка римських чисел: `RomanToDecimal` валідує символи та формат.