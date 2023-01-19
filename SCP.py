import json
from datetime import date
today = date.today()
d4 = today.strftime("%b-%d-%Y")
d5 = d4.split("-")
current_month = (d5[0]+"'"+d5[2][2:4])
# print(current_month)

d = ["Mar'21", "Apr'21", "Mar'21", "Feb'21", "Apr'21", "Feb'21", "Mar'21", "Feb'21", "Apr'21", "Jan'21", "Jan'21", "Dec'20", "Jun'21", "Feb'21", "Mar'21", "Jun'21", "Apr'21", "Nov'20", "Jun'20", "Mar'21", "Feb'21", "Jan'21", "Dec'20", "Nov'20", "Feb'21", "Nov'20", "Apr'21", "Jan'21", "Apr'21", "Sep'20", "Mar'21", "Apr'20", "Apr'21", "Apr'21", "Dec'20", "Sep'20", "Feb'21", "Oct'20", "Aug'20", "Oct'20", "May'21", "Feb'20", "Jun'21", "Nov'20", "Oct'20", "May'21", "Jan'21", "Apr'21", "Oct'20", "Dec'20", "Jun'20", "Mar'21", "Nov'20", "Oct'20", "May'21", "Jun'21", "Feb'21", "Jul'20", "Jun'20", "Jun'21", "Oct'20", "Jan'21", "Mar'21", "Sep'20", "Jun'20", "Apr'21", "Dec'20", "Jul'20", "May'20", "Jun'20", "Apr'21", "Feb'21", "Nov'20", "Aug'20", "May'20", "Mar'21", "Jun'20", "Apr'21", "Mar'20", "Aug'20", "Feb'21", "Jun'20", "Apr'21", "Mar'20", "May'20", "Sep'20", "Apr'21", "Apr'21", "Apr'21"]                                                                                                                                                                                                 
result = dict((i, d.count(i)) for i in d)
print(result)

home=63
cummulative = 81

for x, y in result.items(): 
    if  x == "Feb'20" or x == "Mar'20" or "Apr'20" or "May'20" or "Jun'20":
        home1 = 9
for x, y in result.items():        
    if  x == "Jul'20" or x == "Aug'20":
        home2 = 18
for x, y in result.items():        
    if  x == "Sep'20" or x == "Oct'20" or "Nov'20" or "Dec'20" or "Jan'21":
        home3 = 27 
for x, y in result.items():        
    if  x == "Feb'21" or x == "Mar'21":
        home4 = 36
home5 = 63

test_flag = 0

for x, y in result.items():    
    if x == "Feb'20" and test_flag == 0: 
        if x != current_month:
            test_flag = 1
            cummulative = y
            with open('C:\\Users\\general\\Desktop\\effectivenessdata.json', "w+") as fh:
                fh.write("[\n")
                fh.write("{\"Month\":%a,\"QuantityOfHomes\":\"%d\",\"BugsPerMonth\":\"%d\",\"CumulativeBugs\":\"%d\"}"%(x,home1,y,cummulative))  
                fh.write(",\n")      
for x, y in result.items():    
    if x == "Mar'20" and test_flag == 1: 
        if x != current_month:
            test_flag = 1  
        cummulative1 = y+cummulative       
        fh.write("{\"Month\":%a,\"QuantityOfHomes\":\"%d\",\"BugsPerMonth\":\"%d\",\"CumulativeBugs\":\"%d\"}"%(x,home1,y,cummulative1))  
        fh.write(",\n")      
for x, y in result.items():    
    if x == "Apr'20" and test_flag == 1: 
        if x != current_month:
            test_flag = 1    
        cummulative2 = y+cummulative1     
        fh.write("{\"Month\":%a,\"QuantityOfHomes\":\"%d\",\"BugsPerMonth\":\"%d\",\"CumulativeBugs\":\"%d\"}"%(x,home1,y,cummulative2))  
        fh.write(",\n")      
