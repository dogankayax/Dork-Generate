from colorama import  *

#Color Name
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
BLACK = Fore.LIGHTBLACK_EX
RED = Fore.RED
MAGENTA = Fore.MAGENTA
STYLE = Style.RESET_ALL
def help_menu():
    logo = """
                                                                                 
,--.  ,--.,------.,--.   ,------.     ,--.   ,--.,------.,--.  ,--.,--. ,--. 
|  '--'  ||  .---'|  |   |  .--. '    |   `.'   ||  .---'|  ,'.|  ||  | |  | 
|  .--.  ||  `--, |  |   |  '--' |    |  |'.'|  ||  `--, |  |' '  ||  | |  | 
|  |  |  ||  `---.|  '--.|  | --'     |  |   |  ||  `---.|  | `   |'  '-'  ' 
`--'  `--'`------'`-----'`--'         `--'   `--'`------'`--'  `--' `-----'  
                                                                             """
    print(YELLOW + logo + STYLE)



    print(f"{CYAN}*{STYLE}" * 60 )
    print(f"{BLACK} <> GOOGLE DORKING REHBERİ <> {STYLE }".center(60))
    print(f"{CYAN}*{STYLE}" * 60)
    print(f"{MAGENTA}\n Google Dorking (veya Google Hacking), Google’ın gelişmiş arama")
    print("operatörlerini kullanarak normal aramalarda görünmeyen bilgileri bulma")
    print("yöntemidir. Genelde etik hackerlar ve siber güvenlik uzmanları tarafından")
    print("bilgi toplama (recon) aşamasında kullanılır.\n")
    print("⚙️  TEMEL DORK TERİMLERİ ve ANLAMLARI:\n")
    print("🔸 site:")
    print("   → Belirli bir domain üzerinde arama yapar.")
    print("   Örnek: site:gov.tr\n")
    print("🔸 filetype: (veya ext:)")
    print("   → Belirli bir dosya türünü arar.")
    print("   Örnek: filetype:pdf siber güvenlik\n")
    print("🔸 intitle:")
    print("   → Sayfa başlığında geçen kelimeleri bulur.")
    print("   Örnek: intitle:\"index of\"\n")
    print("🔸 inurl:")
    print("   → URL kısmında belirli kelimeleri arar.")
    print("   Örnek: inurl:login\n")
    print("🔸 intext:")
    print("   → Sayfa içeriğinde geçen kelimeleri arar.")
    print("   Örnek: intext:\"confidential\"\n")
    print("🔸 cache:")
    print("   → Sayfanın Google tarafından kaydedilmiş (önbellek) hâlini gösterir.")
    print("   Örnek: cache:example.com\n")
    print("🔸 related:")
    print("   → Belirtilen siteye benzer siteleri listeler.")
    print("   Örnek: related:facebook.com\n")
    print("🔸 link:")
    print("   → Belirli bir siteye bağlantı veren diğer siteleri bulur.")
    print("   Örnek: link:example.com\n")
    print(" ÖZETLE:")
    print("Google Dorking, hacklemek değil; bilgiyi doğru şekilde arama sanatıdır.")
    print(f"Doğru operatörleri birleştirerek siber güvenlikte güçlü bir bilgi kaynağı sağlar.\n {STYLE}")
    print(f"{CYAN}={STYLE}" * 60)
    print(f"{BLACK}💡 Kısaca: Bilgiyi gizli yerinden bulma sanatıdır.{STYLE}")
    print(f"{CYAN}={STYLE}" * 60)

if __name__ == "__main__":
    help_menu()