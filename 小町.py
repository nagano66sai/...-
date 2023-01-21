import  itertools
#class As:  
    
cnt=0
a=["/","-","*","+","" ]
b=["1","2","3","4","5","6","7","8","9"]
 # for   n  in   itertools.permutations(b,9):
for   m  in   itertools.product(a,repeat=8):


                                                
                              ss=b[0]+m[0]+b[1]+m[1]+b[2]+m[2]+b[3]+m[3]+b[4]+m[4]+b[5]+m[5]+b[6]+m[6]+b[7]+m[7]+b[8]      
                                                
                              sss=eval(ss)
                              if  sss==100  :
                                   cnt=cnt+1
                                   print   ( ss + "=100")          
                           

print  (  cnt)

                                              
#x=As()
