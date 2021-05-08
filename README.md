HeartAttackPrediction

Bu uygulama, sklearn makine öğrenimi kitaplıkları ve grafik kullanıcı arabirimi için pyQt5 kullanılarak yapılmıştır. "Logistik Regression" algoritması kullanılıp girdi verilerini %85 doğrulukla sınıflandırır. "Kaggle Data" bölümünden "Heart Disease UCI" veri seti kullanılmıştır.( https://www.kaggle.com/ronitf/heart-disease-uci )

KULLANIM 

--> Öncelikle aşağıdaki komutla tüm kütüphaneleri kurun.

pip3 install -r libraries.txt

--> Şimdi PC'nizdeki uygulamayı şu şekilde eğitin:

python3 prediction_file.py

--> Son olarak uygulamayı çalıştırın:

python3 test.py

VERİ SETİ ÖZNİTELİK BİLGİLERİ

1.yaş
2.cinsiyet
3.göğüs ağrısı tipi (4 değer)
4.istirahat kan basıncı
5.mg / dl cinsinden serum kolestoral
6.açlık kan şekeri> 120 mg / dl
7.istirahat elektrokardiyografik sonuçları (0,1,2 değerleri)
8.ulaşılan maksimum kalp atış hızı
9.egzersize bağlı anjina
10.oldpeak = dinlenmeye göre egzersizin neden olduğu ST depresyonu
11.pik egzersiz ST segmentinin eğimi
12.florosopi ile renklendirilen ana damarların sayısı (0-3)
13.tal: 3 = normal; 6 = sabit kusur; 7 = tersine çevrilebilir kusur
