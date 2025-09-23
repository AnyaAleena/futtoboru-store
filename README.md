# Tugas 4

## Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
AutheticationForm adalah form bawaan Django yang berfungsi untuk login user. Mencakup menyediakan field username & password, validasi username & password. Kalau valid, info user akan disimpan.
Kelebihan: memudahkan karena siap dipakai, aman, dan tetap bisa dikustomisasi
Kekurangan: fiturnya basic, misalnya pengecekan kekuatan password.

##  Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentikasi: cek user mana yang log in.
Otoriasi: cek peran dari user tersebut.
Di Django, autentikasi diurus lewat sistem login (pakai session + request.user), sementara otorisasi diurus lewat permission dan group. Jadi, Django melakukan autentikasi terlebih dahulu sebelum otorisasi.

##  Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Session:
+ Tidak perlu login ulang setiap ganti halaman karena server menyimpan info user.
+ Data asli ada di server sehingga lebih aman daripada data ada di cookies.
- Butuh storage di server
- Session ID dapat dicuri orang dan akun user dapat dipakai.

Cookies:
+ Data disimpan di browser, server hanya membaca.
+ Ringan untuk server.
- Ukuran terbatas (4KB)
- Mudah diintip sehingga bahaya untuk menyimpan data sensitif.

##  Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Ada risiko potensial. Seperti cookie dicuri lewat serangan XSS, atau direbut jaringan kalau tidak memakai HTTPS, cookie juga bisa dimanfaatkan untuk serangan CSRF.
Cara DJango menangani hal terseeut:
- HttpOnly -> opsi supaya cookies tidak bisa diakses javascript (mencegah XSS)
- Secure -> opsi supaya cookies hanya dikirim lewat HTTPS.
- SameSite -> mencegah cookies dikirim lalu lintas sembarangan.

##  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Register, login, logout
    - Membuat fungsi register, login, logout pada views.py dan routing ke urls.py
    - Membuat RegisterView pakai UserCreationForm
    - Pakai LoginView/LogoutView bawaan Django (hanya menyiapkan template)

Bikin 2 akun + 3 dummy data per akun
    - Buat dua user
    - Pada setiap user, buat 3 product baru

Menghubungkan Product ke User
    - Di models.py tepatnya di model Product, tambah kepemilikan setiap barang
    - Migrate

Menampilkan user login info + last_login
    - Saat login sukses, set cookie last login
    - Tambahkan keterangan username dan last login pada main view



