### Programs that Surf the Web:

#### Unicode characters and strings:

---
In the 70's there was only one character type, which was uppercase letter. However, there was a need to have numbers and a mapping between numbers anc characters, so, they come up with __ASCI (American Standard Code for Information Interchange.)__

ASCI defines a number for each letter. For example, the number for letter H (uppercase) is 72. lowercase e is 101.

In Python we can use ord() function (ordinal) to show the numerical value for each character.

```
>>> print(ord("H"))   // returns 72

>>> print(ord("\n"))   // reutrns 10  (\n for new line)
```    
(photo: asci-definition.jpg)

Using ASCI was fine for a period, but the next problem, was different languages couldn't communicate properly for example Japanese computers couldn't talk to American ones at all. 

Later they came up with __UNICODE system__ that has a lot more characters in it and it maps millions of characters and any kind of combination of characters can fit into this definition.

There are different representations of Unicode which are UTF-32, UTF-16, UTF-8. (photo: UTF.jpg)

It turns out that UTF-8 is the most efficient way, and it also matches with ASCI system.

There used to be a difference between str and unicode in python 2, and we had to covert them to each other putting a 'u' behind the str to convert it to unicode, but now in python3, every character is unicode and it just sees everything as type str.

(photo: unicode-py2-vs-py3.jpg)

However, for bytes, we need to know that byte is the same as str in py2, but different in py3 (photo:byte-py2-vs-py3.jpg) so we may have to convert them into str in py3, when we are dealing with data from outside.

But we don't have to worry so much for it, because 99% of the data on the web are using UTF-8 and we can easily manipulate them using py3.

The data we get from sockets, is byte, and we have to convert them to unicode. that's why whe dealing with data from sockets, we use the method decode(). as we have before when we wrote code for sockets.

(photo: socket-byte-decode.jpg)

Also sometimes we need to send data to the socket, and in this situation, we use method encode() to convert string to bytes. (photo: socket-byte-encode.jpg)

__URLLIB library:__ Luckily, python has this library to deal with all socket deocoding/encoding for us. We just need to write few lines to get all the data, then loop through all lines, and print them.

urllib-basic.jpg

We can simply use this library to open a web page, have it as a file, then count all of its words. (photo: words-count-of-a-webpage.jpg)
 
