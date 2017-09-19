# INDEX #
[1. Judul Program](https://github.com/armyids/WSPMaster#step-(sediment-transport))

[2. Fitur Program](https://github.com/armyids/WSPMaster#fitur)

[3. Software Pendukung](https://github.com/armyids/WSPMaster#software-pendukung-yang-harus-diinstall)

[4. Instalasi Utama Windows](https://github.com/armyids/WSPMaster#instalasi-utama-windows)

[5. Instalasi Utama Linux](https://github.com/armyids/WSPMaster#instalasi-utama-linux-debian)

[6. Video Panduan](https://github.com/armyids/WSPMaster#video-panduan)

[7. Instalasi Tambahan](https://github.com/armyids/WSPMaster#instalasi-tambahan)

[8. Cara Menjalankan WSP](https://github.com/armyids/WSPMaster#cara-menjalankan)

[9. Update Program](https://github.com/armyids/WSPMaster#update)

[10. Credits](https://github.com/armyids/WSPMaster#credits)

[11. Contributor Script](https://github.com/armyids/WSPMaster#contributors-script)

[12. Kontak Dan Saran](https://github.com/armyids/WSPMaster#kontak-dan-saran)

[13. Disclaimer](https://github.com/armyids/WSPMaster#disclaimer)

# asas #

# STEP (Sediment Transport & Erosion Prediction) #
STEP merupakan auto bash / python shell script yang dibuat dengan tujuan untuk menghitung besarnya erosi akibat percikan air (interrill water splash erosion), erosi pada permukaan tanah (rill sheet erosion), laju pengendapan (deposition rate), serta transport sediment pada suatu area daerah aliran sungai (Watershed).

# Fitur #
- [x] Menghitung Erosi Tanah Akibat Percikan Air (Water Splash Erosion)
- [x] Menghitung Erosi Akibat Runoff Pada Permukaan Tanah (Rill and Sheet Erosion)
- [x] Menghitung Laju Pengendapan (Deposition Rate) 
- [x] Menghitung Transport Sediment

# Software Pendukung yang Harus Diinstall #
- Git (Khusus Windows)
	https://git-for-windows.github.io/
- Python 2.7.x (Windows dan Linux)
	https://www.python.org/downloads/windows/

# Instalasi Utama Windows #
Dengan cara klik kanan di folder yang diinginkan dan klik Git Bash Here, kemudian jalankan command berikut: 
- git clone -b master https://github.com/armyids/WSPMaster

Atau bisa juga dapat download file zip langsung : https://github.com/armyids/WSPMaster.git

# Instalasi Utama Linux Debian #

Masuk ke root kemudian jalankan command berikut:
- wget -q --no-check-certificate https://raw.githubusercontent.com/armyids/WSPMaster/linux_debian.sh -O - | bash -

Kemudian clone WSPMaster di folder yang diinginkan
- git clone -b master https://github.com/armyids/WPSMaster && cd WSPMaster && chmod 755 *.sh

# Video Panduan #
- Install Git Bash

[![Install Git Bash](LINK IMG)](LINK VID)

- Install Python 2.7.x

[![Install Python 2.7.x](LINK IMG)](LINK VID)

- Install Clone WPSMaster

[![Git Clone WPSMaster](LINK IMG)](LINK VID)

# Instalasi Tambahan #
- Windows : Jalankan file `install_windows.sh`
- Linux   : Jalankan shell bash `install_debian.sh`

# Cara Menjalankan #
Klik 2 kali file 'WSP.sh', atau juga bisa masukkan command `./WSP.sh` pada git bash atau terminal jika menggunakan linux.

# Update #
Untuk update, buka git bash here di folder WSPMaster, kemudian masukkan command berikut pada git bash :
- `git stash`
- `git pull`
- `git submodule update --init --recursive`

# Credits #

# Contributors Script #

# Kontak Dan Saran #
Kontak, saran, pendapat dan lain-lain bisa menghubungi kami di http://sipil.ft.unsoed.ac.id/
 
# Disclaimer #
Saya selaku penanggungjawab script menyatakan 'Tidak ada backdoor, file, command, virus atau program jahat yang membahayakan di dalam script.'
