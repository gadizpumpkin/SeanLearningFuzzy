Project menentukan kebutuhan kebutuhan berdasarkan greyzone.
tambahkan gambar cuy,

Fuzzy component:
 - Fuzzyfication    : mengubah angka menjadi nilai keanggotaan
 - Rule Base        : aturan IF-THEN
 - Inferensi        : menghitung hasil aturan
 - Defuzzyfication  : mengubah hasil fuzzy menjadi angka pasti


 Fuzzy Tsukamoto => Output setiap rule harus berbentuk fungsi monoton

 Contoh rule:

IF permintaan TINGGI
AND persediaan SEDIKIT
THEN produksi BERTAMBAH

Setiap rule menghasilkan nilai crisp (angka).

Input data
↓
Fuzzifikasi
↓
Evaluasi Rule
↓
Hitung α-predikat (MIN)
↓
Cari nilai z
↓
Defuzzifikasi
↓
Output