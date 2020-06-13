from urllib.request import urlopen

shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')

shakespeare.read()