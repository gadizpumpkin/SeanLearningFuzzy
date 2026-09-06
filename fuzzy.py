<<<<<<< Updated upstream
# Input
=======
# ============================================================
# IMPLEMENTASI FUZZY LOGIC TSUKAMOTO
# Menentukan kecepatan kipas berdasarkan suhu dan kelembapan
# ============================================================


# ------------------------------------------------------------
# INPUT
# ------------------------------------------------------------
# Nilai suhu dalam satuan Celsius (°C)
>>>>>>> Stashed changes
suhu = 30
kelembapan = 70

<<<<<<< Updated upstream
# FUZZIFIKASI SUHU
=======

# ------------------------------------------------------------
# FUZZIFIKASI SUHU
# ------------------------------------------------------------
# Mengubah nilai suhu crisp menjadi derajat keanggotaan
# pada himpunan fuzzy "Dingin".
#
# Aturan keanggotaan:
# - Suhu <= 20°C       -> sepenuhnya Dingin (1)
# - 20°C < suhu < 30°C -> derajat keanggotaan menurun linear
# - Suhu >= 30°C       -> bukan Dingin (0)
>>>>>>> Stashed changes
def suhu_dingin(x):
    if x <= 20:
        return 1
    elif 20 < x < 30:
        return (30 - x) / 10
    else:
        return 0

def suhu_panas(x):
    if x <= 25:
        return 0
    elif 25 < x < 35:
        return (x - 25) / 10
    else:
        return 1

<<<<<<< Updated upstream
# FUZZIFIKASI KELEMBAPAN
=======

# ------------------------------------------------------------
# FUZZIFIKASI KELEMBAPAN
# ------------------------------------------------------------
# Mengubah nilai kelembapan crisp menjadi derajat keanggotaan
# pada himpunan fuzzy "Rendah".
#
# Aturan keanggotaan:
# - Kelembapan <= 40%       -> sepenuhnya Rendah (1)
# - 40% < kelembapan < 60%  -> derajat keanggotaan menurun linear
# - Kelembapan >= 60%       -> bukan Rendah (0)
>>>>>>> Stashed changes
def lembap_rendah(x):
    if x <= 40:
        return 1
    elif 40 < x < 60:
        return (60 - x) / 20
    else:
        return 0

def lembap_tinggi(x):
    if x <= 50:
        return 0
    elif 50 < x < 80:
        return (x - 50) / 30
    else:
        return 1

<<<<<<< Updated upstream
# HITUNG NILAI FUZZY
=======

# ------------------------------------------------------------
# HITUNG NILAI FUZZY
# ------------------------------------------------------------
# Menghitung derajat keanggotaan suhu terhadap:
# - Dingin
# - Panas
>>>>>>> Stashed changes
dingin = suhu_dingin(suhu)
panas = suhu_panas(suhu)

rendah = lembap_rendah(kelembapan)
tinggi = lembap_tinggi(kelembapan)

<<<<<<< Updated upstream
# INFERENSI (MIN)
=======

# ------------------------------------------------------------
# INFERENSI FUZZY
# ------------------------------------------------------------
# Metode MIN digunakan untuk menentukan nilai firing strength
# (α-predicate) dari setiap aturan.
#
# Aturan 1:
# IF suhu Dingin AND kelembapan Tinggi
# THEN kipas Lambat
#
# Nilai z1 = 30 merupakan output crisp untuk kipas lambat.
>>>>>>> Stashed changes
a1 = min(dingin, tinggi)
z1 = 30  # kipas lambat

a2 = min(panas, tinggi)
z2 = 80  # kipas cepat

a3 = min(panas, rendah)
z3 = 60  # kipas sedang

# DEFUZZIFIKASI (TSUKAMOTO)
z = (a1*z1 + a2*z2 + a3*z3) / (a1 + a2 + a3)

print("Nilai Kipas:", z)