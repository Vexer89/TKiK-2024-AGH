# Generated from java_grammar.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,94,726,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,
        78,7,78,2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,7,
        84,2,85,7,85,2,86,7,86,2,87,7,87,2,88,7,88,2,89,7,89,2,90,7,90,2,
        91,7,91,2,92,7,92,2,93,7,93,2,94,7,94,2,95,7,95,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,
        1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,
        1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,27,
        1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,
        1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,
        1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,34,
        1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,
        1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,38,1,38,1,38,
        1,38,1,39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,1,40,
        1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,42,1,42,
        1,42,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,44,1,44,1,45,1,45,
        1,46,1,46,1,47,1,47,1,48,1,48,1,49,1,49,1,50,1,50,1,51,1,51,1,52,
        1,52,1,53,1,53,1,54,1,54,1,55,1,55,1,55,1,56,1,56,1,56,1,57,1,57,
        1,58,1,58,1,59,1,59,1,59,1,60,1,60,1,60,1,61,1,61,1,61,1,62,1,62,
        1,62,1,63,1,63,1,64,1,64,1,64,1,65,1,65,1,65,1,66,1,66,1,67,1,67,
        1,67,1,68,1,68,1,68,1,69,1,69,1,69,1,70,1,70,1,70,1,71,1,71,1,71,
        1,72,1,72,1,73,1,73,1,74,1,74,1,75,1,75,1,76,1,76,1,76,1,76,1,76,
        1,77,1,77,1,77,1,77,1,78,1,78,1,78,1,78,1,78,1,78,1,79,1,79,1,79,
        1,79,1,79,1,79,1,79,1,80,1,80,1,80,1,80,1,80,1,81,1,81,1,81,1,81,
        1,81,1,81,1,82,1,82,1,82,1,82,1,82,1,83,1,83,1,83,1,83,1,83,1,84,
        1,84,1,84,1,84,1,84,1,84,1,84,1,84,1,85,1,85,1,85,1,85,1,85,1,85,
        1,85,1,86,1,86,5,86,655,8,86,10,86,12,86,658,9,86,1,87,1,87,1,88,
        4,88,663,8,88,11,88,12,88,664,1,89,4,89,668,8,89,11,89,12,89,669,
        1,89,1,89,4,89,674,8,89,11,89,12,89,675,1,90,1,90,1,90,5,90,681,
        8,90,10,90,12,90,684,9,90,1,90,1,90,1,91,1,91,1,91,1,92,1,92,1,92,
        1,92,1,93,4,93,696,8,93,11,93,12,93,697,1,93,1,93,1,94,1,94,1,94,
        1,94,5,94,706,8,94,10,94,12,94,709,9,94,1,94,1,94,1,94,1,94,1,94,
        1,95,1,95,1,95,1,95,5,95,720,8,95,10,95,12,95,723,9,95,1,95,1,95,
        1,707,0,96,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,
        12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,
        23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,
        34,69,35,71,36,73,37,75,38,77,39,79,40,81,41,83,42,85,43,87,44,89,
        45,91,46,93,47,95,48,97,49,99,50,101,51,103,52,105,53,107,54,109,
        55,111,56,113,57,115,58,117,59,119,60,121,61,123,62,125,63,127,64,
        129,65,131,66,133,67,135,68,137,69,139,70,141,71,143,72,145,73,147,
        74,149,75,151,76,153,77,155,78,157,79,159,80,161,81,163,82,165,83,
        167,84,169,85,171,86,173,87,175,0,177,88,179,89,181,90,183,0,185,
        91,187,92,189,93,191,94,1,0,6,3,0,65,90,95,95,97,122,5,0,36,36,48,
        57,65,90,95,95,97,122,1,0,48,57,2,0,34,34,92,92,3,0,9,10,13,13,32,
        32,2,0,10,10,13,13,732,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,
        0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,
        0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,
        0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,
        0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,
        0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,
        0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,
        0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,
        0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,
        0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,
        0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,1,0,0,0,0,107,
        1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,0,115,1,0,0,0,
        0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,0,123,1,0,0,0,0,125,1,
        0,0,0,0,127,1,0,0,0,0,129,1,0,0,0,0,131,1,0,0,0,0,133,1,0,0,0,0,
        135,1,0,0,0,0,137,1,0,0,0,0,139,1,0,0,0,0,141,1,0,0,0,0,143,1,0,
        0,0,0,145,1,0,0,0,0,147,1,0,0,0,0,149,1,0,0,0,0,151,1,0,0,0,0,153,
        1,0,0,0,0,155,1,0,0,0,0,157,1,0,0,0,0,159,1,0,0,0,0,161,1,0,0,0,
        0,163,1,0,0,0,0,165,1,0,0,0,0,167,1,0,0,0,0,169,1,0,0,0,0,171,1,
        0,0,0,0,173,1,0,0,0,0,177,1,0,0,0,0,179,1,0,0,0,0,181,1,0,0,0,0,
        185,1,0,0,0,0,187,1,0,0,0,0,189,1,0,0,0,0,191,1,0,0,0,1,193,1,0,
        0,0,3,203,1,0,0,0,5,214,1,0,0,0,7,222,1,0,0,0,9,230,1,0,0,0,11,233,
        1,0,0,0,13,238,1,0,0,0,15,245,1,0,0,0,17,250,1,0,0,0,19,256,1,0,
        0,0,21,260,1,0,0,0,23,266,1,0,0,0,25,275,1,0,0,0,27,278,1,0,0,0,
        29,284,1,0,0,0,31,294,1,0,0,0,33,299,1,0,0,0,35,306,1,0,0,0,37,314,
        1,0,0,0,39,324,1,0,0,0,41,331,1,0,0,0,43,337,1,0,0,0,45,346,1,0,
        0,0,47,354,1,0,0,0,49,362,1,0,0,0,51,373,1,0,0,0,53,383,1,0,0,0,
        55,390,1,0,0,0,57,407,1,0,0,0,59,426,1,0,0,0,61,434,1,0,0,0,63,439,
        1,0,0,0,65,444,1,0,0,0,67,450,1,0,0,0,69,455,1,0,0,0,71,461,1,0,
        0,0,73,465,1,0,0,0,75,471,1,0,0,0,77,479,1,0,0,0,79,483,1,0,0,0,
        81,488,1,0,0,0,83,495,1,0,0,0,85,502,1,0,0,0,87,509,1,0,0,0,89,517,
        1,0,0,0,91,519,1,0,0,0,93,521,1,0,0,0,95,523,1,0,0,0,97,525,1,0,
        0,0,99,527,1,0,0,0,101,529,1,0,0,0,103,531,1,0,0,0,105,533,1,0,0,
        0,107,535,1,0,0,0,109,537,1,0,0,0,111,539,1,0,0,0,113,542,1,0,0,
        0,115,545,1,0,0,0,117,547,1,0,0,0,119,549,1,0,0,0,121,552,1,0,0,
        0,123,555,1,0,0,0,125,558,1,0,0,0,127,561,1,0,0,0,129,563,1,0,0,
        0,131,566,1,0,0,0,133,569,1,0,0,0,135,571,1,0,0,0,137,574,1,0,0,
        0,139,577,1,0,0,0,141,580,1,0,0,0,143,583,1,0,0,0,145,586,1,0,0,
        0,147,588,1,0,0,0,149,590,1,0,0,0,151,592,1,0,0,0,153,594,1,0,0,
        0,155,599,1,0,0,0,157,603,1,0,0,0,159,609,1,0,0,0,161,616,1,0,0,
        0,163,621,1,0,0,0,165,627,1,0,0,0,167,632,1,0,0,0,169,637,1,0,0,
        0,171,645,1,0,0,0,173,652,1,0,0,0,175,659,1,0,0,0,177,662,1,0,0,
        0,179,667,1,0,0,0,181,677,1,0,0,0,183,687,1,0,0,0,185,690,1,0,0,
        0,187,695,1,0,0,0,189,701,1,0,0,0,191,715,1,0,0,0,193,194,5,65,0,
        0,194,195,5,114,0,0,195,196,5,114,0,0,196,197,5,97,0,0,197,198,5,
        121,0,0,198,199,5,76,0,0,199,200,5,105,0,0,200,201,5,115,0,0,201,
        202,5,116,0,0,202,2,1,0,0,0,203,204,5,76,0,0,204,205,5,105,0,0,205,
        206,5,110,0,0,206,207,5,107,0,0,207,208,5,101,0,0,208,209,5,100,
        0,0,209,210,5,76,0,0,210,211,5,105,0,0,211,212,5,115,0,0,212,213,
        5,116,0,0,213,4,1,0,0,0,214,215,5,72,0,0,215,216,5,97,0,0,216,217,
        5,115,0,0,217,218,5,104,0,0,218,219,5,83,0,0,219,220,5,101,0,0,220,
        221,5,116,0,0,221,6,1,0,0,0,222,223,5,72,0,0,223,224,5,97,0,0,224,
        225,5,115,0,0,225,226,5,104,0,0,226,227,5,77,0,0,227,228,5,97,0,
        0,228,229,5,112,0,0,229,8,1,0,0,0,230,231,5,105,0,0,231,232,5,102,
        0,0,232,10,1,0,0,0,233,234,5,101,0,0,234,235,5,108,0,0,235,236,5,
        115,0,0,236,237,5,101,0,0,237,12,1,0,0,0,238,239,5,115,0,0,239,240,
        5,119,0,0,240,241,5,105,0,0,241,242,5,116,0,0,242,243,5,99,0,0,243,
        244,5,104,0,0,244,14,1,0,0,0,245,246,5,99,0,0,246,247,5,97,0,0,247,
        248,5,115,0,0,248,249,5,101,0,0,249,16,1,0,0,0,250,251,5,119,0,0,
        251,252,5,104,0,0,252,253,5,105,0,0,253,254,5,108,0,0,254,255,5,
        101,0,0,255,18,1,0,0,0,256,257,5,102,0,0,257,258,5,111,0,0,258,259,
        5,114,0,0,259,20,1,0,0,0,260,261,5,98,0,0,261,262,5,114,0,0,262,
        263,5,101,0,0,263,264,5,97,0,0,264,265,5,107,0,0,265,22,1,0,0,0,
        266,267,5,99,0,0,267,268,5,111,0,0,268,269,5,110,0,0,269,270,5,116,
        0,0,270,271,5,105,0,0,271,272,5,110,0,0,272,273,5,117,0,0,273,274,
        5,101,0,0,274,24,1,0,0,0,275,276,5,100,0,0,276,277,5,111,0,0,277,
        26,1,0,0,0,278,279,5,99,0,0,279,280,5,108,0,0,280,281,5,97,0,0,281,
        282,5,115,0,0,282,283,5,115,0,0,283,28,1,0,0,0,284,285,5,105,0,0,
        285,286,5,110,0,0,286,287,5,116,0,0,287,288,5,101,0,0,288,289,5,
        114,0,0,289,290,5,102,0,0,290,291,5,97,0,0,291,292,5,99,0,0,292,
        293,5,101,0,0,293,30,1,0,0,0,294,295,5,101,0,0,295,296,5,110,0,0,
        296,297,5,117,0,0,297,298,5,109,0,0,298,32,1,0,0,0,299,300,5,112,
        0,0,300,301,5,117,0,0,301,302,5,98,0,0,302,303,5,108,0,0,303,304,
        5,105,0,0,304,305,5,99,0,0,305,34,1,0,0,0,306,307,5,112,0,0,307,
        308,5,114,0,0,308,309,5,105,0,0,309,310,5,118,0,0,310,311,5,97,0,
        0,311,312,5,116,0,0,312,313,5,101,0,0,313,36,1,0,0,0,314,315,5,112,
        0,0,315,316,5,114,0,0,316,317,5,111,0,0,317,318,5,116,0,0,318,319,
        5,101,0,0,319,320,5,99,0,0,320,321,5,116,0,0,321,322,5,101,0,0,322,
        323,5,100,0,0,323,38,1,0,0,0,324,325,5,115,0,0,325,326,5,116,0,0,
        326,327,5,97,0,0,327,328,5,116,0,0,328,329,5,105,0,0,329,330,5,99,
        0,0,330,40,1,0,0,0,331,332,5,102,0,0,332,333,5,105,0,0,333,334,5,
        110,0,0,334,335,5,97,0,0,335,336,5,108,0,0,336,42,1,0,0,0,337,338,
        5,97,0,0,338,339,5,98,0,0,339,340,5,115,0,0,340,341,5,116,0,0,341,
        342,5,114,0,0,342,343,5,97,0,0,343,344,5,99,0,0,344,345,5,116,0,
        0,345,44,1,0,0,0,346,347,5,100,0,0,347,348,5,101,0,0,348,349,5,102,
        0,0,349,350,5,97,0,0,350,351,5,117,0,0,351,352,5,108,0,0,352,353,
        5,116,0,0,353,46,1,0,0,0,354,355,5,101,0,0,355,356,5,120,0,0,356,
        357,5,116,0,0,357,358,5,101,0,0,358,359,5,110,0,0,359,360,5,100,
        0,0,360,361,5,115,0,0,361,48,1,0,0,0,362,363,5,105,0,0,363,364,5,
        109,0,0,364,365,5,112,0,0,365,366,5,108,0,0,366,367,5,101,0,0,367,
        368,5,109,0,0,368,369,5,101,0,0,369,370,5,110,0,0,370,371,5,116,
        0,0,371,372,5,115,0,0,372,50,1,0,0,0,373,374,5,118,0,0,374,375,5,
        111,0,0,375,376,5,108,0,0,376,377,5,97,0,0,377,378,5,116,0,0,378,
        379,5,97,0,0,379,380,5,105,0,0,380,381,5,108,0,0,381,382,5,101,0,
        0,382,52,1,0,0,0,383,384,5,116,0,0,384,385,5,104,0,0,385,386,5,114,
        0,0,386,387,5,111,0,0,387,388,5,119,0,0,388,389,5,115,0,0,389,54,
        1,0,0,0,390,391,5,83,0,0,391,392,5,121,0,0,392,393,5,115,0,0,393,
        394,5,116,0,0,394,395,5,101,0,0,395,396,5,109,0,0,396,397,5,46,0,
        0,397,398,5,111,0,0,398,399,5,117,0,0,399,400,5,116,0,0,400,401,
        5,46,0,0,401,402,5,112,0,0,402,403,5,114,0,0,403,404,5,105,0,0,404,
        405,5,110,0,0,405,406,5,116,0,0,406,56,1,0,0,0,407,408,5,83,0,0,
        408,409,5,121,0,0,409,410,5,115,0,0,410,411,5,116,0,0,411,412,5,
        101,0,0,412,413,5,109,0,0,413,414,5,46,0,0,414,415,5,111,0,0,415,
        416,5,117,0,0,416,417,5,116,0,0,417,418,5,46,0,0,418,419,5,112,0,
        0,419,420,5,114,0,0,420,421,5,105,0,0,421,422,5,110,0,0,422,423,
        5,116,0,0,423,424,5,108,0,0,424,425,5,110,0,0,425,58,1,0,0,0,426,
        427,5,83,0,0,427,428,5,99,0,0,428,429,5,97,0,0,429,430,5,110,0,0,
        430,431,5,110,0,0,431,432,5,101,0,0,432,433,5,114,0,0,433,60,1,0,
        0,0,434,435,5,110,0,0,435,436,5,101,0,0,436,437,5,120,0,0,437,438,
        5,116,0,0,438,62,1,0,0,0,439,440,5,116,0,0,440,441,5,114,0,0,441,
        442,5,117,0,0,442,443,5,101,0,0,443,64,1,0,0,0,444,445,5,102,0,0,
        445,446,5,97,0,0,446,447,5,108,0,0,447,448,5,115,0,0,448,449,5,101,
        0,0,449,66,1,0,0,0,450,451,5,110,0,0,451,452,5,117,0,0,452,453,5,
        108,0,0,453,454,5,108,0,0,454,68,1,0,0,0,455,456,5,116,0,0,456,457,
        5,104,0,0,457,458,5,114,0,0,458,459,5,111,0,0,459,460,5,119,0,0,
        460,70,1,0,0,0,461,462,5,116,0,0,462,463,5,114,0,0,463,464,5,121,
        0,0,464,72,1,0,0,0,465,466,5,99,0,0,466,467,5,97,0,0,467,468,5,116,
        0,0,468,469,5,99,0,0,469,470,5,104,0,0,470,74,1,0,0,0,471,472,5,
        102,0,0,472,473,5,105,0,0,473,474,5,110,0,0,474,475,5,97,0,0,475,
        476,5,108,0,0,476,477,5,108,0,0,477,478,5,121,0,0,478,76,1,0,0,0,
        479,480,5,110,0,0,480,481,5,101,0,0,481,482,5,119,0,0,482,78,1,0,
        0,0,483,484,5,116,0,0,484,485,5,104,0,0,485,486,5,105,0,0,486,487,
        5,115,0,0,487,80,1,0,0,0,488,489,5,114,0,0,489,490,5,101,0,0,490,
        491,5,116,0,0,491,492,5,117,0,0,492,493,5,114,0,0,493,494,5,110,
        0,0,494,82,1,0,0,0,495,496,5,97,0,0,496,497,5,115,0,0,497,498,5,
        115,0,0,498,499,5,101,0,0,499,500,5,114,0,0,500,501,5,116,0,0,501,
        84,1,0,0,0,502,503,5,105,0,0,503,504,5,109,0,0,504,505,5,112,0,0,
        505,506,5,111,0,0,506,507,5,114,0,0,507,508,5,116,0,0,508,86,1,0,
        0,0,509,510,5,112,0,0,510,511,5,97,0,0,511,512,5,99,0,0,512,513,
        5,107,0,0,513,514,5,97,0,0,514,515,5,103,0,0,515,516,5,101,0,0,516,
        88,1,0,0,0,517,518,5,43,0,0,518,90,1,0,0,0,519,520,5,45,0,0,520,
        92,1,0,0,0,521,522,5,42,0,0,522,94,1,0,0,0,523,524,5,47,0,0,524,
        96,1,0,0,0,525,526,5,37,0,0,526,98,1,0,0,0,527,528,5,40,0,0,528,
        100,1,0,0,0,529,530,5,41,0,0,530,102,1,0,0,0,531,532,5,123,0,0,532,
        104,1,0,0,0,533,534,5,125,0,0,534,106,1,0,0,0,535,536,5,91,0,0,536,
        108,1,0,0,0,537,538,5,93,0,0,538,110,1,0,0,0,539,540,5,61,0,0,540,
        541,5,61,0,0,541,112,1,0,0,0,542,543,5,33,0,0,543,544,5,61,0,0,544,
        114,1,0,0,0,545,546,5,62,0,0,546,116,1,0,0,0,547,548,5,60,0,0,548,
        118,1,0,0,0,549,550,5,62,0,0,550,551,5,61,0,0,551,120,1,0,0,0,552,
        553,5,60,0,0,553,554,5,61,0,0,554,122,1,0,0,0,555,556,5,38,0,0,556,
        557,5,38,0,0,557,124,1,0,0,0,558,559,5,124,0,0,559,560,5,124,0,0,
        560,126,1,0,0,0,561,562,5,33,0,0,562,128,1,0,0,0,563,564,5,43,0,
        0,564,565,5,43,0,0,565,130,1,0,0,0,566,567,5,45,0,0,567,568,5,45,
        0,0,568,132,1,0,0,0,569,570,5,61,0,0,570,134,1,0,0,0,571,572,5,43,
        0,0,572,573,5,61,0,0,573,136,1,0,0,0,574,575,5,45,0,0,575,576,5,
        61,0,0,576,138,1,0,0,0,577,578,5,42,0,0,578,579,5,61,0,0,579,140,
        1,0,0,0,580,581,5,47,0,0,581,582,5,61,0,0,582,142,1,0,0,0,583,584,
        5,37,0,0,584,585,5,61,0,0,585,144,1,0,0,0,586,587,5,58,0,0,587,146,
        1,0,0,0,588,589,5,59,0,0,589,148,1,0,0,0,590,591,5,46,0,0,591,150,
        1,0,0,0,592,593,5,44,0,0,593,152,1,0,0,0,594,595,5,118,0,0,595,596,
        5,111,0,0,596,597,5,105,0,0,597,598,5,100,0,0,598,154,1,0,0,0,599,
        600,5,105,0,0,600,601,5,110,0,0,601,602,5,116,0,0,602,156,1,0,0,
        0,603,604,5,102,0,0,604,605,5,108,0,0,605,606,5,111,0,0,606,607,
        5,97,0,0,607,608,5,116,0,0,608,158,1,0,0,0,609,610,5,100,0,0,610,
        611,5,111,0,0,611,612,5,117,0,0,612,613,5,98,0,0,613,614,5,108,0,
        0,614,615,5,101,0,0,615,160,1,0,0,0,616,617,5,108,0,0,617,618,5,
        111,0,0,618,619,5,110,0,0,619,620,5,103,0,0,620,162,1,0,0,0,621,
        622,5,115,0,0,622,623,5,104,0,0,623,624,5,111,0,0,624,625,5,114,
        0,0,625,626,5,116,0,0,626,164,1,0,0,0,627,628,5,98,0,0,628,629,5,
        121,0,0,629,630,5,116,0,0,630,631,5,101,0,0,631,166,1,0,0,0,632,
        633,5,99,0,0,633,634,5,104,0,0,634,635,5,97,0,0,635,636,5,114,0,
        0,636,168,1,0,0,0,637,638,5,98,0,0,638,639,5,111,0,0,639,640,5,111,
        0,0,640,641,5,108,0,0,641,642,5,101,0,0,642,643,5,97,0,0,643,644,
        5,110,0,0,644,170,1,0,0,0,645,646,5,83,0,0,646,647,5,116,0,0,647,
        648,5,114,0,0,648,649,5,105,0,0,649,650,5,110,0,0,650,651,5,103,
        0,0,651,172,1,0,0,0,652,656,7,0,0,0,653,655,7,1,0,0,654,653,1,0,
        0,0,655,658,1,0,0,0,656,654,1,0,0,0,656,657,1,0,0,0,657,174,1,0,
        0,0,658,656,1,0,0,0,659,660,7,2,0,0,660,176,1,0,0,0,661,663,3,175,
        87,0,662,661,1,0,0,0,663,664,1,0,0,0,664,662,1,0,0,0,664,665,1,0,
        0,0,665,178,1,0,0,0,666,668,3,175,87,0,667,666,1,0,0,0,668,669,1,
        0,0,0,669,667,1,0,0,0,669,670,1,0,0,0,670,671,1,0,0,0,671,673,9,
        0,0,0,672,674,3,175,87,0,673,672,1,0,0,0,674,675,1,0,0,0,675,673,
        1,0,0,0,675,676,1,0,0,0,676,180,1,0,0,0,677,682,5,34,0,0,678,681,
        3,183,91,0,679,681,8,3,0,0,680,678,1,0,0,0,680,679,1,0,0,0,681,684,
        1,0,0,0,682,680,1,0,0,0,682,683,1,0,0,0,683,685,1,0,0,0,684,682,
        1,0,0,0,685,686,5,34,0,0,686,182,1,0,0,0,687,688,5,92,0,0,688,689,
        9,0,0,0,689,184,1,0,0,0,690,691,5,39,0,0,691,692,9,0,0,0,692,693,
        5,39,0,0,693,186,1,0,0,0,694,696,7,4,0,0,695,694,1,0,0,0,696,697,
        1,0,0,0,697,695,1,0,0,0,697,698,1,0,0,0,698,699,1,0,0,0,699,700,
        6,93,0,0,700,188,1,0,0,0,701,702,5,47,0,0,702,703,5,42,0,0,703,707,
        1,0,0,0,704,706,9,0,0,0,705,704,1,0,0,0,706,709,1,0,0,0,707,708,
        1,0,0,0,707,705,1,0,0,0,708,710,1,0,0,0,709,707,1,0,0,0,710,711,
        5,42,0,0,711,712,5,47,0,0,712,713,1,0,0,0,713,714,6,94,0,0,714,190,
        1,0,0,0,715,716,5,47,0,0,716,717,5,47,0,0,717,721,1,0,0,0,718,720,
        8,5,0,0,719,718,1,0,0,0,720,723,1,0,0,0,721,719,1,0,0,0,721,722,
        1,0,0,0,722,724,1,0,0,0,723,721,1,0,0,0,724,725,6,95,0,0,725,192,
        1,0,0,0,10,0,656,664,669,675,680,682,697,707,721,1,6,0,0
    ]

