'''
English is a language which evolved from other germanic languages in northwestern europe
It has rules called grammar which dictate what words do and how they behave or express
information in sentances

A sentance is a collection of words begining with a capital letter,
 ending in a punctuation mark.

A sentance may not be made up solely of prepositions, conjunctions
A sentance must include some noun or verb being used 
    ex. I am running
        (subject) I (adjective) am (verb) running.   -- This is a declaration (statement)
    ex. Pick up the dishes.    
        (verb) Pick (adverb) up (conjunction) the (noun) dishes. -- This is an imperative sentance (command)
    ex. Are we alone?
        (verb) Are (pronoun) we (verb) alone?    -- This is an Interrrogative sentance (question)   
    ex. Ouch! -- This is an exclamative (exclamation)
        -- (we probably do not need to implement exclamative sentances,
            so we can say a '!' denotes an imperative)
'''
'''
Punctuation Marks

. period : Indicates a declaration or imperative
    -- (Since we are not evaluating Interjections, )
? query  : Denotes a question
    -- In our case this could mean a goal we are trying to prove
    -- or the head of a subproof we want to prove
! exclaim: Denotes an exclamation or (for our program) imperative
'''

'''
9 Parts of Speech

-- Main words --
Verb : action or state of being
Noun: person, place, or thing
Pronoun: Word used in place of a noun

-- modifiers/descriptors--
Adjective: modifies or describes a noun or pronoun
Adverb: modifies or describes a verb

-- other --
Preposition: word placed before noun/pronoun to
 form phrase without modifying another word in sentance

Conjunction: joins words, phrases, clauses,

Interjection: Word used to express emotion
    (most likely we do not need to use this type of word)


'''

class Word(object):
    """
    Represents a single english word
    """
    pass

class Sentance(object):
    """
    Represents a string of words which are structured
    in a specific way to declare something, dictate a command, ask a question,
    or exclaim something
    """
    pass

