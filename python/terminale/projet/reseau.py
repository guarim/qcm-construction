class AdresseIP:

    def __init__(self,adr):
        adr_split = adr.split(".")
        assert len(adr_split)==4, "L'adresse IP doit contenir 4 entiers séparés par le caractère '.'"
        for octet in adr_split:
            assert octet.isdigit(), f"{octet} n'est pas un entier positif"
            assert 0<=int(octet)<=255, f"{octet} n'est pas compris entre 0 et 255"
        self.adresse = adr
        self.octets = [int(oct) for oct in adr_split]
    
    def __str__(self):
        return self.adresse

    def binaire(self):
        bin_oct = [bin(oct)[2:].zfill(8) for oct in self.octets]
        return ".".join(bin_oct)
    
    def hexadecimal(self):
        hex_oct = [hex(oct)[2:].zfill(2) for oct in self.octets]
        return ".".join(hex_oct)
    
    def meme_debut(self,other):
        bin1 = self.binaire().replace(".","")
        bin2 = other.binaire().replace(".","")
        md = 0
        while md<32 and bin1[md] == bin2[md]  :
            md += 1
        return md


class Masque:

    def __init__(self,cidr):
        assert type(cidr)==int,"Le masque en notation cidr n'est pas un entier"
        assert 0<= cidr <= 32,"Le masque en notation cidr doit être compris en 0 et 32"
        self.cidr = cidr
    
    def __str__(self):
        return str(self.cidr)
    
    def en_adresse(self):
        adr_bin = "1"*self.cidr+"0"*(32-self.cidr)
        adr = ""
        for n in range(4):
            adr += str(to_dec(adr_bin[n*8:n*8+8]))
            adr +="."
        return AdresseIP(adr[:-1])
    
    def get_cidr(self):
        return self.cidr


class Reseau:
    def __init__(self,adresse):
        adresse_split = adresse.split("/")
        adr_ip, cidr = adresse_split[0], int(adresse_split[1])
        self.ip = AdresseIP(adr_ip)
        self.cidr = Masque(cidr)
    
    def __str__(self):
        return f"{self.ip}/{self.cidr}"

    def adresse_reseau(self):
        machine = self.ip.binaire()
        masque = self.cidr.en_adresse().binaire()
        reseau_bin = ""
        for i in range(len(machine)):
            if machine[i]!=".":
                reseau_bin += et(machine[i],masque[i])
            else:
                reseau_bin+="."
        reseau_dec = ".".join([to_dec(bits) for bits in reseau_bin.split('.')])
        return AdresseIP(reseau_dec)
    
    def adresse_diffusion(self):
        machine = self.ip.binaire()
        masque = self.cidr.en_adresse().binaire()
        reseau_bin = ""
        for i in range(len(machine)):
            if machine[i]!=".":
                if masque[i]=="0":
                    nmasque="1"
                else:
                    nmasque="0"
                reseau_bin += ou(machine[i],nmasque)
            else:
                reseau_bin+="."
        reseau_dec = ".".join([to_dec(bits) for bits in reseau_bin.split('.')])
        return AdresseIP(reseau_dec)


    def nb_adresses(self):
        return 2**(32-self.cidr.get_cidr())-2


def to_dec(bits):
    decimal = 0
    poids = len(bits)-1
    for i in range(len(bits)):
        decimal += int(bits[i])*2**poids
        poids -= 1
    return str(decimal)

def et(bit1,bit2):
    if bit1 !="1" or bit2 !="1":
        return "0"
    else:
        return "1"

def ou(bit1,bit2):
    if bit1 =="1" or bit2 =="1":
        return "1"
    else:
        return "0"
            



        


