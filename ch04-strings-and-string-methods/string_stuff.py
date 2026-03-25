string1 = 'Hello, World'
string2 = "1234"
string3 = "We're #1"
string4 = 'I said, "Put it over by the llama."'
text = "She said, \"What time is it?\""
long_string = "This multiline string is \
displayed on one line"
print(long_string)

paragraph = "This planet has—or rather had—a problem, which was \
this: most of the people living on it were unhappy for pretty much \
of the time. Many solutions were suggested for this problem, but \
most of these were largely concerned with the movements of small \
green pieces of paper, which is odd because on the whole it wasn't \
the small green pieces of paper that were unhappy."
print("\nLong paragraph one quote at begin and end\n")
print(paragraph)

# Triple quoted string preserve whitespace, including newlines
paragraph = """This planet has—or rather had—a problem, which was
this: most of the people living on it were unhappy for pretty much
of the time. Many solutions were suggested for this problem, but
most of these were largely concerned with the movements of small
green pieces of paper, which is odd because on the whole it wasn't
the small green pieces of paper that were unhappy."""
print("\nNew string called paragraph")
print(paragraph)

print("""An example of a
...    string that spans across multiple lines
...        and also preseves whitespace.""")
