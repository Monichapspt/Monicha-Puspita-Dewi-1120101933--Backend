l_pesan = ['Risoles', 'Donat', 'Bakpau']
l_risoles = ['kentang telur', 'kentang ayam', 'kentang']
l_donat = ['coklat meses', 'coklat keju', 'coklat meses keju']
l_bakpau = ['kacang', 'blueberry', 'stroberi']

bayar = []
while True :
    print("=" * 35)
    for pilih in range(0, len(l_pesan)) :
        print(f'{pilih + 1}. {l_pesan[pilih]}')
    Pesan = input('Silahkan Pilih Pesanan : ')
    if Pesan == '1' :
        for pilih_pesan in range(0, len(l_risoles)) :
            print(f'{pilih_pesan + 1}. {l_risoles[pilih_pesan]}')
        ulangi = True
        while ulangi :
            Pesanan = int(input(f'Silahkan Pilih Isi Pesanan Yang Anda Inginkan 1-{len(l_risoles)} : '))
            if Pesanan <= 0 or Pesanan > len(l_risoles) :
                print('Silahkan Masukkan Pilihan yang Benar')
                for pilih_pesan in range(0, len(l_risoles)) :
                    print(f'{pilih_pesan + 1}. {l_risoles[pilih_pesan]}')
                continue
            else:
                bayar.append(l_risoles[Pesanan - 1])
                print('=== Isi Yang Diinginkan ===')
                for l_bayar in range(0, len(bayar)):
                    print(f'{l_bayar + 1}. {bayar[l_bayar]}')
                ulangi = False
            continue
    elif Pesan == '2' :
        for pilih_pesan2 in range(0, len(l_donat)) :
            print(f'{pilih_pesan2 + 1}. {l_donat[pilih_pesan2]}')
        ulangi = True
        while ulangi :
            Pesanan = int(input(f'Silahkan Pilih Isi Pesanan Yang Anda Inginkan 1-{len(l_donat)} : '))
            if Pesanan <= 0 or Pesanan > len(l_donat) :
                print('Silahkan Masukkan Pilihan yang Benar')
                for pilih_pesan2 in range(0, len(l_donat)) :
                    print(f'{pilih_pesan2 + 1}. {l_donat[pilih_pesan2]}')
            else:
                bayar.append(l_donat[Pesanan - 1])
                print('=== Isi Yang Diinginkan ===')
                for l_bayar in range(0, len(bayar)):
                    print(f'{l_bayar + 1}. {bayar[l_bayar]}')
                ulangi = False
            continue
    elif Pesan == '3' :
        for pilih_pesan3 in range(0, len(l_bakpau)) :
            print(f'{pilih_pesan3 + 1}. {l_bakpau[pilih_pesan3]}')
        ulangi = True
        while ulangi :
            Pesanan = int(input(f'Silahkan Pilih Isi Pesanan Yang Anda Inginkan 1-{len(l_bakpau)} : '))
            if Pesanan <= 0 or Pesanan > len(l_bakpau) :
                print('Silahkan Masukkan Pilihan yang Benar')
                for pilih_pesan3 in range(0, len(l_bakpau)) :
                    print(f'{pilih_pesan3 + 1}. {l_bakpau[pilih_pesan3]}')
                continue
            else:
                bayar.append(l_bakpau[Pesanan - 1])
                print('=== Isi Yang Diinginkan ===')
                for l_bayar in range(0, len(bayar)):
                    print(f'{l_bayar + 1}. {bayar[l_bayar]}')
                ulangi = False
            continue
    else :
        print('Pesanan yang anda inginkan tidak ditemukan. Harap isi kembali')
        continue

    pilih = input('Apakah Anda Ingin Memesan Lagi [Y?N] ? ')
    if pilih == 'Y' :
        continue
    else:
        Pembeli = input('Masukkan Nama Pembeli : ')
        print(f'Pesanan atas nama {Pembeli}')
        print('==== list pesanan yang dipesan ====')
        for list_nota in range(0, len(bayar)):
            print(f'{l_bayar +1} . {bayar[l_bayar]}')
        print("=" * 18)
        print(" ")
        print('Terima Kasih.... Pesanan anda sedang di proses')
        break