# Tugas 5

## Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
1. Inline Style (mis. <div style="...">)
2. ID Selector (mis. #id)
3. Class Selector (.class, [type=text], :hover, :focus)
4. Element Selector (div, h1, ::before)
5. Universal Selector (*)

##  Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Responsive design memastikan tampilan nyaman dipakai di berbagai ukuran layar (mobile → desktop), meningkatkan aksesibilitas, usability, dan SEO (Core Web Vitals & mobile-first indexing).

Contoh sudah responsif: Google (pencarian & hasil menyesuaikan lebar layar).
Contoh kurang responsif: beberapa situs lama/versi klasik seperti Craigslist—tata letak grid kaku sehingga di ponsel perlu zoom/scroll horizontal.

##  Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
- Margin: ruang di luar border (jarak antarelemen).
- Border: garis pembatas di sekeliling elemen.
- Padding: ruang di dalam border (jarak konten ke border).

##  Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox -> satu dimensi (baris atau kolom). Cocok untuk navbar, toolbar, daftar tombol.
Grid -> dua dimensi (baris dan kolom). Cocok untuk galeri, catalog card.

##  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Kustomisasi halaman login, register, tambah product, edit product, dan detail product semenarik mungkin.
-> Set color palette, tambahkan sebagai variable di css base.html

-  Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. 
-> Menghubungkan main.html dengan card_product.html agar setiap product lebih rapih

