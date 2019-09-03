
propernouns = []
nouns = []
pluralnouns = []
adjectives = []
verbs = []
places = []
numbers = []
bodyparts = []
word = str()


def propernoun(word):
    word = input("enter a proper noun: ")
    word = str(word)
    propernouns.append(word)


def pluarlnoun(word):
    word = input("enter a noun (pluarl): ")
    word = str(word)
    pluralnouns.append(word)


def noun(word):
    word = input("enter a noun: ")
    word = str(word)
    nouns.append(word)


def verb(word):
    word = input("enter a verb: ")
    word = str(word)
    verbs.append(word)


def place(word):
    word = input("enter a place: ")
    word = str(word)
    places.append(word)


def adjective(word):
    word = input("enter a adjective: ")
    word = str(word)
    adjectives.append(word)


def number(word):
    word = input("enter a number: ")
    word = str(word)
    numbers.append(word)


def bodypart(word):
    word = input("enter a bodypart: ")
    word = str(word)
    bodyparts.append(word)


pluarlnoun(word)
place(word)
noun(word)
pluarlnoun(word)
noun(word)
adjective(word)
verb(word)
number(word)
adjective(word)
bodypart(word)
verb(word)

#Romeo and Juliet: Prologue ad-Lib

print("Two " + pluralnouns[0] + ", both alike in dignity, In fair " + places[0] + ", where we lay our scene, From ancient" + nouns[0] + " to new mutiny, Where civil blood makes civil hands unclean. From forth the fatal loins of these two foes A pair of star-cross`d " + pluralnouns[1] + " take their life; Whole misadventured piteous overthrows Do with their" + nouns[1] + " bury their parents` strife. The fearful passage of their" + adjectives[0] + "love, And the continuance of their parents` rage, Which, but their children`s end, nought could" + verbs[0] + ", Is now the " + numbers[0] + " hours` traffic of our stage; The which if you with " + adjectives[0] + bodyparts[0] + " attend, What here shall " + verbs[1] + ", our toil shall strive to mend")
