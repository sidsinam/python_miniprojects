import os
import re

regex = re.compile('[^a-zA-Z]')
path = "./text"
os.chdir(path)
files = os.listdir(".")
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                      "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
                      "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this",
                      "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has",
                      "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or",
                      "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between",
                      "into", "throough", "during", "before", "after", "above", "below", "to", "from", "up", "down",
                      "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there",
                      "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other",
                      "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t",
                      "can", "will", "just", "don", "should", "now"]
d = dict()
print(files)
for file in files:
    if os.path.isfile(file):
        print(file, " is a file")
        f = open(file, "r")
        s = f.read()
        t = s.split()
        for word in t:
            word = word.lower()
            word = re.sub(regex, '', word)
            if word not in stop_words:
                if len(word) == 0:
                    continue
                if word in d:
                    d[word] += 1
                else:
                    d[word] = 1

d = sorted(d.items(), key=lambda item: item[1], reverse=True)
print(d)
for i in range(20):
    print(d[i])