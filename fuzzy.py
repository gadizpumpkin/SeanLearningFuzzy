# ============================================================
# IMPLEMENTASI FUZZY LOGIC TSUKAMOTO
# Menentukan kecepatan kipas berdasarkan suhu dan kelembapan
# ============================================================


# ------------------------------------------------------------
# 1. INPUT
# ------------------------------------------------------------
# Nilai suhu dalam satuan Celsius (°C)
suhu = 30

# Nilai kelembapan dalam satuan persen (%)
kelembapan = 70


# ------------------------------------------------------------
# 2. FUZZIFIKASI SUHU
# ------------------------------------------------------------
# Mengubah nilai suhu crisp menjadi derajat keanggotaan
# pada himpunan fuzzy "Dingin".
#
# Aturan keanggotaan:
# - Suhu <= 20°C       -> sepenuhnya Dingin (1)
# - 20°C < suhu < 30°C -> derajat keanggotaan menurun linear
# - Suhu >= 30°C       -> bukan Dingin (0)
def suhu_dingin(x):
    if x <= 20:
        return 1
    elif 20 < x < 30:
        return (30 - x) / 10
    else:
        return 0


# Mengubah nilai suhu crisp menjadi derajat keanggotaan
# pada himpunan fuzzy "Panas".
#
# Aturan keanggotaan:
# - Suhu <= 25°C       -> bukan Panas (0)
# - 25°C < suhu < 35°C -> derajat keanggotaan meningkat linear
# - Suhu >= 35°C       -> sepenuhnya Panas (1)
def suhu_panas(x):
    if x <= 25:
        return 0
    elif 25 < x < 35:
        return (x - 25) / 10
    else:
        return 1


# ------------------------------------------------------------
# 3. FUZZIFIKASI KELEMBAPAN
# ------------------------------------------------------------
# Mengubah nilai kelembapan crisp menjadi derajat keanggotaan
# pada himpunan fuzzy "Rendah".
#
# Aturan keanggotaan:
# - Kelembapan <= 40%       -> sepenuhnya Rendah (1)
# - 40% < kelembapan < 60%  -> derajat keanggotaan menurun linear
# - Kelembapan >= 60%       -> bukan Rendah (0)
def lembap_rendah(x):
    if x <= 40:
        return 1
    elif 40 < x < 60:
        return (60 - x) / 20
    else:
        return 0


# Mengubah nilai kelembapan crisp menjadi derajat keanggotaan
# pada himpunan fuzzy "Tinggi".
#
# Aturan keanggotaan:
# - Kelembapan <= 50%       -> bukan Tinggi (0)
# - 50% < kelembapan < 80%  -> derajat keanggotaan meningkat linear
# - Kelembapan >= 80%       -> sepenuhnya Tinggi (1)
def lembap_tinggi(x):
    if x <= 50:
        return 0
    elif 50 < x < 80:
        return (x - 50) / 30
    else:
        return 1


# ------------------------------------------------------------
# 4. HITUNG NILAI FUZZY
# ------------------------------------------------------------
# Menghitung derajat keanggotaan suhu terhadap:
# - Dingin
# - Panas
dingin = suhu_dingin(suhu)
panas = suhu_panas(suhu)

# Menghitung derajat keanggotaan kelembapan terhadap:
# - Rendah
# - Tinggi
rendah = lembap_rendah(kelembapan)
tinggi = lembap_tinggi(kelembapan)


# ------------------------------------------------------------
# 5. INFERENSI FUZZY
# ------------------------------------------------------------
# Metode MIN digunakan untuk menentukan nilai firing strength
# (α-predicate) dari setiap aturan.
#
# Aturan 1:
# IF suhu Dingin AND kelembapan Tinggi
# THEN kipas Lambat
#
# Nilai z1 = 30 merupakan output crisp untuk kipas lambat.
a1 = min(dingin, tinggi)
z1 = 30


# Aturan 2:
# IF suhu Panas AND kelembapan Tinggi
# THEN kipas Cepat
#
# Nilai z2 = 80 merupakan output crisp untuk kipas cepat.
a2 = min(panas, tinggi)
z2 = 80


# Aturan 3:
# IF suhu Panas AND kelembapan Rendah
# THEN kipas Sedang
#
# Nilai z3 = 60 merupakan output crisp untuk kipas sedang.
a3 = min(panas, rendah)
z3 = 60


# ------------------------------------------------------------
# 6. DEFUZZIFIKASI TSUKAMOTO
# ------------------------------------------------------------
# Metode Tsukamoto menghasilkan satu nilai crisp (z)
# berdasarkan rata-rata terbobot dari setiap aturan.
#
# Rumus:
#
#          α1*z1 + α2*z2 + α3*z3
# z = -------------------------------
#              α1 + α2 + α3
#
# α = nilai firing strength setiap aturan
# z = nilai output crisp setiap aturan
z = (a1*z1 + a2*z2 + a3*z3) / (a1 + a2 + a3)


# ------------------------------------------------------------
# 7. OUTPUT
# ------------------------------------------------------------
# Menampilkan hasil akhir berupa kecepatan kipas.
print("Nilai Kipas:", z)