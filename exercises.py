
def reverse_list(l):
    """
    Reverses order of elements in list l.
    """
    return l[::-1]


def test_reverse_list():
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]


# ------------------------------------------------------------------------------

def reverse_string(s):
    """
    Reverses order of characters in string s.
    """
    return s[::-1]

def test_reverse_string():
    assert reverse_string("foobar") == "raboof"


# ------------------------------------------------------------------------------

def is_english_vowel(c):
    """
    Returns True if c is an english vowel
    and False otherwise.
    """
    cVowel=False
    if c.lower() in "aeiyuo": 
       cVowel=True
    return cVowel


def test_is_english_vowel():
    assert is_english_vowel('a')
    assert is_english_vowel('e')
    assert is_english_vowel('i')
    assert is_english_vowel('o')
    assert is_english_vowel('u')
    assert is_english_vowel('y')
    assert is_english_vowel('A')
    assert is_english_vowel('E')
    assert is_english_vowel('I')
    assert is_english_vowel('O')
    assert is_english_vowel('U')
    assert is_english_vowel('Y')
    assert not is_english_vowel('k')
    assert not is_english_vowel('z')
    assert not is_english_vowel('?')


# ------------------------------------------------------------------------------

def count_num_vowels(s):
    """
    Returns the number of vowels in a string s.
    """
    out=0
    for c in s:
      if c.lower() in "aeiuyo":
        out+=1
    return out


def test_count_num_vowels():
    sentence = "hey ho let's go"
    assert count_num_vowels(sentence) == 5
    sentence = "HEY ho let's GO"
    assert count_num_vowels(sentence) == 5
    paragraph = """She told me her name was Billie Jean,
                   as she caused a scene
                   Then every head turned with eyes
                   that dreamed of being the one
                   Who will dance on the floor in the round"""
    assert count_num_vowels(paragraph) == 54


# ------------------------------------------------------------------------------

def histogram(l):
    """
    Converts a list of integers into a simple string histogram.
    """
    out=""
    for n in list(range(len(l))):
      for m in list(range(l[n])):
        out+="#"
      if n<len(l)-1:
        out+="\n"
    return out


def test_histogram():
    assert histogram([2, 5, 1]) == '##\n#####\n#'


# ------------------------------------------------------------------------------

def get_word_lengths(s):
    """
    Returns a list of integers representing
    the word lengths in string s.
    """
    wordIndex=0
    out=[]
    for c in list(range(len(s))):
      if s[c]==" ":
        if wordIndex==0:
          out.append(c-wordIndex)
          wordIndex=c
        else:
          out.append(c-wordIndex-1)
          wordIndex=c
    if wordIndex<=c:
      out.append(len(s)-wordIndex-1)
    return out


def test_get_word_lengths():
    text = "Three tomatoes are walking down the street"
    assert get_word_lengths(text) == [5, 8, 3, 7, 4, 3, 6]


# ------------------------------------------------------------------------------

def find_longest_word(s):
    """
    Returns the longest word in string s.
    In case there are several, return the first.
    """
    wordIndex=0
    longestWord=""
    out=[]
    for c in list(range(len(s))):
      if s[c]==" ":
        if wordIndex==0:
          out.append(s[wordIndex:c])
          wordIndex=c
        else:
          out.append(s[wordIndex+1:c])
          wordIndex=c
    if wordIndex<=c:
      out.append(s[wordIndex+1:len(s)])
    for w in out:
      if len(w)>len(longestWord):
        longestWord=w
    return longestWord


def test_find_longest_word():
    text = "Three tomatoes are walking down the street"
    assert find_longest_word(text) == "tomatoes"
    text = "foo foo1 foo2 foo3"
    assert find_longest_word(text) == "foo1"


# ------------------------------------------------------------------------------

def validate_dna(s):
    """
    Return True if the DNA string only contains characters
    a, c, t, or g (lower or uppercase). False otherwise.
    """
    out=True
    for c in s:
      if c.lower() not in 'ctga':
        out=False
    return out


def test_validate_dna():
    assert validate_dna('CCGGAAGAGCTTACTTAGccggaagagcttacttag')
    assert not validate_dna('xCCGGAAGAGCTTACTTAGccggaagagcttacttag')


# ------------------------------------------------------------------------------

def base_pair(c):
    """
    Return the corresponding character (lowercase)
    of the base pair. If the base is not recognized,
    return 'unknown'.
    """
    out='unknown'
    refbp={"a":"t","t":"a","c":"g","g":"c"}
    if c.lower() in list(refbp.keys()):
      if c.lower() == refbp[refbp[c.lower()]]:
        out=refbp[c.lower()]
    return out


