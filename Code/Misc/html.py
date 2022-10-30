# Neccessary Imports
import urllib.request 
import re

website_log = open("website_log.txt","w") # Opens/Creates file to log html of website to, for debugging purposes

# Intro
print("")
print("")
print("--------------------------")
print("Welcome to this website keyword scrapper thingy i don't know what to call this")
print("--------------------------")
print("")

while True: # Try & Catch(s) for URL Input
    try:   
        url = input("Enter a URL: ")
        print("")

        print("[Debug] URL before filtering:", url)
        print("")

        # Adds a 'https:// or http:// to the url if it doesn't have one already
        if 'https://' in url:
            print("\'https://\' found in URL, passing")
        elif 'http://' in url:
            print("\'http://\' found in URL, passing")
        else:
            print("No http found in URL, amending URL")
            url = 'https://' + url

        # Adds a 'www.' to the url if it doesn't have one already
        if 'https://www.' in url:
            print("Found Mid Level Domain in URL, passing")
            print("")
        else:
            print("No Mid Level Domain found in URL, amending URL")
            print("")
            url = url.replace("://", "://www.")

        # Counts the number of dots in the url
        dot = "\."
        tld = re.findall(dot, url)
        print("[Debug] list 'tld' is now:", tld)
        
        try: # Try & Catch for checking if the url has a top level domain
            x = tld[1] # Uses tld (list) to check the number of dots, if this fails, the url only has 1 or no dots, meaning that there is no top level domain in the url
            print("")
            print("[Debug] Passed try at line 46")
            print("")
        except IndexError:
            print("[Debug] cannot find tld[1] in URL")
            url += ".com" # Adds a '.com' to the url just to see if it works

        try:
            test_page = urllib.request.urlopen(url) # Tests the url with '.com'
        except urllib.error.URLError:
            url = url.replace(".com", "") # Get rid of the '.com' added earlier
            while True:
                try: # Try & Catch for testing if inputted value works with the URL 
                    print("")
                    print("[URL Error] No top level domain found in URL")
                    print("")
                    print("--------------------------")
                    print("")
                    new_url = input("Please enter a top level domain (e.g. '.com', '.co.uk'): ")
                    print("")
                    url_a = url + new_url # Storing url as a seperate value (url_a) so it doesn't change the main url until it knows its correct
                    test_page = urllib.request.urlopen(url_a) # Tests the url with the inputted value (url_a)
                    url = url_a
                    break
                except urllib.error.URLError:
                    if 'discord' in url or 'twitch' in url: # Not needed in most cases, but in school, adding this stop an infinite loop of an inaccessible website
                        url = url_a
                        break
                    else:
                        print("Couldn't connect to the website, please try agian with a different top level domain")
                except:
                    print("ot oh big bad error occurred")

        print("")        
        print("[Debug] URL after filtering:", url)
        print("[Debug] list 'tld' is now:", tld)

        print("")
        print("Querying website...")

        fp = urllib.request.urlopen(url) # Query the website and get the raw html
        break
        
    except ValueError: # Simple check to make sure it's not just a number or injection
        print("That is not a valid URL! Please try again")

    except urllib.error.URLError: # This checks if the URL can be accessed before trying to access it
        print("")
        print("[URL ERROR]")
        print("Website failed to respond, this is most likley the school network blocking the website")
        print("Examples of these websites are: https://www.discord.com, https://twitch.tv")
        print("Please try again with a different URL")
        print("")
    
mybytes = fp.read() # Assigns 'mybytes' to the string of 'fp'

try: 
    # Try & Catch for utf8 decoding process, sometimes the decode will fail because utf8 doesn't support some characters e.g emojis
    mystr = mybytes.decode("utf8")
except UnicodeEncodeError:
    print("")
    print("Unable to decode website, this most likley means that the website you queried has emojis etc..")
    print("File may be a bit messy due to the non-decoded format")
    print("")
    mystr = mybytes


print("Website data retrived!")
print("")
print("Writing html to file...")

# Writing the html (decoded or not) to a file
# This was previously used for debugging purposes but it is no longer neccessary
# Might be useful for a feature in the future

furl = "Website: " + url
website_log.write("-----------------------------------------\n")
website_log.write(furl)
website_log.write("\n[Dev] RAW HTML:\n")
website_log.write("-----------------------------------------\n\n")
try: # Same Try & Catch with decoding, only this for the text file
    website_log.write(mystr)
    website_log.write("\n\n-----------------------------------------\n")
    website_log.write("**EOF**")
    website_log.close()
    print("Write complete!")
except UnicodeEncodeError:
    print("[UNICODE ERROR]")
    print("Unable to decode website, this most likley means that the website you queried has emojis etc..")
    website_log.write("Unable to decode website :c")
    website_log.write("\n\n-----------------------------------------\n")
    website_log.write("**EOF**")
    website_log.close()
    print("Write complete! - File will be emtpy due encoding error")

print("")

keyword = input("Enter the keyword you would like to find: ") # The main purpose of the program, to find keywords in a webpage

m = re.findall(keyword.lower(), mystr) # Simple regex function to find all strings matching keyword in mystr
print(m)
print("Found", len(m) , "instances of '" + keyword + "' in string '" + "[mystr]" + "'")

fp.close()