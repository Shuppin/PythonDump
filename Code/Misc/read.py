import collections
import re

def loadwords_re(s):
    return (re.sub(r"[^a-z']", " ", s.lower())
            .split())

sourcefile_words = loadwords_re("""this is a sentence. This is another sentence.
Let's write many sentences here.
Here comes another sentence.
And another one.
In English, we use plenty of "a" and "the". A whole lot, actually.
""")

wordcount_all = collections.Counter(sourcefile_words)

# Lookup word counts like this (Counter is a dictionary)
count_this = wordcount_all["this"] # returns 2
print(count_this)