// 6.1

user_input - search_query
// поисковый запрос пользователя

result - project_names
// список в методе получения имен проектов из БД. В него записывались результаты запроса

notification - alert_user_of_error
// флаг в методе, отвечающий за то, показывать уведомление пользователю или нет

calculate - determine_monthly_expenses
//метод рассчитывает месячные расходы

process_image - add_rectangle_and_text_to_image
// метод считывает изображение и добавляет прямоугольник в текст

// 6.2

undo_stack - undo_stack
// В классе буфера обмена в качестве атрибута использовался стек, в который записывались действия отмены. Аналогично был
redo_stack

DataCache - DataCache
// использовался термин 'кэш' в реализации кэша


image_processor - image_filter_decorator
// использование "decorator" указывает на паттерн декоратор

create_button - ButtonFactory.create_button
// "Factory" в названии класса указвает на паттерн фабричный метод

// 6.3

name - name
// класс user - имя пользователя.

adress - shipping_address
// адрес доставки в методе обработки заказа

host - host
//хост в методе установки соединения с БД

// 6.4

r - radius
// слишком короткое имя переменной, хранящей радиус

send_notification_to_all_users_via_email - email_all_users
// метод рассылки писем всем пользователям

number_of_users_in_the_company - users_count
// число пользователей

total_amount_of_money_earned_by_the_company_last_year - last_year_revenue
// слишком длинное имя. заработок компаний за прошлый год

i - index
// i в цикле можно заменить на index