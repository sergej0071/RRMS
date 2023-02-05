class DataMapperHelper():
    def splitArrayBykey(self, realData, key):
        value = []
        
        for i in realData:
            value.append(i[key])

        return value