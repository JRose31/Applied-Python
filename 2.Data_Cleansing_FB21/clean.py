import pandas as pd
import math

file = 'G2_EDL.xlsx'

df = pd.read_excel(file)

#create function to split values by character (built in split function splits by space)
def split(word):
    return [char for char in word]


#specify which attributes should only hold integers
int_only = ["Qty", "Length (in)", "Width (in)", "Height (in)", "Weight (lb)"]

for i in int_only:
    index = 0 #used for manual reference based on terminal print output @ line 23
    for dim in df[i]:
        #try to convert instance into integer, if not we'll extract the integer from it
        try:
            int(dim)
        except:
            print(f"{dim}: Not a string @ index {index}") #used as a manual reference
            
            #if there is an integer in the instance, we'll grab it using list comprehension
            try:
                nums = [int(digit) for digit in split(dim) if digit.isdigit()]
                print(nums)
                
                #initialize empty string
                num2str = ""
                
                #add every element of the list as a string to the empty string
                for num in nums:
                    num2str += str(num)               
                print(num2str)
                
                #replace non-int value with converted integer value
                df[i] = df[i].replace([dim], int(num2str))
            except:
                pass

        index += 1

df.to_excel("revised_G2_EDL.xlsx")
        
           