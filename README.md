# **Battle of the Robots: The Rise of Uroboros**

## **Cerita**
Di masa depan, dunia dilanda kehancuran ketika sebuah robot raksasa bernama **Uroboros** bangkit dari bawah tanah, mengancam untuk menghancurkan segala sesuatu yang tersisa. Uroboros, yang memiliki kekuatan regeneratif luar biasa, tidak bisa dihentikan oleh senjata biasa. Namun, ada harapan terakhir: **Thunder**, **Blaze**, dan **Frost**, tiga robot tempur legendaris dengan kekuatan unik. 

Misi Anda sebagai pemain adalah memilih salah satu dari ketiga robot ini dan menghadapi Uroboros dalam pertempuran hidup dan mati. Seranglah Uroboros secepat mungkin, tetapi hati-hati! Uroboros menyerang secara otomatis setiap detik. Jika Anda lambat atau terlalu sering menekan tombol tanpa strategi, robot Anda akan hancur.

Apakah Anda dapat menghancurkan Uroboros sebelum robot Anda kehabisan tenaga? Itu semua bergantung pada kecepatan dan ketepatan Anda!

---

## **Cara Bermain**
1. Pilih satu dari tiga robot yang tersedia: **Thunder**, **Blaze**, atau **Frost**.
2. Setiap robot memiliki **kesehatan (health)** dan **serangan (damage)** yang berbeda.
3. Uroboros akan menyerang secara otomatis setiap 1 detik.
4. Tekan tombol **Enter** secepat mungkin untuk menyerang Uroboros sebelum robot Anda dikalahkan.
5. Jika Uroboros kehabisan kesehatan, Anda menang. Jika robot Anda kehabisan kesehatan, Anda kalah.

---

## **Penjelasan Kode**

### Struktur Program

- **Class `Character`:**
   Kelas ini merepresentasikan robot atau musuh dalam permainan. Setiap objek `Character` memiliki atribut:
   - `name`: Nama karakter.
   - `health`: Jumlah health karakter.
   - `health_max`: Batas maksimal health karakter.
   - `damage`: Jumlah damage yang bisa diberikan karakter saat menyerang.
   
   Fungsi `attack()` digunakan untuk menyerang target, yang mengurangi `health` target berdasarkan damage.

- **Fungsi `pilih_robot()`:**
   Pemain dapat memilih salah satu dari tiga robot:
   - **Thunder**: Kesehatan tinggi (120), damage sedang (7).
   - **Blaze**: Kesehatan sedang (100), damage tinggi (10).
   - **Frost**: Kesehatan rendah (80), damage sangat tinggi (12).
   
   Fungsi ini mengembalikan objek `Character` sesuai pilihan pemain.

- **Fungsi `serang_terus()`:**
   Fungsi ini dijalankan dalam thread terpisah untuk membuat musuh (Uroboros) menyerang secara otomatis setiap 1 detik. Setiap kali Uroboros menyerang, kesehatan robot pemain berkurang sesuai damage musuh.

- **Fungsi `game()`:**
   Fungsi utama yang mengatur alur permainan:
   - Pemain memilih robot.
   - Uroboros mulai menyerang pemain secara otomatis di thread terpisah.
   - Pemain harus menyerang balik dengan menekan **Enter** secepat mungkin hingga Uroboros kehabisan kesehatan.
   
   Permainan berakhir jika kesehatan robot pemain atau Uroboros mencapai 0.

### Mekanisme Perang
- Pemain dan musuh bergiliran menyerang, namun Uroboros menyerang otomatis setiap 1 detik.
- Pemain hanya bisa menyerang Uroboros dengan menekan **Enter** setelah setiap serangan sebelumnya, sehingga waktu reaksi sangat penting.
- 
---
### **Nikmati pertempurannya dan hancurkan Uroboros!**
---
**Refrensi** : Learn. (2023, July 2). Learn Python Classes With a Text-Based Battle - OOP Tutorial. YouTube. https://youtu.be/cM_ocyOrs_k?si=25rop2OfMNDv68wJ



