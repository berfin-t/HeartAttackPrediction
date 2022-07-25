# HeartAttackPrediction

This application is built using sklearn machine learning libraries and PyQt5 for the graphical user interface. It uses the "Logistic Regression" algorithm to classify the input data with 85% accuracy. The [Heart Disease UCI](https://www.kaggle.com/ronitf/heart-disease-uci) dataset in the "Kaggle Data" section was used.

# UTILIZATION

```bash
# Install libraries
$ pip3 install -r libraries.txt

# Get Build
$ py .\src\setup.py build

# Run it 
$ .\build\exe.win-amd64-3.10\heart_attack_prediction.exe
```

# DATASET ATTRIBUTE INFORMATION

- yaş
- cinsiyet
- göğüs ağrısı tipi (4 değer)
- istirahat kan basıncı
- mg / dl cinsinden serum kolestoral
- açlık kan şekeri> 120 mg / dl
- istirahat elektrokardiyografik sonuçları (0,1,2 değerleri)
- ulaşılan maksimum kalp atış hızı
- egzersize bağlı anjina
- oldpeak = dinlenmeye göre egzersizin neden olduğu ST depresyonu
- pik egzersiz ST segmentinin eğimi
- florosopi ile renklendirilen ana damarların sayısı (0-3)
- tal: 3 = normal; 6 = sabit kusur; 7 = tersine çevrilebilir kusur
