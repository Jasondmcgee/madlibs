
propernouns = []
adjectives = []
verbs = []
word = str()


def propernoun(word):
    word = raw_input("enter a proper noun: ")
    propernouns.append(word)


propernoun(word)
propernoun(word)

print("this morning I went to " + propernouns[0] + "'s" + " house with my friend " + propernouns[1] + ".")
