class Money(float):
    def __str__(self) -> str:
        return f'${self.__float__():>13,.2f}'

class Percent(float):
    def __str__(self) -> str:
        return f'{self.__float__():.0%}'