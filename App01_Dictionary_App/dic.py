import json
from difflib import get_close_matches
import mysql.connector

filepath = 'C:/Repos/Udemy_Python_Mega_Course_10_Apps/App01_Dictionary_App/'
keepSearching = True

#Load json file into object
data = json.load(open(filepath+'data.json','r'))

# If we were using a database #########
conn = mysql.connector.connect(
    user = 'ardit700_student',
    password = 'ardit700_student',
    host = '100.167.140.122',
    database='ardit700_pm1database'
)
cursor = conn.cursor()
cursor.execute(f"Select * From Dictionary Where Expression = '{word}' ")
#results contain a tuples of tuples(expression, definition)
results = cursor.fetchall()
for t in results:
    for e,d in t:
        print(d)
########################################

def find(word):
    if word in data:
        return data[word]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data,cutoff=0.8)) > 0:
        print('\n'+'*'*20)
        print('Closest matching words: ',end='')
        print(get_close_matches(word,data,5,cutoff=0.8))
        print('*'*20+'\n')
        
        closest_matching_word = get_close_matches(word,data,cutoff=0.8)[0]
        if askForClarity(closest_matching_word):
            return data[closest_matching_word]
        else:
            return 'Word does not exist'
    else:
        return 'Word does not exist'

def askForClarity(closest_word):
    clarity = input(f'Did you mean {closest_word} (y/n): ')
    return clarity == 'y'

def getWord():
    word = input('Enter word: ')
    return word.lower()

def getDecision():
    decision = input('Keep searching? (y/n): ')
    decision = decision.lower()
    while decision not in ['y', 'n']:
        print("Invalid input, only 'y' or 'n'")
        decision = input('Keep searching? (y/n): ')
        decision = decision.lower()
    return decision == 'y'

def printResults(output):
    if type(output) == list:
        for idx,d in enumerate(output):
            print(f'{idx+1}. {d}')
    else:
        print(output)

while(keepSearching):
    word_to_search = getWord()
    printResults(find(word_to_search))
    keepSearching = getDecision()
