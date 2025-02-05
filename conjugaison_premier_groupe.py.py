SYMBOLE = '-'
ESPACE = ' '

# Verbes particuliers
VERBES_EXCEPTIONS_01 = ("acheter", "haleter", "crocheter", "geler", "déceler", "modeler", "ciseler", "congeler", "marteler")
VERBES_EXCEPTIONS_02 = ("ébrer", "écher", "écrer", "égler", "égner", "égrer", "éguer", "équer", "étrer", "évrer")
VERBES_EXCEPTIONS_03 = ("écer", "éder", "éler", "émer", "éner", "érer", "éser", "éter", "éyer")
VERBES_EXCEPTIONS_04 = ("ecer", "emer", "eper", "erer", "eser", "ever", "evrer", "ener")

# Terminaisons temps présent
TERMINAISONS_01 = ("e", "es", "e", "ons", "ez", "ent")
TERMINAISONS_GER_01 = ("e", "es", "e", "eons", "ez", "ent")
TERMINAISONS_CER_01 = ("ce", "ces", "ce", "çons", "cez", "cent")
TERMINAISONS_OYER_UYER_01 = ("ie", "ies", "ie", "yons", "yez", "ient")
TERMINAISONS_ETER_01 = ("te", "tes", "te", "ons", "ez", "tent")
TERMINAISONS_ELER_01 = ("le", "les", "le", "ons", "ez", "lent")

# Teminaisons temps imparfait
TERMINAISONS_02 = ("ais", "ais", "ait", "ions", "iez", "aient")
TERMINAISONS_GER_02 = ("eais", "eais", "eait", "ions", "iez", "eaient")
TERMINAISONS_CER_02 = ("çais", "çais", "çait", "cions", "ciez", "çaient")

# Terminaisons temps futur
TERMINAISONS_03 = ("erai", "eras", "era", "erons", "erez", "eront")
TERMINAISONS_OYER_UYER_03 = ("ierai", "ieras", "iera", "ierons", "ierez", "ieront")
TERMINAISONS_ETER_03 = ("terai", "teras", "tera", "terons", "terez", "teront")
TERMINAISONS_ELER_03 = ("lerai", "leras", "lera", "lerons", "lerez", "leront")


