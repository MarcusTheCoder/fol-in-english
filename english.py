
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

class Word(string):
    """
    Represents a single english word
    """
    'Inherits string version of __init__
    self.isPunct = False
    
    def isPunct(self):
        self.isPunct = !isalnum(self)
        return !isalnum(self) 

class Verb(Word):
    """
    Represents a Verb in the English Language
    """

class Punctuation:
    period="."
    question="?"
    exclaim="!"
    comma=","
    semicolon=";"
    colon=":"
    

class SentanceTypes:
    declaration=0
    imperative=1
    interrogative=2
    exclamation=3

class Sentance(object):
    """
    Represents a string of words which are structured
    in a specific way to declare something, dictate a command, ask a question,
    or exclaim something.
   
    """

    def __init__(self,rawtext = ""):
        self.rawtext = rawtext
        self.words = []
        self.punct = []
        self.indepClauses = [] 'Can act as their own sentances'

    '''
    Returns a list of tuples which stores the index and the punctuation mark 
    '''
    def __determinePunctuation(self):
        puncts = []
        for part in self.parts:
          pass
        return puncts

    '''
    Returns a list of tuples of words and the index in order of occurence. Does not include punctuation
    '''
    def __determineWords(self):
        pass

class AnalyzedSentance(Sentance):
    """
    Represents a sentance which upon construction has words broken
    down by part of speech, as well as determining independent and dependent clauses
    Uses a dictionary to determine the parts of speech for words and to perform analysis
    on the sentance structure
    """

    def __init__(self,rawtext="",dictionary="",grammarbook=""):
        Sentance.__init__(self,rawtext)
        self.words = __determineClassifiedWords()
        self.sentanceType = 
    '''
    Makes analysis of sentance to find commas and conjunctions which do not represent 
    collections gathering in order to find parts of this sentance which themselves
    could be considered sentances
    ex. "I am a witch, but are you a witch?"
        I am a witch. (declaration) are you a witch? (question)
    '''
    def __determineIndependentClauses(self):
        pass
    '''
    Returns a list of tuples (word,index of occurence) where each word is classified
    into parts of speech (word will be one of the childclasses of "Word")
    '''
    def __determineClassifiedWords(self):
        pass

    '''
    Returns the type of sentance. Will either be DECLARATION
    '''
    def __determineSentanceType(self):
        pass

    

