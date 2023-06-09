#import json file

import json

#open the json file 
#store it in dictionary
#append the content need to be added
#print it to check


with open('ex5.json') as json_file:
    ex5 = json.load(json_file)
    ex5[2]['batters']['batter'].append({'id': '1003', 'type': 'Coffee'})
    print(ex5)


#open the file in Write mode
#dumb the updated value to the existing json file


with open('ex5.json','w') as json_file:
    json.dump(ex5,json_file)
    
