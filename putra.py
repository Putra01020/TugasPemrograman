def buat_daftar_buku():
    daftar_buku = [

        {"judul": "The Catcher in the Rye", "harga": 35000},
        {"judul": "1984", "harga": 30000},
        {"judul": "To Kill a Mockingbird", "harga": 40000},
        {"judul": "Harry Potter and the Philosopher's Stone", "harga": 45000},
        {"judul": "The Lord of the Rings", "harga": 60000},
    ]

    return daftar_buku


def tampilkan_daftar_buku(daftar_buku):
    print("Daftar Buku:")
    for buku in daftar_buku:
        print(f"{buku['judul']} - Rp.{buku['harga']}")


def beli_buku(daftar_buku, uang):
    buku_terbeli = None
    total_harga = 0
    while total_harga <= uang:
        buku_terbeli = input("Masukkan judul buku yang ingin Anda beli: ")
        for buku in daftar_buku:
            if buku["judul"].lower() == buku_terbeli.lower():
                total_harga += buku["harga"]
                break
        else:
            print("Buku tidak ditemukan.")
            buku_terbeli = None
            continue
        print(f"Anda telah berhasil membeli {buku_terbeli} dengan harga Rp.{total_harga}")
        break
    return total_harga

def main():
    daftar_buku = buat_daftar_buku()
    tampilkan_daftar_buku(daftar_buku)
    uang = int(input("Masukkan jumlah uang Anda: "))
    total_harga = beli_buku(daftar_buku, uang)
    if total_harga is None:
        print("Belum ada buku yang dibeli.")

    else:
        kembalian = uang - total_harga
        print(f"Kembalian Anda adalah Rp.{kembalian}")


if _name_ == "_main_":
    main()
