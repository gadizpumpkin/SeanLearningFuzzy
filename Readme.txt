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

Penentuan Kecepatan Kipas Otomatis

Sebuah ruangan server di sebuah perusahaan teknologi membutuhkan sistem pendingin yang dapat menyesuaikan kecepatan kipas secara otomatis agar suhu ruangan tetap stabil. Namun, kondisi suhu dan kelembapan di ruangan tersebut tidak selalu pasti atau berada pada batas yang jelas. Oleh karena itu, digunakan metode Fuzzy Logic untuk membantu menentukan tingkat kecepatan kipas. Sistem akan menerima dua input yaitu suhu ruangan dan kelembapan udara. Suhu dikategorikan menjadi himpunan fuzzy seperti dingin, normal, dan panas, sedangkan kelembapan dikategorikan menjadi rendah dan tinggi. Berdasarkan kombinasi kedua nilai tersebut, sistem menerapkan aturan (rule) seperti: Jika suhu panas dan kelembapan tinggi maka kecepatan kipas sangat cepat, atau Jika suhu normal dan kelembapan rendah maka kecepatan kipas sedang. Melalui proses fuzzifikasi, inferensi aturan, dan defuzzifikasi, sistem dapat menghasilkan nilai output berupa tingkat kecepatan kipas yang paling sesuai dengan kondisi ruangan saat itu.

