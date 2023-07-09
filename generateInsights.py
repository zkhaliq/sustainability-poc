import json


class generateInsights:
    # input into the class
    totalProduct = dict(oldSeriesknt=0, oldChassisknt=0, newSeriesknt=0, newChassisknt=0)
    asisSustainabilityParams = dict(Power=0, co2Emission=0, heat=0, cost=0)
    newSustainabilityParams = dict(Power=0, co2Emission=0, heat=0, cost=0)

    # qtrs
    __qtr = ("Total", "Q1", "Q2", "Q3", "Q4")

    # equipments
    __models = ("M3/M4 Rack and Blade Servers Decommission", "M3/M4 Chassis Decommission", "M7 Blade Servers Installation", "M7 Chassis Installation")

    # savingstypes
    __typs = ("Power", "co2Emission", "heat", "cost")
    response: json
    __savinglist = list()
    __productcount = list()

    def __computePower(self):
        num = 1
        svgs = dict()
        intervallist = list()
        for itrqtr in self.__qtr:
            itrvl = dict()
            itrvl["Period"] = itrqtr
            if itrqtr == "Total":
                itrvl["count"] = round((self.asisSustainabilityParams[self.__typs[0]] - self.newSustainabilityParams[
                    self.__typs[0]]), 3)
            else:
                itrvl["count"] = round(((self.asisSustainabilityParams[self.__typs[0]] - self.newSustainabilityParams[
                    self.__typs[0]]) * (num) * (1 / 4)), 3)
                num += 1
            intervallist.append(itrvl)
            svgs["type:"] = "Power"
            svgs["interval"] = intervallist
        self.__savinglist.append(svgs)

    def __computeCo2Emission(self):
        coefficient: float
        coefficient = 0.6 / 1000
        num = 1
        svgs = dict()
        intervallist = list()
        for itrqtr in self.__qtr:
            itrvl = dict()
            itrvl["Period"] = itrqtr
            if itrqtr == "Total":
                itrvl["count"] = round(((self.asisSustainabilityParams[self.__typs[0]] - self.newSustainabilityParams[
                    self.__typs[0]]) * (coefficient)), 5)
            else:
                itrvl["count"] = round(((self.asisSustainabilityParams[self.__typs[0]] - self.newSustainabilityParams[
                    self.__typs[0]]) * (num) * (1 / 4) * (coefficient)), 5)
                num += 1
            intervallist.append(itrvl)
            svgs["type:"] = "co2Emission"
            svgs["interval"] = intervallist
        self.__savinglist.append(svgs)

    def __computeHeat(self):
        num = 1
        revnum = 3
        svgs = dict()
        intervallist = list()
        for itrqtr in self.__qtr:
            itrvl = dict()
            itrvl["Period"] = itrqtr
            if itrqtr == "Total":
                itrvl["count"] = round((self.asisSustainabilityParams[self.__typs[2]] - self.newSustainabilityParams[
                    self.__typs[2]]), 2)
            else:
                itrvl["count"] = round((self.asisSustainabilityParams[self.__typs[2]] - (
                        (self.asisSustainabilityParams[self.__typs[2]]) * (revnum) * (1 / 4) + (
                    self.newSustainabilityParams[
                        self.__typs[2]]) * (num) * (1 / 4))), 2)
                num += 1
                revnum -= 1
            intervallist.append(itrvl)
            svgs["type:"] = "Heat"
            svgs["interval"] = intervallist
        self.__savinglist.append(svgs)

    def __computeCost(self):
        coefficient = 0.105
        num = 1
        svgs = dict()
        intervallist = list()
        for itrqtr in self.__qtr:
            itrvl = dict()
            itrvl["Period"] = itrqtr
            if itrqtr == "Total":
                itrvl["count"] = round(((self.asisSustainabilityParams[self.__typs[0]] - self.newSustainabilityParams[
                    self.__typs[0]]) * (coefficient)), 2)
            else:
                itrvl["count"] = round(((self.asisSustainabilityParams[self.__typs[0]] - self.newSustainabilityParams[
                    self.__typs[0]]) * (num) * (1 / 4) * (coefficient)), 2)
                num += 1
            intervallist.append(itrvl)
            svgs["type:"] = "Cost"
            svgs["interval"] = intervallist
        self.__savinglist.append(svgs)

    def __sustainabilityInsights(self):
        self.__computePower()
        self.__computeCo2Emission()
        self.__computeHeat()
        self.__computeCost()

    def __productInsight(self):
        x = divmod(self.totalProduct["oldSeriesknt"] / 4, 4)
        itr = 0

        for itrqtr in self.__qtr:
            prd = dict()
            eqlst = list()
            i = 0
            for itrkey, itrval in self.totalProduct.items():
                eq = dict()
                if itrqtr == "Total":
                    eq["count"] = itrval
                elif itrqtr == 'Q1':
                    eq["count"] = divmod(itrval, 4)[0] + divmod(itrval, 4)[1]
                else:
                    eq["count"] = divmod(itrval, 4)[0]
                eq["model"] = self.__models[i]
                eqlst.append(eq)
                i += 1
            prd["period"] = itrqtr
            prd["equipment"] = eqlst
            self.__productcount.append(prd)

    def runInsights(self):
        powerCoEfficient = (24 * 365) / 1000
        self.asisSustainabilityParams["Power"] = self.asisSustainabilityParams["Power"] * powerCoEfficient
        self.newSustainabilityParams["Power"] = self.newSustainabilityParams["Power"] * powerCoEfficient

        self.__productInsight()
        self.__sustainabilityInsights()

        response = dict()
        response["ProductCount"] = self.__productcount
        response["Savings"] = self.__savinglist
        #self.response = json.dumps(response)
        self.response = response