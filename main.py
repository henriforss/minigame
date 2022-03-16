# TEE PELI TÄHÄN


import pygame
import random



class Robotti():                    # Luodaan Robotti-luokka
    id_nro = 0                      # Jokaiselle Robotti-luokasta muodostetulle oliolle annetaan om id_nro


    @classmethod                    # Luokkametodi jonka avulla palautetaan yksilöllinen id_nro
    def robo_id(cls) -> int:        
        cls.id_nro += 1             
        return cls.id_nro           


    def __init__(self, ) -> None:                       # Luodaan Robotti-olio
        self.id_nro = Robotti.robo_id()                 # Robotin uniikki id_nro
        self.kuva = pygame.image.load("robo.png")       # Ladataan robotin kuva
        self.x = 0                                      # Tässä pelissä käytetään pygamen Rect-olioita: Robotti-olion x- ja y- koordinaatit annetaan muutoksena edellisiin koordinaatteihin
        self.y = 0
        self.rect = self.kuva.get_rect()                # Luodaan kuvan kokoinen Rect-olio
        self.rect.center = 800 / 2, 600 / 2             # Asetetaan Robotti-olion keskikohta keskelle näyttöä pelin aluksi


    def __repr__(self) -> str:                          # __repr__-funktio joka palauttaa tietoa Robotti-oliosta
        return f"Robotti(id: {self.id_nro})"            


    def liiku(self, naytto):                            # Metodi jonka avulla Robotti-oliota liiutetaan   
        self.rect = self.rect.move(self.x, self.y)
        self.rect.clamp_ip(naytto)



class Kolikko():                                    # Luodaan Kolikko-luokka, jolla on samoja toimintoja kuin edellisellä
    id_nro = 0


    @classmethod                                    
    def kolikko_id(cls) -> int:
        cls.id_nro += 1
        return cls.id_nro


    def __init__(self) -> None:                     
         self.id_nro = Kolikko.kolikko_id()
         self.kuva = pygame.image.load("kolikko.png")
         self.rect = self.kuva.get_rect()
         self.rect.center = random.randint(50, 750), random.randint(50, 550)


    def __repr__(self) -> str:
        return f"Kolikko(id: {self.id_nro})"



class Hirvio():                 # Luodaan Hirvio-luokka jolla on saman tyyppisiä toimintoja kuin edellisillä
    id_nro = 0
    hirvio_liikesuunnat = {     # Sanakirja jossa määritellään hirviön liikesuunnat
        "vasen": (-2, 0),
        "oikea": (2, 0),
        "ylos": (0, -2),
        "alas": (0, 2)
        }


    @classmethod
    def hirvio_id(cls) -> int:          # Luokkametodi jolla annetaan jokaiselle Hirvio-oliolle oma id_nro 
        cls.id_nro += 1
        return cls.id_nro


    @classmethod
    def hirvio_suunta(cls) -> tuple:                            # Luokkametodi jolla arvotaan mihin suuntaan luotu Hirvio-olio liikkuu
        suunta = random.choice(list(cls.hirvio_liikesuunnat))
        return cls.hirvio_liikesuunnat[suunta]


    @classmethod
    def hirvio_aloituspaikka(cls, x: int, y: int) -> tuple:     # Luokkametodi jolla arvotaan mihin kohtaan hirviökenttää Hirviö-olio luodaan. Hirviökenttä on näytön ulkopuolinen alue jossa Hirvio-oliot luodaan ja poistetaan.
        if x > 0 and y == 0:                                    
            return -50, random.randint(50, 550)
        elif x < 0 and y == 0:
            return 850, random.randint(50, 550)
        elif y > 0 and x == 0:
            return random.randint(50, 750), -50
        elif y < 0 and x == 0:
            return random.randint(50, 750), 650


    def __init__(self) -> None:                                 # Luodaan Hirvio-olio
        self.id_nro = Hirvio.hirvio_id()                        # Palautetaan Hirvio-oliolle uniikki id_nro
        self.kuva = pygame.image.load("hirvio.png")             # Annetaan Hirvio-oliolle kuva
        self.rect = self.kuva.get_rect()                        # Luodaan Hirvio-olion kokoinen Rect-olio
        self.x, self.y = Hirvio.hirvio_suunta()                 # Arvotaan Hirvio-olion suunta
        self.rect.center = Hirvio.hirvio_aloituspaikka(self.x, self.y)  # Arvotaan mihin kohtaan hirviökenttää Hirvio-olio luodaan
        self.kentalla = True                                    # Hirviökenttä: näytön ulkopuolinen alue jossa Hirvio-olio luodaan ja poistetaan


    def __repr__(self) -> str:
        return f"Hirviö(id: {self.id_nro}, x: {self.x}, y: {self.y})"


    def liiku(self):                                            # Funktio jolla liikutetaan Hirvio-oliota
        self.rect = self.rect.move(self.x, self.y)



