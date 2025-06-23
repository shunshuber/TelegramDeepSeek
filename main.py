import time
import random
import sys
import os

class Terminator:
    def __init__(self):
        self.username = ""
        self.phone = ""
        self.delay = 0.05
        self.colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'magenta': '\033[95m',
            'cyan': '\033[96m',
            'white': '\033[97m',
            'reset': '\033[0m'
        }
        
    def print_banner(self):
        print(f"""{self.colors['red']}
    ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██████╗ ██████╗ 
    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██╔══██╗██╔══██╗
       ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██████╔╝██║  ██║
       ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██╔══██╗██║  ██║
       ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║██║  ██║██████╔╝
       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
        {self.colors['cyan']}v2.0 | Telegram Account Terminator (Simulation){self.colors['reset']}
        """)
        
        print(f"{self.colors['magenta']}")
        print("              ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print("              █░▄▄█░▄▀▄░█▀▄▄▀█░▄▄█░▄▄▀█░▄▀▄░█░▄▄▀█▄░▄█░▄▄▀█░▄▄█░▄▄▀█░▄▄")
        print("              █░▄▄█░█▄█░█░██░█░▄▄█░▀▀░█░█▄█░█░▀▀▄██░██░▀▀░█░▄▄█░██░█▄▄▀")
        print("              █▄▄▄█▄███▄█▄██▄█▄▄▄█▄██▄█▄███▄█▄█▄▄██▄██▄██▄█▄▄▄█▄▄██▄▄▄▄")
        print("              ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
        print(f"{self.colors['reset']}")
        
        print(f"{self.colors['yellow']}[!] ВНИМАНИЕ: Это симуляция разрушения. Никакие данные не будут изменены.{self.colors['reset']}")
        print(f"{self.colors['yellow']}[!] Программа создана исключительно для образовательных целей{self.colors['reset']}\n")

    def typewriter(self, text, color='reset'):
        for char in text:
            sys.stdout.write(f"{self.colors[color]}{char}{self.colors['reset']}")
            sys.stdout.flush()
            time.sleep(self.delay)
        print()

    def hacking_animation(self, duration=3):
        end_time = time.time() + duration
        chars = ["/", "-", "\\", "|"]
        while time.time() < end_time:
            for c in chars:
                sys.stdout.write(f"\r{self.colors['green']}[ХАКИНГ] Взлом системы Telegram {c}{self.colors['reset']}")
                sys.stdout.flush()
                time.sleep(0.1)
        print("\n")

    def delete_account(self):
        self.print_banner()
        
        # Запрос данных
        self.typewriter(">>> Введите номер телефона Telegram аккаунта: ", 'cyan')
        self.phone = input()
        self.typewriter(">>> Введите username цели: ", 'cyan')
        self.username = input()
        
        # Начало атаки
        self.typewriter(f"\n>>> ИНИЦИАЛИЗАЦИЯ АТАКИ НА @{self.username} ({self.phone})", 'red')
        self.hacking_animation()
        
        # Процесс "удаления"
        steps = [
            ("ПОДКЛЮЧЕНИЕ К СЕРВЕРАМ TELEGRAM", 0.8),
            ("ОБХОД ДВУХФАКТОРНОЙ АУТЕНТИФИКАЦИИ", 0.9),
            ("ДЕШИФРОВКА КЛЮЧЕЙ СЕССИИ", 1.2),
            ("ДОСТУП К БАЗЕ ДАННЫХ ПОЛЬЗОВАТЕЛЯ", 0.7),
            ("ПЕРЕЗАПИСЬ MESSAGE HISTORY", 1.5),
            ("УДАЛЕНИЕ ВЛОЖЕНИЙ И МЕДИА", 1.0),
            ("СБРОС НАСТРОЕК ПРОФИЛЯ", 0.6),
            ("ОТЗЫВ СЕССИЙ АВТОРИЗАЦИИ", 0.8),
            ("ПЕРЕЗАПИСЬ КОДА АВТОРИЗАЦИИ", 1.1),
            ("ОТПРАВКА ЗАПРОСА НА ПОЛНОЕ УДАЛЕНИЕ", 0.9),
            ("ПОДТВЕРЖДЕНИЕ ОПЕРАЦИИ ОТ СЕРВЕРА", 1.3)
        ]
        
        for step, duration in steps:
            self.typewriter(f"[$] {step}...", 'magenta')
            time.sleep(duration)
            print(f"{self.colors['green']}[+] УСПЕШНО{self.colors['reset']}\n")
            time.sleep(0.3)
        
        # Финальная анимация
        print(f"{self.colors['red']}")
        print("              █████████████████████████████████████████████████")
        print("              ████▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀████")
        print("              ████  АККАУНТ УСПЕШНО УНИЧТОЖЕН  ████████████████")
        print("              ████▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄████")
        print("              █████████████████████████████████████████████████")
        print(f"{self.colors['reset']}")
        
        # Заключительное сообщение
        time.sleep(2)
        self.typewriter(f"\n>>> ОПЕРАЦИЯ TERMINATE УСПЕШНО ЗАВЕРШЕНА", 'green')
        self.typewriter(f">>> Аккаунт @{self.username} ({self.phone}) больше не существует", 'green')
        self.typewriter(f">>> Все данные стерты с серверов Telegram", 'green')
        self.typewriter(f">>> Восстановление невозможно", 'red')
        
        # Шутка
        time.sleep(3)
        print(f"\n{self.colors['yellow']}[!] PS: Это была симуляция. Ваш аккаунт в безопасности! ;){self.colors['reset']}")
        print(f"{self.colors['cyan']}    (Никакие реальные действия не были выполнены){self.colors['reset']}")

    def run(self):
        self.delete_account()

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    terminator = Terminator()
    terminator.run()
