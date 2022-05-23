from balok import Balok 
from hitung_balok import HitungBalok

class ViewBalok :
    def show_luas (self, balok:Balok , hitung_balok : HitungBalok ) :
        print (hitung_balok.hitung_luas(balok))
    
    def show_keliling (self, balok:Balok , hitung_balok : HitungBalok ) :
        print (hitung_balok.hitung_keliling(balok))
    
    def show_volume (self, balok:Balok , hitung_balok : HitungBalok ) :
        print (hitung_balok.hitung_volume(balok)) 