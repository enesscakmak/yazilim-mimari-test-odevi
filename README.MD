# Login Test

Bu proje, https://the-internet.herokuapp.com/login sayfasında hatalı kullanıcı girişi yapıldığında hata mesajının görünürlüğünü test eder.

## 📍 Test Senaryosu

-   Tarayıcı açılır
-   Login sayfasına gidilir: [`https://the-internet.herokuapp.com/login`](https://the-internet.herokuapp.com/login)
-   Geçersiz kullanıcı adı veya şifre girilir
-   “Your username is invalid!” mesajının görünüp görünmediği kontrol edilir
-   Test sonucu raporlanır

## Gereksinimler

-   Python 3.x
-   Selenium
-   ChromeDriver

## Çalıştırmak için

```bash
pip install selenium
python tests/test_login_invalid.py
```
