
'''
Thoughts

PREREQ DECLARATION (All proper nouns are human) (yes/no)
PREREQ DECLARATION (All nouns can take actions) (yes/no)


Alice drank the red drink.

Alice (human)
    (action) drank (past tense of drink)
    

Drink
    (quality) red

The red drink drank Alice
Drink
    (quality) red
    (action) drank


Rules

-- Proper Nouns --
All proper nounds are capitalized.
Not all capitalized words are proper nouns.

--Sentance Rules--
Begining of sentances start with a capitalized word
All sentances end with periods.

Diagram breakdown for sentances:
Legend:
    () = Keyword
    [x] = Variable
    [collection] = Collection variable

A sentance can be translated into a single line of FOL
    Sentance parts can be broken down into smaller pieces of FOL

    (For all) [x] and [y] in [collection],
    (For all) [x],[y], and [z] in [collection],
    (For all) = (For every)

    (There exists) a(n)[x] 
    (In) [collection], (There exists)
    -- the comma separates pieces of the FOL statement, initialized collections, and in general, provides pauses --

    (In) our [collection:universe], (there exists) (a) [tree].
    -- English Quantifiers
    -- a/an specifies one
    -- many specifies multiple objects



-- Quantifier Rules --
Only collections can be evaluated by quantifiers


'''

if __name__ == "__main__":
    print("Hi")