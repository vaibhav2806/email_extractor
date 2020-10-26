#email collector

import re 

str ='''
When you go to a website and click on the contact section, by pressing CTRL+A,<verma88lko@gmail.com>
all the content of the website gets added to the clipboard. 
Paste the data in your python file or in a string. 
Extract an email from the above data, (alpha1vaibhav@gmail.com) and after extracting email, write it into a file with a new line character. 
Your text file after writing data should look similar to this:
abc123@gmail.com

cdf456@gmail.com
'''
i = 1
patt = re.compile(r'[a-zA-Z0-9._]+@+[a-zA-Z]+\.+[a-zA-Z]+')
matches = patt.finditer(str)
with open ("all_emails.txt" , "w") as f:
    for match in matches:
        f.write(f"email {i} : {match.group()}\n")
        i += 1