import random

class AmtikaAssistant:
    def __init__(self):
        self.opsi_map = {
            "penjumlahan": "tambah", "soal penjumlahan": "tambah", "tambah": "tambah", "pertambahan": "tambah",
            "pengurangan": "kurang", "soal pengurangan": "kurang", "kurang": "kurang",
            "perkalian": "kali", "soal perkalian": "kali", "kali": "kali",
            "pembagian": "bagi", "soal pembagian": "bagi", "bagi": "bagi"
        }

        # penyimpanan riwayat
        self.history = []

        print("=== Hai, Aku Adalah AMTIKA. Yang bakal bantu kamu belajar matematika ===")
        print("(Ketik 'riwayat' untuk melihat hasil perhitungan sebelumnya atau ketik jenis soal)")

    def operasi(self, opsi):
        # Generate angka random
        angka1 = random.randint(1, 20)
        angka2 = random.randint(1, 20)

        # Pastikan pembagian hasilnya bulat
        if opsi == "bagi":
            angka1 = angka2 * random.randint(1, 10)

        # Tentukan simbol & hasil
        simbol_map = {"tambah": "+", "kurang": "-", "kali": "×", "bagi": "÷"}
        simbol = simbol_map.get(opsi, "?")

        if opsi == "tambah":
            hasil_benar = angka1 + angka2
        elif opsi == "kurang":
            hasil_benar = angka1 - angka2
        elif opsi == "kali":
            hasil_benar = angka1 * angka2
        elif opsi == "bagi":
            hasil_benar = angka1 / angka2

        print("\nAmtika : Jawab soal berikut!")
        print(f"Soal: {angka1} {simbol} {angka2} = ?")

        # User input jawaban
        try:
            jawaban = float(input("Jawaban Anda: "))
        except ValueError:
            print("Jawaban harus berupa angka!")
            return None

        # Penilaian
        if jawaban == hasil_benar:
            print("Benar! Kamu hebat!")
            status = "Benar"
        else:
            print(f"Salah! Jawaban yang benar adalah: {hasil_benar}")
            status = "Salah"

        # Simpan ke riwayat
        riwayat = f"{angka1} {simbol} {angka2} = {jawaban}  ({status}, benar: {hasil_benar})"
        self.history.append(riwayat)

    def tampilkan_riwayat(self):
        if not self.history:
            print("Amtika : Belum ada riwayat perhitungan.")
        else:
            print("\n=== Riwayat Perhitungan ===")
            for index, item in enumerate(self.history, start=1):
                print(f"{index}. {item}")
            print("================================\n")

    def handle_unknown(self):
        print("Amtika :  Maaf, aku tidak mengerti. Bisa ulangi?")

    def tanya_lagi(self):
        lanjut = input("\nAmtika : Mau lanjut soal lagi? (iya/tidak): ").lower().strip()
        if lanjut in ["iya", "ya", "lanjut", "boleh"]:
            print("Amtika : Soal apa berikutnya?")
            return True
        else:
            print("Amtika : Terima kasih sudah belajar bersama AMTIKA. Sampai jumpa!")
            return False

    def run(self):
        while True:
            user = input("\nAnda: ").lower().strip()

            if user in ["keluar", "stop", "tidak", "exit"]:
                print("Amtika : Baik, sampai jumpa! ")
                break

            elif user == "riwayat":
                self.tampilkan_riwayat()

            elif user in self.opsi_map:
                self.operasi(self.opsi_map[user])
                if not self.tanya_lagi():
                    break

            else:
                self.handle_unknown()


# ============ Jalankan Program ============
amtika = AmtikaAssistant()
amtika.run()
