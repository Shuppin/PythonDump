import re

txt = "The cow goes over the moon! He was a cool cow"

keyword = input("Enter the keyword you would like to find: ")

m = re.findall(keyword.lower(), txt)
print("Found", len(m) , "instances of '" + keyword + "' in string '" + txt + "'")