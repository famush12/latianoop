class InputForm:
    @staticmethod
    def input_data():
        nama = input("Masukkan nama: ")
        nilai = float(input("Masukkan nilai: "))
        return nama, nilai

    @staticmethod
    def input_nama():
        return input("Masukkan nama: ")

    @staticmethod
    def input_nilai():
        return float(input("Masukkan nilai baru: "))
