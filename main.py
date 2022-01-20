# Импорт необходимых функций из других файлов
from StartScreen import start_screen
from Registration import registration
from Reg_rules import reg_rules


def main():  # Основная функция, которая отвечает за запуск всех программы
    reg_rules()
    registration()
    start_screen()


if __name__ == "__main__":
    main()