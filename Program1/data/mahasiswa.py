class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai


class DataMahasiswa:
    def __init__(self):
        self.data = []

    def tambah(self, mahasiswa):
        self.data.append(mahasiswa)
        print(f"Data {mahasiswa.nama} berhasil ditambahkan.")

    def hapus(self, nama):
        for mhs in self.data:
            if mhs.nama.lower() == nama.lower():
                self.data.remove(mhs)
                print(f"Data {nama} berhasil dihapus.")
                return
        print(f"Data {nama} tidak ditemukan.")

    def ubah(self, nama, nilai_baru):
        for mhs in self.data:
            if mhs.nama.lower() == nama.lower():
                mhs.nilai = nilai_baru
                print(f"Data {nama} berhasil diubah.")
                return
        print(f"Data {nama} tidak ditemukan.")

    def cari(self, nama):
        for mhs in self.data:
            if mhs.nama.lower() == nama.lower():
                return mhs
        print(f"Data {nama} tidak ditemukan.")
        return None
