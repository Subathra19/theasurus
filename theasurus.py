import json
# a lib to compare text
import difflib
#from difflib import SequenceMatcher
#SequenceMatcher(None,"rain","rainn").ratio //Output:0.888. Gives the similarity between two words
#None is a function used to ignore junk(breakline and spaces) in the text entered
from difflib import get_close_matches
#get_close_matches("rain,["rainn","help","road"])

content=json.load(open("data.json"))
#json file will be loaded as dictionary

def find(data):
    # As all data in json file are in lower case. We convert our input into lower case for comparison
    mod_data=data.lower() 
    no_of_matches=len(get_close_matches(mod_data,content.keys()))
  
    if mod_data in content:
        return content[mod_data]
    #Modification 1: For proper nouns such as Delhi or Chennai in json file
    elif mod_data.title() in content:
        return content[mod_data.title()]
    #Modification 2: For acronyms such as USA or NATO in json file
    elif mod_data.upper() in content:
        return content[mod_data.upper()]
    elif no_of_matches>0:
        print("Did you mean {}?".format(get_close_matches(mod_data,content.keys())[0]))
        #print(get_close_matches(mod_data,content.keys()))//['rain', 'train', 'rainy']. First item will be the most closest match.
        #We can increase the matching ratio by using cutoff:get_close_matches(mod_data,content.keys(),cutoff=0.8)
        # we get an empty list in case of mismatch
        
        check=input("Enter yes/no:")
        if check=="yes":
            return content[get_close_matches(mod_data,content.keys())[0]]
        elif check=="no": 
            return "Word does not exist. Please check the data you have entered."
        else:
            return "We didn't understand"
    else:
        return "Word does not exist. Please check the data you have entered." 

data=input("Enter the word:")
output=find(data)
if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)
