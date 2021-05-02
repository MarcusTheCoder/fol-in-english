
"""
English is a language which evolved from other germanic languages in northwestern europe
It has rules (grammar) which dictate what words do and how they behave or express
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
"""
from typing import Text


class SentanceTypes:
    DECLARATION=0
    IMPERATIVE=1
    INTERROGATIVE=2
    EXCLAMATION=3

class Punctuation:
    """
    Punctuation Marks

    . period : Indicates a declaration or imperative
        -- (Since we are not evaluating Interjections, )
    ? query  : Denotes a question
        -- In our case this could mean a goal we are trying to prove
        -- or the head of a subproof we want to prove
    ! exclaim: Denotes an exclamation or (for our program) imperative
    """
    PERIOD="."
    QUESTION="?"
    EXCLAIM="!"
    COMMA=","
    SEMICOLON=";"
    COLON=":"
    PUNCTUATION_LIST = [".","?","!",",",";",":"]

def numPuncExist(text):
    """
    Returns total count of punctuation in a given bit of text
    """
    totalC = 0
    for ele in Punctuation.PUNCTUATION_LIST:
        totalC += text.count(ele)           
    return totalC


class PartsOfSpeech:
    """
    8 Parts of Speech

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


    """
    UNKNOWN = -1
    NOUN=0
    VERB=1
    PRONOUN=2
    ADJECTIVE=3
    ADVERB=4
    PREPOSITION=5
    CONJUNCTION=6
    INTERJECTION=7

class Word(object):
    """
    Represents a single english word
    """
    'Inherits string version of __init__'
    def __init__(self,txt,partOfSpeech=-1):
        self.txt = txt
        self.partOfSpeech = partOfSpeech

    
    def isPunct(self):        
        return not self.txt.isalnum()

    def __str__(self) -> str:
        return self.txt
    def length(self):
        return len(self.txt)

#-------------------------------------------
# PARTS OF SPEECH CLASSES
#
class Verb(Word):
    def __init__(self, txt):
        super().__init__(txt, pos=PartsOfSpeech.VERB)
class Noun(Word):
    def __init__(self, txt):
        super().__init__(txt, pos=PartsOfSpeech.NOUN)
class Pronoun(Word):
    def __init(self,txt):
        super().__init__(txt,pos=PartsOfSpeech.PRONOUN)
class Adjective(Word):
    def __init(self,txt):
        super().__init__(txt,pos=PartsOfSpeech.ADJECTIVE)
class Adverb(Word):
    def __init(self,txt):
        super().__init__(txt,pos=PartsOfSpeech.ADVERB)

class Preposition(Word):
    def __init(self,txt):
        super().__init__(txt,pos=PartsOfSpeech.PREPOSITION) 

class Conjunction(Word):
    def __init(self,txt):
        super().__init__(txt,pos=PartsOfSpeech.CONJUNCTION)

#---------------------------------------------------------------
# SENTANCE CLASSES
#

class Sentance(object):
    """
    Represents a string of words which are structured
    in a specific way to declare something, dictate a command, ask a question,
    or exclaim something.
   
    """

    def __init__(self,rawtext = ""):
        self.rawtext = rawtext        
        self.elements = self.__determineSeparatedComponents() # Contains both words and non words (punctuation)
        self.words = [] # list with tuples of format (int (index of occurence),Word)
        self.punct = [] # list with tuples of format (int (index of occurence),str (punct))
        
        'Can act as their own sentances'
        
    def __determineElements(self):
        # First, separate based on commas and other punctuation
        components = []
        components = self.rawtext.split(' ')
        for c in components:
            # Break up further by punctuation
            numP = numPuncExist(c)
            if numP > 0:
                # We must handle punctuation
                if numP > 1:
                    # This text chunk has invalid spacing!
                    print("error: __determineElements(): Sentance specified has invalid spacing!")
                    return []
                else:
                    if numPuncExist(c[len(c) - 1]) != 1:
                        # Punctuation occurs at begining!
                        print("error: __determineElements(): Sentance specified has invalid punctuation locations!")
                        return []
                    else:
                        # Punctuation is at the back
                        theWord = c[0:len(c) - 1]
                        punct = c[len(c) - 1]
                        components.append(Word(theWord))
                        components.append(punct)
            else:
                # No punctuation parsing required
                components.append(Word(c))
        
        return components
    
    def __determinePunctuation(self):
        """
        Returns a list of tuples which 
        stores the index and the punctuation mark 
        """
        puncts = []
        for i in range(0,len(self.elements)):
            ele = self.elements[i]
            if ele is not Word:
                puncts.append((i,ele))
        return puncts

    
    def __determineWords(self):
        """
        Returns a list of tuples of words and the
        index in order of occurence. Does not include punctuation
        """
        words = []
        for i in range(0,len(self.elements)):
            ele = self.elements[i]
            if ele is Word:
                words.append((i,ele))
        return words
        

    def isValid(self):
        """
        Returns whether this sentance obeys the basic rules of english Sentances
        (is the first word capitalized, are there any odd formats? is there a period or other terminator)
        """
        validity = True
        validity = validity and len(self.elements) > 0 # There are at least some words
        validity = validity and self.elements[0] is Word # The first element is a word
        validity = validity and Word(self.elements[0]).txt[0].isupper() # The first Word is capitalized
        validity = validity and numPuncExist(self.elements[len(self.elements) - 1]) == 1 # The sentance ends with punctuation

        return validity

class AnalyzedSentance(Sentance):
    """
    Represents a sentance which upon construction has words broken
    down by part of speech, as well as determining independent and dependent clauses
    Uses a dictionary to determine the parts of speech for words and to perform analysis
    on the sentance structure
    """

    def __init__(self,rawtext="",dictionary="",grammarbook=""):
        '''Construct an AnalyzedSentance object'''
        Sentance.__init__(self,rawtext)
        self.words = __determineClassifiedWords()
        self.sentanceType = SentanceTypes.DECLARATION
        self.indepClauses = []
    
    def __determineIndependentClauses(self):
        """
        Makes analysis of sentance to find commas and conjunctions which do not represent 
        collections gathering in order to find parts of this sentance which themselves
        could be considered sentances
        ex. "I am a witch, but are you a witch?"
            I am a witch. (declaration) are you a witch? (question)
        """
        pass
    
    def __determineClassifiedWords(self):
        """
        Returns a list of tuples (word,index of occurence) where each word is classified
        into parts of speech (word will be one of the childclasses of "Word")
        """
        rtrn = []
        return rtrn

    
    def __determineSentanceType(self):
        """
        Returns the type of sentance. Will either be DECLARATION
        """
        pass

    def __classifyWord(self,word):
        """
        Will classify a word using the dictionary specified in the constructor
        """
        pass

 #
 #  MODULE METHODS
 #    

class DictionaryFileFormats:
    TXT=0
    JSON=1 # Not supported yet
    CSV=2 # Not supported yet

def loadWordDictionary(filePath,format=DictionaryFileFormats.TXT):
    """
    Returns a dictionary which establishes words to parts of speech
    """ 
    d = {}
    if format is DictionaryFileFormats.TXT:
        df = open(filePath,"r")
        currentMode = PartsOfSpeech.NOUN
        for x in df:
            if x.startswith("//"):
                # This line is a comment
                continue
            if x[0].isnumeric():
                currentMode = int(x)
                continue
            if not x[0].isalpha():
                #Not valid word
                continue
            # -----------------------------------
            d[x.strip()] = currentMode           
        # Once done in the for loop, close
        df.close()

    return d



  

