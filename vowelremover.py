def shortcut( s ):
    startlen = len(s)
    for vowel in "aeiou":
        
        s = s.replace(vowel, "")
    endlen = len(s)
    print(startlen - endlen)

shortcut('abracadabra')