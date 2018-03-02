#pset 2 #2

for i in range (0,168,24):
    j = range(0,168,1)[i-5]
    if (j>i):
        df['hour'].replace(range(j,i+19,1),range(0,24,5), inplace=True) #replacing range from i value to and whatever value it is i+19 with 24
        df['hour'].replace()
    else:
        df['hour'].replace(range(j,i+19,1),range(0,24,1), inplace=True)

# ex. if i=0; then j should return 163

# kate crawford,
# Joy Buolamwini, facial recognition https://www.seattletimes.com/business/facial-recognition-technology-works-best-if-youre-a-white-guy/
#
# women vs men cell phone ownership
#
# "god trick" is a high level view; looks true and neutral and complete because the bodies in rendering those views are invisible
# From whose perspective are we looking? white is default #wow -___-
# address isues of structural powe
#
# globe.mediameter.org -- most coverage on the news; geography/spatial bias
# who's getting the most coverage
# But also what words are being used most often, in headlines

examine power and aspire to empowerment (?) --> people want to use data in positive way/PR remove
data literacy

databasic.io

embrace pluralism -> more people at the table T__T"""""""""
data murals :)

legitimize affect and embodiment --> acknkolwedge that people who do this data stuff has emotions
Edward Tufte =? data-ink ratio; only use ink for the data parts

"data visceralization" – 
