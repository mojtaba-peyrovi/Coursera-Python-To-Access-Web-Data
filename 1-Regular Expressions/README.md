### Regular Expressions:

In Python we don't have RegEx built in, so we need to import it like this:
```
Import re
```
RegEx, is a programming language for string matching.

```
Python: <string>.rstrip()  // removes any empty character from the right side of a string.
Python: <string1>.find(string2,beg=0, end=len(string1) // it returns an integer that represents the position of the second string inside the first string based on what charachter we tell it to start from.
```
For saying find a line in a text that starts with the word "Tomorrow":
```
import re
txt = open("sample.txt")
for line in txt:
    if re.search('^Tomorrow', line):
        print(line)
```
`The ^ means begining of the line.`

Here is another example:
```
import re
txt = open("sample.txt")
for line in txt:
    if re.search('^X.*:', line):
        print(line)

```
It means print any line that has an X in the beginning following by any number of any character(. means any character) followed by a colon. (* means zero or more times of repeat.)

We can make it more specific like this: fine-tuning.jpg
```
^X-\s+:   // it is shown in the saved photo above.
```
In regx, [] means one character. for example [0-9] ,means a character between 0 and 9.

when we add + to it like this: [0-9]+ , it means a character between 0-9 but repeated one or more times.

One nice method in regex, is:
```
re.findall('<regex>', string_name)  e.g. re.findall('[0-9]+', str) // it finds all numbers in the string saved in str variable.
```

There is another concept called __greedy Matching__ that happens in regex, that means it tries to get as biggest strings as possible matching the expression. 
here is an example(greedy-matching.jpg)

If we don't want the greedy matching, then we will tell it to be non-greedy as we see in this example: (non-greedy-matching.jpg)

Her is another example for matching the email address: (email-matching.com)

\s+ means at least one non-blank character.

Important point, is the email example is also greedy to show the whole address, otherwise it would return only d@u.

Using parenthesis, can make it exact. as we can see in the photo parenthesis.jpg

Check this photo: double-split-pattern.jpg which is using python strings, to split the value after @. But using regex we can do all of it in one expression in photo(regex-version,two,three.jpg)

:









