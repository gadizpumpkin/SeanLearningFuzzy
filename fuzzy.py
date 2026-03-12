# Input
suhu = 30
kelembapan = 70

# FUZZIFIKASI SUHU
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

# FUZZIFIKASI KELEMBAPAN
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

# HITUNG NILAI FUZZY
dingin = suhu_dingin(suhu)
panas = suhu_panas(suhu)

rendah = lembap_rendah(kelembapan)
tinggi = lembap_tinggi(kelembapan)

# INFERENSI (MIN)
a1 = min(dingin, tinggi)
z1 = 30  # kipas lambat

a2 = min(panas, tinggi)
z2 = 80  # kipas cepat

a3 = min(panas, rendah)
z3 = 60  # kipas sedang

# DEFUZZIFIKASI (TSUKAMOTO)
z = (a1*z1 + a2*z2 + a3*z3) / (a1 + a2 + a3)

print("Nilai Kipas:", z)