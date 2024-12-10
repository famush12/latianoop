from data.mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import TampilkanMahasiswa

def main():
    data_mahasiswa = DataMahasiswa()

    while True:
        print("\n=== Menu ===")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Cari Data")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            nama, nilai = InputForm.input_data()
            mahasiswa = Mahasiswa(nama, nilai)
            data_mahasiswa.tambah(mahasiswa)
        elif pilihan == '2':
            TampilkanMahasiswa.tampilkan_list(data_mahasiswa)
        elif pilihan == '3':
            nama = InputForm.input_nama()
            data_mahasiswa.hapus(nama)
        elif pilihan == '4':
            nama = InputForm.input_nama()
            nilai_baru = InputForm.input_nilai()
            data_mahasiswa.ubah(nama, nilai_baru)
        elif pilihan == '5':
            nama = InputForm.input_nama()
            mahasiswa = data_mahasiswa.cari(nama)
            TampilkanMahasiswa.tampilkan_detail(mahasiswa)
        elif pilihan == '6':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
