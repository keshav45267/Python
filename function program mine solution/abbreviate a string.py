# Write a Program to Abbreviate a given Phrase/String
# ex as soon as possible = asap [ this is abbreviation]

def abbreviation(phrase):
   
    #non python way    
   
    # l= len(phrase)
    # word=''
    # for i in range(l):
    #     if i==0:
    #         word+=phrase[i]
    #     elif phrase[i]==' ':
    #         word+=phrase[i+1]
    # return print(word.upper())

    # python way
    words = phrase.split() # split():- it splits the the given phrase by default 
                           #with space charachters ex as soon is split into ['as','soon']
    print("after use of split() how phrase/string will look",words)
    result = ""
    for word in words:
        result += word[0]
    return result.upper()

st= input("enter the string:")
abr= abbreviation(st)  
print(st,":",abr)    