class Peli():                   # Luodaan Peli-luokka
    id_nro = 0                  # Jokaiselle Peli-luokasta muodostetulle oliolle annetaan oma id_nro tämän avulla
    RED = (255, 0, 0)

    @classmethod                # Luokkametodi jonka avulla palautetaan yksilöllinen id_nro jokaiselle Peli-oliolle
    def peli_id(cls) -> int:        
        cls.id_nro += 1             
        return cls.id_nro           

    def __init__(self) -> None:                                                 # Luodaan peli-olio
        self.id_nro = Peli.peli_id()                                            # Peli-olion id_nro
                                                                                
        pygame.init()                                                           # Käynnistetään pygame
                                                                                    
        pygame.display.set_caption("Kultakuume")                                # Näytön asetukset
        self.leveys = 800                                                       
        self.korkeus = 600                                                      
        self.naytto = pygame.display.set_mode((self.leveys, self.korkeus))      
        self.naytto_rect = self.naytto.get_rect()                               # Näyton kokoinen Rect-olio

        self.hirviokentta_rect = pygame.Rect((-100, -100), (1000, 800))         # Pelikentän ulkopuolinen rect, muodostaa pelikentän ulpuolisen alueen jossa hirviöt syntyvät ja poistuvat 

        self.fontti_iso = pygame.font.SysFont("Arial", 100)                     # Pelissä käytetty iso fontti
        self.fontti_pieni = pygame.font.SysFont("Arial", 25)                    # Pelissä käytetty pieni fontti
                                                                                
        self.kello = pygame.time.Clock()                                        # Pelin kello
                                                                                
        self.pelaaja = Robotti()                                                # Luodaan pelaaja, eli Robotti-olio
                                                                                
        self.pisteet = 0                        # Pisteet
        self.elamat = 5                         # Elämät, nämä tulisi oikeastaan tallentaa Robotti-olioon
        self.hirviot_lista = []                 # Lista johon hirviöt tallennetaan
        self.kolikot_lista = []                 # Lista johon kolikot tallennetaan
                                                                  
        self.silmukka()                         # Kutsutaan peli-silmukkaa


    def silmukka(self) -> None:                         # Peli-silmukka. Käydään läpi pelin toiminnot.
        while True:                                     
            self.tutki_syotteet()                     
            self.liikuta_pelaajaa()
            self.tormaa_hirvioon(self.pelaaja, self.hirviot_lista)
            self.luo_kolikko()
            self.keraa_kolikko(self.pelaaja)                          
            self.luo_hirvio(self.hirviot_lista)
            self.liikuta_hirviota(self.hirviot_lista)
            self.poista_hirvio(self.hirviot_lista)
            self.piirra_naytto()                        
            self.peli_loppu()
            self.peli_lapi()
            self.kello.tick(60)                         


    def tutki_syotteet(self) -> None:                       # Tutki peliin syotettyja tapahtumia
        for tapahtuma in pygame.event.get():                
            if tapahtuma.type == pygame.QUIT:               
                exit()                                      
            if tapahtuma.type == pygame.KEYDOWN:            
                if tapahtuma.key == pygame.K_ESCAPE:        # Escape-näppäin lopettaa pelin
                    exit()
                if tapahtuma.key == pygame.K_LEFT:          # Nuolinäppäimet muuttavat pelaajan Robotti-olion koordinaatteja, joilla oliota liikutellaan.   
                    self.pelaaja.x = -5                     
                if tapahtuma.key == pygame.K_RIGHT:         
                    self.pelaaja.x = 5                      
                if tapahtuma.key == pygame.K_UP:            
                    self.pelaaja.y = -5                     
                if tapahtuma.key == pygame.K_DOWN:          
                    self.pelaaja.y = 5     
                if tapahtuma.key == pygame.K_SPACE:         # Välilyöntinäppäin aloittaa uuden pelin, jos peli_loppu tai peli_läpi on True.
                    if self.peli_loppu() == True or self.peli_lapi() == True:
                        self.uusi_peli()                 
            if tapahtuma.type == pygame.KEYUP:              
                if tapahtuma.key == pygame.K_LEFT:          
                    self.pelaaja.x = 0                      
                if tapahtuma.key == pygame.K_RIGHT:         
                    self.pelaaja.x = 0                      
                if tapahtuma.key == pygame.K_UP:            
                    self.pelaaja.y = 0                      
                if tapahtuma.key == pygame.K_DOWN:          
                    self.pelaaja.y = 0                      


    def piirra_naytto(self) -> None:                                        # Piirrä tapahtumat näytölle.
        self.naytto.fill((70, 220, 45))                                     # Täytä näyttö pohjavärillä.

        for alkio in self.kolikot_lista:                                    # Piirrä kolikot.
            self.naytto.blit(alkio.kuva, alkio.rect)

        for alkio in self.hirviot_lista:                                    # Piirrä hirviöt.
            self.naytto.blit(alkio.kuva, alkio.rect)

        self.naytto.blit(self.pelaaja.kuva, self.pelaaja.rect)              # Piirrä Pelaaja-olio.

        pisteet = self.tulosta_teksti_pieni(f"Pisteet: {self.pisteet}/10")      # Piirrä pisteet.
        self.naytto.blit(pisteet, (620, 20))

        elamat = self.tulosta_teksti_pieni(f"Elämät: {self.elamat}/5")          # Piirrä elämät.
        self.naytto.blit(elamat, (40, 20))

        if self.peli_lapi() == True:                                        # Tarkasta onko pelaaja voittanut pelin.                     
            teksti = self.tulosta_teksti_iso("VOITTO!")                     # Tulosta voitto-teksti.
            tekstin_leveys = teksti.get_width()
            tekstin_korkeus = teksti.get_height()
            tekstin_x = 400 - tekstin_leveys / 2
            tekstin_y = 240 - tekstin_korkeus / 2
            self.naytto.blit(teksti, (tekstin_x, tekstin_y))

        if self.peli_loppu() == True:
            teksti = self.tulosta_teksti_iso("Hävisit pelin.")              # Tarkasta onko pelaaja hävinnyt pelin.
            tekstin_leveys = teksti.get_width()                             # Tulosta häviö-teksti.
            tekstin_korkeus = teksti.get_height()
            tekstin_x = 400 - tekstin_leveys / 2
            tekstin_y = 240 - tekstin_korkeus / 2
            self.naytto.blit(teksti, (tekstin_x, tekstin_y))

        if self.peli_lapi() == True or self.peli_loppu() == True:
            ohje = self.tulosta_teksti_pieni("(Pelaa uudestaan painamalla 'välilyönti'. Lopeta painamalla 'poistu'.)")
            ohje_leveys = ohje.get_width()
            ohje_korkeus = ohje.get_height()
            ohje_x = 400 - ohje_leveys / 2
            ohje_y = 350 - ohje_korkeus / 2
            self.naytto.blit(ohje, (ohje_x, ohje_y))

        pygame.display.flip()                                           # Päivitä näyttö.


    def liikuta_pelaajaa(self):                                         # Funktio joka liikuttaa pelaajaa.
        if self.peli_lapi() == True or self.peli_loppu() == True:
            return
        else:
            self.pelaaja.liiku(self.naytto_rect)                        # Funktio kutsuu Pelaaja-olion liiku-metodia.


    def luo_kolikko(self):                          # Funktio joka luo uuden kolikon, jos kentällä ei tiettyä määrää kolikkoita.
        if len(self.kolikot_lista) < 2:
            kolikko = Kolikko()
            print(f"{kolikko} luotu")               # Tulostetaan tietoa pelitapahtumasta
            self.kolikot_lista.append(kolikko)
        else:
            return


    def keraa_kolikko(self, pelaaja: object):                           # Funktio jonka avulla pelaaja kerää kolikoita.
        for alkio in self.kolikot_lista:                                # Funktio käy läpi kaikki kolikot.   
            if pygame.Rect.colliderect(pelaaja.rect, alkio.rect):       # Jos kolikko ja pelaaja törmäävät toisiinsa...
                self.pisteet += 1                                       # ...pelaaja saa pisteen.
                print(f"{alkio} kerätty")                               # Tulostetaan tietoa pelitapahtumasta.
                self.kolikot_lista.remove(alkio)
            else:
                continue


    def luo_hirvio(self, hirviot_lista: list):      # Funktio joka luo Hirvio-olion jos oliota on vähemmän kuin kuusi, ja lisää sen listaan.
        if len(hirviot_lista) < 6:
            hirvio = Hirvio()
            print(f"{hirvio} luotu")
            hirviot_lista.append(hirvio)


    def liikuta_hirviota(self, hirviot_lista: list):                    # Funktio joka liikuttaa Hirvio-oliota. Paitsi jos peli on loppu tai läpi.
        if self.peli_lapi() == True or self.peli_loppu() == True:
            return
        else:
            for alkio in hirviot_lista:
                alkio.liiku()


    def tormaa_hirvioon(self, pelaaja: object, hirviot_lista: list):    # Funktio joka tutkii jos pelaaja ja Hirvio-olio törmäävät.
        for alkio in hirviot_lista:
            if pygame.Rect.colliderect(pelaaja.rect, alkio.rect):       # Käytetään colliderect-metodia. Jos True niin eteenpäin.
                self.elamat -= 1                                        # Törmäyksessä pelaajalta vähennetään yksi elämä.
                print(f"{alkio} törmäys")     
                hirviot_lista.remove(alkio)                             # Hirvio-olio poistetaan listasta.
                if self.elamat > 0:                
                    pelaaja.rect.center = 800 / 2, 600 / 2                  # Pelaaja asetetaan keskelle ruutua.
            else:
                continue


    def poista_hirvio(self, hirviot_lista: list):               # Funktio joka postaa Hirvio-oliot jotka ovat matkanneet näytön yli törmäämättä pelaajaan.
        for alkio in hirviot_lista:                     
            if self.hirviokentta_rect.contains(alkio):          # Käytetään Rect-olion contains-metodia. Huom: hirviökenttä on suurempi kuin näyttö. Jos hirviökentän sijaan käytettäisiin näytön mittoja, hirviöt poistuisivat heti kun osuvat näytön reunaan. Eli eivät vasta sitten kun ovat menneet näytön reunojen yli.
                alkio.kentalla = True                           # Hirvio-olion attribuutti kentalla on True. Tätä ei varsinaisesti käytetä mihinkään tässä vaiheessa.
            else:
                alkio.kentalla = False                          # Hirvio.kentalla == False. Ei käytetä mihinkään tällä hetkellä.
                print(f"{alkio} poistettu")                     
                hirviot_lista.remove(alkio)                     # Jos Hirvio-olio törmää hirviökentän seinään, olio poistetaan listasta.


    def peli_lapi(self):                    # Funktio joka tarkastaa pelin tilanteen.
        if self.pisteet >= 10:
            return True
        else:
            return False


    def peli_loppu(self):                   # Toinen funktio joka tarkastaa pelin tilanteen.
        if self.elamat <= 0:
            return True
        else:
            return False


    def uusi_peli(self):                    # Funktio joka käynnistää uuden pelin, kun edellinen peli on ohi ja pelaaja painaa välilyönti-näppäintä.
        self.elamat = 5
        self.pisteet = 0
        self.hirviot_lista.clear()
        self.kolikot_lista.clear()


    def tulosta_teksti_iso(self, merkkijono: str) -> pygame.Surface:        # Funktio joka muotoilee tekstiä.
        teksti = self.fontti_iso.render(merkkijono, True, (255, 0, 0))
        return teksti


    def tulosta_teksti_pieni(self, merkkijono: str) -> pygame.Surface:      # Toinen funktio joka muotoilee tekstiä.
        teksti = self.fontti_pieni.render(merkkijono, True, (255, 0, 0))
        return teksti



if __name__ == "__main__":

    peli1 = Peli()          # Luodaan Peli-olio pelin testailua varten



