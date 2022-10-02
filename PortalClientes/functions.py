def is_user_valid(user):   

        upper, lower, count = 0, 0, 0

        if (len(user) >= 6):

          for i in user:

              if (i.islower()):
                  lower+=1            
    
              if (i.isupper()):
                  upper+=1            
    
              if (i.isnumeric()):
                  count+=1                
          
        if (upper>=1 and lower >=1 and count>=1 and lower+upper+count == len(user)):
           return True
        else:
           return False   

def is_password_valid(password):  
     upper, lower, count = 0, 0, 0  
     if (len(password) >= 8):  
       for i in password:  
           if (i.islower()):
               lower+=1            
 
           if (i.isupper()):
               upper+=1            
 
           if (i.isnumeric()):
               count+=1                
       
     if (upper>=1 and lower >=1 and count>=3 and lower+upper+count==len(password)):
        return True
     else:
        return False