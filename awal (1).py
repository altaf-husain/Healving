import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from PyQt5 import QtGui
        
class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("E:/Kuliah/PemTek/GUI/tugas akhir/tampilan awal.ui", self)
        self.Next.clicked.connect(self.tombolnext)
        self.Start.clicked.connect(self.konversi)
        self.Nama.textChanged.connect(self.kosong)

    def konversi(self):
        C = self.Nama.text()
        D = 'Selamat Datang '
        e = D+C
        
        self.Hai.setText(e)
        
    def kosong(self):
        self.Hai.setText('')
    
    def tombolnext(self):
        halaman2 = Screen2()
        widget.addWidget(halaman2)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class Screen2(QDialog):
    def __init__(self):
        super(Screen2, self).__init__()
        loadUi("E:/Kuliah/PemTek/GUI/tugas akhir/LAYER 2.ui", self)
        self.Kebkal.clicked.connect(self.kebutuhan)
        self.Perk.clicked.connect(self.perhitungan)
        
    def kebutuhan(self):
        halaman4 = Screen4()
        widget.addWidget(halaman4)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def perhitungan(self):
        halaman3 = Screen3()
        widget.addWidget(halaman3)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
class Screen3(QDialog):
    def __init__(self):
        super(Screen3, self).__init__()
        loadUi("Layer 3.ui", self)
        self.Hitung.clicked.connect(self.user_info)
        self.Back.clicked.connect(self.kembali)
        self.Umur.textChanged.connect(self.kosong1)
        self.Bb.textChanged.connect(self.kosong1)
        self.Tinggi.textChanged.connect(self.kosong1)
        self.Aktivitas.addItems(["sangat jarang", "jarang", "normal", "sering", "sangat sering"])
        self.Aktivitas.currentIndexChanged.connect(self.kosong1)
        self.Gender.addItems(["Laki-laki", "Perempuan"])
        self.Gender.currentIndexChanged.connect(self.kosong1)

    def user_info(self):
        age = self.Umur.text()
        gender = self.Gender.currentText()
        weight = self.Bb.text()
        height = self.Tinggi.text()
        aktivitas = self.Aktivitas.currentText()

        if gender == 'Laki-laki':
            c1 = 66
            hm = (5) * int(height)
            wm = (13.7) * int(weight)
            am = (6.76) * int(age)

            bmr_result = c1 + hm + wm - am
            if aktivitas == 'sangat jarang' :
                kebutuhan_kalori = int(1.2 * bmr_result)
                self.Hasil.setText(str(kebutuhan_kalori))
                kalori.kaloriTeoritis(kebutuhan_kalori)
                
            elif aktivitas == 'jarang' :
                kebutuhan_kalori = int(1.375 * bmr_result)
                self.Hasil.setText(str(kebutuhan_kalori))
                kalori.kaloriTeoritis(kebutuhan_kalori)
                
            elif aktivitas == 'normal' :
                kebutuhan_kalori = int(1.55 * bmr_result)
                self.Hasil.setText(str(kebutuhan_kalori))
                kalori.kaloriTeoritis(kebutuhan_kalori)
                
            elif aktivitas == 'sering' :
                kebutuhan_kalori = int(1.725 * bmr_result)
                self.Hasil.setText(str(kebutuhan_kalori))
                kalori.kaloriTeoritis(kebutuhan_kalori)
                
            elif aktivitas == 'sangat sering' :
                kebutuhan_kalori = int(1.9 * bmr_result)
                self.Hasil.setText(str(kebutuhan_kalori))
                kalori.kaloriTeoritis(kebutuhan_kalori)
                

        elif gender == 'Perempuan':
            c1 = 655.1
            hm = (1.8) * int(height)
            wm = (9.6) * int(weight)
            am = (4.7) * int(age)

            # BMR = 665 + (9.6 X 69) + (1.8 x 178) – (4.7 x 27)
            bmr_result = c1 + hm + wm - am
            if aktivitas == 'sangat jarang' :
                kebutuhan_kalori = int(1.2 * bmr_result)
                self.Hasil.setText(str(kebutuhan_kalori))
                kalori.kaloriTeoritis(kebutuhan_kalori)
                
            elif aktivitas == 'jarang' :
                kebutuhan_kalori = int(1.375 * bmr_result)
                self.Hasil.setText(str(kebutuhan_kalori))
                kalori.kaloriTeoritis(kebutuhan_kalori)
                
            elif aktivitas == 'normal' :
                kebutuhan_kalori = int(1.55 * bmr_result)
                self.Hasil.setText(str(kebutuhan_kalori))
                kalori.kaloriTeoritis(kebutuhan_kalori)
                
            elif aktivitas == 'sering' :
                kebutuhan_kalori = int(1.725 * bmr_result)
                self.Hasil.setText(str(kebutuhan_kalori))
                kalori.kaloriTeoritis(kebutuhan_kalori)
                
            elif aktivitas == 'sangat sering' :
                kebutuhan_kalori = int(1.9 * bmr_result)
                self.Hasil.setText(str(kebutuhan_kalori))
                kalori.kaloriTeoritis(kebutuhan_kalori)
    def kosong1(self):
        self.Hasil.setText('')
    
    def kembali(self):
        halaman2 = Screen2()
        widget.addWidget(halaman2)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class Screen4(QDialog):
    def __init__(self):
        super(Screen4, self).__init__()
        loadUi("Layer 4.ui", self)
        
        self.Hitung.clicked.connect(self.total)
        self.Kembali.clicked.connect(self.back)
        self.Selesai.clicked.connect(self.keluar)
        self.Pagi.addItems(["Nasi Putih", "Mie Instant","Nasi Uduk","Roti Tawar", "Nasi Goreng", "Bubur","Bihun Goreng", "Nasi Putih Kentucky","Kentang Rebus", "Bubur Ayam","Kentang Goreng","Mie Goreng", "Spaghetti", "Toge Goreng", "Gado-Gado", "Ketoprak", "Pempek","Rawon", "Soto Ayam", "Hamburger", "Mie Bakso", "Pizza", "Sate Kambing", "Siomay", "Soto Makasar", "Ayam Panggang", "Daging Panggang", "Sambal Goreng Tempe", "Telur Asin Rebus", "Telur Ayam Rebus", "Ati Ayam Panggang", "Ayam Pop", "Bakso Daging Sapi", "Empal Daging", "Ikan Bandeng Goreng", "Ikan Lele Goreng", "Ikan Tuna Goreng", "Tahu Bacem", "Telur Mata Sapi", "Tempe Bacem", "Tempe Goreng", "Sambal Goreng Tempe Teri", "Sambal Goreng Ati Sapi", "Sambal Goreng Udang", "Sop Sapi", "Tahu Goreng", "Tahu Isi", "Telur Dadar"])
        self.Pagi.currentIndexChanged.connect
        self.Siang.addItems(["Nasi Putih", "Mie Instant","Nasi Uduk","Roti Tawar", "Nasi Goreng", "Bubur","Bihun Goreng", "Nasi Putih Kentucky","Kentang Rebus", "Bubur Ayam","Kentang Goreng","Mie Goreng", "Spaghetti", "Toge Goreng", "Gado-Gado", "Ketoprak", "Pempek","Rawon", "Soto Ayam", "Hamburger", "Mie Bakso", "Pizza", "Sate Kambing", "Siomay", "Soto Makasar", "Ayam Panggang", "Daging Panggang", "Sambal Goreng Tempe", "Telur Asin Rebus", "Telur Ayam Rebus", "Ati Ayam Panggang", "Ayam Pop", "Bakso Daging Sapi", "Empal Daging", "Ikan Bandeng Goreng", "Ikan Lele Goreng", "Ikan Tuna Goreng", "Tahu Bacem", "Telur Mata Sapi", "Tempe Bacem", "Tempe Goreng", "Sambal Goreng Tempe Teri", "Sambal Goreng Ati Sapi", "Sambal Goreng Udang", "Sop Sapi", "Tahu Goreng", "Tahu Isi", "Telur Dadar"])
        self.Siang.currentIndexChanged.connect(self.kalori)
        self.Malam.addItems(["Nasi Putih", "Mie Instant","Nasi Uduk","Roti Tawar", "Nasi Goreng", "Bubur","Bihun Goreng", "Nasi Putih Kentucky","Kentang Rebus", "Bubur Ayam","Kentang Goreng","Mie Goreng", "Spaghetti", "Toge Goreng", "Gado-Gado", "Ketoprak", "Pempek","Rawon", "Soto Ayam", "Hamburger", "Mie Bakso", "Pizza", "Sate Kambing", "Siomay", "Soto Makasar", "Ayam Panggang", "Daging Panggang", "Sambal Goreng Tempe", "Telur Asin Rebus", "Telur Ayam Rebus", "Ati Ayam Panggang", "Ayam Pop", "Bakso Daging Sapi", "Empal Daging", "Ikan Bandeng Goreng", "Ikan Lele Goreng", "Ikan Tuna Goreng", "Tahu Bacem", "Telur Mata Sapi", "Tempe Bacem", "Tempe Goreng", "Sambal Goreng Tempe Teri", "Sambal Goreng Ati Sapi", "Sambal Goreng Udang", "Sop Sapi", "Tahu Goreng", "Tahu Isi", "Telur Dadar"])
        self.Malam.currentIndexChanged.connect(self.kalori)
        self.MinumanP.addItems(["Air Putih", "Susu Putih", "Susu Skim Rendah Lemak", "Teh", "Kopi", "Air Lemon", "Jus Apel", "Cokelat Milkshake", "Stoberi Milkshake", "Minuman Ringan", "Minuman Energi"])
        self.MinumanP.currentIndexChanged.connect(self.kalori)
        self.MinumanS.addItems(["Air Putih", "Susu Putih", "Susu Skim Rendah Lemak", "Teh", "Kopi", "Air Lemon", "Jus Apel", "Cokelat Milkshake", "Stoberi Milkshake", "Minuman Ringan", "Minuman Energi"])
        self.MinumanS.currentIndexChanged.connect(self.kalori)
        self.MinumanM.addItems(["Air Putih", "Susu Putih", "Susu Skim Rendah Lemak", "Teh", "Kopi", "Air Lemon", "Jus Apel", "Cokelat Milkshake", "Stoberi Milkshake", "Minuman Ringan", "Minuman Energi"])
        self.MinumanM.currentIndexChanged.connect(self.kalori)
        self.TambahanP.addItems(["None", "Nasi Putih", "Mie Instant","Nasi Uduk","Roti Tawar", "Nasi Goreng", "Bubur","Bihun Goreng", "Nasi Putih Kentucky","Kentang Rebus", "Bubur Ayam","Kentang Goreng","Mie Goreng", "Spaghetti", "Toge Goreng", "Gado-Gado", "Ketoprak", "Pempek","Rawon", "Soto Ayam", "Hamburger", "Mie Bakso", "Pizza", "Sate Kambing", "Siomay", "Soto Makasar", "Ayam Panggang", "Daging Panggang", "Sambal Goreng Tempe", "Telur Asin Rebus", "Telur Ayam Rebus", "Ati Ayam Panggang", "Ayam Pop", "Bakso Daging Sapi", "Empal Daging", "Ikan Bandeng Goreng", "Ikan Lele Goreng", "Ikan Tuna Goreng", "Tahu Bacem", "Telur Mata Sapi", "Tempe Bacem", "Tempe Goreng", "Sambal Goreng Tempe Teri", "Sambal Goreng Ati Sapi", "Sambal Goreng Udang", "Sop Sapi", "Tahu Goreng", "Tahu Isi", "Telur Dadar"])
        self.TambahanP.currentIndexChanged.connect(self.kalori)
        self.TambahanS.addItems(["None", "Nasi Putih", "Mie Instant","Nasi Uduk","Roti Tawar", "Nasi Goreng", "Bubur","Bihun Goreng", "Nasi Putih Kentucky","Kentang Rebus", "Bubur Ayam","Kentang Goreng","Mie Goreng", "Spaghetti", "Toge Goreng", "Gado-Gado", "Ketoprak", "Pempek","Rawon", "Soto Ayam", "Hamburger", "Mie Bakso", "Pizza", "Sate Kambing", "Siomay", "Soto Makasar", "Ayam Panggang", "Daging Panggang", "Sambal Goreng Tempe", "Telur Asin Rebus", "Telur Ayam Rebus", "Ati Ayam Panggang", "Ayam Pop", "Bakso Daging Sapi", "Empal Daging", "Ikan Bandeng Goreng", "Ikan Lele Goreng", "Ikan Tuna Goreng", "Tahu Bacem", "Telur Mata Sapi", "Tempe Bacem", "Tempe Goreng", "Sambal Goreng Tempe Teri", "Sambal Goreng Ati Sapi", "Sambal Goreng Udang", "Sop Sapi", "Tahu Goreng", "Tahu Isi", "Telur Dadar"])
        self.TambahanS.currentIndexChanged.connect(self.kalori)
        self.Tm.addItems(["None", "Nasi Putih", "Mie Instant","Nasi Uduk","Roti Tawar", "Nasi Goreng", "Bubur","Bihun Goreng", "Nasi Putih Kentucky","Kentang Rebus", "Bubur Ayam","Kentang Goreng","Mie Goreng", "Spaghetti", "Toge Goreng", "Gado-Gado", "Ketoprak", "Pempek","Rawon", "Soto Ayam", "Hamburger", "Mie Bakso", "Pizza", "Sate Kambing", "Siomay", "Soto Makasar", "Ayam Panggang", "Daging Panggang", "Sambal Goreng Tempe", "Telur Asin Rebus", "Telur Ayam Rebus", "Ati Ayam Panggang", "Ayam Pop", "Bakso Daging Sapi", "Empal Daging", "Ikan Bandeng Goreng", "Ikan Lele Goreng", "Ikan Tuna Goreng", "Tahu Bacem", "Telur Mata Sapi", "Tempe Bacem", "Tempe Goreng", "Sambal Goreng Tempe Teri", "Sambal Goreng Ati Sapi", "Sambal Goreng Udang", "Sop Sapi", "Tahu Goreng", "Tahu Isi", "Telur Dadar"])
        self.Tm.currentIndexChanged.connect(self.kalori)

    def total(self):
        pagi = self.Pagi.currentText()
        siang = self.Siang.currentText()
        malam = self.Malam.currentText()
        minum_pagi = self.MinumanP.currentText()
        minum_siang = self.MinumanS.currentText()
        minum_malam = self.MinumanM.currentText()
        pagi2 = self.TambahanP.currentText()
        siang2 = self.TambahanS.currentText()
        malam2 = self.Tm.currentText()
        
        #Minum Pagi
        if minum_pagi == 'Air Putih' :
            a = int (0)
        elif minum_pagi == 'Susu Putih' :
            a = int (250)
        elif minum_pagi == 'Susu Skim Rendah Lemak' :
            a = int (125)
        elif minum_pagi == 'Kopi' :
            a = int (15)
        elif minum_pagi == 'Teh' :
            a = int (29)
        elif minum_pagi == 'Jus Apel' :
            a = int (117)
        elif minum_pagi == 'Cokelat Milkshake' :
            a = int (238)
        elif minum_pagi == 'Stoberi Milkshake' :
            a = int (320)
        elif minum_pagi == 'Minuman Ringan' :
            a = int (153)
        elif minum_pagi == 'Minuman Energi' :
            a = int (105)
        elif minum_pagi == 'Air Lemon' :
            a = int (99)
        
        #Menu Pagi
        if  pagi == 'Nasi Putih':
            x = int(175)
            
        elif pagi == 'Mie Instant':
            x = int (168)
        
        elif pagi == 'Nasi Uduk':
            x = int (506)
        
        elif pagi == 'Roti Tawar':
            x = int (128)
            
        elif pagi == 'Bubur':
            x = int (44)
        
        elif pagi == 'Kentang Rebus':
            x = int (166)
            
        elif pagi == 'Nasi Putih Kentucky':
            x = int (349)
            
        elif pagi == 'Bubur Ayam':
            x = int (165)
        
        elif pagi == 'Kentang Goreng':
            x = int (211)
        
        elif pagi == 'Nasi Goreng':
            x = int (267)
        
        elif pagi == 'Mie Goreng':
            x = int (321)
        
        elif pagi == 'Spaghetti':
            x = int (642)
        
        elif pagi == 'Toge Goreng':
            x = int (243)
        
        elif pagi == 'Gado-Gado':
            x = int (295)
        
        elif pagi == 'Ketoprak':
            x = int (153)
        
        elif pagi == 'Pempek':
            x = int (384)
        
        elif pagi == 'Rawon':
            x = int (331)
        
        elif pagi == 'Soto Ayam':
            x = int (101)
        
        elif pagi == 'Hamburger':
            x = int (257)
        
        elif pagi == 'Mie Bakso':
            x = int (302)
        
        elif pagi == 'Pizza':
            x = int (163)
        
        elif pagi == 'Sate Kambing':
            x = int (729)
        
        elif pagi == 'Siomay':
            x = int (361)
        
        elif pagi == 'Soto Makassar':
            x = int (525)
        
        elif pagi == 'Bihun Goreng':
            x = int (296)
        elif pagi == 'Ayam Panggang' :
            x = int (164)
        elif pagi == 'Daging Panggang':
            x = int (150)
        elif pagi == 'Tempe Goreng':
            x = int (116)
        elif pagi == 'Telur Asin Rebus':
            x = int (138)
        elif pagi == 'Telur Ayam Rebus':
            x = int (97)
        elif pagi == 'Ati Ayam Goreng':
            x = int (98)
        elif pagi == 'Ayam Pop':
            x = int (265)
        elif pagi == 'Bakso Daging Sapi':
            x = int (260)
        elif pagi == 'Empal Daging':
            x = int (147)
        elif pagi == 'Ikan Bandeng Goreng':
            x = int (181)
        elif pagi == 'Ikan Lele Goreng':
            x = int (58)
        elif pagi == 'Ikan Tuna Goreng':
            x = int (110)
        elif pagi == 'Tahu Bacem':
            x = int (147)
        elif pagi == 'Telur Mata Sapi':
            x = int (40)
        elif pagi == 'Tempe Bacem':
            x = int (157)
        elif pagi == 'Tempe Goreng':
            x = int (118)
        elif pagi == 'Sambal Goreng Tempe Teri':
            x = int (267)
        elif pagi == 'Sambal Goreng Ati Sapi':
            x = int (200)
        elif pagi == 'Sambal Goreng Udang':
            x = int (123)
        elif pagi == 'Sop Sapi':
            x = int (227)
        elif pagi == 'Tahu Goreng':
            x = int (111)
        elif pagi == 'Tahu Isi':
            x = int (124)
        elif pagi == 'Telur Dadar':
            x = int (188)
        
        #Tamaham pagi
        if  pagi2 == 'Nasi Putih':
            l = int(175)
            
        elif pagi2 == 'None':
            l = int (0)
            
        elif pagi2 == 'Mie Instant':
            l = int (168)
        
        elif pagi2 == 'Nasi Uduk':
            l = int (506)
        
        elif pagi2 == 'Roti Tawar':
            l = int (128)
            
        elif pagi2 == 'Bubur':
            l = int (44)
        
        elif pagi2 == 'Kentang Rebus':
            l = int (166)
            
        elif pagi2 == 'Nasi Putih Kentucky':
            l = int (349)
            
        elif pagi2 == 'Bubur Ayam':
            l = int (165)
        
        elif pagi2 == 'Kentang Goreng':
            l = int (211)
        
        elif pagi2 == 'Nasi Goreng':
            l = int (267)
        
        elif pagi2 == 'Mie Goreng':
            l = int (321)
        
        elif pagi2 == 'Spaghetti':
            l = int (642)
        
        elif pagi2 == 'Toge Goreng':
            l = int (243)
        
        elif pagi2 == 'Gado-Gado':
            l = int (295)
        
        elif pagi2 == 'Ketoprak':
            l = int (153)
        
        elif pagi2 == 'Pempek':
            l = int (384)
        
        elif pagi2 == 'Rawon':
            l = int (331)
        
        elif pagi2 == 'Soto Ayam':
            l = int (101)
        
        elif pagi2 == 'Hamburger':
            l = int (257)
        
        elif pagi2 == 'Mie Bakso':
            l = int (302)
        
        elif pagi2 == 'Pizza':
            l = int (163)
        
        elif pagi2 == 'Sate Kambing':
            l = int (729)
        
        elif pagi2 == 'Siomay':
            l = int (361)
        
        elif pagi2 == 'Soto Makassar':
            l = int (525)
        
        elif pagi2 == 'Bihun Goreng':
            l = int (296)
        elif pagi2 == 'Ayam Panggang' :
            l = int (164)
        elif pagi2 == 'Daging Panggang':
            l = int (150)
        elif pagi2 == 'Tempe Goreng':
            l = int (116)
        elif pagi2 == 'Telur Asin Rebus':
            l = int (138)
        elif pagi2 == 'Telur Ayam Rebus':
            l = int (97)
        elif pagi2 == 'Ati Ayam Goreng':
            l = int (98)
        elif pagi2 == 'Ayam Pop':
            l = int (265)
        elif pagi2 == 'Bakso Daging Sapi':
            l = int (260)
        elif pagi2 == 'Empal Daging':
            l = int (147)
        elif pagi2 == 'Ikan Bandeng Goreng':
            l = int (181)
        elif pagi2 == 'Ikan Lele Goreng':
            l = int (58)
        elif pagi2 == 'Ikan Tuna Goreng':
            l = int (110)
        elif pagi2 == 'Tahu Bacem':
            l = int (147)
        elif pagi2 == 'Telur Mata Sapi':
            l = int (40)
        elif pagi2 == 'Tempe Bacem':
            l = int (157)
        elif pagi2 == 'Tempe Goreng':
            l = int (118)
        elif pagi2 == 'Sambal Goreng Tempe Teri':
            l = int (267)
        elif pagi2 == 'Sambal Goreng Ati Sapi':
            l = int (200)
        elif pagi2 == 'Sambal Goreng Udang':
            l = int (123)
        elif pagi2 == 'Sop Sapi':
            l = int (227)
        elif pagi2 == 'Tahu Goreng':
            l = int (111)
        elif pagi2 == 'Tahu Isi':
            l = int (124)
        elif pagi2 == 'Telur Dadar':
            l = int (188)
        
        #Menu siang     
        if  siang == 'Nasi Putih':
            y = int(175)
            
        elif siang == 'Mie Instant':
            y = int (168)
        
        elif siang == 'Nasi Uduk':
            y = int (506)
        
        elif siang == 'Roti Tawar':
            y = int (128)
            
        elif siang == 'Bubur':
            y = int (44)
        
        elif siang == 'Kentang Rebus':
            y = int (166)
            
        elif siang == 'Nasi Putih Kentucky':
            y = int (349)
            
        elif siang == 'Bubur Ayam':
            y = int (165)
        
        elif siang == 'Kentang Goreng':
            y = int (211)
        
        elif siang == 'Nasi Goreng':
            y = int (267)
        
        elif siang == 'Mie Goreng':
            y = int (321)
        
        elif siang == 'Spaghetti':
            y = int (642)
        
        elif siang == 'Toge Goreng':
            y = int (243)
        
        elif siang == 'Gado-Gado':
            y = int (295)
        
        elif siang == 'Ketoprak':
            y = int (153)
        
        elif siang == 'Pempek':
            y = int (384)
        
        elif siang == 'Rawon':
            y = int (331)
        
        elif siang == 'Soto Ayam':
            y = int (101)
        
        elif siang == 'Hamburger':
            y = int (257)
        
        elif siang == 'Mie Bakso':
            y = int (302)
        
        elif siang == 'Pizza':
            y = int (163)
        
        elif siang == 'Sate Kambing':
            y = int (729)
        
        elif siang == 'Siomay':
            y = int (361)
        
        elif siang == 'Soto Makassar':
            y = int (525)
        
        elif siang == 'Bihun Goreng':
            y = int (296)
        elif siang == 'Ayam Panggang' :
            y = int (164)
        elif siang == 'Daging Panggang':
            y = int (150)
        elif siang == 'Tempe Goreng':
            y = int (116)
        elif siang == 'Telur Asin Rebus':
            y = int (138)
        elif siang == 'Telur Ayam Rebus':
            y = int (97)
        elif siang == 'Ati Ayam Goreng':
            y = int (98)
        elif siang == 'Ayam Pop':
            y = int (265)
        elif siang == 'Bakso Daging Sapi':
            y = int (260)
        elif siang == 'Empal Daging':
            y = int (147)
        elif siang == 'Ikan Bandeng Goreng':
            y = int (181)
        elif siang == 'Ikan Lele Goreng':
            y = int (58)
        elif siang == 'Ikan Tuna Goreng':
            y = int (110)
        elif siang == 'Tahu Bacem':
            y = int (147)
        elif siang == 'Telur Mata Sapi':
            y = int (40)
        elif siang == 'Tempe Bacem':
            y = int (157)
        elif siang == 'Tempe Goreng':
            y = int (118)
        elif siang == 'Sambal Goreng Tempe Teri':
            y = int (267)
        elif siang == 'Sambal Goreng Ati Sapi':
            y = int (200)
        elif siang == 'Sambal Goreng Udang':
            y = int (123)
        elif siang == 'Sop Sapi':
            y = int (227)
        elif siang == 'Tahu Goreng':
            y = int (111)
        elif siang == 'Tahu Isi':
            y = int (124)
        elif siang == 'Telur Dadar':
            y = int (188)
        
        #Tambahan Siang
        if  siang2 == 'Nasi Putih':
            m = int(175)
        
        elif siang2 == 'None' :
            m = int (0)
        
        elif siang2 == 'Mie Instant':
            m = int (168)
        
        elif siang2 == 'Nasi Uduk':
            m = int (506)
        
        elif siang2 == 'Roti Tawar':
            m = int (128)
            
        elif siang2 == 'Bubur':
            m = int (44)
        
        elif siang2 == 'Kentang Rebus':
            m = int (166)
            
        elif siang2 == 'Nasi Putih Kentucky':
            m = int (349)
            
        elif siang2 == 'Bubur Ayam':
            m = int (165)
        
        elif siang2 == 'Kentang Goreng':
            m = int (211)
        
        elif siang2 == 'Nasi Goreng':
            m = int (267)
        
        elif siang2 == 'Mie Goreng':
            m = int (321)
        
        elif siang2 == 'Spaghetti':
            m = int (642)
        
        elif siang2 == 'Toge Goreng':
            m = int (243)
        
        elif siang2 == 'Gado-Gado':
            m = int (295)
        
        elif siang2 == 'Ketoprak':
            m = int (153)
        
        elif siang2 == 'Pempek':
            m = int (384)
        
        elif siang2 == 'Rawon':
            m = int (331)
        
        elif siang2 == 'Soto Ayam':
            m = int (101)
        
        elif siang2 == 'Hamburger':
            m = int (257)
        
        elif siang2 == 'Mie Bakso':
            m = int (302)
        
        elif siang2 == 'Pizza':
            m = int (163)
        
        elif siang2 == 'Sate Kambing':
            m = int (729)
        
        elif siang2 == 'Siomay':
            m = int (361)
        
        elif siang2 == 'Soto Makassar':
            m = int (525)
        
        elif siang2 == 'Bihun Goreng':
            m = int (296)
        elif siang2 == 'Ayam Panggang' :
            m = int (164)
        elif siang2 == 'Daging Panggang':
            m = int (150)
        elif siang2 == 'Tempe Goreng':
            m = int (116)
        elif siang2 == 'Telur Asin Rebus':
            m = int (138)
        elif siang2 == 'Telur Ayam Rebus':
            m = int (97)
        elif siang2 == 'Ati Ayam Goreng':
            m = int (98)
        elif siang2 == 'Ayam Pop':
            m = int (265)
        elif siang2 == 'Bakso Daging Sapi':
            m = int (260)
        elif siang2 == 'Empal Daging':
            m = int (147)
        elif siang2 == 'Ikan Bandeng Goreng':
            m = int (181)
        elif siang2 == 'Ikan Lele Goreng':
            m = int (58)
        elif siang2 == 'Ikan Tuna Goreng':
            m = int (110)
        elif siang2 == 'Tahu Bacem':
            m = int (147)
        elif siang2 == 'Telur Mata Sapi':
            m = int (40)
        elif siang2 == 'Tempe Bacem':
            m = int (157)
        elif siang2 == 'Tempe Goreng':
            m = int (118)
        elif siang2 == 'Sambal Goreng Tempe Teri':
            m = int (267)
        elif siang2 == 'Sambal Goreng Ati Sapi':
            m = int (200)
        elif siang2 == 'Sambal Goreng Udang':
            m = int (123)
        elif siang2 == 'Sop Sapi':
            m = int (227)
        elif siang2 == 'Tahu Goreng':
            m = int (111)
        elif siang2 == 'Tahu Isi':
            m = int (124)
        elif siang2 == 'Telur Dadar':
            m = int (188)
        
        #Minum Siang    
        if minum_siang == 'Air Putih' :
            b = int (0)
        elif minum_siang == 'Susu Putih' :
            b = int (250)
        elif minum_siang == 'Susu Skim Rendah Lemak' :
            b = int (125)
        elif minum_siang == 'Kopi' :
            b = int (15)
        elif minum_siang == 'Teh' :
            b = int (29)
        elif minum_siang == 'Jus Apel' :
            b = int (117)
        elif minum_siang == 'Cokelat Milkshake' :
            b = int (238)
        elif minum_siang == 'Stoberi Milkshake' :
            b = int (320)
        elif minum_siang == 'Minuman Ringan' :
            b = int (153)
        elif minum_siang == 'Minuman Energi' :
            b = int (105)
        elif minum_siang == 'Air Lemon' :
            b = int (99)
        
        
        #Menu Malam
        if  malam == 'Nasi Putih':
            z = int(175)

        elif malam == 'Mie Instant':
            z = int (168)
        
        elif malam == 'Nasi Uduk':
            z = int (506)
        
        elif malam == 'Roti Tawar':
            z = int (128)
            
        elif malam == 'Bubur':
            z = int (44)
        
        elif malam == 'Kentang Rebus':
            z = int (166)
            
        elif malam == 'Nasi Putih Kentucky':
            z = int (349)
            
        elif malam == 'Bubur Ayam':
            z = int (165)
        
        elif malam == 'Kentang Goreng':
            z = int (211)
        
        elif malam == 'Nasi Goreng':
            z = int (267)
        
        elif malam == 'Mie Goreng':
            z = int (321)
        
        elif malam == 'Spaghetti':
            z = int (642)
        
        elif malam == 'Toge Goreng':
            z = int (243)
        
        elif malam == 'Gado-Gado':
            z = int (295)
        
        elif malam == 'Ketoprak':
            z = int (153)
        
        elif malam == 'Pempek':
            z = int (384)
        
        elif malam == 'Rawon':
            z = int (331)
        
        elif malam == 'Soto Ayam':
            z = int (101)
        
        elif malam == 'Hamburger':
            z = int (257)
        
        elif malam == 'Mie Bakso':
            z = int (302)
        
        elif malam == 'Pizza':
            z = int (163)
        
        elif malam == 'Sate Kambing':
            z = int (729)
        
        elif malam == 'Siomay':
            z = int (361)
        
        elif malam == 'Soto Makassar':
            z = int (525)
            
        elif malam == 'Bihun Goreng':
            z = int (296)
        elif malam == 'Ayam Panggang' :
            z = int (164)
        elif malam == 'Daging Panggang':
            z = int (150)
        elif malam == 'Tempe Goreng':
            z = int (116)
        elif malam == 'Telur Asin Rebus':
            z = int (138)
        elif malam == 'Telur Ayam Rebus':
            z = int (97)
        elif malam == 'Ati Ayam Goreng':
            z = int (98)
        elif malam == 'Ayam Pop':
            z = int (265)
        elif malam == 'Bakso Daging Sapi':
            z = int (260)
        elif malam == 'Empal Daging':
            z = int (147)
        elif malam == 'Ikan Bandeng Goreng':
            z = int (181)
        elif malam == 'Ikan Lele Goreng':
            z = int (58)
        elif malam == 'Ikan Tuna Goreng':
            z = int (110)
        elif malam == 'Tahu Bacem':
            z = int (147)
        elif malam == 'Telur Mata Sapi':
            z = int (40)
        elif malam == 'Tempe Bacem':
            z = int (157)
        elif malam == 'Tempe Goreng':
            z = int (118)
        elif malam == 'Sambal Goreng Tempe Teri':
            z = int (267)
        elif malam == 'Sambal Goreng Ati Sapi':
            z = int (200)
        elif malam == 'Sambal Goreng Udang':
            z = int (123)
        elif malam == 'Sop Sapi':
            z = int (227)
        elif malam == 'Tahu Goreng':
            z = int (111)
        elif malam == 'Tahu Isi':
            z = int (124)
        elif malam == 'Telur Dadar':
            z = int (188)
            
        #Tambahan malam
        if  malam2 == 'Nasi Putih':
            n = int(175)

        elif malam2 == 'None' :
            n = int (0)
        
        elif malam2 == 'Mie Instant':
            n = int (168)
        
        elif malam2 == 'Nasi Uduk':
            n = int (506)
        
        elif malam2 == 'Roti Tawar':
            n = int (128)
            
        elif malam2 == 'Bubur':
            n = int (44)
        
        elif malam2 == 'Kentang Rebus':
            n = int (166)
            
        elif malam2 == 'Nasi Putih Kentucky':
            n = int (349)
            
        elif malam2 == 'Bubur Ayam':
            n = int (165)
        
        elif malam2 == 'Kentang Goreng':
            n = int (211)
        
        elif malam2 == 'Nasi Goreng':
            n = int (267)
        
        elif malam2 == 'Mie Goreng':
            n = int (321)
        
        elif malam2 == 'Spaghetti':
            n = int (642)
        
        elif malam2 == 'Toge Goreng':
            n = int (243)
        
        elif malam2 == 'Gado-Gado':
            n = int (295)
        
        elif malam2 == 'Ketoprak':
            n = int (153)
        
        elif malam2 == 'Pempek':
            n = int (384)
        
        elif malam2 == 'Rawon':
            n = int (331)
        
        elif malam2 == 'Soto Ayam':
            n = int (101)
        
        elif malam2 == 'Hamburger':
            n = int (257)
        
        elif malam2 == 'Mie Bakso':
            n = int (302)
        
        elif malam2 == 'Pizza':
            n = int (163)
        
        elif malam2 == 'Sate Kambing':
            n = int (729)
        
        elif malam2 == 'Siomay':
            n = int (361)
        
        elif malam2 == 'Soto Makassar':
            n = int (525)
            
        elif malam2 == 'Bihun Goreng':
            n = int (296)
        elif malam2 == 'Ayam Panggang' :
            n = int (164)
        elif malam2 == 'Daging Panggang':
            n = int (150)
        elif malam2 == 'Tempe Goreng':
            n = int (116)
        elif malam2 == 'Telur Asin Rebus':
            n = int (138)
        elif malam2 == 'Telur Ayam Rebus':
            n = int (97)
        elif malam2 == 'Ati Ayam Goreng':
            n = int (98)
        elif malam2 == 'Ayam Pop':
            n = int (265)
        elif malam2 == 'Bakso Daging Sapi':
            n = int (260)
        elif malam2 == 'Empal Daging':
            n = int (147)
        elif malam2 == 'Ikan Bandeng Goreng':
            n = int (181)
        elif malam2 == 'Ikan Lele Goreng':
            n = int (58)
        elif malam2 == 'Ikan Tuna Goreng':
            n = int (110)
        elif malam2 == 'Tahu Bacem':
            n = int (147)
        elif malam2 == 'Telur Mata Sapi':
            n = int (40)
        elif malam2 == 'Tempe Bacem':
            n = int (157)
        elif malam2 == 'Tempe Goreng':
            n = int (118)
        elif malam2 == 'Sambal Goreng Tempe Teri':
            n = int (267)
        elif malam2 == 'Sambal Goreng Ati Sapi':
            n = int (200)
        elif malam2 == 'Sambal Goreng Udang':
            n = int (123)
        elif malam2 == 'Sop Sapi':
            n = int (227)
        elif malam2 == 'Tahu Goreng':
            n = int (111)
        elif malam2 == 'Tahu Isi':
            n = int (124)
        elif malam2 == 'Telur Dadar':
            n = int (188)
        
        # Minum Malam
        if minum_malam == 'Air Putih' :
            c = int (0)
        elif minum_malam == 'Susu Putih' :
            c = int (250)
        elif minum_malam == 'Susu Skim Rendah Lemak' :
            c = int (125)
        elif minum_malam == 'Kopi' :
            c = int (15)
        elif minum_malam == 'Teh' :
            c = int (29)
        elif minum_malam == 'Jus Apel' :
            c = int (117)
        elif minum_malam == 'Cokelat Milkshake' :
            c = int (238)
        elif minum_malam == 'Stoberi Milkshake' :
            c = int (320)
        elif minum_malam == 'Minuman Ringan' :
            c = int (153)
        elif minum_malam == 'Minuman Energi' :
            c = int (105)
        elif minum_malam == 'Air Lemon' :
            c = int (99)
        
        
        totalpagi = a + x + l
        totalsiang = b + y + m
        totalmalam = z + n + c
        self.Jum1.setText(str(totalpagi))
        self.Jum2.setText(str(totalsiang))
        self.Jum3.setText(str(totalmalam))
        total = totalpagi + totalsiang + totalmalam
        kalori.kaloriAktual(total)
        self.Total.setText(str(total))
        self.Kesimpulan.setText(f'{kalori.Kalori()}')
        
    def kalori (self):
        self.Jum1.setText('')
        self.Jum2.setText('')
        self.Jum3.setText('')
        self.Total.setText('')
        self.Kesimpulan.setText('')
            
    def back(self):
        halaman2 = Screen2()
        widget.addWidget(halaman2)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def keluar(self):
        sys.exit(app.exec_())
        
class TotalKalori:
    def __init__(self):
        self.kebutuhan_kalori = int(0)
        self.total = int(0)
    def kaloriTeoritis(self,kalori_teoritis):
        self.kebutuhan_kalori = kalori_teoritis
    def kaloriAktual(self,kalori_aktual):
        self.total = kalori_aktual
    def Kalori(self):
        if self.total <= self.kebutuhan_kalori :
            a = 'Makan Lagi kak'
            return a
        elif self.total == self.kebutuhan_kalori :
            a = 'kakak sehat'
            return a
        elif self.total >= self.kebutuhan_kalori :
            a = 'kebanyakan makan kak'
            return a
        # self.Kesimpulan.setText(str(a))
        
    

app=QApplication(sys.argv)
mainwindow=MainWindow()
kalori = TotalKalori()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
# Setingan Width dan Height untuk Fullscreen
# widget.setFixedWidth(1920)
# widget.setFixedHeight(1000)
widget.setFixedWidth(1080)
widget.setFixedHeight(1920)
widget.show()
sys.exit(app.exec_())