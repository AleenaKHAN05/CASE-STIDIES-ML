#ASSIGNMENT-5
import re

#Q.1
##import re
##astring='dial:- 0755-888932,055-7999806,077-9630121'
##match=re.findall(r'\d{1,4}-(\d{0,7})',astring)
##print(match)

#Q.2
##Write a Python program which search the first occurrence of "it was good"
##and print start index and end index of the match.

##astring= "yessss,it was good"
##match=re.search(r'it was good',astring)
##print('start',match.start(),'end',match.end())

#Q.3
##Write a Python program which takes an input from the user and checks
##if the input is a valid company id . Company Id format
##INV1234 (INV followed by number which is upto 4 digit long
##astring=input('enter id')
##if re.findall(r'INV\d{4}\b',astring):
##    print('valid company id')
##else:
##    print('invalid company id')
##        
#Q.4
##a) Write a Python program which searches for the word farmer in its
##singular and plural forms and prints
##the number of matches.
##astring='farmer provides us food farmers grow different crops Farmers are the backbone of our societyfarmers live in a small house farmer are very hardworking'
##match1=re.findall(r'\bfarmer+',astring)
##match2=re.findall(r'\bfarmers+',astring)
##print(match1,'no of matches',len(match1))
##print(match2,'no of matches',len(match2))
###b:-
##match3=re.findall(r'\b[Ff]armers+',astring)
##print(match3)



#5.Write a Python program which searches in
#a text file for all the occurrences
##of an entered text and then prints
##start indices of all the matches
##file=open('test.txt')
##read=file.read()
##file.close()
##text=input('enter the text you want to search')
##for match in re.finditer(text,read):
##    print('it is at', match.start())





##6.Write a Python program which prints
#"Starts with a number " if  a given text
#starts with a Number, prints
#"Ends with a number " if a given text ends
##with a Number, prints both the messages
##if both the cases are true and prints
##"Neither starts nor ends with a number"
##if both the cases are not true.
##This number can have any number of digits.

##astring = input('enter your text:-')
##if re.match(r'\d+', astring):
##    print('starts with a number')
##elif re.search(r'\d+$', astring):
##    print('ends with a number')
##else:
##    re.search(r'\d', astring)
##    print('neither starts nor ends with a number')

##7.Write a Python program which reads a
##textfile and makes the following changes:  
##a) Removes all the special characters from
##the text.
##b) Removes all the new line characters from the text
##c) Removes all the words which have length two or less
##d) Replaces all the email Ids in the text with string -'EmailID'
##Class comments
file=open('test.txt')#reading the text file
read=file.read()
file.close()
##match=re.sub(r'[^A-Za-z0-9\s]', '',read)
##match= re.sub('\n', '',read)
##match= re.sub(r'\b\w{1,2}\b', '',read)
##print('filtered text',match)

match=re.sub(r'[\w\._%+-]{1,20}@[\w]{1,10}\.[\w]{1,10}','emailid',read)
print(match)
print(read)







































