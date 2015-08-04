import types

#The structure for contestants will be:
#{userId:[countryId, newWeight]}
contestants = {}

#The structure for averageWeightPerCountry will be:
#{countryId:[totalCountryWeight, totalUsersPerCountry]}
averageWeightPerCountry = {}

keepUserTrack = []

def checkUser(user):
    if user in contestants.keys():
        return True
    else:
        return False
    

def updateLeaderBoard(countryId="", userId=0, newWeight=0.0):
    if type(countryId) == types.StringType and type(userId) == types.IntType and type(newWeight) == types.FloatType:
        #checking for exitence of the user before submitting data
        if checkUser(userId):
            #update user's weight loss
            contestants[userId][1] = abs(newWeight-contestants[userId][1])
            averageWeightPerCountry[countryId][0] += contestants[userId][1]
        else:
            #new user
            contestants[userId] = [countryId, newWeight]
            if averageWeightPerCountry.get(countryId):
                #Calculate total users per country
                averageWeightPerCountry[countryId][1] += 1
            else:
                #new country
                averageWeightPerCountry[countryId] = [0,1]
        
        #print "contestants " + str(contestants)
        #print "averageWeightPerCountry " + str(averageWeightPerCountry)
        print "The new weight average per country is:"
        for eachCountry, eachCountryData in averageWeightPerCountry.iteritems():
            totalCountryWeight = eachCountryData[0]
            totalUsersPerCountry = eachCountryData[1]
            print eachCountry+": "+str(totalCountryWeight/totalUsersPerCountry)+""        
        
    else:
        print "Some of the values, if not all of them, are wrong:"
        print "CountryId must be a string"
        print "userId must be an integer"
        print "newWeight must be a float"
        
    return "OK"

if __name__ == '__main__':
    #updateLeaderBoard("US", 123, 170.5)
    #updateLeaderBoard("DR", 1234, 170.5)
    #updateLeaderBoard("DR", 1234, 160.5)
    #updateLeaderBoard("DR", 12345, 200.5)
    #updateLeaderBoard("DR", 12345, 170.5)

    updateLeaderBoard('US', 123, 175.5) 
    updateLeaderBoard('DE', 444, 203.0) 
    updateLeaderBoard('GB', 555, 164.5) 
    updateLeaderBoard('US', 123, 171.5) 
    updateLeaderBoard('DE', 444, 202.0) 
    updateLeaderBoard('GB', 555, 164.0) 
