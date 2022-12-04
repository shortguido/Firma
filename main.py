class Person():
    def __init__(self, firstname, lastname, ismale):
        self.firstname = firstname
        self.lastname = lastname
        self.ismale = ismale


class Mitarbeiter(Person):
    def __init__(self,firstname, lastname, ismale, work):
        super().__init__(firstname, lastname, ismale)
        self.work = work

    def worken(self):
        print("Ich bin ein Mitarbeiter am Arbeiten.")


class Gruppenleiter(Mitarbeiter):
    def __init__(self,firstname, lastname, ismale, work, lead = True):
        super().__init__(firstname, lastname, ismale, work)
        self.lead = lead

    def lead(self):
        print("Ich leite meine Mitarbeiter")


class Firma:
    def __init__(self, name):
        self.name = name
        self.abteilungen = []

    def countma(self):
        count = 0
        for a in self.abteilungen:
            count += len(a.mitarbeiter)
        return count

    def countabts(self):
        return len(self.abteilungen)

    def countgl(self):
        count = 0
        for a in self.abteilungen:
            count += len(a.gruppenleiter)
        return count

    def meistema(self):
        bigabt = self.abteilungen[0]
        for a in self.abteilungen:
            if len(a.mitarbeiter) > len(bigabt.mitarbeiter):
                bigabt = a
        return bigabt

    def prozentfm(self):
        countm = 0
        countw = 0
        for a in self.abteilungen:
            for m in a.mitarbeiter:
                if m.ismale == True:
                    countm += 1
                else:
                    countw += 1

            for g in a.gruppenleiter:
                if g.ismale == True:
                    countm += 1
                else:
                    countw += 1

        all = countm + countw
        return "male percentage: " + "{:.2f}".format((countm/all)*100) + " %, female percentage: " + "{:.2f}".format((countw/all)*100) +" %"


class Abteilung:
    def __init__(self, name, gruppenleiter = []):
        self.name = name
        self.mitarbeiter = []
        self.gruppenleiter = []
        self.gruppenleiter.append(gruppenleiter)


if __name__ == '__main__':
    gl = Gruppenleiter("Guido", "Kurz", True, 10)
    gl2 = Gruppenleiter("Andreas", "Remair", True, 10)

    firma = Firma("Schule")
    abt = Abteilung("Wirtschaft", gl)
    firma.abteilungen.append(abt)
    abt2 = Abteilung("Maschinbau", gl2)
    firma.abteilungen.append(abt2)

    ma1 = Mitarbeiter("Jürgen", "von der Lippe", True, True)
    ma2 = Mitarbeiter("Barbara", "Rabarbara", False, True)
    ma3 = Mitarbeiter("Andreas", "Holzmann", True, True)
    abt.mitarbeiter.append(ma1)
    abt.mitarbeiter.append(ma2)
    abt.mitarbeiter.append(ma3)
    abt2.mitarbeiter.append(ma1)

    print(firma.meistema().name)
    print(firma.countabts())
    print(firma.prozentfm())
    print(firma.countma())
    print(firma.countgl())