for x, y in result.items():    
    if x == "May'20" and test_flag == 1: 
        if x != current_month:
            test_flag = 1      
        cummulative3 = y+cummulative2    
        fh.write("{\"Month\":%a,\"QuantityOfHomes\":\"%d\",\"BugsPerMonth\":\"%d\",\"CumulativeBugs\":\"%d\"}"%(x,home1,y,cummulative3))  
        fh.write(",\n") 
for x, y in result.items():    
    if x == "Jun'20" and test_flag == 1: 
        if x != current_month:
            test_flag = 1      
        cummulative4 = y+cummulative3    
        fh.write("{\"Month\":%a,\"QuantityOfHomes\":\"%d\",\"BugsPerMonth\":\"%d\",\"CumulativeBugs\":\"%d\"}"%(x,home1,y,cummulative4))  
        fh.write(",\n") 
for x, y in result.items():    
    if x == "Jul'20" and test_flag == 1: 
        if x != current_month:
            test_flag = 1      
        cummulative5 = y+cummulative4    
        fh.write("{\"Month\":%a,\"QuantityOfHomes\":\"%d\",\"BugsPerMonth\":\"%d\",\"CumulativeBugs\":\"%d\"}"%(x,home2,y,cummulative5))  
        fh.write(",\n") 
for x, y in result.items():    
    if x == "Aug'20" and test_flag == 1: 
        if x != current_month:
            test_flag = 1      
        cummulative6 = y+cummulative5    
        fh.write("{\"Month\":%a,\"QuantityOfHomes\":\"%d\",\"BugsPerMonth\":\"%d\",\"CumulativeBugs\":\"%d\"}"%(x,home2,y,cummulative6))  
        fh.write(",\n") 
for x, y in result.items():    
    if x == "Sep'20" and test_flag == 1: 
        if x != current_month:
            test_flag = 1      
        cummulative7 = y+cummulative6    
        fh.write("{\"Month\":%a,\"QuantityOfHomes\":\"%d\",\"BugsPerMonth\":\"%d\",\"CumulativeBugs\":\"%d\"}"%(x,home3,y,cummulative7))  
        fh.write(",\n") 
for x, y in result.items():    
    if x == "Oct'20" and test_flag == 1: 
        if x != current_month:
            test_flag = 1      
        cummulative8 = y+cummulative7    
        fh.write("{\"Month\":%a,\"QuantityOfHomes\":\"%d\",\"BugsPerMonth\":\"%d\",\"CumulativeBugs\":\"%d\"}"%(x,home3,y,cummulative8))  
        fh.write(",\n") 
for x, y in result.items():    
    if x == "Nov'20" and test_flag == 1: 
        if x != current_month:
            test_flag = 1      
        cummulative9 = y+cummulative8    
        fh.write("{\"Month\":%a,\"QuantityOfHomes\":\"%d\",\"BugsPerMonth\":\"%d\",\"CumulativeBugs\":\"%d\"}"%(x,home3,y,cummulative9))  
        fh.write(",\n") 
for x, y in result.items():    
    if x == "Dec'20" and test_flag == 1: 
        if x != current_month:
            test_flag = 1      
        cummulative10 = y+cummulative9    
        fh.write("{\"Month\":%a,\"QuantityOfHomes\":\"%d\",\"BugsPerMonth\":\"%d\",\"CumulativeBugs\":\"%d\"}"%(x,home3,y,cummulative10))  
        fh.write(",\n") 
for x, y in result.items():    
    if x == "Jan'21" and test_flag == 1: 
        if x != current_month:
            test_flag = 1      
        cummulative11 = y+cummulative10    
        fh.write("{\"Month\":%a,\"QuantityOfHomes\":\"%d\",\"BugsPerMonth\":\"%d\",\"CumulativeBugs\":\"%d\"}"%(x,home3,y,cummulative11))  
        fh.write(",\n") 
for x, y in result.items():    
    if x == "Feb'21" and test_flag == 1: 
        if x != current_month:
            test_flag = 1      
        cummulative12 = y+cummulative11    
        fh.write("{\"Month\":%a,\"QuantityOfHomes\":\"%d\",\"BugsPerMonth\":\"%d\",\"CumulativeBugs\":\"%d\"}"%(x,home4,y,cummulative12))  
        fh.write(",\n") 
