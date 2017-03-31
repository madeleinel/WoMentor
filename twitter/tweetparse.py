import re
from acceptedlangs import accepted_langs_normal, accepted_langs_lower

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
    substring_3 = toMultiStrings(substring_3, isOffer=True)
    substring_1, substring_2 = checkTheLists(substring_1, substring_2)
    substring_3 = checkOffers(substring_3)
    return isMentor, substring_1, substring_2, substring_3

def toMultiStrings(string, isOffer=False):
  if isOffer:
    string = re.sub('-(.*?):', '', string)
    string = string.split(',')
    string = string.strip() if type(string) is str else stripString(string)
    return string
  else:
    string = re.sub('-(.*?):', '', string)
    string = re.sub(',', '', string)
    string = string.strip()
    string = string.split()
    return string

def stripString(string):
  for indx, strng in enumerate(string):
    strng = strng.strip()
    string[indx] = strng
  return string


def checkTheLists(langstore, skillstore):
    langs = []
    skills = []
    for language in langstore:
        if language.lower() in accepted_langs_lower:
            langs.append(language)
        elif 'SQL' in language:
            langs.append(language)
        else:
            skills.append(language)
    if len(langs) > 4:
        langs = langs[:3]
        langs.append('and more...')
    if len(skillstore) <= 4:
        if len(skills) != 0:
            for skill in skills:
                skillstore.append(skill)
    if len(skillstore) > 4:
        print skillstore
        skillstore = skillstore[:3]
        skillstore.append('and more...')
    return langs, skillstore

def checkOffers(offerstore):
    offers = []
    for offer in offerstore:
      if 'start' in offer:
        offers.append('getting started')
      elif 'career' in offer:
        offers.append('career advice')
      elif 'project' in offer:
        offers.append('project help')
    return offers

# example tweets:
# #WomenToTech #Mentor -langs: javascript, python, haskell -skill: node.js, d3.js, jinja2 -offering: help getting started
# #WomenToTech #Mentee -langs: ruby, -skills: french, baking, SVG -seeking: help getting started
# if they have more than 3 languages change the third to 'and more' in the db
# if it contains SQL just include it as is
# we need to link to the tweet thread on the mentor list
