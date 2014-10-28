#!/usr/bin/env python

DUT="./ueb01"

chars     = ['a', 'b', 'c', 'd', 'e']
chars    += [c.upper() for c in chars]
mirchars  = ['v', 'w', 'x', 'y', 'z']
mirchars += [c.upper() for c in mirchars]

def forward(x):
    return Test (
        name = "Forwardtest %d" % x,
        description = "Test the straight forward displaying of image #%d" % x,
        command = "$DUT %d > testtmp && diff testtmp testfiles/ueb01_img0%d.txt" % (x, x),
        stdout = "",
        returnCode = 0
    )

def forwardLetter(x):
    n = 1 + ord(x.lower()) - ord('a')
    return Test (
        name = "Forwardtest %c" % x,
        description = "Test the straight forward displaying of image #%d, choosen by letter %c" % (n, x),
        command = "$DUT %c > testtmp && diff testtmp testfiles/ueb01_img0%d.txt" % (x, n),
        stdout = "",
        returnCode = 0
    )

def mirrored(x):
    return Test (
        name = "Mirroredtest -%d" % x,
        description = "Test the mirrored displaying of image #%d" % x,
        command = "$DUT -%d > testtmp; tac testfiles/ueb01_img0%d.txt | diff testtmp -" % (x, x),
        stdout = "",
        returnCode = 0
    )

def mirroredLetter(x):
    n = -1*(ord(x.lower()) - ord('z') - 1)
    return Test (
        name = "Mirroredtest %c" % x,
        description = "Test the mirrored displaying of image #%d, choosen by letter %c" % (n, x),
        command = "$DUT %c > testtmp; tac testfiles/ueb01_img0%d.txt | diff testtmp -" % (x, n),
        stdout = "",
        returnCode = 0
    )

suite = [
    Test (
        name = "No arguments",
        description = "Test without any arguments",
        command = "$DUT 2> testtmp; RC=$?; tail -n10 testtmp | diff testfiles/usage.txt -; return $RC",
        stdout = "",
        returnCode = lambda rc : rc != 0
    ),
    Test (
        name = "Too many arguments",
        description = "Test with too many arguments",
        command = "$DUT a b c d e 2> testtmp; RC=$?; tail -n10 testtmp | diff testfiles/usage.txt -; return $RC",
        stdout = "",
        returnCode = lambda rc : rc != 0
    ),
    Test (
        name = "Overflowing argument",
        description = "Test with argument that could overflow to -1",
        command = "$DUT 11111111111111111111",
        stdout = "",
        returnCode = lambda rc : rc != 0
    )
]

for i in range(1, 6):
    suite.append(forward(i))
    suite.append(mirrored(i))

for i in chars:
    suite.append(forwardLetter(i))

for i in mirchars:
    suite.append(mirroredLetter(i))
