from typing import final


# Есть приём с аннотацией метода декоратором @final, в таком случае при статическом анализе подсветится ошибка.
# На уровне интерпретатора, в Python нет никаких ограничений -- код выполнится, аннотация не ограничит.


class Base:
    @final
    def do_not_override(self) -> None:
        print("Это метод final — IDE подсветит ошибку при переопределении")


class Derived(Base):
    def do_not_override(self) -> None:
        # error: Cannot override final attribute "Base.do_not_override"
        print("Тем не менее, в рантайме Python это сработает")
