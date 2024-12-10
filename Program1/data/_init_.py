class Mahasiswa:
    def __init__(self):  # Perbaikan nama metode
        self.data = []

    def tambah(self, nama, nilai):
        self.data.append({'nama': nama, 'nilai': nilai})
        print(f"Data {nama} berhasil ditambahkan.")

    def tampilkan(self):
        print("\nDaftar Nilai Mahasiswa:")
        if not self.data:
            print("Tidak ada data.")
        else:
            for idx, mhs in enumerate(self.data, start=1):
                print(f"{idx}. Nama: {mhs['nama']}, Nilai: {mhs['nilai']}")

    def hapus(self, nama):
        for mhs in self.data:
            if mhs['nama'].lower() == nama.lower():
                self.data.remove(mhs)
                print(f"Data {nama} berhasil dihapus.")
                return
        print(f"Data {nama} tidak ditemukan.")

    def ubah(self, nama, nilai_baru):
        for mhs in self.data:
            if mhs['nama'].lower() == nama.lower():
                mhs['nilai'] = nilai_baru
                print(f"Data {nama} berhasil diubah.")
                return
        print(f"Data {nama} tidak ditemukan.")


if __name__ == "__main__":  # Perbaikan kondisi
    daftar_mahasiswa = Mahasiswa()

    while True:
        print("\n=== Menu ===")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            nama = input("Masukkan nama: ")
            nilai = float(input("Masukkan nilai: "))
            daftar_mahasiswa.tambah(nama, nilai)
        elif pilihan == '2':
            daftar_mahasiswa.tampilkan()
        elif pilihan == '3':
            nama = input("Masukkan nama yang ingin dihapus: ")
            daftar_mahasiswa.hapus(nama)
        elif pilihan == '4':
            nama = input("Masukkan nama yang ingin diubah: ")
            nilai_baru = float(input("Masukkan nilai baru: "))
            daftar_mahasiswa.ubah(nama, nilai_baru)
        elif pilihan == '5':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")
