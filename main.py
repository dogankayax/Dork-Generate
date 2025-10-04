import os
import sys
import time
from colorama import Fore, Style, init
from datetime import datetime
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'files'))
from files.help import help_menu

sys.path.append(os.path.join(os.path.dirname(__file__),'files'))
from files.dork_extract import ext_dork

init(autoreset=True)


class Colors:
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE
    BRIGHT = Style.BRIGHT
    DIM = Style.DIM
    RESET = Style.RESET_ALL


class Animation:
    @staticmethod
    def loading(text: str, duration: int = 3):
        chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        start_time = time.time()
        i = 0

        while time.time() - start_time < duration:
            print(f"\r{Colors.CYAN}{chars[i % len(chars)]} {text}{Colors.RESET}", end="", flush=True)
            time.sleep(0.1)
            i += 1
        print("\r" + " " * (len(text) + 10) + "\r", end="", flush=True)

    @staticmethod
    def typewriter(text: str, delay: float = 0.03):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    @staticmethod
    def countdown(seconds: int):
        for i in range(seconds, 0, -1):
            print(f"\r{Colors.YELLOW}⏳ {i} saniye sonra devam edecek...{Colors.RESET}", end="")
            time.sleep(0.1)
        print("\r" + " " * 50 + "\r", end="")


def display_logo():
    logo = f"""
{Colors.BRIGHT}{Colors.RED}
  ___          _      ___                       _          _ 
 |   \ ___ _ _| |__  / __|___ _ _  ___ _ _ __ _| |_ ___ __| |
 | |) / _ \ '_| / / | (_ / -_) ' \/ -_) '_/ _` |  _/ -_) _` |
 |___/\___/_| |_\_\  \___\___|_||_\___|_| \__,_|\__\___\__,_|
                                                             
    """

    os.system('cls' if os.name == 'nt' else 'clear')
    Animation.typewriter(logo)
    print(f"\n{Colors.DIM}{'=' * 60}{Colors.RESET}")
    print(f"{Colors.WHITE} Dev: {Colors.CYAN}Dogan Kaya{Colors.RESET}")
    print(f"{Colors.WHITE} Time: {Colors.GREEN}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.RESET}")
    print(f"{Colors.DIM}{'=' * 60}{Colors.RESET}\n")


# Ana menü
def display_menu():
    menu_items = [
        f"{Colors.BRIGHT}{Colors.GREEN} {Colors.WHITE}Yardım Menüsü{Colors.RESET}",
        f"{Colors.BRIGHT}{Colors.BLUE} {Colors.WHITE}Dork Oluşturucu{Colors.RESET}",
        f"{Colors.BRIGHT}{Colors.RED} {Colors.WHITE}Çıkış{Colors.RESET}"
    ]

    print(f"\n{Colors.BRIGHT}{Colors.YELLOW} {Colors.WHITE}ANA MENÜ{Colors.RESET}")
    print(f"{Colors.DIM}{'─' * 40}{Colors.RESET}")

    for i, item in enumerate(menu_items, 1):
        print(f"  {Colors.BRIGHT}{Colors.CYAN}{i}.{Colors.RESET} {item}")

    print(f"{Colors.DIM}{'─' * 40}{Colors.RESET}")


def dork_creation_interface():
    print(f"\n{Colors.BRIGHT}{Colors.BLUE}🔧 {Colors.WHITE}DORK OLUŞTURUCU{Colors.RESET}")
    print(f"{Colors.DIM}{'─' * 60}{Colors.RESET}")

    inputs = [
        (" İntext değeri", "intext"),
        ("🏷  İntitle değeri", "intitle"),
        (" İnurl değeri", "inurl"),
        (" Hedef site URL", "target"),
        (" Dosya türü", "filetype")
    ]

    results = {}

    for display_name, key in inputs:
        if "dosya" in display_name.lower():
            print(f"\n{Colors.YELLOW} İpucu: {Colors.WHITE}pdf, doc, xls, txt, vb.{Colors.RESET}")

        value = input(f"\n{Colors.GREEN}➡️  {Colors.WHITE}{display_name} girin (boş bırakabilirsiniz): {Colors.CYAN}")
        results[key] = value if value.strip() else ""

    return results



def exit_program():
    print(f"\n{Colors.BRIGHT}{Colors.RED}👋 {Colors.WHITE}Programdan Çıkılıyor...{Colors.RESET}")
    Animation.loading("Son işlemler tamamlanıyor", 2)

    farewell_messages = [
        f"{Colors.GREEN}✅ {Colors.WHITE} Çıkış  yapıldı{Colors.RESET}",
    ]

    for message in farewell_messages:
        print(message)
        time.sleep(0.5)

    sys.exit(0)


def handle_error(message: str):
    print(f"\n{Colors.RED}❌ {Colors.WHITE}Hata: {message}{Colors.RESET}")
    input(f"\n{Colors.YELLOW}⏎ {Colors.WHITE}Devam etmek için Enter'a basın...{Colors.RESET}")


def main_function():
    try:
        while True:
            display_logo()
            display_menu()

            try:
                secim = input(f"\n{Colors.BRIGHT}{Colors.WHITE} {Colors.CYAN}Seçiminiz (1-4): {Colors.RESET}").strip()

                if secim == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    help_menu()
                    input(f"\n{Colors.YELLOW}⏎ {Colors.WHITE}Ana menüye dönmek için Enter'a basın...{Colors.RESET}")

                elif secim == "2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    display_logo()

                    inputs = dork_creation_interface()

                    print(f"\n{Colors.YELLOW}🔄 {Colors.WHITE}Dork oluşturuluyor...{Colors.RESET}")
                    Animation.loading("Bilgiler işleniyor", 2)

                    try:
                        ext_dork(
                            target=inputs['target'],
                            intitle=inputs['intitle'],
                            intext=inputs['intext'],
                            filetype=inputs['filetype'],
                            inurl=inputs['inurl']
                        )
                    except Exception as e:
                        handle_error(f"Dork oluşturma hatası: {str(e)}")

                    input(f"\n{Colors.YELLOW}⏎ {Colors.WHITE}Devam etmek için Enter'a basın...{Colors.RESET}")

                elif secim == "3":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    display_logo()

                elif secim == "4":
                    exit_program()

                else:
                    print(
                        f"\n{Colors.RED}⚠️  {Colors.WHITE}Geçersiz seçim! Lütfen 1-4 arası bir sayı girin.{Colors.RESET}")
                    Animation.countdown(3)

            except KeyboardInterrupt:
                print(f"\n\n{Colors.YELLOW}⚠️  {Colors.WHITE}İşlem kullanıcı tarafından iptal edildi.{Colors.RESET}")
                if input(f"\n{Colors.RED}❓ {Colors.WHITE}Çıkmak istiyor musunuz? (e/h): {Colors.RESET}").lower() == 'e':
                    exit_program()

    except Exception as e:
        handle_error(f"Beklenmeyen hata: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main_function()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}🚪 {Colors.WHITE}Program kapatıldı.{Colors.RESET}")
        sys.exit(0)