class Conjugaison:
    def __init__(self, verbe: str) -> None:
        # On contrôle ici que le verbe donné par l'utilisateur est bien un verbe du premier groupe, que ce n'est pas le verbe "aller".
        if not verbe.endswith("er") or verbe == "aller":
            raise ValueError(f"Le verbe {verbe} n'est pas un verbe du premier groupe.")
        self.verbe = verbe.lower()
        self.radical = self.verbe[:-2]
    
    def present(self):
        print(f"\n{SYMBOLE*8}Verbe {self.verbe} au present{SYMBOLE*8}")

        # Pour garder le son [j], un e apparaît avec nous.
        if self.verbe.endswith("ger"):
            terminaisons = TERMINAISONS_GER_01

        # Pour garder le son [s], une cédille apparaît avec nous.
        elif self.verbe.endswith("cer"):
            self.radical = self.radical[:-1]
            terminaisons = TERMINAISONS_CER_01

        # Ces verbes peuvent changer leur y en un i mais pas toujours. Devant NOUS et VOUS, ils ne changent JAMAIS leur y.
        elif self.verbe.endswith("oyer") or self.verbe.endswith("uyer"):
            self.radical = self.radical[:-1]
            terminaisons = TERMINAISONS_OYER_UYER_01

        # Ces verbes doublent leur t pour garder le son è sauf avec NOUS et VOUS. 
        elif self.verbe.endswith("eter") and self.verbe not in VERBES_EXCEPTIONS_01:
            terminaisons = TERMINAISONS_ETER_01

        # Ces verbes doublent leur l pour garder le son è sauf avec NOUS et VOUS. 
        elif self.verbe.endswith("eler") and self.verbe not in VERBES_EXCEPTIONS_01:
            terminaisons = TERMINAISONS_ELER_01

        # Ces verbes ne doublent pas leur t ou leur l et ont un accent grave à la place.
        elif self.verbe in VERBES_EXCEPTIONS_01:
            terminaisons = (f"{'è'+self.verbe[-3]+'e'}", 
                            f"{'è'+self.verbe[-3]+'es'}", 
                            f"{'è'+self.verbe[-3]+'e'}", 
                            f"{self.verbe[-4:-2]+'ons'}", 
                            f"{self.verbe[-4:-2]+'ez'}", 
                            f"{'è'+self.verbe[-3]+'ent'}"
                            )
            self.radical = self.radical[:-2]

        # Ces verbes changent leur é en è sauf avec nous et vous.
        elif self.verbe[-5:] in VERBES_EXCEPTIONS_02:
            terminaisons = (f"{'è'+self.verbe[-4:-2]+'e'}", 
                            f"{'è'+self.verbe[-4:-2]+'es'}", 
                            f"{'è'+self.verbe[-4:-2]+'e'}", 
                            f"{self.verbe[-5:-2]+'ons'}", 
                            f"{self.verbe[-5:-2]+'ez'}", 
                            f"{'è'+self.verbe[-4:-2]+'ent'}"
                            )
            self.radical = self.radical[:-3]

        # Ces verbes changent leur é en è sauf avec nous et vous.
        elif self.verbe[-4:] in VERBES_EXCEPTIONS_03:
            terminaisons = (f"{'è'+self.verbe[-3]+'e'}", 
                            f"{'è'+self.verbe[-3]+'es'}", 
                            f"{'è'+self.verbe[-3]+'e'}", 
                            f"{self.verbe[-4:-2]+'ons'}", 
                            f"{self.verbe[-4:-2]+'ez'}", 
                            f"{'è'+self.verbe[-3]+'ent'}"
                            )
            self.radical = self.radical[:-2]
        
        # Les verbes ayant un e à l'avant-dernière syllabe de l'infinitif, ils changent leur e en un è sauf avec nous et vous.
        elif self.verbe[-4:] in VERBES_EXCEPTIONS_04:
            terminaisons = (f"{'è'+self.verbe[-3]+'e'}", 
                            f"{'è'+self.verbe[-3]+'es'}", 
                            f"{'è'+self.verbe[-3]+'e'}", 
                            f"{self.verbe[-4:-2]+'ons'}", 
                            f"{self.verbe[-4:-2]+'ez'}", 
                            f"{'è'+self.verbe[-3]+'ent'}"
                            )
            self.radical = self.radical[:-2]

        else:
            # Tous les autres verbes.    
            terminaisons = TERMINAISONS_01
            
        for terminaison in terminaisons:
            print(f"{self.radical}{terminaison}")
        self.radical = self.verbe[:-2]
    
    def imparfait(self):
        print(f"\n{SYMBOLE*8}Verbe {self.verbe} à l'imparfait{SYMBOLE*8}")

        if self.verbe.endswith("ger"):
            terminaisons = TERMINAISONS_GER_02
        elif self.verbe.endswith("cer"):
            terminaisons = TERMINAISONS_CER_02
            self.radical = self.verbe[:-3]           
        else:
            terminaisons = TERMINAISONS_02
            
        for terminaison in terminaisons:
            print(f"{self.radical}{terminaison}")
        self.radical = self.verbe[:-2]
    
    def futur(self):
        print(f"\n{SYMBOLE*8}Verbe {self.verbe} au futur{SYMBOLE*8}")

        if self.verbe.endswith("oyer") or self.verbe.endswith("uyer"):
            self.radical = self.verbe[:-3]
            terminaisons = TERMINAISONS_OYER_UYER_03
        elif self.verbe.endswith("eter") and self.verbe not in VERBES_EXCEPTIONS_01:
            terminaisons = TERMINAISONS_ETER_03
        elif self.verbe.endswith("eler") and self.verbe not in VERBES_EXCEPTIONS_01:
            terminaisons = TERMINAISONS_ELER_03
        elif self.verbe in VERBES_EXCEPTIONS_01 or self.verbe[-4:] in VERBES_EXCEPTIONS_04:
            terminaisons = (f"{'è'+self.verbe[-3]+'erai'}", 
                            f"{'è'+self.verbe[-3]+'eras'}", 
                            f"{'è'+self.verbe[-3]+'era'}", 
                            f"{'è'+self.verbe[-3]+'erons'}", 
                            f"{'è'+self.verbe[-3]+'erez'}", 
                            f"{'è'+self.verbe[-3]+'eront'}"
                            )
            self.radical = self.radical[:-2]
        else:
            terminaisons = TERMINAISONS_03
       
        for terminaison in terminaisons:
            print(f"{self.radical}{terminaison}")
        self.radical = self.verbe[:-2]


class Affichage:
    def __init__(self) -> None:
        choix_01 = input("\nEntrez l'infinif du verbe du premier groupe à conjuguer : ")
        self.conjugaison = Conjugaison(choix_01)

    def boucle_de_saisie(self):
        choix = 0

        while choix != '4':
            print(f"\nChoisissez le temps de la conjugaison : \nPrésent{ESPACE*5}: tapez 1") 
            print(f"Imparfait{ESPACE*3}: tapez 2 \nFutur{ESPACE*7}: tapez 3\nPour sortir : tapez 4")

            choix = input("\nVotre choix : ")
            if choix == '1':
                self.conjugaison.present()
            elif choix == '2':
                self.conjugaison.imparfait()
            elif choix == '3':
                self.conjugaison.futur()


affichage = Affichage()
affichage.boucle_de_saisie()