for x, y in result.items():    
    if x == "Mar'21" and test_flag == 1: 
        if x != current_month:
            test_flag = 1      
        cummulative13 = y+cummulative12    
        fh.write("{\"Month\":%a,\"QuantityOfHomes\":\"%d\",\"BugsPerMonth\":\"%d\",\"CumulativeBugs\":\"%d\"}"%(x,home4,y,cummulative13))  
        fh.write(",\n") 
for x, y in result.items():    
    if x == "Apr'21" and test_flag == 1: 
        if x != current_month:
            test_flag = 1      
        cummulative14 = y+cummulative13    
        fh.write("{\"Month\":%a,\"QuantityOfHomes\":\"%d\",\"BugsPerMonth\":\"%d\",\"CumulativeBugs\":\"%d\"}"%(x,home,y,cummulative14))  
        fh.write(",\n") 
for x, y in result.items():    
    if x == "May'21" and test_flag == 1: 
        if x != current_month:
            test_flag = 1      
        cummulative15 = y+cummulative14    
        fh.write("{\"Month\":%a,\"QuantityOfHomes\":\"%d\",\"BugsPerMonth\":\"%d\",\"CumulativeBugs\":\"%d\"}"%(x,home,y,cummulative15))           
for x, y in result.items():    
    if x == "Jun'21" and test_flag == 1: 
        if x != current_month:
            test_flag = 1      
        cummulative16 = y+cummulative15 
        fh.write(",\n")   
        fh.write("{\"Month\":%a,\"QuantityOfHomes\":\"%d\",\"BugsPerMonth\":\"%d\",\"CumulativeBugs\":\"%d\"}"%(x,home,y,cummulative16))                                                                                                                                                                                  
for x, y in result.items():    
    if x == "Jul'21" and test_flag == 1: 
        if x != current_month:
            test_flag = 1      
        cummulative16 = y+cummulative15 
        fh.write(",\n")   
        fh.write("{\"Month\":%a,\"QuantityOfHomes\":\"%d\",\"BugsPerMonth\":\"%d\",\"CumulativeBugs\":\"%d\"}"%(x,home,y,cummulative16))                                                                                                                                                                                  
for x, y in result.items():    
    if x == "Aug'21" and test_flag == 1: 
        if x != current_month:
            test_flag = 1      
        cummulative16 = y+cummulative15 
        fh.write(",\n")   
        fh.write("{\"Month\":%a,\"QuantityOfHomes\":\"%d\",\"BugsPerMonth\":\"%d\",\"CumulativeBugs\":\"%d\"}"%(x,home,y,cummulative16))                                                                                                                                                                                  
for x, y in result.items():    
    if x == "Sep'21" and test_flag == 1: 
        if x != current_month:
            test_flag = 1      
        cummulative16 = y+cummulative15 
        fh.write(",\n")   
        fh.write("{\"Month\":%a,\"QuantityOfHomes\":\"%d\",\"BugsPerMonth\":\"%d\",\"CumulativeBugs\":\"%d\"}"%(x,home,y,cummulative16))                                                                                                                                                                                  
for x, y in result.items():    
    if x == "Nov'21" and test_flag == 1: 
        if x != current_month:
            test_flag = 1      
        cummulative16 = y+cummulative15 
        fh.write(",\n")   
        fh.write("{\"Month\":%a,\"QuantityOfHomes\":\"%d\",\"BugsPerMonth\":\"%d\",\"CumulativeBugs\":\"%d\"}"%(x,home,y,cummulative16))                                                                                                                                                                                  
for x, y in result.items():    
    if x == "Dec'21" and test_flag == 1: 
        if x != current_month:
            test_flag = 1      
        cummulative16 = y+cummulative15 
        fh.write(",\n")   
        fh.write("{\"Month\":%a,\"QuantityOfHomes\":\"%d\",\"BugsPerMonth\":\"%d\",\"CumulativeBugs\":\"%d\"}"%(x,home,y,cummulative16))                                                                                                                                                                                                                                  
             
fh.write("\n]")   
