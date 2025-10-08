# Tugas 6

##  Apa perbedaan antara synchronous request dan asynchronous request?
- **Synchronous request**: Proses akan berhenti menunggu respon dari server sebelum melanjutkan eksekusi kode lainnya.
- **Asynchronous request**: Proses tidak akan menunggu respon dari server, sehingga kode lainnya bisa terus berjalan sembari menunggu respon dari server.

## Bagaimana AJAX bekerja di Django (alur request–response)?
Django menerima request AJAX melalui URL endpoint tertentu. Request tersebut akan diproses di backend (misalnya, dengan views yang menangani AJAX), kemudian Django mengirimkan respon ke frontend dalam bentuk JSON atau HTML yang kemudian digunakan untuk memperbarui tampilan tanpa reload halaman.

## Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
- Mengurangi beban server dan waktu muat karena hanya bagian yang berubah yang diperbarui.
- Pengalaman pengguna menjadi lebih interaktif dan cepat, tanpa perlu reload halaman penuh. 

## Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
- Gunakan CSRF token untuk melindungi dari serangan Cross-Site Request Forgery (CSRF).
- Pastikan data sensitif dienkripsi melalui HTTPS.
- Gunakan validasi sisi server untuk setiap data yang dikirimkan melalui AJAX.

## Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
AJAX meningkatkan interaktivitas dan kecepatan website karena tidak perlu reload halaman penuh, membuat pengguna merasa website lebih responsif.