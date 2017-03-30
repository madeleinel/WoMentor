import re

def tweetParse(tweetString):
    # first identify if mentor or mentee
    isMentorBool = '#mentor' in tweetString.lower()
    isMentor = 'mentor' if isMentorBool else 'mentee'
    # then identify indices of '-'s in string
    indices = [i for i, x in enumerate(tweetString) if x == "-"]
    index_1 = indices[0]
    index_2 = indices[1]
    index_3 = indices[2]
    tweetStringLength = len(tweetString)
    # slice string into substrings and make the lists into an array of values
    substring_1 = tweetString[index_1:index_2]
    substring_2 = tweetString[index_2:index_3]
    substring_3 = tweetString[index_3:tweetStringLength]
    substring_1 = toMultiStrings(substring_1)
    substring_2 = toMultiStrings(substring_2)
    substring_3 = toMultiStrings(substring_3)

    return isMentor, substring_1, substring_2, substring_3

def toMultiStrings(string):
    string = re.sub('-(.*?):', '', string)
    string = re.sub(',', '', string)
    string = string.strip()
    string = string.split()
    for str in string:
        str = str.strip()
    return string

# example tweets:
# #WomenToTech #Mentor -langs: javascript, python, haskell -skill: node.js, d3.js, jinja2 -offering: help getting started
# #WomenToTech #Mentee -langs: ruby, -skills: french, baking, SVG -seeking: help getting started
# if they have more than 3 languages change the third to 'and more' in the db
# if it contains SQL just include it as is
# we need to link to the tweet thread on the mentor list
