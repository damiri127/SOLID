from balok import Balok
from hitung_balok import HitungBalok
from view_balok import ViewBalok 

balok = Balok (2,3,4) 
hitung_balok = HitungBalok () 
view_balok = ViewBalok () 

view_balok.show_luas(balok,hitung_balok) 
view_balok.show_keliling(balok,hitung_balok)
view_balok.show_volume(balok,hitung_balok)