#!/usr/bin/env python

DUT="./ueb02"

suite = [
    Test (
        name = "Print Usage",
        description = "Usage is printed correctly",
        command = "$DUT -h",
        stdout = StringifiedFile("testfiles2/Usage.txt"),
        returnCode = 0
    ),
    Test (
        name = "Error 1",
        description = "No parameters were entered",
        command = "$DUT",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
	Test (
        name = "Error 2",
        description = "Wrong input -> ./ueb02 -h 2",
        command = "$DUT -h 2",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 3.1",
        description = "Wrong argument -> ./ueb02 asd",
        command = "$DUT asd",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 3.2",
        description = "Wrong argument -> ./ueb02 2 2 255 -h 1 1 0 -v k12 2 3",
        command = "$DUT 2 2 255 -h 1 1 0 -v k12 2 3",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 3.3",
        description = "Wrong argument -> ./ueb02 2 2 255 -h 1 1 0 -v 12 2 3 -c 12 2 3 3 f2",
        command = "$DUT 2 2 255 -h 1 1 0 -v 12 2 3 -c 12 2 3 3 f2",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 3.4",
        description = "Wrong argument -> ./ueb02 2 2 255 -v 1 1 0 -v 12 2 3 -h 12 2 s3",
        command = "$DUT 2 2 255 -h 1 1 0 -v 12 2 3 -c 12 2 3 3 f2",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 4",
        description = "No existing operator -> ./ueb02 10 10 255 -l 3 4 0",
        command = "$DUT 10 10 255 -l 3 4 0",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 5",
        description = "Image size is too big -> ./ueb02 1000 100 255 -l 3 4 0",
        command = "$DUT 1000 100 255 -l 3 4 0",
        stderr = StringifiedFile("testfiles2/ERR_IMAGE_SIZE.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 6.0",
        description = "Character in Argument -> ./ueb02 10a 10 255 -v 3 4 0",
        command = "$DUT 10a 10 255 -v 3 4 0",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 6.1",
        description = "Character in Argument -> ./ueb02 10 10a 255 -v 3 4 0",
        command = "$DUT 10 10a 255 -v 3 4 0",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 6.2",
        description = "Character in Argument -> ./ueb02 10 10 255a -v 3 4 0",
        command = "$DUT 10 10 255a -v 3 4 0",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 6.3",
        description = "Character in Argument -> ./ueb02 10 10 255 -h 3d 4 0",
        command = "$DUT 10 10 255 -h 3d 4 0",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 6.4",
        description = "Character in Argument -> ./ueb02 10 10 255 -h 3 4s 0",
        command = "$DUT 10 10 255 -h 3 4s 0",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 6.5",
        description = "Character in Argument -> ./ueb02 10 10 255 -h 3 4 0d",
        command = "$DUT 10 10 255 -h 3 4 0d",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 6.6",
        description = "Character in Argument -> ./ueb02 10 10 255 -v 3s 4 0",
        command = "$DUT 10 10 255 -h -v 3s 4 0",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 6.7",
        description = "Character in Argument -> ./ueb02 10 10 255 -v 3 4s 0",
        command = "$DUT 10 10 255 -v 3 4s 0",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 6.8",
        description = "Character in Argument -> ./ueb02 10 10 255 -v 3 4 0s",
        command = "$DUT 10 10 255 -v 3 4 0s",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 6.9",
        description = "Character in Argument -> ./ueb02 10 10 255 -c 3s 3 1 5 4",
        command = "$DUT 10 10 255 -c 3s 3 1 5 4",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 6.10",
        description = "Character in Argument -> ./ueb02 10 10 255 -c 3 3s 1 5 4",
        command = "$DUT 10 10 255 -c 3 3s 1 5 4",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 6.11",
        description = "Character in Argument -> ./ueb02 10 10 255 -c 3 3 1s 5 6",
        command = "$DUT 10 10 255 -c 3 3 1s 5 6",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 6.12",
        description = "Character in Argument -> ./ueb02 10 10 255 -c 3 3 1 5s 4",
        command = "$DUT 10 10 255 -c 3 3 1 5s 4",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 6.13",
        description = "Character in Argument -> ./ueb02 10 10 255 -c 3 3 1 5 4f",
        command = "$DUT 10 10 255 -c 3 3 1 5 4f",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 7.1",
        description = "Missing parameters -> ./ueb02 10 10 255 -h 3",
        command = "$DUT 10 10 255 -h 3",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 7.2",
        description = "Missing parameters -> ./ueb02 10 10 255 -v 3",
        command = "$DUT 10 10 255 -v 3",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 7.3",
        description = "Missing parameters -> ./ueb02 10 10 255 -c 3",
        command = "$DUT 10 10 255 -c 3",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 7.4",
        description = "Missing parameters -> ./ueb02 10 10 255 -o",
        command = "$DUT 10 10 255 -o",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 7.5",
        description = "Missing parameters -> ./ueb02 10 10 255 -h",
        command = "$DUT 10 10 255 -h",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 7.6",
        description = "Missing parameters -> ./ueb02 10 10 255 -v",
        command = "$DUT 10 10 255 -v",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 7.7",
        description = "Missing parameters -> ./ueb02 10 10 255 -c",
        command = "$DUT 10 10 255 -c",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 7.8",
        description = "Missing parameters -> ./ueb02 10 10",
        command = "$DUT 10 10",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 7.9",
        description = "Missing parameters -> ./ueb02 10",
        command = "$DUT 10",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error 8",
        description = "Intensity too big -> ./ueb02 10 13 256",
        command = "$DUT 10 13 256",
        stderr = StringifiedFile("testfiles2/ERR_INVALID_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Output1",
        description = "./ueb02 13 10 255 -v 2 3 0",
        command = "$DUT 13 10 255 -v 2 3 0",
        stdout = StringifiedFile("testfiles2/Output1.txt"),
        returnCode = 0
    ),
    Test (
        name = "Output2",
        description = "./ueb02 13 10 255 -h 2 3 0",
        command = "$DUT 13 10 255 -h 2 3 0",
        stdout = StringifiedFile("testfiles2/Output2.txt"),
        returnCode = 0
    ),
    Test (
        name = "Output3",
        description = "./ueb02 13 10 255 -c 2 3 2 4 0",
        command = "$DUT 13 10 255 -c 2 3 2 4 0",
        stdout = StringifiedFile("testfiles2/Output3.txt"),
        returnCode = 0
    ),
    Test (
        name = "Output4",
        description = "./ueb02 13 10 255",
        command = "$DUT 13 10 255",
        stdout = StringifiedFile("testfiles2/Output4.txt"),
        returnCode = 0
    ),
    Test (
        name = "Output5",
        description = "./ueb02 0 0 255",
        command = "$DUT 0 0 255",
        stdout = StringifiedFile("testfiles2/Output5.txt"),
        returnCode = 0
    ),
    Test (
        name = "Output6",
        description = "./ueb02 0 0 255 -h 12 21 0",
        command = "$DUT 0 0 255 -h 12 21 0",
        stdout = StringifiedFile("testfiles2/Output5.txt"),
        returnCode = 0
    ),
    Test (
        name = "Output7",
        description = "./ueb02 10 10 0 -h 1 1 2 -v 1 1 3 -h 1 1 4 -c 2 1 1 2 7",
        command = "$DUT 10 10 0 -h 1 1 2 -v 1 1 3 -h 1 1 4 -c 2 1 1 2 7",
        stdout = StringifiedFile("testfiles2/Output7.txt"),
        returnCode = 0
    )
]
