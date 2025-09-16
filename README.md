# Tugas 3

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Biar data dari backend bisa dipake di manapun, tidah hanya di web saja. Jadi frontend (web, mobile) atau bahkan service lain bisa konsumsi data yang sama dengan format yang jelas. Pada intinya, membuat aplikasi mudah diintegrasiin dan lebih fleksibel.
 
## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Untuk kebutuhan aplikasi modern, JSON cenderung lebih unggul dibandingkan XML karena strukturnya lebih ringkas, mudah dibaca, dan sangat mudah diproses di berbagai bahasa pemrograman, terutama JavaScript. Sementara itu, XML masih relevan untuk sistem lama atau dokumen kompleks yang membutuhkan schema atau namespace. Namun secara umum, JSON lebih populer karena lebih efisien dan lebih praktis dipakai untuk web ataupun mobile.

## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
is_valid() berfungsi untuk memvalidasi data yang dikirimkan melalui form. Jika data valid, Django akan menyediakan cleaned_data yang siap digunakan atau disimpan ke database. Jika tidak valid, error akan ditampilkan. Method ini penting untuk memastikan data yang masuk sesuai aturan dan mencegah data yang salah langsung tersimpan di database.

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token digunakan untuk mencegah serangan Cross-Site Request Forgery (CSRF). Tanpa token ini, penyerang dapat memanipulasi pengguna yang sedang login agar secara tidak sadar mengirimkan request berbahaya ke server, misalnya menambah, mengubah, atau menghapus data. Dengan adanya csrf_token, server dapat memverifikasi bahwa request POST benar-benar berasal dari form aplikasi sendiri, bukan dari pihak luar.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Menambahkan 4 fungsi tersebut pada views.py
2. Menambahkan 4 fungsi tersebut pada path di urls.py aplikasi
3. Membuat fungsi pada views.py untuk penambahan produk dan penampilan detail produk.
4. Menambahkan fungsi tersebut pada urls.py aplikasi
5. Membuat template berupa html baru untuk penambahan produk dan penampilan detail produk.

## Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Sudah baik.

## Hasil akses URL Postman
### XML
![Postman xml](/postman_screenshot/xml.png)

### JSON
![Postman json](/postman_screenshot/json.png)

### XML BY ID
![Postman xml by id](/postman_screenshot/xml_by_id.png)

### JSON BY ID
![Postman json by id](/postman_screenshot/json_by_id.png)

