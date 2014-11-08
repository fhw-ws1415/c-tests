#!/usr/bin/env python

DUT="./ueb03"

suite = [
    Test (
        name = "Print Usage",
        description = "Usage is printed correctly",
        command = "$DUT -h",
        stdout = StringifiedFile("testfiles/Usage.txt"),
        returnCode = 0
    ),
#    Test (
#        name = "Error Usage 1",
#        description = "Wrong input",
#        command = "$DUT -h2",
#        stdout = StringifiedFile("testfiles/"),
#        returnCode = lambda v: v != 0
#    ),
#    Test (
#        name = "Error Usage 2",
#        description = "Wrong input",
#        command = "$DUT -f",
#        stdout = StringifiedFile("testfiles/"),
#        returnCode = lambda v: v != 0
#    ),
	Test (
        name = "Error WRONG ARG CNT 1",
        description = "No parameters entered",
        command = "$DUT",
        stderr = StringifiedFile("testfiles/ERR_WRONG_ARG_CNT.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error WRONG ARG CNT 2",
        description = "Too many parameters entered",
        command = "$DUT \"-2.0x^2+1.0x^2\" 5.0 0.0 10.0 100 x 12",
        stderr = StringifiedFile("testfiles/ERR_WRONG_ARG_CNT.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error WRONG ARG CNT 3",
        description = "Too less parameters entered",
        command = "$DUT \"-2.0x^2+1.0x^2\" 5.0 0.0 10.0 100",
        stderr = StringifiedFile("testfiles/ERR_WRONG_ARG_CNT.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error INVALID EXPO 1",
        description = "An invalid exponent (negativ) was entered",
        command = "$DUT \"-2.0x^-2+1.0x^2\" 5.0 0.0 10.0 100 x",
        stderr = StringifiedFile("testfiles/ERR_INVALID_EXPO.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error INVALID EXPO 2",
        description = "An invalid exponent (too big) was entered",
        command = "$DUT \"-2.0x^10000+1.0x^2\" 5.0 0.0 10.0 100 x",
        stderr = StringifiedFile("testfiles/ERR_INVALID_EXPO.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error SYNTAX ERROR 1",
        description = "Polynom has got wrong syntax",
        command = "$DUT \"-2.0x^2+1.0x^3-d\" 5.0 0.0 10.0 100 x",
        stderr = StringifiedFile("testfiles/ERR_SYNTAX_ERROR.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error SYNTAX ERROR 2",
        description = "Polynom has got wrong syntax",
        command = "$DUT \"-2.0x^2+1.0x^\" 5.0 0.0 10.0 100 x",
        stderr = StringifiedFile("testfiles/ERR_SYNTAX_ERROR.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error SYNTAX ERROR 3",
        description = "Polynom has got wrong syntax",
        command = "$DUT \"-2.0x^2+1.0^3\" 5.0 0.0 10.0 100 x",
        stderr = StringifiedFile("testfiles/ERR_SYNTAX_ERROR.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error SYNTAX ERROR 4",
        description = "Polynom has got wrong syntax",
        command = "$DUT \"-2.0x^2+1.0x3\" 5.0 0.0 10.0 100 x",
        stderr = StringifiedFile("testfiles/ERR_SYNTAX_ERROR.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error SYNTAX ERROR 5",
        description = "Polynom has got wrong syntax",
        command = "$DUT \"-2fx^2+1.0x^3\" 5.0 0.0 10.0 100 x",
        stderr = StringifiedFile("testfiles/ERR_SYNTAX_ERROR.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error SYNTAX ERROR 6",
        description = "Polynom has got wrong syntax",
        command = "$DUT \"-2.1x^2+ix^3\" 5.0 0.0 10.0 100 x",
        stderr = StringifiedFile("testfiles/ERR_SYNTAX_ERROR.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error SYNTAX ERROR 7",
        description = "Polynom has got wrong syntax",
        command = "$DUT \"-2.1x^2+2.0^3\" 5.0 0.0 10.0 100 x",
        stderr = StringifiedFile("testfiles/ERR_SYNTAX_ERROR.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error SYNTAX ERROR 8",
        description = "Polynom has got wrong syntax",
        command = "$DUT \"-2.1x      ^2+2.0x^3\" 5.0 0.0 10.0 100 x",
        stderr = StringifiedFile("testfiles/ERR_SYNTAX_ERROR.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error SYNTAX ERROR 9",
        description = "Polynom has got wrong syntax",
        command = "$DUT \"-        2.1x^2+2.0x^3\" 5.0 0.0 10.0 100 x",
        stderr = StringifiedFile("testfiles/ERR_SYNTAX_ERROR.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error SYNTAX ERROR 10",
        description = "Polynom has got wrong syntax",
        command = "$DUT \"-2.1ax^2+2.0x^3\" 5.0 0.0 10.0 100 x",
        stderr = StringifiedFile("testfiles/ERR_SYNTAX_ERROR.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error SYNTAX ERROR 11",
        description = "Polynom has got wrong syntax",
        command = "$DUT \"-2.1x^2*2.0x^3\" 5.0 0.0 10.0 100 x",
        stderr = StringifiedFile("testfiles/ERR_SYNTAX_ERROR.txt"),
        returnCode = lambda v: v != 0
    ),
#    Test (
#        name = "Error SYNTAX ERROR 12",
#        description = "Polynom has got wrong syntax",						"2" auch als float gueltig??
#        command = "$DUT \"-2.1x^2+2x^3\" 5.0 0.0 10.0 100 x",
#        stderr = StringifiedFile("testfiles/ERR_SYNTAX_ERROR.txt"),
#        returnCode = lambda v: v != 0
#    ),
    Test (
        name = "Error SYNTAX ERROR 13",
        description = "Polynom has got wrong syntax",
        command = "$DUT \"-2.0x^2+1.0x^3.0\" 5.0 0.0 10.0 100 x",
        stderr = StringifiedFile("testfiles/ERR_SYNTAX_ERROR.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error SYNTAX ERROR 14",
        description = "Polynom has got wrong syntax",
        command = "$DUT \"-2.0x^2+1.0x^a\" 5.0 0.0 10.0 100 x",
        stderr = StringifiedFile("testfiles/ERR_SYNTAX_ERROR.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error SYNTAX ERROR 15",
        description = "Polynom has got wrong syntax",
        command = "$DUT \"-2.0x^2+1.0x^3a\" 5.0 0.0 10.0 100 x",
        stderr = StringifiedFile("testfiles/ERR_SYNTAX_ERROR.txt"),
        returnCode = lambda v: v != 0
    ),
#    Test (
#        name = "Error NODOUBLE 1",
#        description = "Parameter is no float",
#        command = "$DUT \"-2.1x^2+2.0x^3\" 5 0.0 10.0 100 x",
#        stderr = StringifiedFile("testfiles/ERR_NODOUBLE.txt"),
#        returnCode = lambda v: v != 0
#    ),
#    Test (
#        name = "Error NODOUBLE 2",
#        description = "Parameter is no float",
#        command = "$DUT \"-2.1x^2+2.0x^3\" 5.0 0 10.0 100 x",
#        stderr = StringifiedFile("testfiles/ERR_NODOUBLE.txt"),
#        returnCode = lambda v: v != 0
#    ),
#    Test (
#        name = "Error NODOUBLE 3",
#        description = "Parameter is no float",
#        command = "$DUT \"-2.1x^2+2.0x^3\" 5.0 0.0 10 100 x",
#        stderr = StringifiedFile("testfiles/ERR_NODOUBLE.txt"),
#        returnCode = lambda v: v != 0
#    ),
    Test (
        name = "Error NODOUBLE 4",
        description = "Parameter is no float",
        command = "$DUT \"-2.1x^2+2.0x^3\" 5.0v 0.0 10.0 100 x",
        stderr = StringifiedFile("testfiles/ERR_NODOUBLE.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error NODOUBLE 5",
        description = "Parameter is no float",
        command = "$DUT \"-2.1x^2+2.0x^3\" v5.0 0.0 10.0 100 x",
        stderr = StringifiedFile("testfiles/ERR_NODOUBLE.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error NODOUBLE 6",
        description = "Parameter is no float",
        command = "$DUT \"-2.1x^2+2.0x^3\" 5.0 v0.0 10.0 100 x",
        stderr = StringifiedFile("testfiles/ERR_NODOUBLE.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error NODOUBLE 7",
        description = "Parameter is no float",
        command = "$DUT \"-2.1x^2+2.0x^3\" 5.0 0.0v 10.0 100 x",
        stderr = StringifiedFile("testfiles/ERR_NODOUBLE.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error NODOUBLE 8",
        description = "Parameter is no float",
        command = "$DUT \"-2.1x^2+2.0x^3\" 5.0 0.0 v10.0 100 x",
        stderr = StringifiedFile("testfiles/ERR_NODOUBLE.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error NODOUBLE 9",
        description = "Parameter is no float",
        command = "$DUT \"-2.1x^2+2.0x^3\" 5.0 0.0 10.0v 100 x",
        stderr = StringifiedFile("testfiles/ERR_NODOUBLE.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error NODOUBLE 10",
        description = "Parameter is no float",
        command = "$DUT \"-2.1x^2+2.0x^3\" 5s.0 0.0 10.0 100 x",
        stderr = StringifiedFile("testfiles/ERR_NODOUBLE.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error NOUINT 1",
        description = "Parameter is no unsigned int",
        command = "$DUT \"-2.1x^2+2.0x^3\" 5.0 0.0 10.0 -100 x",
        stderr = StringifiedFile("testfiles/ERR_NOUINT.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error NOUINT 2",
        description = "Parameter is no unsigned int",
        command = "$DUT \"-2.1x^2+2.0x^3\" 5.0 0.0 10.0 100.0 x",
        stderr = StringifiedFile("testfiles/ERR_NOUINT.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error NOUINT 3",
        description = "Parameter is no unsigned int",
        command = "$DUT \"-2.1x^2+2.0x^3\" 5.0 0.0 10.0 10s x",
        stderr = StringifiedFile("testfiles/ERR_NOUINT.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error INVALID OP ARG 1",
        description = "Parameter is no valid operator (x,c,g)",
        command = "$DUT \"-2.1x^2+2.0x^3\" 5.0 0.0 10.0 10 o",
        stderr = StringifiedFile("testfiles/ERR_INVALID_OP_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error INVALID OP ARG 2",
        description = "Parameter is no valid operator (x,c,g)",
        command = "$DUT \"-2.1x^2+2.0x^3\" 5.0 0.0 10.0 10 xxgxggxgc0",
        stderr = StringifiedFile("testfiles/ERR_INVALID_OP_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error INVALID OP ARG 3",
        description = "Parameter is no valid operator (x,c,g)",
        command = "$DUT \"-2.1x^2+2.0x^3\" 5.0 0.0 10.0 10 cgcgcag",
        stderr = StringifiedFile("testfiles/ERR_INVALID_OP_ARG.txt"),
        returnCode = lambda v: v != 0
    ),
    Test (
        name = "Error INVALID OP ARG 4",
        description = "Parameter is no valid operator (x,c,g)",
        command = "$DUT \"-2.1x^2+2.0x^3\" 5.0 0.0 10.0 10 2",
        stderr = StringifiedFile("testfiles/ERR_INVALID_OP_ARG.txt"),
        returnCode = lambda v: v != 0
    )
]
