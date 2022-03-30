def wrap(string, max_width):
   
    return"\n".join([string[i:i+max_width] for i in range(0,len(string),max_width)])
    
    
    

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
text="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
max_width=4
result = wrap(text, max_width)
print(result)
        
        
    
    
        
        
    
    
    