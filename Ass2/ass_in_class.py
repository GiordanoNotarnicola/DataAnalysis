import math

class Particle:
    def __init__(self, mass, charge, name, momentum=0.):
        self._mass=mass #MeV
        self._charge=charge
        self._name= name
        self._momentum=momentum

    @property
    def mass(self):
        return self._mass

    @property
    def charge(self):
        return self._charge

    @property
    def name(self):
        return self._name

    @property
    def energy(self):
        return math.sqrt(self.mass**2+self.momentum**2) #posso chiamare la property anche all'interno della classe... non cambia niente, ma chiamo una funzione in più

    @property
    def beta(self):
        return self.momentum/self.energy

    @property
    def gamma(self):
        return self.energy/self.mass

    @property
    def momentum(self):
        return self._momentum

    @momentum.setter #uso la validazione nel setter e viene chiamata anche dal costruttore
    def momentum(self, new_momentum):
        if new_momentum<0:
            print("ERROR: Particle can't have a momentum less than 0. Momentum will be set to 0")
            self._momentum=0
        else:
            self._momentum=new_momentum

    @energy.setter #nome_property.setter e deve chiamarsi come la property la nuova funzione
    def energy(self, new_energy):#new_energy non usa self perchè non è nè un metodo nè un attributo
        if new_energy<self.mass:
            print(f"ERROR:you can't have an energy lower than particle mass ({self.mass})")
            return
        new_momentum=math.sqrt(new_energy**2- self.mass**2)
        self.momentum=new_momentum

    @beta.setter
    def beta(self, new_beta):
        if new_beta>1 or new_beta<0:
            return print("ERROR: beta must be between 0 and 1")
        else:
            self.momentum=new_beta*self.mass/math.sqrt(1-new_beta**2)

    def __str__(self):
        return f"Particle {self.name} of mass {self.mass} MeV, charge {self.charge} and momentum {self.momentum} MeV"


class Proton(Particle):

    NAME="Proton"
    MASS=939 #MeV
    CHARGE=1

    def __init__(self, momentum=0):
        Particle.__init__(self, 
                          name=Proton.NAME,
                          mass=Proton.MASS, 
                          charge=Proton.CHARGE,
                          momentum=momentum)#puoi usare anche super(). (non serve il self) per chiamare la classe madre(uh uh python moderno)








if __name__=="__main__":
    muon= Particle(mass=105.6, charge=-1, name="Muon", momentum=100)
    print(muon.name, muon.energy, muon.beta, muon.gamma)
    muon.energy=200
    print(muon.energy)
    muon.beta=0.5
    print(muon)
    proton=Proton(momentum=200)
    print(proton)
    proton.beta=0.8
    print(proton)
