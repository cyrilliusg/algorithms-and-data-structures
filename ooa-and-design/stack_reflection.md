# Рефлексия к 1 заданию "Стек"

Изначальная версия ограниченного стека работает, но не учитывает формальные требования к АТД, а именно:

1. Не задокументированы подробно предусловия и постусловия операций.

2. Отсутствует механизм возврата статусов операций (через специальные геттеры), позволяющий явно отслеживать корректность выполнения команд.

3. Использовались исключения для контроля переполнения стека, что не соответствует требованию, поскольку предпочтительнее - применение статусных кодов.

Таким образом, первоначальное решение задания практически полностью не соответствует ожидаемому результату, что будет учтено при выполнении будущих заданий.