class Person():
    def __init__(self, firstname, lastname, ismale):
        self.firstname = firstname
        self.lastname = lastname
        self.ismale = ismale


class Mitarbeiter(Person):
    def __init__(self,firstname, lastname, ismale, work):
        Person.__init__(self, firstname, lastname, ismale)
        self.work = work

    def work(self):
        print("Ich bin ein Mitarbeiter am Arbeiten.")


class Gruppenleiter(Mitarbeiter):
    def __init__(self,firstname, lastname, ismale, work, lead = True):
        Mitarbeiter.__init__(self, firstname, lastname, ismale, work)
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
        return "male percentage: " + countm/all + ", female percentage: " + countw/all


class Abteilung:
    def __init__(self, name, gruppenleiter = []):
        self.name = name
        self.mitarbeiter = []
        self.gruppenleiter = []
        self.gruppenleiter.append(gruppenleiter)



if __name__ == '__main__':
    gl = Gruppenleiter("Guido", "Kurz", True, 10)
    print(gl.lead)
