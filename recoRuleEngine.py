class recoRuleEngine:
    asisConfig = dict(chassis="", bServer="", rServer="", fi="")
    recommendedConfig = dict(chassis="", bServer="", fi="")

    # computes qty of reco rules
    def runRule(self):
        asis = self.asisConfig
        reccomend = self.recommendedConfig
        totalServer = asis["bServer"] + asis["rServer"]
        reccomend["bServer"] = round(totalServer / 4)
        reccomend["chassis"] = round(reccomend["bServer"] / 8)
        reccomend["fi"] = round((reccomend["chassis"] * 4) / 44)

    # calculate no of FIs needed for existing config
    def calcFI(self):
        asis = self.asisConfig
        asis["fi"] = round((asis["bServer"] + asis["rServer"]) / 60)
