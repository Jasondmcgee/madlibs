
propernouns = []
nouns = []
adjectives = []
verbs = []
word = str()


def propernoun(word):
    word = input("enter a proper noun: ")
    word = str(word)
    propernouns.append(word)


def noun(word):
    word = input("enter a noun: ")
    word = str(word)
    nouns.append(word)


def verb(word):
    word = input("enter a verb: ")
    word = str(word)
    verbs.append(word)


propernoun(word)
propernoun(word)
noun(word)
verb(word)

print("this morning I went to " + propernouns[0] + "'s" + " house with my friend " + propernouns[1] + ". we played videogames on the couch until " + propernouns[1] + " mom, " + propernouns[0] + ", walked in with some " + nouns[0] + "s" + ". " + nouns[0] + " was so delecious that stopped" + verbs[0] + "ing")