class java_grammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ARRAYLIST = 1
    LINKEDLIST = 2
    HASHSET = 3
    HASHMAP = 4
    IF = 5
    ELSE = 6
    SWITCH = 7
    CASE = 8
    WHILE = 9
    FOR = 10
    BREAK = 11
    CONTINUE = 12
    DO = 13
    CLASS = 14
    INTERFACE = 15
    ENUM = 16
    PUBLIC = 17
    PRIVATE = 18
    PROTECTED = 19
    STATIC = 20
    FINAL = 21
    ABSTRACT = 22
    DEFAULT = 23
    EXTENDS = 24
    IMPLEMENTS = 25
    VOLATAILE = 26
    THROWS = 27
    PRINT = 28
    PRINTLN = 29
    SCANNER = 30
    NEXT = 31
    TRUE = 32
    FALSE = 33
    NULL = 34
    THROW = 35
    TRY = 36
    CATCH = 37
    FINALLY = 38
    NEW = 39
    THIS = 40
    RETURN = 41
    ASSERT = 42
    IMPORT = 43
    PACKAGE = 44
    ADD = 45
    SUB = 46
    MUL = 47
    DIV = 48
    MOD = 49
    LPAREN = 50
    RPAREN = 51
    LBRACE = 52
    RBRACE = 53
    LSQUARE = 54
    RSQUARE = 55
    EQUAL = 56
    NOT_EQUAL = 57
    GREATER_THAN = 58
    LESS_THAN = 59
    GREATER_THAN_OR_EQUAL = 60
    LESS_THAN_OR_EQUAL = 61
    LOGICAL_AND = 62
    LOGICAL_OR = 63
    LOGICAL_NOT = 64
    INCREMENT = 65
    DECREMENT = 66
    ASSIGN = 67
    ADD_ASSIGN = 68
    SUB_ASSIGN = 69
    MUL_ASSIGN = 70
    DIV_ASSIGN = 71
    MOD_ASSIGN = 72
    COLON = 73
    SEMICOLON = 74
    DOT = 75
    COMMA = 76
    VOID = 77
    INT = 78
    FLOAT = 79
    DOUBLE = 80
    LONG = 81
    SHORT = 82
    BYTE = 83
    CHAR = 84
    BOOLEAN = 85
    STRING = 86
    ID = 87
    INTEGER_NUMBER = 88
    FLOAT_NUMBER = 89
    STRING_TEXT = 90
    CHARACTER = 91
    WHITESPACES = 92
    BLOCKCOMMENT = 93
    SINGLELINECOMMENT = 94

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'ArrayList'", "'LinkedList'", "'HashSet'", "'HashMap'", "'if'", 
            "'else'", "'switch'", "'case'", "'while'", "'for'", "'break'", 
            "'continue'", "'do'", "'class'", "'interface'", "'enum'", "'public'", 
            "'private'", "'protected'", "'static'", "'final'", "'abstract'", 
            "'default'", "'extends'", "'implements'", "'volataile'", "'throws'", 
            "'System.out.print'", "'System.out.println'", "'Scanner'", "'next'", 
            "'true'", "'false'", "'null'", "'throw'", "'try'", "'catch'", 
            "'finally'", "'new'", "'this'", "'return'", "'assert'", "'import'", 
            "'package'", "'+'", "'-'", "'*'", "'/'", "'%'", "'('", "')'", 
            "'{'", "'}'", "'['", "']'", "'=='", "'!='", "'>'", "'<'", "'>='", 
            "'<='", "'&&'", "'||'", "'!'", "'++'", "'--'", "'='", "'+='", 
            "'-='", "'*='", "'/='", "'%='", "':'", "';'", "'.'", "','", 
            "'void'", "'int'", "'float'", "'double'", "'long'", "'short'", 
            "'byte'", "'char'", "'boolean'", "'String'" ]

    symbolicNames = [ "<INVALID>",
            "ARRAYLIST", "LINKEDLIST", "HASHSET", "HASHMAP", "IF", "ELSE", 
            "SWITCH", "CASE", "WHILE", "FOR", "BREAK", "CONTINUE", "DO", 
            "CLASS", "INTERFACE", "ENUM", "PUBLIC", "PRIVATE", "PROTECTED", 
            "STATIC", "FINAL", "ABSTRACT", "DEFAULT", "EXTENDS", "IMPLEMENTS", 
            "VOLATAILE", "THROWS", "PRINT", "PRINTLN", "SCANNER", "NEXT", 
            "TRUE", "FALSE", "NULL", "THROW", "TRY", "CATCH", "FINALLY", 
            "NEW", "THIS", "RETURN", "ASSERT", "IMPORT", "PACKAGE", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
            "LSQUARE", "RSQUARE", "EQUAL", "NOT_EQUAL", "GREATER_THAN", 
            "LESS_THAN", "GREATER_THAN_OR_EQUAL", "LESS_THAN_OR_EQUAL", 
            "LOGICAL_AND", "LOGICAL_OR", "LOGICAL_NOT", "INCREMENT", "DECREMENT", 
            "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
            "MOD_ASSIGN", "COLON", "SEMICOLON", "DOT", "COMMA", "VOID", 
            "INT", "FLOAT", "DOUBLE", "LONG", "SHORT", "BYTE", "CHAR", "BOOLEAN", 
            "STRING", "ID", "INTEGER_NUMBER", "FLOAT_NUMBER", "STRING_TEXT", 
            "CHARACTER", "WHITESPACES", "BLOCKCOMMENT", "SINGLELINECOMMENT" ]

    ruleNames = [ "ARRAYLIST", "LINKEDLIST", "HASHSET", "HASHMAP", "IF", 
                  "ELSE", "SWITCH", "CASE", "WHILE", "FOR", "BREAK", "CONTINUE", 
                  "DO", "CLASS", "INTERFACE", "ENUM", "PUBLIC", "PRIVATE", 
                  "PROTECTED", "STATIC", "FINAL", "ABSTRACT", "DEFAULT", 
                  "EXTENDS", "IMPLEMENTS", "VOLATAILE", "THROWS", "PRINT", 
                  "PRINTLN", "SCANNER", "NEXT", "TRUE", "FALSE", "NULL", 
                  "THROW", "TRY", "CATCH", "FINALLY", "NEW", "THIS", "RETURN", 
                  "ASSERT", "IMPORT", "PACKAGE", "ADD", "SUB", "MUL", "DIV", 
                  "MOD", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LSQUARE", 
                  "RSQUARE", "EQUAL", "NOT_EQUAL", "GREATER_THAN", "LESS_THAN", 
                  "GREATER_THAN_OR_EQUAL", "LESS_THAN_OR_EQUAL", "LOGICAL_AND", 
                  "LOGICAL_OR", "LOGICAL_NOT", "INCREMENT", "DECREMENT", 
                  "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
                  "MOD_ASSIGN", "COLON", "SEMICOLON", "DOT", "COMMA", "VOID", 
                  "INT", "FLOAT", "DOUBLE", "LONG", "SHORT", "BYTE", "CHAR", 
                  "BOOLEAN", "STRING", "ID", "DIGIT", "INTEGER_NUMBER", 
                  "FLOAT_NUMBER", "STRING_TEXT", "ESC", "CHARACTER", "WHITESPACES", 
                  "BLOCKCOMMENT", "SINGLELINECOMMENT" ]

    grammarFileName = "java_grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