def test_base_pair():
    assert base_pair('a') == 't'
    assert base_pair('t') == 'a'
    assert base_pair('c') == 'g'
    assert base_pair('g') == 'c'
    assert base_pair('A') == 't'
    assert base_pair('T') == 'a'
    assert base_pair('C') == 'g'
    assert base_pair('G') == 'c'
    assert base_pair('x') == 'unknown'
    assert base_pair('foo') == 'unknown'


# ------------------------------------------------------------------------------

def transcribe_dna_to_rna(s):
    """
    Return string s with each letter T replaced by U.
    Result is always uppercase.
    """
    out=""
    for c in s:
      if c.upper()=="T":
        out+="U"
      else:
        out+=c.upper()
    return out


def test_transcribe_dna_to_rna():
    dna = 'CCGGAAGAGCTTACTTAGccggaagagcttacttag'
    assert transcribe_dna_to_rna(dna) == 'CCGGAAGAGCUUACUUAGCCGGAAGAGCUUACUUAG'


# ------------------------------------------------------------------------------

def get_complement(s):
    """
    Return the DNA complement in uppercase
    (A -> T, T-> A, C -> G, G-> C).
    """
    out=""
    refbp={"a":"t","t":"a","c":"g","g":"c"}
    for c in s:
      if c.lower() in list(refbp.keys()):
        if c.lower() == refbp[refbp[c.lower()]]:
          out+=refbp[c.lower()]
    out=out.upper()
    return out


def test_get_complement():
    assert get_complement('CCGGAAGAGCTTACTTAG') == 'GGCCTTCTCGAATGAATC'
    assert get_complement('ccggaagagcttacttag') == 'GGCCTTCTCGAATGAATC'


# ------------------------------------------------------------------------------

def get_reverse_complement(s):
    """
    Return the reverse complement of string s
    (complement reversed in order).
    """
    out=""
    refbp={"a":"t","t":"a","c":"g","g":"c"}
    for c in s:
      if c.lower() in list(refbp.keys()):
        if c.lower() == refbp[refbp[c.lower()]]:
          out+=refbp[c.lower()]
    out=out.upper()
    out=out[::-1]
    return out


def test_get_reverse_complement():
    assert get_reverse_complement('CCGGAAGAGCTTACTTAG') == 'CTAAGTAAGCTCTTCCGG'
    assert get_reverse_complement('ccggaagagcttacttag') == 'CTAAGTAAGCTCTTCCGG'


# ------------------------------------------------------------------------------

def remove_substring(substring, string):
    """
    Returns string with all occurrences of substring removed.
    """
    out = string.replace(substring,"")
    return out

def test_remove_substring():
    assert remove_substring('GAA', 'CCGGAAGAGCTTACTTAG') == 'CCGGAGCTTACTTAG'
    assert remove_substring('CCG', 'CCGGAAGAGCTTACTTAG') == 'GAAGAGCTTACTTAG'
    assert remove_substring('TAG', 'CCGGAAGAGCTTACTTAG') == 'CCGGAAGAGCTTACT'
    assert remove_substring('GAA', 'GAAGAAGAA') == ''


# ------------------------------------------------------------------------------

