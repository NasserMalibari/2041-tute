import sys


"""
chomp - The Perl function chomp removes a single newline from the 
end of a string (if there is one). 
"""
def chomp(string):
    if (string.endswith('\n')):
        return string[0:-1]
    # string[-1]
    return string

# qw - The Perl function qw splits a string into a list of words.
def qw(string):
    return string.split()
    # pass

# die - The Perl function die prints an error message and exits the program
def die(message, status=1):
    print(message, file=sys.stderr)
    sys.exit(status)

if __name__ == "__main__":
    print(chomp("hello\n"),end = "")