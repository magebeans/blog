---
layout: post
---

I'll try and explain how I solved the 16th Natas challenge in this post. You
can find the challenge page [here](http://natas16.natas.labs.overthewire.org).

Playing around with the page shows that the the page takes input, greps the
input against a dictionary file, and returns the filtered output.

For instance, entering "clock" returns a list of all the words in the file
dictionary.txt that contain the substring "clock"

![clock]({{ site.url }}/assets/clock.png)

What if we tried something that isn't in the dictionary? A random input
takes you to a page with empty output. This will be important - the idea
that you can extract information from the page based on whether or not some
string is in the dictionary. We can use this to figure out the password
for the next phase.

We know that the password will be contained in  the file /etc/natas_webpass/natas17
on the server. We simply need to somehow access this. The page takes our input
and executes it. This means that we can enclose any arbitrary shell command
in between $() and have the server execute it. This will help us determine the
password, character by character.

Consider the command `grep -E ^"1" /etc/natas_webpass/natas17`
The -E option tells grep to treat the following part as a regex. The regex that
follows returns true if the line in the natas17 file starts with the string "1".
Together, this command returns the password if it begins with the character 1,
and nothing otherwise. Cycling through all possible first characters, trying
commands like `grep -E ^"2" /etc/natas_webpass/natas17`, 
`grep -E ^"3" /etc/natas_webpass/natas17`, etc, for every possible first
character of the password, until we hit the right first character. When we do,
the command will return the entire password. Now we need to figure out how to
convert this into something we can detect.

If we pass the string `$(grep -E ^"1" /etc/natas_webpass/natas17)test` to the
input box in the page, what happens?
The server first  executes the command within the $(), grepping the password
file against the regex we provide, and returning nothing if it does not match.
If the password does not begin with the character 1, nothing is returned. The
server then grep simply the string test against the dictionary file, returning
a list of words in the dictionary containing the substring test.
But suppose the first character of the password was the character 1. In this
case, the command within $() returns the password, which is prepended to the
string test. The server then greps the string $password+test against the
dictionary. Now, the password is usually something like WaIHEacj63wnNIBROHeqi3p9t0m5nhmh,
which means that the server greps something like WaIHEacj63wnNIBROHeqi3p9t0m5nhmhtest
against the dictionary, which returns a page containing nothing.

In short, we can guess the first character of the password in this manner, checking
to see if the result page is empty of not - it will be empty if the character we
guess is correct, and a list of strings containing the substring test if it is
not. By cycling through every possible number and letter, we can obtain the
first character of the password in this way.

Continuing, we can use a command like `$(grep -E ^"1a" /etc/natas_webpass/natas17)test`,
assuming that the first character of the password is 1, in order to check the second
character of the password. Here, we test to see if the second character is a.
Similarly to the previous case, the server returns an empty list if our guess for
the second character is correct, and a list of strings with substring test in
them if it is incorrect.

Generalizing, assuming we've found the first k characters of the password, represented
by the string p, we can find the k+1'th character using by trying all possible
values of the k+1'th character x in the command `$(grep -E ^"px" /etc/natas_webpass/natas17)test`,
where p is expanded to the password prefix we know, and x is the character we're guessing,
and listening for the response from the server - our guess is correct if the
server return nothing, and incorrect if it returns a list of words.

Continuing, we can find all the characters of the password, at which point we've
solved the challenge!

You can find the code I used to automate the process described above [here](https://www.github.com/ManasGeorge/OverTheWire.git)
I hope you found the post helpful! Don't hesitate to email me if you have any questions.
