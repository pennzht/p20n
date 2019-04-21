from sys import argv

def abbreviate (word):
    chars = [ch for ch in word if ch.isalpha ()]
    if len (chars) <= 1:
        return ''.join(chars)
    else:
        return chars[0] + str (len (chars) - 2) + chars[-1]

def main (wordlist):
    ans = [(word, abbreviate (word)) for word in wordlist]
    if len (ans) == 0:
        pass
    else:
        maxwordlength = max (len (word) for (word, abbreviation) in ans)
        columnwidth = maxwordlength + 4
        for (word, abbreviation) in ans:
            print (word.ljust (columnwidth) + abbreviation)

if __name__ == '__main__':
    main (argv[1:])

