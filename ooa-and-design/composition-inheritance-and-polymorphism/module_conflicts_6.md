## 1. Существуют ли ситуации, когда связи между модулями должны делаться публичными?

Да, конечно, например, когда один модуль предоставляет интерфейсы другим модулям, связь должна быть публичной.
Публичные методы нужны, чтобы один класс мог запросить у другого какие-то действия, данные или ресурсы. Класс с
константами / конфигами -- минимум.

## 2. Какие метрики вы бы предложили для количественной оценки принципов организации модулей?

* Размер класса: число методов, строк кода, чтобы было не слишком много.
* Количество публичных методов и атрибутов.
* Количество связей текущего модуля с другими.

## 3. Если вы разрабатывали программы, в которых было хотя бы 3-5 классов, как бы вы оценили их модульность по этим метрикам?

* Зависимость классов друг от друга, как правило, очень высокая. В тех случаях, где нужно хранить состояние, очень
  сложно "вырвать" какой-то один класс и воспользоваться им -- протестировать, или переиспользовать. Слабая зависимость
  только в тех классах, которые являются набором "расчётных" методов, объединенных.

* Размер классов - строк по 200 в среднем, всегда по разному. Очень маленьких классов практически нет, только если
  логика совсем мелкая. Часто пихаю смежные вещи не по двум классам а в один.

* Публичность методов -- слежу за этим и выношу только важные операции / команды.
