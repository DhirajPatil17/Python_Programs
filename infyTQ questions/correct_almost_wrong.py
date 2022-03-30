

def find_correct(word_dict):
    tup=""
    #start writing your code here
    for key,value in word_dict.items():
        for index in key:
            if index in key==index in value: 
                tup=tup+index
            
    return tup


word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))
dict={"THEIR": "THEIR", "BUSINESS": "BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
count=0
correct=0
wrong=0
almost=0

for key,values in dict.items():
    if key==values:
        correct+=1
    
    elif len(key)==len(values):
        for i in range(0,len(values)):
            if key[i]!=values[i]:
                count+=1
        if count<=2:
            almost+=1
        else:
            wrong+=1
    else:
        wrong+=1 
list=[correct,almost,wrong]
print(list)  
            



                
                  
                    

        

    
