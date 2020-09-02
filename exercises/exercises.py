abbr = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
states = {"AL":"Alabama","AK":"Alaska","AZ":"Arizona","AR":"Arkansas","CA":"California","CO":"Colorado","CT":"Connecticut","DE":"Delaware","FL":"Florida","GA":"Georgia","HI":"Hawaii","ID":"Idaho","IL":"Illinois","IN":"Indiana","IA":"Iowa","KS":"Kansas","KY":"Kentucky","LA":"Louisiana","ME":"Maine","MD":"Maryland","MA":"Massachusetts","MI":"Michigan","MN":"Minnesota","MS":"Mississippi","MO":"Missouri","MT":"Montana","NE":"Nebraska","NV":"Nevada","NH":"New Hampshire","NJ":"New Jersey","NM":"New Mexico","NY":"New York","NC":"North Carolina","ND":"North Dakota","OH":"Ohio","OK":"Oklahoma","OR":"Oregon","PA":"Pennsylvania","RI":"Rhode Island","SC":"South Carolina","SD":"South Dakota","TN":"Tennessee","TX":"Texas","UT":"Utah","VT":"Vermont","VA":"Virginia","WA":"Washington","WV":"West Virginia","WI":"Wisconsin","WY":"Wyoming"}

# ************************************************* 1 *************************************************
# create a list with the full name of every state
dictlist=[]

#1os tropos --classic
#for key,value in states.items():
#    dictlist.append(value)

#2os tropos --etoimi entoli
#dictlist=states.values()

#3os tropos -- list coprehension
#dictlist= [v for k,v in states.items()]

#4os tropos -- lambda
dictlist = map(lambda v: v[1], states.items())

print(dictlist)
# ************************************************* 2 *************************************************
# create a list with the lower case of the states abbreviations
low=[]
low=map(lambda x:x.lower(),abbr)
print(low)

# ************************************************* 3 *************************************************
# create a list with the full names of the states that their name ends with 'a'
result = [x for x in dictlist if x.endswith('a')]
print(result)

# ************************************************* 4 *************************************************
# create a list of dictionaries for every state eg. [{"AL":"Alabama"}, {"AK":"Alaska"}, ...]
res = [dict(zip(states, i)) for i in zip(states.values())] 
print(res)
### NOTE: USE ONLY LIST COPREHENSIONS OR LAMBDA FUNCTIONS!!!