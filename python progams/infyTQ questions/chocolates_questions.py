
child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

def calculate_total_chocolates():
    sum=0
    for i in chocolates_received:
        sum=sum+i
    return sum
    #Remove pass and write your logic here to find and return the total number of chocolates

def reward_child(child_id_rewarded,extra_chocolates):
    if extra_chocolates>1:
        for i in range(len(child_id)):
            if child_id[i]==child_id_rewarded:
                chocolates_received[i]=chocolates_received[i]+extra_chocolates
                print(chocolates_received)
                break
        
        if child_id_rewarded not in child_id:
            print("Child id is invalid")
    else:
        print("Extra chocolates is less than 1")
        

#Test your code by passing different values for child_id_rewarded,extra_chocolates
reward_child(20,2)



