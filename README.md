
# Dork-Generate

Dork-Generate, siber güvenlik uzmanları ve etik hackerlar için gelişmiş Google Dork sorguları oluşturmayı kolaylaştıran Python tabanlı bir araçtır. Google arama operatörlerini kullanarak bilgi toplama ve keşif süreçlerini otomatikleştirir.

## Özellikler
- Etkileşimli CLI menüsü ile özel Google Dork oluşturma
- Selenium ile otomatik tarayıcı etkileşimi
- Colorama ile renkli terminal çıktısı
- Google Dorking kavramlarını açıklayan yerleşik yardım menüsü
- intext, intitle, inurl, filetype ve hedef site için özel giriş desteği

## Nasıl Çalışır?
Dork-Generate, Selenium kullanarak https://dorkgenerator.com/ sitesine bağlanır ve kullanıcıdan alınan girdilerle Google Dork sorguları oluşturur. Kullanıcı dostu arayüzü ile etkili arama sorguları oluşturmanıza yardımcı olur.

## Kurulum
1. Depoyu klonlayın veya `Dork-Generate` dizinini kopyalayın.
2. Gerekli kütüphaneleri yükleyin:
   ```
   pip install -r requirements.txt
   ```

## Kullanım
Ana dosyayı çalıştırın:
```bash
python main.py
```
Etkileşimli menüden kendi Google Dork'unuzu oluşturun.

## Dizin Yapısı
```
Dork-Generate/
  main.py           # Ana CLI arayüzü
  requirements.txt  # Poejede kullanılan python kütüphaneleri
  files/
    dork_extract.py # Selenium tabanlı dork oluşturucu
    help.py         # Yardım menüsü ve Google Dorking rehberi
```

## Kütüphaneler
- selenium
- colorama

## Örnek
```
$ python main.py
  ___          _      ___                       _          _ 
 |   \ ___ _ _| |__  / __|___ _ _  ___ _ _ __ _| |_ ___ __| |
 | |) / _ \ '_| / / | (_ / -_) ' \/ -_) '_/ _` |  _/ -_) _` |
 |___/\___/_| |_\_\  \___\___|_||_\___|_| \__,_|\__\___\__,_|

ANA MENÜ
1. Yardım Menüsü
2. Dork Oluşturucu
3. Çıkış
```

## Google Dorking
Yerleşik yardım menüsünde Google Dorking operatörleri ve kullanımı hakkında kapsamlı bir rehber bulabilirsiniz.

## Dev
- Doğan Kaya

## Lisans
Bu proje yalnızca eğitim ve araştırma amaçlıdır.
