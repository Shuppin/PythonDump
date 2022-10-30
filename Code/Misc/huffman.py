import collections


text = list(input("Enter your text to be compressed: "))
freq = collections.Counter(text)
freq = dict(freq)


ordered = sorted(freq, key=freq.get, reverse=False)
print(freq, ordered)