def get_position_indices(triplet, dna):
    """
    Returns list of position indices for a specific triplet (3-mer)
    in a DNA sequence. We start counting from 0
    and jump by 3 characters from one position to the next.
    """
    out=[]
    for n in range(0,len(dna),3):
      if dna[n:n+3]==triplet:
        out.append(n//3)
    return out


def test_get_position_indices():
    assert get_position_indices('GAA', 'CCGGAAGAGCTTACTTAG') == [1]
    assert get_position_indices('GAA', 'CCGGAAGAGCTTACTTAGGAAGAA') == [1, 6, 7]


# ------------------------------------------------------------------------------

def get_3mer_usage_chart(s):
    """
    This routine implements a 'sliding window'
    and extracts all possible consecutive 3-mers.
    It counts how often they appear and returns
    a list of tuples with (name, occurrence).
    The list is alphabetically sorted by the name
    of the 3-mer.
    """
    triplet=[]
    for n in list(range(len(s))):
      if n<=len(s)-3:
        triplet.append(s[n:n+3])
    triplet = list(set(triplet))
    triplet = sorted(triplet)
    
    tripcountOut=[]
    for t in triplet:
      tmpS = s
      tmpS = tmpS.replace(t,'X')
      tripcount=0
      for c in tmpS:
        if c=='X':
          tripcount+=1
      tripcountOut.append(tripcount)
    out=list(zip(triplet,tripcountOut))
    return out


def test_get_3mer_usage_chart():
    s = 'CCGGAAGAGCTTACTTAGGAAGAA'
    result = []
    result.append(('AAG', 2))
    result.append(('ACT', 1))
    result.append(('AGA', 2))
    result.append(('AGC', 1))
    result.append(('AGG', 1))
    result.append(('CCG', 1))
    result.append(('CGG', 1))
    result.append(('CTT', 2))
    result.append(('GAA', 3))
    result.append(('GAG', 1))
    result.append(('GCT', 1))
    result.append(('GGA', 2))
    result.append(('TAC', 1))
    result.append(('TAG', 1))
    result.append(('TTA', 2))
    assert get_3mer_usage_chart(s) == result


# ------------------------------------------------------------------------------

def read_column(file_name, column_number):
    """
    Reads column column_number from file file_name
    and returns the values as floats in a list.
    """
    import csv
    fieldHandle=open(file_name, 'r')
    out=[]
    for line in fieldHandle:
      fields=line.split()
      if len(fields)!=0:
        out.append(float(fields[column_number-1]))
    fieldHandle.close()
    return out


def test_read_column():

    import tempfile
    import os

    text = """
1   0.1  0.001
2   0.2  0.002
3   0.3  0.003
4   0.4  0.004
5   0.5  0.005
6   0.6  0.006"""

    # we save this text to a temporary file
    file_name = tempfile.mkstemp()[1]
    with open(file_name, 'w') as f:
        f.write(text)

    # and now we pass the file name to the function which will read the column
    assert read_column(file_name, 2) == [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

    # we remove the temporary file
    os.unlink(file_name)


# ------------------------------------------------------------------------------

def character_statistics(file_name):
    """
    Reads text from file file_name, then
    lowercases the text, and then returns
    a tuple (x, y), where x is the most abundant
    and y is the least abundant character found.
    Use the isalpha() method to figure out
    whether the character is in the alphabet.
    """
    import csv
    import string
    import operator
    fieldHandle=open(file_name, 'r')
    out=[]
    for line in fieldHandle:
      fields=line.split()
      out+=fields
    fieldHandle.close()
    charCount=[]
    out=''.join(out)
    out = out.lower()
    refString = string.ascii_lowercase
    print(refString)
    for c in list(refString):
       charCount.append(out.count(c))
    print(charCount)
    index, value = max(enumerate(charCount), key=operator.itemgetter(1))
    firstMax= refString[index]
    index, value = min(enumerate(charCount), key=operator.itemgetter(1))
    secondMax= refString[index]
    refString2nd = refString[:index] + refString[index+1:]
    #del charCount[index]
    #secondMax= refString2nd[index]
    return (firstMax,secondMax)


def test_character_statistics():

    import tempfile
    import os

    text = """
To be, or not to be: that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles,
And by opposing end them? To die: to sleep;
No more; and by a sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to, 'tis a consummation
Devoutly to be wish'd. To die, to sleep;
To sleep: perchance to dream: ay, there's the rub;
For in that sleep of death what dreams may come
When jjj xxx we have shuffled off this mortal coil,
Must give us pause: there's the respect
That makes calamity of so long life;
For who would bear the whips and scorns of time,
The oppressor's wrong, the proud man's contumely,
The pangs of despised love, the law's delay,
The insolence of office and the spurns
That patient merit of the unworthy takes,
When he himself might his quietus make
With a bare bodkin? who would fardels bear,
To grunt and sweat under a weary life,
But that the dread of something after death,
The undiscover'd country from whose bourn
No traveller returns, puzzles the will
And makes us rather bear those ills we have
Than fly to others that we know not of?
Thus conscience does make cowards of us all;
And thus the native hue of resolution
Is sicklied o'er with the pale cast of thought,
And enterprises of great pith and moment
With this regard their currents turn awry,
And lose the name of action.--Soft you now!
The fair Ophelia! Nymph, in thy orisons
Be all my sins remember'd."""

    # we save this text to a temporary file
    file_name = tempfile.mkstemp()[1]
    with open(file_name, 'w') as f:
        f.write(text)

    # and now we pass the file name to the function which will get the stats
    (most_abundant, least_abundant) = character_statistics(file_name)
    assert (most_abundant, least_abundant) == ('e', 'q')

    # we remove the temporary file
    os.unlink(file_name)


# ------------------------------------------------------------------------------

def pythagorean_triples(n):
    """
    Returns list of all unique pythagorean triples
    (a, b, c) where a < b < c <= n.
    """
    l = []
    # loop over all a < b < c <= n
    for c in range(1, n + 1):
        for b in range(1, c):
            for a in range(1, b):
                if a*a + b*b == c*c:
                    l.append((a, b, c))
    return l


# ------------------------------------------------------------------------------

def test_pythagorean_triples():
  assert pythagorean_triples(20) == [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20)]
  pass  # so far we do not test anything, check also test coverage
