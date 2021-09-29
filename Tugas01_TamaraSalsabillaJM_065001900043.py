# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 11:05:31 2021

@author: TamaraSalsabilla
"""

bulan = "JanFebMarAprMeiJunJulAgtSepOktNovDes"
#29/09/2021
#kiri -> (angkaBulan * 3) - 3
#kanan -> angkaBulan * 3

# x = tamarasalsabillajm
tgl = input("tanggal : ") #20/10/2001

tanggalSetelahDiSplit = tgl.split("/")
#

angkaBulan = int(tanggalSetelahDiSplit[1]) #[30:33] ?
bulanJadi = bulan[(angkaBulan * 3) - 3 : angkaBulan * 3] #Nov
print(tanggalSetelahDiSplit[0] + "-" + bulanJadi + "-" + tanggalSetelahDiSplit[2])
#output di atas : 20-Okt-2001