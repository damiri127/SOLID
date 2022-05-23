from balok import Balok

class HitungBalok:
    
    def hitung_luas(self,balok: Balok):
        return 2 * (balok.get_panjang() + balok.get_lebar() + balok.get_tinggi())
    
    def hitung_keliling(self, balok: Balok):
        return 4 * (balok.get_panjang + balok.get_lebar() + balok.get_tinggi())
    
    def hitung_volume(self, balok: Balok):
        return balok.get_panjang() + balok.get_lebar() + balok.get_tinggi()
    