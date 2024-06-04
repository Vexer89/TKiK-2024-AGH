# Generated from grammar/java_grammar.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,92,695,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,65,7,65,
        2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,71,2,72,
        7,72,1,0,1,0,5,0,149,8,0,10,0,12,0,152,9,0,1,0,1,0,4,0,156,8,0,11,
        0,12,0,157,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,3,3,171,8,
        3,1,4,3,4,174,8,4,1,4,1,4,1,4,3,4,179,8,4,1,4,3,4,182,8,4,1,4,1,
        4,1,5,1,5,5,5,188,8,5,10,5,12,5,191,9,5,1,5,1,5,1,6,1,6,1,6,1,6,
        5,6,199,8,6,10,6,12,6,202,9,6,1,7,1,7,1,7,1,7,5,7,208,8,7,10,7,12,
        7,211,9,7,1,8,1,8,1,8,1,8,3,8,217,8,8,1,9,3,9,220,8,9,1,9,1,9,1,
        9,1,9,1,10,1,10,1,10,1,10,5,10,230,8,10,10,10,12,10,233,9,10,1,10,
        1,10,1,10,1,11,3,11,239,8,11,1,11,1,11,1,11,1,11,1,12,1,12,5,12,
        247,8,12,10,12,12,12,250,9,12,1,12,1,12,1,13,1,13,1,13,3,13,257,
        8,13,1,14,3,14,260,8,14,1,14,1,14,1,14,1,15,3,15,266,8,15,1,15,3,
        15,269,8,15,1,15,1,15,1,15,1,15,3,15,275,8,15,1,15,1,15,3,15,279,
        8,15,1,15,1,15,1,16,1,16,1,16,1,16,5,16,287,8,16,10,16,12,16,290,
        9,16,1,17,1,17,1,17,5,17,295,8,17,10,17,12,17,298,9,17,1,18,1,18,
        1,18,1,19,1,19,1,20,1,20,5,20,307,8,20,10,20,12,20,310,9,20,1,20,
        1,20,1,21,1,21,1,22,1,22,1,22,1,22,3,22,320,8,22,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,3,23,354,8,23,1,24,1,24,1,24,1,24,3,24,360,8,24,1,
        24,1,24,3,24,364,8,24,1,24,1,24,3,24,368,8,24,1,24,1,24,1,24,1,24,
        1,24,3,24,375,8,24,1,25,1,25,1,25,1,25,3,25,381,8,25,1,25,1,25,3,
        25,385,8,25,1,25,1,25,3,25,389,8,25,1,25,1,25,1,25,1,25,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,3,26,403,8,26,1,26,1,26,3,26,407,8,
        26,1,26,1,26,3,26,411,8,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,
        27,1,28,1,28,3,28,423,8,28,1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,
        30,3,30,433,8,30,1,31,1,31,1,31,3,31,438,8,31,1,32,1,32,1,32,1,32,
        1,32,1,33,1,33,1,33,1,33,1,33,1,33,1,34,1,34,5,34,453,8,34,10,34,
        12,34,456,9,34,1,34,1,34,1,35,4,35,461,8,35,11,35,12,35,462,1,35,
        1,35,1,36,1,36,1,36,1,36,1,36,1,36,3,36,473,8,36,1,37,1,37,1,37,
        4,37,478,8,37,11,37,12,37,479,1,37,3,37,483,8,37,1,37,3,37,486,8,
        37,1,38,1,38,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,40,1,40,1,40,1,
        41,1,41,1,41,1,41,3,41,504,8,41,1,41,1,41,1,42,1,42,1,42,1,43,1,
        43,1,43,1,44,1,44,1,44,3,44,517,8,44,1,44,1,44,1,45,1,45,3,45,523,
        8,45,1,46,1,46,1,46,1,46,1,46,1,46,1,46,5,46,532,8,46,10,46,12,46,
        535,9,46,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,
        1,47,3,47,549,8,47,1,48,1,48,1,48,1,49,1,49,1,50,1,50,1,50,1,50,
        1,50,1,50,1,50,5,50,563,8,50,10,50,12,50,566,9,50,1,51,1,51,1,51,
        1,51,1,51,1,51,1,51,3,51,575,8,51,1,52,1,52,1,52,1,53,1,53,1,54,
        3,54,583,8,54,1,54,1,54,1,54,1,54,1,54,1,54,1,54,3,54,592,8,54,1,
        55,1,55,1,56,1,56,1,57,1,57,1,57,3,57,601,8,57,1,57,1,57,1,57,1,
        57,1,58,1,58,1,58,1,59,1,59,1,59,1,60,1,60,1,60,3,60,616,8,60,1,
        60,1,60,5,60,620,8,60,10,60,12,60,623,9,60,1,60,1,60,1,61,1,61,1,
        61,3,61,630,8,61,1,62,1,62,1,63,4,63,635,8,63,11,63,12,63,636,1,
        64,1,64,1,65,4,65,642,8,65,11,65,12,65,643,1,66,1,66,1,67,1,67,1,
        67,1,67,3,67,652,8,67,1,67,1,67,1,67,1,68,1,68,1,69,1,69,1,69,1,
        69,1,69,1,69,1,70,1,70,1,70,1,70,1,70,1,70,1,70,1,70,1,70,1,70,1,
        70,1,70,1,70,1,70,1,71,1,71,1,71,3,71,682,8,71,1,71,3,71,685,8,71,
        1,72,1,72,1,72,5,72,690,8,72,10,72,12,72,693,9,72,1,72,0,2,92,100,
        73,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,
        88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,120,122,
        124,126,128,130,132,134,136,138,140,142,144,0,10,1,0,54,61,1,0,43,
        44,1,0,43,47,1,0,65,70,3,0,30,32,84,84,86,87,1,0,76,84,2,0,17,20,
        22,22,1,0,21,22,1,0,1,4,1,0,26,27,718,0,150,1,0,0,0,2,159,1,0,0,
        0,4,163,1,0,0,0,6,170,1,0,0,0,8,173,1,0,0,0,10,185,1,0,0,0,12,194,
        1,0,0,0,14,203,1,0,0,0,16,216,1,0,0,0,18,219,1,0,0,0,20,225,1,0,
        0,0,22,238,1,0,0,0,24,244,1,0,0,0,26,256,1,0,0,0,28,259,1,0,0,0,
        30,265,1,0,0,0,32,282,1,0,0,0,34,291,1,0,0,0,36,299,1,0,0,0,38,302,
        1,0,0,0,40,304,1,0,0,0,42,313,1,0,0,0,44,315,1,0,0,0,46,353,1,0,
        0,0,48,355,1,0,0,0,50,376,1,0,0,0,52,394,1,0,0,0,54,412,1,0,0,0,
        56,422,1,0,0,0,58,424,1,0,0,0,60,432,1,0,0,0,62,437,1,0,0,0,64,439,
        1,0,0,0,66,444,1,0,0,0,68,450,1,0,0,0,70,460,1,0,0,0,72,472,1,0,
        0,0,74,474,1,0,0,0,76,487,1,0,0,0,78,493,1,0,0,0,80,496,1,0,0,0,
        82,499,1,0,0,0,84,507,1,0,0,0,86,510,1,0,0,0,88,513,1,0,0,0,90,522,
        1,0,0,0,92,524,1,0,0,0,94,548,1,0,0,0,96,550,1,0,0,0,98,553,1,0,
        0,0,100,555,1,0,0,0,102,574,1,0,0,0,104,576,1,0,0,0,106,579,1,0,
        0,0,108,582,1,0,0,0,110,593,1,0,0,0,112,595,1,0,0,0,114,597,1,0,
        0,0,116,606,1,0,0,0,118,609,1,0,0,0,120,612,1,0,0,0,122,629,1,0,
        0,0,124,631,1,0,0,0,126,634,1,0,0,0,128,638,1,0,0,0,130,641,1,0,
        0,0,132,645,1,0,0,0,134,647,1,0,0,0,136,656,1,0,0,0,138,658,1,0,
        0,0,140,664,1,0,0,0,142,684,1,0,0,0,144,686,1,0,0,0,146,149,3,2,
        1,0,147,149,3,4,2,0,148,146,1,0,0,0,148,147,1,0,0,0,149,152,1,0,
        0,0,150,148,1,0,0,0,150,151,1,0,0,0,151,153,1,0,0,0,152,150,1,0,
        0,0,153,155,5,17,0,0,154,156,3,6,3,0,155,154,1,0,0,0,156,157,1,0,
        0,0,157,155,1,0,0,0,157,158,1,0,0,0,158,1,1,0,0,0,159,160,5,41,0,
        0,160,161,3,144,72,0,161,162,5,72,0,0,162,3,1,0,0,0,163,164,5,42,
        0,0,164,165,3,144,72,0,165,166,5,72,0,0,166,5,1,0,0,0,167,171,3,
        8,4,0,168,171,3,22,11,0,169,171,3,18,9,0,170,167,1,0,0,0,170,168,
        1,0,0,0,170,169,1,0,0,0,171,7,1,0,0,0,172,174,3,130,65,0,173,172,
        1,0,0,0,173,174,1,0,0,0,174,175,1,0,0,0,175,176,5,14,0,0,176,178,
        5,85,0,0,177,179,3,12,6,0,178,177,1,0,0,0,178,179,1,0,0,0,179,181,
        1,0,0,0,180,182,3,14,7,0,181,180,1,0,0,0,181,182,1,0,0,0,182,183,
        1,0,0,0,183,184,3,10,5,0,184,9,1,0,0,0,185,189,5,50,0,0,186,188,
        3,16,8,0,187,186,1,0,0,0,188,191,1,0,0,0,189,187,1,0,0,0,189,190,
        1,0,0,0,190,192,1,0,0,0,191,189,1,0,0,0,192,193,5,51,0,0,193,11,
        1,0,0,0,194,195,5,23,0,0,195,200,5,85,0,0,196,197,5,74,0,0,197,199,
        5,85,0,0,198,196,1,0,0,0,199,202,1,0,0,0,200,198,1,0,0,0,200,201,
        1,0,0,0,201,13,1,0,0,0,202,200,1,0,0,0,203,204,5,24,0,0,204,209,
        5,85,0,0,205,206,5,74,0,0,206,208,5,85,0,0,207,205,1,0,0,0,208,211,
        1,0,0,0,209,207,1,0,0,0,209,210,1,0,0,0,210,15,1,0,0,0,211,209,1,
        0,0,0,212,217,3,28,14,0,213,217,3,30,15,0,214,217,3,8,4,0,215,217,
        3,22,11,0,216,212,1,0,0,0,216,213,1,0,0,0,216,214,1,0,0,0,216,215,
        1,0,0,0,217,17,1,0,0,0,218,220,5,22,0,0,219,218,1,0,0,0,219,220,
        1,0,0,0,220,221,1,0,0,0,221,222,5,16,0,0,222,223,5,85,0,0,223,224,
        3,20,10,0,224,19,1,0,0,0,225,226,5,50,0,0,226,231,5,85,0,0,227,228,
        5,74,0,0,228,230,5,85,0,0,229,227,1,0,0,0,230,233,1,0,0,0,231,229,
        1,0,0,0,231,232,1,0,0,0,232,234,1,0,0,0,233,231,1,0,0,0,234,235,
        5,72,0,0,235,236,5,51,0,0,236,21,1,0,0,0,237,239,5,22,0,0,238,237,
        1,0,0,0,238,239,1,0,0,0,239,240,1,0,0,0,240,241,5,15,0,0,241,242,
        5,85,0,0,242,243,3,24,12,0,243,23,1,0,0,0,244,248,5,50,0,0,245,247,
        3,26,13,0,246,245,1,0,0,0,247,250,1,0,0,0,248,246,1,0,0,0,248,249,
        1,0,0,0,249,251,1,0,0,0,250,248,1,0,0,0,251,252,5,51,0,0,252,25,
        1,0,0,0,253,257,3,28,14,0,254,257,3,30,15,0,255,257,3,22,11,0,256,
        253,1,0,0,0,256,254,1,0,0,0,256,255,1,0,0,0,257,27,1,0,0,0,258,260,
        3,126,63,0,259,258,1,0,0,0,259,260,1,0,0,0,260,261,1,0,0,0,261,262,
        3,44,22,0,262,263,5,72,0,0,263,29,1,0,0,0,264,266,3,126,63,0,265,
        264,1,0,0,0,265,266,1,0,0,0,266,268,1,0,0,0,267,269,5,21,0,0,268,
        267,1,0,0,0,268,269,1,0,0,0,269,270,1,0,0,0,270,271,3,122,61,0,271,
        272,5,85,0,0,272,274,5,48,0,0,273,275,3,34,17,0,274,273,1,0,0,0,
        274,275,1,0,0,0,275,276,1,0,0,0,276,278,5,49,0,0,277,279,3,32,16,
        0,278,277,1,0,0,0,278,279,1,0,0,0,279,280,1,0,0,0,280,281,3,38,19,
        0,281,31,1,0,0,0,282,283,5,25,0,0,283,288,5,85,0,0,284,285,5,74,
        0,0,285,287,5,85,0,0,286,284,1,0,0,0,287,290,1,0,0,0,288,286,1,0,
        0,0,288,289,1,0,0,0,289,33,1,0,0,0,290,288,1,0,0,0,291,296,3,36,
        18,0,292,293,5,74,0,0,293,295,3,36,18,0,294,292,1,0,0,0,295,298,
        1,0,0,0,296,294,1,0,0,0,296,297,1,0,0,0,297,35,1,0,0,0,298,296,1,
        0,0,0,299,300,3,122,61,0,300,301,5,85,0,0,301,37,1,0,0,0,302,303,
        3,40,20,0,303,39,1,0,0,0,304,308,5,50,0,0,305,307,3,42,21,0,306,
        305,1,0,0,0,307,310,1,0,0,0,308,306,1,0,0,0,308,309,1,0,0,0,309,
        311,1,0,0,0,310,308,1,0,0,0,311,312,5,51,0,0,312,41,1,0,0,0,313,
        314,3,46,23,0,314,43,1,0,0,0,315,316,3,122,61,0,316,319,5,85,0,0,
        317,318,5,65,0,0,318,320,3,112,56,0,319,317,1,0,0,0,319,320,1,0,
        0,0,320,45,1,0,0,0,321,354,3,48,24,0,322,354,3,50,25,0,323,354,3,
        52,26,0,324,354,3,54,27,0,325,354,3,66,33,0,326,354,3,74,37,0,327,
        354,3,82,41,0,328,354,3,84,42,0,329,354,3,86,43,0,330,354,3,88,44,
        0,331,332,3,90,45,0,332,333,5,72,0,0,333,354,1,0,0,0,334,354,3,40,
        20,0,335,336,3,108,54,0,336,337,5,72,0,0,337,354,1,0,0,0,338,339,
        3,116,58,0,339,340,5,72,0,0,340,354,1,0,0,0,341,342,3,118,59,0,342,
        343,5,72,0,0,343,354,1,0,0,0,344,345,3,120,60,0,345,346,5,72,0,0,
        346,354,1,0,0,0,347,348,3,138,69,0,348,349,5,72,0,0,349,354,1,0,
        0,0,350,351,3,140,70,0,351,352,5,72,0,0,352,354,1,0,0,0,353,321,
        1,0,0,0,353,322,1,0,0,0,353,323,1,0,0,0,353,324,1,0,0,0,353,325,
        1,0,0,0,353,326,1,0,0,0,353,327,1,0,0,0,353,328,1,0,0,0,353,329,
        1,0,0,0,353,330,1,0,0,0,353,331,1,0,0,0,353,334,1,0,0,0,353,335,
        1,0,0,0,353,338,1,0,0,0,353,341,1,0,0,0,353,344,1,0,0,0,353,347,
        1,0,0,0,353,350,1,0,0,0,354,47,1,0,0,0,355,367,5,5,0,0,356,368,3,
        92,46,0,357,359,5,48,0,0,358,360,5,62,0,0,359,358,1,0,0,0,359,360,
        1,0,0,0,360,363,1,0,0,0,361,364,3,142,71,0,362,364,3,112,56,0,363,
        361,1,0,0,0,363,362,1,0,0,0,364,365,1,0,0,0,365,366,5,49,0,0,366,
        368,1,0,0,0,367,356,1,0,0,0,367,357,1,0,0,0,368,369,1,0,0,0,369,
        370,5,50,0,0,370,371,3,46,23,0,371,374,5,51,0,0,372,373,5,6,0,0,
        373,375,3,46,23,0,374,372,1,0,0,0,374,375,1,0,0,0,375,49,1,0,0,0,
        376,388,5,9,0,0,377,389,3,92,46,0,378,380,5,48,0,0,379,381,5,62,
        0,0,380,379,1,0,0,0,380,381,1,0,0,0,381,384,1,0,0,0,382,385,3,142,
        71,0,383,385,3,112,56,0,384,382,1,0,0,0,384,383,1,0,0,0,385,386,
        1,0,0,0,386,387,5,49,0,0,387,389,1,0,0,0,388,377,1,0,0,0,388,378,
        1,0,0,0,389,390,1,0,0,0,390,391,5,50,0,0,391,392,3,46,23,0,392,393,
        5,51,0,0,393,51,1,0,0,0,394,395,5,13,0,0,395,396,5,50,0,0,396,397,
        3,46,23,0,397,398,5,51,0,0,398,410,5,9,0,0,399,411,3,92,46,0,400,
        402,5,48,0,0,401,403,5,62,0,0,402,401,1,0,0,0,402,403,1,0,0,0,403,
        406,1,0,0,0,404,407,3,142,71,0,405,407,3,112,56,0,406,404,1,0,0,
        0,406,405,1,0,0,0,407,408,1,0,0,0,408,409,5,49,0,0,409,411,1,0,0,
        0,410,399,1,0,0,0,410,400,1,0,0,0,411,53,1,0,0,0,412,413,5,10,0,
        0,413,414,5,48,0,0,414,415,3,56,28,0,415,416,5,49,0,0,416,417,5,
        50,0,0,417,418,3,46,23,0,418,419,5,51,0,0,419,55,1,0,0,0,420,423,
        3,64,32,0,421,423,3,58,29,0,422,420,1,0,0,0,422,421,1,0,0,0,423,
        57,1,0,0,0,424,425,3,60,30,0,425,426,5,72,0,0,426,427,3,92,46,0,
        427,428,5,72,0,0,428,429,3,62,31,0,429,59,1,0,0,0,430,433,3,108,
        54,0,431,433,3,142,71,0,432,430,1,0,0,0,432,431,1,0,0,0,433,61,1,
        0,0,0,434,438,3,100,50,0,435,438,3,116,58,0,436,438,3,118,59,0,437,
        434,1,0,0,0,437,435,1,0,0,0,437,436,1,0,0,0,438,63,1,0,0,0,439,440,
        3,122,61,0,440,441,5,85,0,0,441,442,5,71,0,0,442,443,3,142,71,0,
        443,65,1,0,0,0,444,445,5,7,0,0,445,446,5,48,0,0,446,447,3,142,71,
        0,447,448,5,49,0,0,448,449,3,68,34,0,449,67,1,0,0,0,450,454,5,50,
        0,0,451,453,3,70,35,0,452,451,1,0,0,0,453,456,1,0,0,0,454,452,1,
        0,0,0,454,455,1,0,0,0,455,457,1,0,0,0,456,454,1,0,0,0,457,458,5,
        51,0,0,458,69,1,0,0,0,459,461,3,72,36,0,460,459,1,0,0,0,461,462,
        1,0,0,0,462,460,1,0,0,0,462,463,1,0,0,0,463,464,1,0,0,0,464,465,
        3,40,20,0,465,71,1,0,0,0,466,467,5,8,0,0,467,468,3,112,56,0,468,
        469,5,71,0,0,469,473,1,0,0,0,470,471,5,22,0,0,471,473,5,71,0,0,472,
        466,1,0,0,0,472,470,1,0,0,0,473,73,1,0,0,0,474,475,5,34,0,0,475,
        485,3,40,20,0,476,478,3,76,38,0,477,476,1,0,0,0,478,479,1,0,0,0,
        479,477,1,0,0,0,479,480,1,0,0,0,480,482,1,0,0,0,481,483,3,80,40,
        0,482,481,1,0,0,0,482,483,1,0,0,0,483,486,1,0,0,0,484,486,3,80,40,
        0,485,477,1,0,0,0,485,484,1,0,0,0,486,75,1,0,0,0,487,488,5,35,0,
        0,488,489,5,48,0,0,489,490,3,78,39,0,490,491,5,49,0,0,491,492,3,
        40,20,0,492,77,1,0,0,0,493,494,3,122,61,0,494,495,5,85,0,0,495,79,
        1,0,0,0,496,497,5,36,0,0,497,498,3,40,20,0,498,81,1,0,0,0,499,503,
        5,39,0,0,500,504,3,90,45,0,501,504,3,142,71,0,502,504,3,112,56,0,
        503,500,1,0,0,0,503,501,1,0,0,0,503,502,1,0,0,0,503,504,1,0,0,0,
        504,505,1,0,0,0,505,506,5,72,0,0,506,83,1,0,0,0,507,508,5,11,0,0,
        508,509,5,72,0,0,509,85,1,0,0,0,510,511,5,12,0,0,511,512,5,72,0,
        0,512,87,1,0,0,0,513,516,5,33,0,0,514,517,5,85,0,0,515,517,3,114,
        57,0,516,514,1,0,0,0,516,515,1,0,0,0,517,518,1,0,0,0,518,519,5,72,
        0,0,519,89,1,0,0,0,520,523,3,92,46,0,521,523,3,100,50,0,522,520,
        1,0,0,0,522,521,1,0,0,0,523,91,1,0,0,0,524,525,6,46,-1,0,525,526,
        3,94,47,0,526,533,1,0,0,0,527,528,10,1,0,0,528,529,3,98,49,0,529,
        530,3,94,47,0,530,532,1,0,0,0,531,527,1,0,0,0,532,535,1,0,0,0,533,
        531,1,0,0,0,533,534,1,0,0,0,534,93,1,0,0,0,535,533,1,0,0,0,536,549,
        3,142,71,0,537,549,3,112,56,0,538,549,3,96,48,0,539,540,5,48,0,0,
        540,541,3,92,46,0,541,542,5,49,0,0,542,549,1,0,0,0,543,544,5,48,
        0,0,544,545,3,100,50,0,545,546,5,49,0,0,546,549,1,0,0,0,547,549,
        3,100,50,0,548,536,1,0,0,0,548,537,1,0,0,0,548,538,1,0,0,0,548,539,
        1,0,0,0,548,543,1,0,0,0,548,547,1,0,0,0,549,95,1,0,0,0,550,551,5,
        62,0,0,551,552,3,94,47,0,552,97,1,0,0,0,553,554,7,0,0,0,554,99,1,
        0,0,0,555,556,6,50,-1,0,556,557,3,102,51,0,557,564,1,0,0,0,558,559,
        10,1,0,0,559,560,3,106,53,0,560,561,3,102,51,0,561,563,1,0,0,0,562,
        558,1,0,0,0,563,566,1,0,0,0,564,562,1,0,0,0,564,565,1,0,0,0,565,
        101,1,0,0,0,566,564,1,0,0,0,567,575,3,142,71,0,568,575,3,112,56,
        0,569,575,3,104,52,0,570,571,5,48,0,0,571,572,3,100,50,0,572,573,
        5,49,0,0,573,575,1,0,0,0,574,567,1,0,0,0,574,568,1,0,0,0,574,569,
        1,0,0,0,574,570,1,0,0,0,575,103,1,0,0,0,576,577,7,1,0,0,577,578,
        3,102,51,0,578,105,1,0,0,0,579,580,7,2,0,0,580,107,1,0,0,0,581,583,
        3,122,61,0,582,581,1,0,0,0,582,583,1,0,0,0,583,584,1,0,0,0,584,585,
        3,142,71,0,585,591,3,110,55,0,586,592,3,142,71,0,587,592,3,112,56,
        0,588,592,3,114,57,0,589,592,3,90,45,0,590,592,3,120,60,0,591,586,
        1,0,0,0,591,587,1,0,0,0,591,588,1,0,0,0,591,589,1,0,0,0,591,590,
        1,0,0,0,592,109,1,0,0,0,593,594,7,3,0,0,594,111,1,0,0,0,595,596,
        7,4,0,0,596,113,1,0,0,0,597,600,5,37,0,0,598,601,5,85,0,0,599,601,
        3,134,67,0,600,598,1,0,0,0,600,599,1,0,0,0,601,602,1,0,0,0,602,603,
        5,48,0,0,603,604,3,34,17,0,604,605,5,49,0,0,605,115,1,0,0,0,606,
        607,3,142,71,0,607,608,5,63,0,0,608,117,1,0,0,0,609,610,3,142,71,
        0,610,611,5,64,0,0,611,119,1,0,0,0,612,613,3,142,71,0,613,615,5,
        48,0,0,614,616,3,142,71,0,615,614,1,0,0,0,615,616,1,0,0,0,616,621,
        1,0,0,0,617,618,5,74,0,0,618,620,3,142,71,0,619,617,1,0,0,0,620,
        623,1,0,0,0,621,619,1,0,0,0,621,622,1,0,0,0,622,624,1,0,0,0,623,
        621,1,0,0,0,624,625,5,49,0,0,625,121,1,0,0,0,626,630,3,124,62,0,
        627,630,5,75,0,0,628,630,3,134,67,0,629,626,1,0,0,0,629,627,1,0,
        0,0,629,628,1,0,0,0,630,123,1,0,0,0,631,632,7,5,0,0,632,125,1,0,
        0,0,633,635,3,128,64,0,634,633,1,0,0,0,635,636,1,0,0,0,636,634,1,
        0,0,0,636,637,1,0,0,0,637,127,1,0,0,0,638,639,7,6,0,0,639,129,1,
        0,0,0,640,642,3,132,66,0,641,640,1,0,0,0,642,643,1,0,0,0,643,641,
        1,0,0,0,643,644,1,0,0,0,644,131,1,0,0,0,645,646,7,7,0,0,646,133,
        1,0,0,0,647,648,3,136,68,0,648,651,5,57,0,0,649,652,3,124,62,0,650,
        652,5,85,0,0,651,649,1,0,0,0,651,650,1,0,0,0,652,653,1,0,0,0,653,
        654,5,56,0,0,654,655,5,85,0,0,655,135,1,0,0,0,656,657,7,8,0,0,657,
        137,1,0,0,0,658,659,7,9,0,0,659,660,5,48,0,0,660,661,3,90,45,0,661,
        662,5,49,0,0,662,663,5,72,0,0,663,139,1,0,0,0,664,665,3,122,61,0,
        665,666,5,85,0,0,666,667,5,65,0,0,667,668,5,37,0,0,668,669,5,28,
        0,0,669,670,5,48,0,0,670,671,3,90,45,0,671,672,5,49,0,0,672,673,
        5,73,0,0,673,674,5,29,0,0,674,675,5,48,0,0,675,676,5,49,0,0,676,
        677,5,72,0,0,677,141,1,0,0,0,678,685,5,38,0,0,679,680,5,38,0,0,680,
        682,5,74,0,0,681,679,1,0,0,0,681,682,1,0,0,0,682,683,1,0,0,0,683,
        685,3,144,72,0,684,678,1,0,0,0,684,681,1,0,0,0,685,143,1,0,0,0,686,
        691,5,85,0,0,687,688,5,74,0,0,688,690,5,85,0,0,689,687,1,0,0,0,690,
        693,1,0,0,0,691,689,1,0,0,0,691,692,1,0,0,0,692,145,1,0,0,0,693,
        691,1,0,0,0,64,148,150,157,170,173,178,181,189,200,209,216,219,231,
        238,248,256,259,265,268,274,278,288,296,308,319,353,359,363,367,
        374,380,384,388,402,406,410,422,432,437,454,462,472,479,482,485,
        503,516,522,533,548,564,574,582,591,600,615,621,629,636,643,651,
        681,684,691
    ]

class java_grammarParser ( Parser ):

    grammarFileName = "java_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'ArrayList'", "'LinkedList'", "'HashSet'", 
                     "'HashMap'", "'if'", "'else'", "'switch'", "'case'", 
                     "'while'", "'for'", "'break'", "'continue'", "'do'", 
                     "'class'", "'interface'", "'enum'", "'public'", "'private'", 
                     "'protected'", "'static'", "'abstract'", "'default'", 
                     "'extends'", "'implements'", "'throws'", "'System.out.print'", 
                     "'System.out.println'", "'Scanner'", "'next'", "'true'", 
                     "'false'", "'null'", "'throw'", "'try'", "'catch'", 
                     "'finally'", "'new'", "'this'", "'return'", "'assert'", 
                     "'import'", "'package'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'('", "')'", "'{'", "'}'", "'['", "']'", "'=='", 
                     "'!='", "'>'", "'<'", "'>='", "'<='", "'&&'", "'||'", 
                     "'!'", "'++'", "'--'", "'='", "'+='", "'-='", "'*='", 
                     "'/='", "'%='", "':'", "';'", "'.'", "','", "'void'", 
                     "'int'", "'float'", "'double'", "'long'", "'short'", 
                     "'byte'", "'char'", "'boolean'", "'String'" ]

    symbolicNames = [ "<INVALID>", "ARRAYLIST", "LINKEDLIST", "HASHSET", 
                      "HASHMAP", "IF", "ELSE", "SWITCH", "CASE", "WHILE", 
                      "FOR", "BREAK", "CONTINUE", "DO", "CLASS", "INTERFACE", 
                      "ENUM", "PUBLIC", "PRIVATE", "PROTECTED", "STATIC", 
                      "ABSTRACT", "DEFAULT", "EXTENDS", "IMPLEMENTS", "THROWS", 
                      "PRINT", "PRINTLN", "SCANNER", "NEXT", "TRUE", "FALSE", 
                      "NULL", "THROW", "TRY", "CATCH", "FINALLY", "NEW", 
                      "THIS", "RETURN", "ASSERT", "IMPORT", "PACKAGE", "ADD", 
                      "SUB", "MUL", "DIV", "MOD", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "LSQUARE", "RSQUARE", "EQUAL", "NOT_EQUAL", 
                      "GREATER_THAN", "LESS_THAN", "GREATER_THAN_OR_EQUAL", 
                      "LESS_THAN_OR_EQUAL", "LOGICAL_AND", "LOGICAL_OR", 
                      "LOGICAL_NOT", "INCREMENT", "DECREMENT", "ASSIGN", 
                      "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
                      "MOD_ASSIGN", "COLON", "SEMICOLON", "DOT", "COMMA", 
                      "VOID", "INT", "FLOAT", "DOUBLE", "LONG", "SHORT", 
                      "BYTE", "CHAR", "BOOLEAN", "STRING", "ID", "INTEGER_NUMBER", 
                      "FLOAT_NUMBER", "STRING_TEXT", "CHARACTER", "WHITESPACES", 
                      "BLOCKCOMMENT", "SINGLELINECOMMENT" ]

    RULE_program = 0
    RULE_importDeclaration = 1
    RULE_packageDeclaration = 2
    RULE_structerDeclaration = 3
    RULE_classDeclaration = 4
    RULE_classBody = 5
    RULE_superClass = 6
    RULE_interfaces = 7
    RULE_classMemberDeclaration = 8
    RULE_enumDeclaration = 9
    RULE_enumBody = 10
    RULE_interfaceDeclaration = 11
    RULE_interfaceBody = 12
    RULE_interfaceMemberDeclaration = 13
    RULE_fieldDeclaration = 14
    RULE_methodDeclaration = 15
    RULE_throwedExeption = 16
    RULE_formalParameters = 17
    RULE_formalParameter = 18
    RULE_methodBody = 19
    RULE_block = 20
    RULE_blockStatement = 21
    RULE_variableDeclarators = 22
    RULE_statement = 23
    RULE_ifStatement = 24
    RULE_whileStatement = 25
    RULE_doWhileStatement = 26
    RULE_forStatement = 27
    RULE_forControl = 28
    RULE_traditionalForControl = 29
    RULE_forInit = 30
    RULE_forUpdate = 31
    RULE_enhancedForControl = 32
    RULE_switchStatement = 33
    RULE_switchBlock = 34
    RULE_switchBlockStatementGroup = 35
    RULE_switchLabel = 36
    RULE_tryStatement = 37
    RULE_catchClause = 38
    RULE_catchFormalParameter = 39
    RULE_finallyBlock = 40
    RULE_returnStatement = 41
    RULE_breakStatement = 42
    RULE_continueStatement = 43
    RULE_throwStatement = 44
    RULE_expression = 45
    RULE_logicalExpression = 46
    RULE_logicalTerm = 47
    RULE_unaryLogicalExpression = 48
    RULE_logicalOperator = 49
    RULE_arithmeticExpression = 50
    RULE_arithmeticTerm = 51
    RULE_unaryArithmeticExpression = 52
    RULE_arithmeticOperator = 53
    RULE_assignmentStatement = 54
    RULE_assignmentOperator = 55
    RULE_literal = 56
    RULE_newInstance = 57
    RULE_incrementStatement = 58
    RULE_decrementStatement = 59
    RULE_functionCall = 60
    RULE_type = 61
    RULE_dataType = 62
    RULE_modifiers = 63
    RULE_modifier = 64
    RULE_classModifiers = 65
    RULE_classModifier = 66
    RULE_dataStructerDeclaration = 67
    RULE_dataStructers = 68
    RULE_printStatement = 69
    RULE_inputStatement = 70
    RULE_extendedIDwithThis = 71
    RULE_extendedID = 72

    ruleNames =  [ "program", "importDeclaration", "packageDeclaration", 
                   "structerDeclaration", "classDeclaration", "classBody", 
                   "superClass", "interfaces", "classMemberDeclaration", 
                   "enumDeclaration", "enumBody", "interfaceDeclaration", 
                   "interfaceBody", "interfaceMemberDeclaration", "fieldDeclaration", 
                   "methodDeclaration", "throwedExeption", "formalParameters", 
                   "formalParameter", "methodBody", "block", "blockStatement", 
                   "variableDeclarators", "statement", "ifStatement", "whileStatement", 
                   "doWhileStatement", "forStatement", "forControl", "traditionalForControl", 
                   "forInit", "forUpdate", "enhancedForControl", "switchStatement", 
                   "switchBlock", "switchBlockStatementGroup", "switchLabel", 
                   "tryStatement", "catchClause", "catchFormalParameter", 
                   "finallyBlock", "returnStatement", "breakStatement", 
                   "continueStatement", "throwStatement", "expression", 
                   "logicalExpression", "logicalTerm", "unaryLogicalExpression", 
                   "logicalOperator", "arithmeticExpression", "arithmeticTerm", 
                   "unaryArithmeticExpression", "arithmeticOperator", "assignmentStatement", 
                   "assignmentOperator", "literal", "newInstance", "incrementStatement", 
                   "decrementStatement", "functionCall", "type", "dataType", 
                   "modifiers", "modifier", "classModifiers", "classModifier", 
                   "dataStructerDeclaration", "dataStructers", "printStatement", 
                   "inputStatement", "extendedIDwithThis", "extendedID" ]

    EOF = Token.EOF
    ARRAYLIST=1
    LINKEDLIST=2
    HASHSET=3
    HASHMAP=4
    IF=5
    ELSE=6
    SWITCH=7
    CASE=8
    WHILE=9
    FOR=10
    BREAK=11
    CONTINUE=12
    DO=13
    CLASS=14
    INTERFACE=15
    ENUM=16
    PUBLIC=17
    PRIVATE=18
    PROTECTED=19
    STATIC=20
    ABSTRACT=21
    DEFAULT=22
    EXTENDS=23
    IMPLEMENTS=24
    THROWS=25
    PRINT=26
    PRINTLN=27
    SCANNER=28
    NEXT=29
    TRUE=30
    FALSE=31
    NULL=32
    THROW=33
    TRY=34
    CATCH=35
    FINALLY=36
    NEW=37
    THIS=38
    RETURN=39
    ASSERT=40
    IMPORT=41
    PACKAGE=42
    ADD=43
    SUB=44
    MUL=45
    DIV=46
    MOD=47
    LPAREN=48
    RPAREN=49
    LBRACE=50
    RBRACE=51
    LSQUARE=52
    RSQUARE=53
    EQUAL=54
    NOT_EQUAL=55
    GREATER_THAN=56
    LESS_THAN=57
    GREATER_THAN_OR_EQUAL=58
    LESS_THAN_OR_EQUAL=59
    LOGICAL_AND=60
    LOGICAL_OR=61
    LOGICAL_NOT=62
    INCREMENT=63
    DECREMENT=64
    ASSIGN=65
    ADD_ASSIGN=66
    SUB_ASSIGN=67
    MUL_ASSIGN=68
    DIV_ASSIGN=69
    MOD_ASSIGN=70
    COLON=71
    SEMICOLON=72
    DOT=73
    COMMA=74
    VOID=75
    INT=76
    FLOAT=77
    DOUBLE=78
    LONG=79
    SHORT=80
    BYTE=81
    CHAR=82
    BOOLEAN=83
    STRING=84
    ID=85
    INTEGER_NUMBER=86
    FLOAT_NUMBER=87
    STRING_TEXT=88
    CHARACTER=89
    WHITESPACES=90
    BLOCKCOMMENT=91
    SINGLELINECOMMENT=92

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUBLIC(self):
            return self.getToken(java_grammarParser.PUBLIC, 0)

        def importDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(java_grammarParser.ImportDeclarationContext)
            else:
                return self.getTypedRuleContext(java_grammarParser.ImportDeclarationContext,i)


        def packageDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(java_grammarParser.PackageDeclarationContext)
            else:
                return self.getTypedRuleContext(java_grammarParser.PackageDeclarationContext,i)


        def structerDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(java_grammarParser.StructerDeclarationContext)
            else:
                return self.getTypedRuleContext(java_grammarParser.StructerDeclarationContext,i)


        def getRuleIndex(self):
            return java_grammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = java_grammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41 or _la==42:
                self.state = 148
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [41]:
                    self.state = 146
                    self.importDeclaration()
                    pass
                elif token in [42]:
                    self.state = 147
                    self.packageDeclaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 153
            self.match(java_grammarParser.PUBLIC)
            self.state = 155 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 154
                self.structerDeclaration()
                self.state = 157 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6406144) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(java_grammarParser.IMPORT, 0)

        def extendedID(self):
            return self.getTypedRuleContext(java_grammarParser.ExtendedIDContext,0)


        def SEMICOLON(self):
            return self.getToken(java_grammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_importDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportDeclaration" ):
                listener.enterImportDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportDeclaration" ):
                listener.exitImportDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportDeclaration" ):
                return visitor.visitImportDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def importDeclaration(self):

        localctx = java_grammarParser.ImportDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_importDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(java_grammarParser.IMPORT)
            self.state = 160
            self.extendedID()
            self.state = 161
            self.match(java_grammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PackageDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PACKAGE(self):
            return self.getToken(java_grammarParser.PACKAGE, 0)

        def extendedID(self):
            return self.getTypedRuleContext(java_grammarParser.ExtendedIDContext,0)


        def SEMICOLON(self):
            return self.getToken(java_grammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_packageDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPackageDeclaration" ):
                listener.enterPackageDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPackageDeclaration" ):
                listener.exitPackageDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPackageDeclaration" ):
                return visitor.visitPackageDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def packageDeclaration(self):

        localctx = java_grammarParser.PackageDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_packageDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(java_grammarParser.PACKAGE)
            self.state = 164
            self.extendedID()
            self.state = 165
            self.match(java_grammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructerDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDeclaration(self):
            return self.getTypedRuleContext(java_grammarParser.ClassDeclarationContext,0)


        def interfaceDeclaration(self):
            return self.getTypedRuleContext(java_grammarParser.InterfaceDeclarationContext,0)


        def enumDeclaration(self):
            return self.getTypedRuleContext(java_grammarParser.EnumDeclarationContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_structerDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructerDeclaration" ):
                listener.enterStructerDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructerDeclaration" ):
                listener.exitStructerDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructerDeclaration" ):
                return visitor.visitStructerDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def structerDeclaration(self):

        localctx = java_grammarParser.StructerDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_structerDeclaration)
        try:
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.classDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.interfaceDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 169
                self.enumDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(java_grammarParser.CLASS, 0)

        def ID(self):
            return self.getToken(java_grammarParser.ID, 0)

        def classBody(self):
            return self.getTypedRuleContext(java_grammarParser.ClassBodyContext,0)


        def classModifiers(self):
            return self.getTypedRuleContext(java_grammarParser.ClassModifiersContext,0)


        def superClass(self):
            return self.getTypedRuleContext(java_grammarParser.SuperClassContext,0)


        def interfaces(self):
            return self.getTypedRuleContext(java_grammarParser.InterfacesContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_classDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDeclaration" ):
                listener.enterClassDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDeclaration" ):
                listener.exitClassDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDeclaration" ):
                return visitor.visitClassDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def classDeclaration(self):

        localctx = java_grammarParser.ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_classDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21 or _la==22:
                self.state = 172
                self.classModifiers()


            self.state = 175
            self.match(java_grammarParser.CLASS)
            self.state = 176
            self.match(java_grammarParser.ID)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 177
                self.superClass()


            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 180
                self.interfaces()


            self.state = 183
            self.classBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(java_grammarParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(java_grammarParser.RBRACE, 0)

        def classMemberDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(java_grammarParser.ClassMemberDeclarationContext)
            else:
                return self.getTypedRuleContext(java_grammarParser.ClassMemberDeclarationContext,i)


        def getRuleIndex(self):
            return java_grammarParser.RULE_classBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassBody" ):
                listener.enterClassBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassBody" ):
                listener.exitClassBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassBody" ):
                return visitor.visitClassBody(self)
            else:
                return visitor.visitChildren(self)




    def classBody(self):

        localctx = java_grammarParser.ClassBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_classBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(java_grammarParser.LBRACE)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8306718) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & 1023) != 0):
                self.state = 186
                self.classMemberDeclaration()
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 192
            self.match(java_grammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuperClassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXTENDS(self):
            return self.getToken(java_grammarParser.EXTENDS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(java_grammarParser.ID)
            else:
                return self.getToken(java_grammarParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(java_grammarParser.COMMA)
            else:
                return self.getToken(java_grammarParser.COMMA, i)

        def getRuleIndex(self):
            return java_grammarParser.RULE_superClass

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuperClass" ):
                listener.enterSuperClass(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuperClass" ):
                listener.exitSuperClass(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuperClass" ):
                return visitor.visitSuperClass(self)
            else:
                return visitor.visitChildren(self)




    def superClass(self):

        localctx = java_grammarParser.SuperClassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_superClass)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(java_grammarParser.EXTENDS)
            self.state = 195
            self.match(java_grammarParser.ID)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==74:
                self.state = 196
                self.match(java_grammarParser.COMMA)
                self.state = 197
                self.match(java_grammarParser.ID)
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfacesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPLEMENTS(self):
            return self.getToken(java_grammarParser.IMPLEMENTS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(java_grammarParser.ID)
            else:
                return self.getToken(java_grammarParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(java_grammarParser.COMMA)
            else:
                return self.getToken(java_grammarParser.COMMA, i)

        def getRuleIndex(self):
            return java_grammarParser.RULE_interfaces

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaces" ):
                listener.enterInterfaces(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaces" ):
                listener.exitInterfaces(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaces" ):
                return visitor.visitInterfaces(self)
            else:
                return visitor.visitChildren(self)




    def interfaces(self):

        localctx = java_grammarParser.InterfacesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_interfaces)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(java_grammarParser.IMPLEMENTS)
            self.state = 204
            self.match(java_grammarParser.ID)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==74:
                self.state = 205
                self.match(java_grammarParser.COMMA)
                self.state = 206
                self.match(java_grammarParser.ID)
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassMemberDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldDeclaration(self):
            return self.getTypedRuleContext(java_grammarParser.FieldDeclarationContext,0)


        def methodDeclaration(self):
            return self.getTypedRuleContext(java_grammarParser.MethodDeclarationContext,0)


        def classDeclaration(self):
            return self.getTypedRuleContext(java_grammarParser.ClassDeclarationContext,0)


        def interfaceDeclaration(self):
            return self.getTypedRuleContext(java_grammarParser.InterfaceDeclarationContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_classMemberDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassMemberDeclaration" ):
                listener.enterClassMemberDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassMemberDeclaration" ):
                listener.exitClassMemberDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassMemberDeclaration" ):
                return visitor.visitClassMemberDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def classMemberDeclaration(self):

        localctx = java_grammarParser.ClassMemberDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_classMemberDeclaration)
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.fieldDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.methodDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 214
                self.classDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 215
                self.interfaceDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENUM(self):
            return self.getToken(java_grammarParser.ENUM, 0)

        def ID(self):
            return self.getToken(java_grammarParser.ID, 0)

        def enumBody(self):
            return self.getTypedRuleContext(java_grammarParser.EnumBodyContext,0)


        def DEFAULT(self):
            return self.getToken(java_grammarParser.DEFAULT, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_enumDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumDeclaration" ):
                listener.enterEnumDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumDeclaration" ):
                listener.exitEnumDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumDeclaration" ):
                return visitor.visitEnumDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def enumDeclaration(self):

        localctx = java_grammarParser.EnumDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_enumDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 218
                self.match(java_grammarParser.DEFAULT)


            self.state = 221
            self.match(java_grammarParser.ENUM)
            self.state = 222
            self.match(java_grammarParser.ID)
            self.state = 223
            self.enumBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(java_grammarParser.LBRACE, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(java_grammarParser.ID)
            else:
                return self.getToken(java_grammarParser.ID, i)

        def SEMICOLON(self):
            return self.getToken(java_grammarParser.SEMICOLON, 0)

        def RBRACE(self):
            return self.getToken(java_grammarParser.RBRACE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(java_grammarParser.COMMA)
            else:
                return self.getToken(java_grammarParser.COMMA, i)

        def getRuleIndex(self):
            return java_grammarParser.RULE_enumBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumBody" ):
                listener.enterEnumBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumBody" ):
                listener.exitEnumBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumBody" ):
                return visitor.visitEnumBody(self)
            else:
                return visitor.visitChildren(self)




    def enumBody(self):

        localctx = java_grammarParser.EnumBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_enumBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(java_grammarParser.LBRACE)
            self.state = 226
            self.match(java_grammarParser.ID)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==74:
                self.state = 227
                self.match(java_grammarParser.COMMA)
                self.state = 228
                self.match(java_grammarParser.ID)
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 234
            self.match(java_grammarParser.SEMICOLON)
            self.state = 235
            self.match(java_grammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERFACE(self):
            return self.getToken(java_grammarParser.INTERFACE, 0)

        def ID(self):
            return self.getToken(java_grammarParser.ID, 0)

        def interfaceBody(self):
            return self.getTypedRuleContext(java_grammarParser.InterfaceBodyContext,0)


        def DEFAULT(self):
            return self.getToken(java_grammarParser.DEFAULT, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_interfaceDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceDeclaration" ):
                listener.enterInterfaceDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceDeclaration" ):
                listener.exitInterfaceDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceDeclaration" ):
                return visitor.visitInterfaceDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def interfaceDeclaration(self):

        localctx = java_grammarParser.InterfaceDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_interfaceDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 237
                self.match(java_grammarParser.DEFAULT)


            self.state = 240
            self.match(java_grammarParser.INTERFACE)
            self.state = 241
            self.match(java_grammarParser.ID)
            self.state = 242
            self.interfaceBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(java_grammarParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(java_grammarParser.RBRACE, 0)

        def interfaceMemberDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(java_grammarParser.InterfaceMemberDeclarationContext)
            else:
                return self.getTypedRuleContext(java_grammarParser.InterfaceMemberDeclarationContext,i)


        def getRuleIndex(self):
            return java_grammarParser.RULE_interfaceBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceBody" ):
                listener.enterInterfaceBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceBody" ):
                listener.exitInterfaceBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceBody" ):
                return visitor.visitInterfaceBody(self)
            else:
                return visitor.visitChildren(self)




    def interfaceBody(self):

        localctx = java_grammarParser.InterfaceBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_interfaceBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(java_grammarParser.LBRACE)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8290334) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & 1023) != 0):
                self.state = 245
                self.interfaceMemberDeclaration()
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 251
            self.match(java_grammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceMemberDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldDeclaration(self):
            return self.getTypedRuleContext(java_grammarParser.FieldDeclarationContext,0)


        def methodDeclaration(self):
            return self.getTypedRuleContext(java_grammarParser.MethodDeclarationContext,0)


        def interfaceDeclaration(self):
            return self.getTypedRuleContext(java_grammarParser.InterfaceDeclarationContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_interfaceMemberDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceMemberDeclaration" ):
                listener.enterInterfaceMemberDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceMemberDeclaration" ):
                listener.exitInterfaceMemberDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceMemberDeclaration" ):
                return visitor.visitInterfaceMemberDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def interfaceMemberDeclaration(self):

        localctx = java_grammarParser.InterfaceMemberDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_interfaceMemberDeclaration)
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.fieldDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.methodDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 255
                self.interfaceDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclarators(self):
            return self.getTypedRuleContext(java_grammarParser.VariableDeclaratorsContext,0)


        def SEMICOLON(self):
            return self.getToken(java_grammarParser.SEMICOLON, 0)

        def modifiers(self):
            return self.getTypedRuleContext(java_grammarParser.ModifiersContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_fieldDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldDeclaration" ):
                listener.enterFieldDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldDeclaration" ):
                listener.exitFieldDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldDeclaration" ):
                return visitor.visitFieldDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def fieldDeclaration(self):

        localctx = java_grammarParser.FieldDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_fieldDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 6160384) != 0):
                self.state = 258
                self.modifiers()


            self.state = 261
            self.variableDeclarators()
            self.state = 262
            self.match(java_grammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(java_grammarParser.TypeContext,0)


        def ID(self):
            return self.getToken(java_grammarParser.ID, 0)

        def LPAREN(self):
            return self.getToken(java_grammarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(java_grammarParser.RPAREN, 0)

        def methodBody(self):
            return self.getTypedRuleContext(java_grammarParser.MethodBodyContext,0)


        def modifiers(self):
            return self.getTypedRuleContext(java_grammarParser.ModifiersContext,0)


        def ABSTRACT(self):
            return self.getToken(java_grammarParser.ABSTRACT, 0)

        def formalParameters(self):
            return self.getTypedRuleContext(java_grammarParser.FormalParametersContext,0)


        def throwedExeption(self):
            return self.getTypedRuleContext(java_grammarParser.ThrowedExeptionContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_methodDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDeclaration" ):
                listener.enterMethodDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDeclaration" ):
                listener.exitMethodDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDeclaration" ):
                return visitor.visitMethodDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def methodDeclaration(self):

        localctx = java_grammarParser.MethodDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_methodDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 6160384) != 0):
                self.state = 264
                self.modifiers()


            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 267
                self.match(java_grammarParser.ABSTRACT)


            self.state = 270
            self.type_()
            self.state = 271
            self.match(java_grammarParser.ID)
            self.state = 272
            self.match(java_grammarParser.LPAREN)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & 1023) != 0):
                self.state = 273
                self.formalParameters()


            self.state = 276
            self.match(java_grammarParser.RPAREN)
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 277
                self.throwedExeption()


            self.state = 280
            self.methodBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThrowedExeptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THROWS(self):
            return self.getToken(java_grammarParser.THROWS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(java_grammarParser.ID)
            else:
                return self.getToken(java_grammarParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(java_grammarParser.COMMA)
            else:
                return self.getToken(java_grammarParser.COMMA, i)

        def getRuleIndex(self):
            return java_grammarParser.RULE_throwedExeption

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThrowedExeption" ):
                listener.enterThrowedExeption(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThrowedExeption" ):
                listener.exitThrowedExeption(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThrowedExeption" ):
                return visitor.visitThrowedExeption(self)
            else:
                return visitor.visitChildren(self)




    def throwedExeption(self):

        localctx = java_grammarParser.ThrowedExeptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_throwedExeption)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(java_grammarParser.THROWS)
            self.state = 283
            self.match(java_grammarParser.ID)
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==74:
                self.state = 284
                self.match(java_grammarParser.COMMA)
                self.state = 285
                self.match(java_grammarParser.ID)
                self.state = 290
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formalParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(java_grammarParser.FormalParameterContext)
            else:
                return self.getTypedRuleContext(java_grammarParser.FormalParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(java_grammarParser.COMMA)
            else:
                return self.getToken(java_grammarParser.COMMA, i)

        def getRuleIndex(self):
            return java_grammarParser.RULE_formalParameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameters" ):
                listener.enterFormalParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameters" ):
                listener.exitFormalParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormalParameters" ):
                return visitor.visitFormalParameters(self)
            else:
                return visitor.visitChildren(self)




    def formalParameters(self):

        localctx = java_grammarParser.FormalParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_formalParameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.formalParameter()
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==74:
                self.state = 292
                self.match(java_grammarParser.COMMA)
                self.state = 293
                self.formalParameter()
                self.state = 298
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(java_grammarParser.TypeContext,0)


        def ID(self):
            return self.getToken(java_grammarParser.ID, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_formalParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameter" ):
                listener.enterFormalParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameter" ):
                listener.exitFormalParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormalParameter" ):
                return visitor.visitFormalParameter(self)
            else:
                return visitor.visitChildren(self)




    def formalParameter(self):

        localctx = java_grammarParser.FormalParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_formalParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.type_()
            self.state = 300
            self.match(java_grammarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(java_grammarParser.BlockContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_methodBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodBody" ):
                listener.enterMethodBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodBody" ):
                listener.exitMethodBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodBody" ):
                return visitor.visitMethodBody(self)
            else:
                return visitor.visitChildren(self)




    def methodBody(self):

        localctx = java_grammarParser.MethodBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_methodBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(java_grammarParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(java_grammarParser.RBRACE, 0)

        def blockStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(java_grammarParser.BlockStatementContext)
            else:
                return self.getTypedRuleContext(java_grammarParser.BlockStatementContext,i)


        def getRuleIndex(self):
            return java_grammarParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = java_grammarParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(java_grammarParser.LBRACE)
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4613120639711067838) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & 8191) != 0):
                self.state = 305
                self.blockStatement()
                self.state = 310
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 311
            self.match(java_grammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(java_grammarParser.StatementContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_blockStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStatement" ):
                listener.enterBlockStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStatement" ):
                listener.exitBlockStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatement" ):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def blockStatement(self):

        localctx = java_grammarParser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_blockStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclaratorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(java_grammarParser.TypeContext,0)


        def ID(self):
            return self.getToken(java_grammarParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(java_grammarParser.ASSIGN, 0)

        def literal(self):
            return self.getTypedRuleContext(java_grammarParser.LiteralContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_variableDeclarators

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclarators" ):
                listener.enterVariableDeclarators(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclarators" ):
                listener.exitVariableDeclarators(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclarators" ):
                return visitor.visitVariableDeclarators(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclarators(self):

        localctx = java_grammarParser.VariableDeclaratorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_variableDeclarators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.type_()
            self.state = 316
            self.match(java_grammarParser.ID)
            self.state = 319
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==65:
                self.state = 317
                self.match(java_grammarParser.ASSIGN)
                self.state = 318
                self.literal()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStatement(self):
            return self.getTypedRuleContext(java_grammarParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(java_grammarParser.WhileStatementContext,0)


        def doWhileStatement(self):
            return self.getTypedRuleContext(java_grammarParser.DoWhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(java_grammarParser.ForStatementContext,0)


        def switchStatement(self):
            return self.getTypedRuleContext(java_grammarParser.SwitchStatementContext,0)


        def tryStatement(self):
            return self.getTypedRuleContext(java_grammarParser.TryStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(java_grammarParser.ReturnStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(java_grammarParser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(java_grammarParser.ContinueStatementContext,0)


        def throwStatement(self):
            return self.getTypedRuleContext(java_grammarParser.ThrowStatementContext,0)


        def expression(self):
            return self.getTypedRuleContext(java_grammarParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(java_grammarParser.SEMICOLON, 0)

        def block(self):
            return self.getTypedRuleContext(java_grammarParser.BlockContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(java_grammarParser.AssignmentStatementContext,0)


        def incrementStatement(self):
            return self.getTypedRuleContext(java_grammarParser.IncrementStatementContext,0)


        def decrementStatement(self):
            return self.getTypedRuleContext(java_grammarParser.DecrementStatementContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(java_grammarParser.FunctionCallContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(java_grammarParser.PrintStatementContext,0)


        def inputStatement(self):
            return self.getTypedRuleContext(java_grammarParser.InputStatementContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = java_grammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_statement)
        try:
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.ifStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.whileStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 323
                self.doWhileStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 324
                self.forStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 325
                self.switchStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 326
                self.tryStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 327
                self.returnStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 328
                self.breakStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 329
                self.continueStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 330
                self.throwStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 331
                self.expression()
                self.state = 332
                self.match(java_grammarParser.SEMICOLON)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 334
                self.block()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 335
                self.assignmentStatement()
                self.state = 336
                self.match(java_grammarParser.SEMICOLON)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 338
                self.incrementStatement()
                self.state = 339
                self.match(java_grammarParser.SEMICOLON)
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 341
                self.decrementStatement()
                self.state = 342
                self.match(java_grammarParser.SEMICOLON)
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 344
                self.functionCall()
                self.state = 345
                self.match(java_grammarParser.SEMICOLON)
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 347
                self.printStatement()
                self.state = 348
                self.match(java_grammarParser.SEMICOLON)
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 350
                self.inputStatement()
                self.state = 351
                self.match(java_grammarParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(java_grammarParser.IF, 0)

        def LBRACE(self):
            return self.getToken(java_grammarParser.LBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(java_grammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(java_grammarParser.StatementContext,i)


        def RBRACE(self):
            return self.getToken(java_grammarParser.RBRACE, 0)

        def logicalExpression(self):
            return self.getTypedRuleContext(java_grammarParser.LogicalExpressionContext,0)


        def LPAREN(self):
            return self.getToken(java_grammarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(java_grammarParser.RPAREN, 0)

        def ELSE(self):
            return self.getToken(java_grammarParser.ELSE, 0)

        def extendedIDwithThis(self):
            return self.getTypedRuleContext(java_grammarParser.ExtendedIDwithThisContext,0)


        def literal(self):
            return self.getTypedRuleContext(java_grammarParser.LiteralContext,0)


        def LOGICAL_NOT(self):
            return self.getToken(java_grammarParser.LOGICAL_NOT, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = java_grammarParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(java_grammarParser.IF)
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 356
                self.logicalExpression(0)
                pass

            elif la_ == 2:
                self.state = 357
                self.match(java_grammarParser.LPAREN)
                self.state = 359
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==62:
                    self.state = 358
                    self.match(java_grammarParser.LOGICAL_NOT)


                self.state = 363
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [38, 85]:
                    self.state = 361
                    self.extendedIDwithThis()
                    pass
                elif token in [30, 31, 32, 84, 86, 87]:
                    self.state = 362
                    self.literal()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 365
                self.match(java_grammarParser.RPAREN)
                pass


            self.state = 369
            self.match(java_grammarParser.LBRACE)
            self.state = 370
            self.statement()
            self.state = 371
            self.match(java_grammarParser.RBRACE)
            self.state = 374
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 372
                self.match(java_grammarParser.ELSE)
                self.state = 373
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(java_grammarParser.WHILE, 0)

        def LBRACE(self):
            return self.getToken(java_grammarParser.LBRACE, 0)

        def statement(self):
            return self.getTypedRuleContext(java_grammarParser.StatementContext,0)


        def RBRACE(self):
            return self.getToken(java_grammarParser.RBRACE, 0)

        def logicalExpression(self):
            return self.getTypedRuleContext(java_grammarParser.LogicalExpressionContext,0)


        def LPAREN(self):
            return self.getToken(java_grammarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(java_grammarParser.RPAREN, 0)

        def extendedIDwithThis(self):
            return self.getTypedRuleContext(java_grammarParser.ExtendedIDwithThisContext,0)


        def literal(self):
            return self.getTypedRuleContext(java_grammarParser.LiteralContext,0)


        def LOGICAL_NOT(self):
            return self.getToken(java_grammarParser.LOGICAL_NOT, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = java_grammarParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(java_grammarParser.WHILE)
            self.state = 388
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 377
                self.logicalExpression(0)
                pass

            elif la_ == 2:
                self.state = 378
                self.match(java_grammarParser.LPAREN)
                self.state = 380
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==62:
                    self.state = 379
                    self.match(java_grammarParser.LOGICAL_NOT)


                self.state = 384
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [38, 85]:
                    self.state = 382
                    self.extendedIDwithThis()
                    pass
                elif token in [30, 31, 32, 84, 86, 87]:
                    self.state = 383
                    self.literal()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 386
                self.match(java_grammarParser.RPAREN)
                pass


            self.state = 390
            self.match(java_grammarParser.LBRACE)
            self.state = 391
            self.statement()
            self.state = 392
            self.match(java_grammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(java_grammarParser.DO, 0)

        def LBRACE(self):
            return self.getToken(java_grammarParser.LBRACE, 0)

        def statement(self):
            return self.getTypedRuleContext(java_grammarParser.StatementContext,0)


        def RBRACE(self):
            return self.getToken(java_grammarParser.RBRACE, 0)

        def WHILE(self):
            return self.getToken(java_grammarParser.WHILE, 0)

        def logicalExpression(self):
            return self.getTypedRuleContext(java_grammarParser.LogicalExpressionContext,0)


        def LPAREN(self):
            return self.getToken(java_grammarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(java_grammarParser.RPAREN, 0)

        def extendedIDwithThis(self):
            return self.getTypedRuleContext(java_grammarParser.ExtendedIDwithThisContext,0)


        def literal(self):
            return self.getTypedRuleContext(java_grammarParser.LiteralContext,0)


        def LOGICAL_NOT(self):
            return self.getToken(java_grammarParser.LOGICAL_NOT, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_doWhileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoWhileStatement" ):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoWhileStatement" ):
                listener.exitDoWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoWhileStatement" ):
                return visitor.visitDoWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def doWhileStatement(self):

        localctx = java_grammarParser.DoWhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_doWhileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(java_grammarParser.DO)
            self.state = 395
            self.match(java_grammarParser.LBRACE)
            self.state = 396
            self.statement()
            self.state = 397
            self.match(java_grammarParser.RBRACE)
            self.state = 398
            self.match(java_grammarParser.WHILE)
            self.state = 410
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 399
                self.logicalExpression(0)
                pass

            elif la_ == 2:
                self.state = 400
                self.match(java_grammarParser.LPAREN)
                self.state = 402
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==62:
                    self.state = 401
                    self.match(java_grammarParser.LOGICAL_NOT)


                self.state = 406
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [38, 85]:
                    self.state = 404
                    self.extendedIDwithThis()
                    pass
                elif token in [30, 31, 32, 84, 86, 87]:
                    self.state = 405
                    self.literal()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 408
                self.match(java_grammarParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(java_grammarParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(java_grammarParser.LPAREN, 0)

        def forControl(self):
            return self.getTypedRuleContext(java_grammarParser.ForControlContext,0)


        def RPAREN(self):
            return self.getToken(java_grammarParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(java_grammarParser.LBRACE, 0)

        def statement(self):
            return self.getTypedRuleContext(java_grammarParser.StatementContext,0)


        def RBRACE(self):
            return self.getToken(java_grammarParser.RBRACE, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = java_grammarParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(java_grammarParser.FOR)
            self.state = 413
            self.match(java_grammarParser.LPAREN)
            self.state = 414
            self.forControl()
            self.state = 415
            self.match(java_grammarParser.RPAREN)
            self.state = 416
            self.match(java_grammarParser.LBRACE)
            self.state = 417
            self.statement()
            self.state = 418
            self.match(java_grammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForControlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enhancedForControl(self):
            return self.getTypedRuleContext(java_grammarParser.EnhancedForControlContext,0)


        def traditionalForControl(self):
            return self.getTypedRuleContext(java_grammarParser.TraditionalForControlContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_forControl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForControl" ):
                listener.enterForControl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForControl" ):
                listener.exitForControl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForControl" ):
                return visitor.visitForControl(self)
            else:
                return visitor.visitChildren(self)




    def forControl(self):

        localctx = java_grammarParser.ForControlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_forControl)
        try:
            self.state = 422
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 420
                self.enhancedForControl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 421
                self.traditionalForControl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TraditionalForControlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forInit(self):
            return self.getTypedRuleContext(java_grammarParser.ForInitContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(java_grammarParser.SEMICOLON)
            else:
                return self.getToken(java_grammarParser.SEMICOLON, i)

        def logicalExpression(self):
            return self.getTypedRuleContext(java_grammarParser.LogicalExpressionContext,0)


        def forUpdate(self):
            return self.getTypedRuleContext(java_grammarParser.ForUpdateContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_traditionalForControl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTraditionalForControl" ):
                listener.enterTraditionalForControl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTraditionalForControl" ):
                listener.exitTraditionalForControl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTraditionalForControl" ):
                return visitor.visitTraditionalForControl(self)
            else:
                return visitor.visitChildren(self)




    def traditionalForControl(self):

        localctx = java_grammarParser.TraditionalForControlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_traditionalForControl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.forInit()
            self.state = 425
            self.match(java_grammarParser.SEMICOLON)
            self.state = 426
            self.logicalExpression(0)
            self.state = 427
            self.match(java_grammarParser.SEMICOLON)
            self.state = 428
            self.forUpdate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentStatement(self):
            return self.getTypedRuleContext(java_grammarParser.AssignmentStatementContext,0)


        def extendedIDwithThis(self):
            return self.getTypedRuleContext(java_grammarParser.ExtendedIDwithThisContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_forInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInit" ):
                listener.enterForInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInit" ):
                listener.exitForInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInit" ):
                return visitor.visitForInit(self)
            else:
                return visitor.visitChildren(self)




    def forInit(self):

        localctx = java_grammarParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_forInit)
        try:
            self.state = 432
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.assignmentStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 431
                self.extendedIDwithThis()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForUpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmeticExpression(self):
            return self.getTypedRuleContext(java_grammarParser.ArithmeticExpressionContext,0)


        def incrementStatement(self):
            return self.getTypedRuleContext(java_grammarParser.IncrementStatementContext,0)


        def decrementStatement(self):
            return self.getTypedRuleContext(java_grammarParser.DecrementStatementContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_forUpdate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForUpdate" ):
                listener.enterForUpdate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForUpdate" ):
                listener.exitForUpdate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForUpdate" ):
                return visitor.visitForUpdate(self)
            else:
                return visitor.visitChildren(self)




    def forUpdate(self):

        localctx = java_grammarParser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 434
                self.arithmeticExpression(0)
                pass

            elif la_ == 2:
                self.state = 435
                self.incrementStatement()
                pass

            elif la_ == 3:
                self.state = 436
                self.decrementStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnhancedForControlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(java_grammarParser.TypeContext,0)


        def ID(self):
            return self.getToken(java_grammarParser.ID, 0)

        def COLON(self):
            return self.getToken(java_grammarParser.COLON, 0)

        def extendedIDwithThis(self):
            return self.getTypedRuleContext(java_grammarParser.ExtendedIDwithThisContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_enhancedForControl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnhancedForControl" ):
                listener.enterEnhancedForControl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnhancedForControl" ):
                listener.exitEnhancedForControl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnhancedForControl" ):
                return visitor.visitEnhancedForControl(self)
            else:
                return visitor.visitChildren(self)




    def enhancedForControl(self):

        localctx = java_grammarParser.EnhancedForControlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_enhancedForControl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.type_()
            self.state = 440
            self.match(java_grammarParser.ID)
            self.state = 441
            self.match(java_grammarParser.COLON)
            self.state = 442
            self.extendedIDwithThis()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(java_grammarParser.SWITCH, 0)

        def LPAREN(self):
            return self.getToken(java_grammarParser.LPAREN, 0)

        def extendedIDwithThis(self):
            return self.getTypedRuleContext(java_grammarParser.ExtendedIDwithThisContext,0)


        def RPAREN(self):
            return self.getToken(java_grammarParser.RPAREN, 0)

        def switchBlock(self):
            return self.getTypedRuleContext(java_grammarParser.SwitchBlockContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_switchStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStatement" ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStatement" ):
                listener.exitSwitchStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchStatement" ):
                return visitor.visitSwitchStatement(self)
            else:
                return visitor.visitChildren(self)




    def switchStatement(self):

        localctx = java_grammarParser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_switchStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(java_grammarParser.SWITCH)
            self.state = 445
            self.match(java_grammarParser.LPAREN)
            self.state = 446
            self.extendedIDwithThis()
            self.state = 447
            self.match(java_grammarParser.RPAREN)
            self.state = 448
            self.switchBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(java_grammarParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(java_grammarParser.RBRACE, 0)

        def switchBlockStatementGroup(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(java_grammarParser.SwitchBlockStatementGroupContext)
            else:
                return self.getTypedRuleContext(java_grammarParser.SwitchBlockStatementGroupContext,i)


        def getRuleIndex(self):
            return java_grammarParser.RULE_switchBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchBlock" ):
                listener.enterSwitchBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchBlock" ):
                listener.exitSwitchBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchBlock" ):
                return visitor.visitSwitchBlock(self)
            else:
                return visitor.visitChildren(self)




    def switchBlock(self):

        localctx = java_grammarParser.SwitchBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_switchBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(java_grammarParser.LBRACE)
            self.state = 454
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8 or _la==22:
                self.state = 451
                self.switchBlockStatementGroup()
                self.state = 456
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 457
            self.match(java_grammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchBlockStatementGroupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(java_grammarParser.BlockContext,0)


        def switchLabel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(java_grammarParser.SwitchLabelContext)
            else:
                return self.getTypedRuleContext(java_grammarParser.SwitchLabelContext,i)


        def getRuleIndex(self):
            return java_grammarParser.RULE_switchBlockStatementGroup

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchBlockStatementGroup" ):
                listener.enterSwitchBlockStatementGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchBlockStatementGroup" ):
                listener.exitSwitchBlockStatementGroup(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchBlockStatementGroup" ):
                return visitor.visitSwitchBlockStatementGroup(self)
            else:
                return visitor.visitChildren(self)




    def switchBlockStatementGroup(self):

        localctx = java_grammarParser.SwitchBlockStatementGroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_switchBlockStatementGroup)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 459
                self.switchLabel()
                self.state = 462 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==8 or _la==22):
                    break

            self.state = 464
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchLabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(java_grammarParser.CASE, 0)

        def literal(self):
            return self.getTypedRuleContext(java_grammarParser.LiteralContext,0)


        def COLON(self):
            return self.getToken(java_grammarParser.COLON, 0)

        def DEFAULT(self):
            return self.getToken(java_grammarParser.DEFAULT, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_switchLabel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchLabel" ):
                listener.enterSwitchLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchLabel" ):
                listener.exitSwitchLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchLabel" ):
                return visitor.visitSwitchLabel(self)
            else:
                return visitor.visitChildren(self)




    def switchLabel(self):

        localctx = java_grammarParser.SwitchLabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_switchLabel)
        try:
            self.state = 472
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 466
                self.match(java_grammarParser.CASE)
                self.state = 467
                self.literal()
                self.state = 468
                self.match(java_grammarParser.COLON)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 470
                self.match(java_grammarParser.DEFAULT)
                self.state = 471
                self.match(java_grammarParser.COLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TryStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRY(self):
            return self.getToken(java_grammarParser.TRY, 0)

        def block(self):
            return self.getTypedRuleContext(java_grammarParser.BlockContext,0)


        def finallyBlock(self):
            return self.getTypedRuleContext(java_grammarParser.FinallyBlockContext,0)


        def catchClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(java_grammarParser.CatchClauseContext)
            else:
                return self.getTypedRuleContext(java_grammarParser.CatchClauseContext,i)


        def getRuleIndex(self):
            return java_grammarParser.RULE_tryStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTryStatement" ):
                listener.enterTryStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTryStatement" ):
                listener.exitTryStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTryStatement" ):
                return visitor.visitTryStatement(self)
            else:
                return visitor.visitChildren(self)




    def tryStatement(self):

        localctx = java_grammarParser.TryStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_tryStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(java_grammarParser.TRY)
            self.state = 475
            self.block()
            self.state = 485
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                self.state = 477 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 476
                    self.catchClause()
                    self.state = 479 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==35):
                        break

                self.state = 482
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 481
                    self.finallyBlock()


                pass
            elif token in [36]:
                self.state = 484
                self.finallyBlock()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CatchClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CATCH(self):
            return self.getToken(java_grammarParser.CATCH, 0)

        def LPAREN(self):
            return self.getToken(java_grammarParser.LPAREN, 0)

        def catchFormalParameter(self):
            return self.getTypedRuleContext(java_grammarParser.CatchFormalParameterContext,0)


        def RPAREN(self):
            return self.getToken(java_grammarParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(java_grammarParser.BlockContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_catchClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatchClause" ):
                listener.enterCatchClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatchClause" ):
                listener.exitCatchClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCatchClause" ):
                return visitor.visitCatchClause(self)
            else:
                return visitor.visitChildren(self)




    def catchClause(self):

        localctx = java_grammarParser.CatchClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_catchClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.match(java_grammarParser.CATCH)
            self.state = 488
            self.match(java_grammarParser.LPAREN)
            self.state = 489
            self.catchFormalParameter()
            self.state = 490
            self.match(java_grammarParser.RPAREN)
            self.state = 491
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CatchFormalParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(java_grammarParser.TypeContext,0)


        def ID(self):
            return self.getToken(java_grammarParser.ID, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_catchFormalParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatchFormalParameter" ):
                listener.enterCatchFormalParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatchFormalParameter" ):
                listener.exitCatchFormalParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCatchFormalParameter" ):
                return visitor.visitCatchFormalParameter(self)
            else:
                return visitor.visitChildren(self)




    def catchFormalParameter(self):

        localctx = java_grammarParser.CatchFormalParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_catchFormalParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            self.type_()
            self.state = 494
            self.match(java_grammarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FinallyBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINALLY(self):
            return self.getToken(java_grammarParser.FINALLY, 0)

        def block(self):
            return self.getTypedRuleContext(java_grammarParser.BlockContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_finallyBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinallyBlock" ):
                listener.enterFinallyBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinallyBlock" ):
                listener.exitFinallyBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFinallyBlock" ):
                return visitor.visitFinallyBlock(self)
            else:
                return visitor.visitChildren(self)




    def finallyBlock(self):

        localctx = java_grammarParser.FinallyBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_finallyBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            self.match(java_grammarParser.FINALLY)
            self.state = 497
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(java_grammarParser.RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(java_grammarParser.SEMICOLON, 0)

        def expression(self):
            return self.getTypedRuleContext(java_grammarParser.ExpressionContext,0)


        def extendedIDwithThis(self):
            return self.getTypedRuleContext(java_grammarParser.ExtendedIDwithThisContext,0)


        def literal(self):
            return self.getTypedRuleContext(java_grammarParser.LiteralContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = java_grammarParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.match(java_grammarParser.RETURN)
            self.state = 503
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 500
                self.expression()

            elif la_ == 2:
                self.state = 501
                self.extendedIDwithThis()

            elif la_ == 3:
                self.state = 502
                self.literal()


            self.state = 505
            self.match(java_grammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(java_grammarParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(java_grammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_breakStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = java_grammarParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(java_grammarParser.BREAK)
            self.state = 508
            self.match(java_grammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(java_grammarParser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(java_grammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_continueStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStatement" ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStatement" ):
                listener.exitContinueStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = java_grammarParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.match(java_grammarParser.CONTINUE)
            self.state = 511
            self.match(java_grammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThrowStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THROW(self):
            return self.getToken(java_grammarParser.THROW, 0)

        def SEMICOLON(self):
            return self.getToken(java_grammarParser.SEMICOLON, 0)

        def ID(self):
            return self.getToken(java_grammarParser.ID, 0)

        def newInstance(self):
            return self.getTypedRuleContext(java_grammarParser.NewInstanceContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_throwStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThrowStatement" ):
                listener.enterThrowStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThrowStatement" ):
                listener.exitThrowStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThrowStatement" ):
                return visitor.visitThrowStatement(self)
            else:
                return visitor.visitChildren(self)




    def throwStatement(self):

        localctx = java_grammarParser.ThrowStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_throwStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.match(java_grammarParser.THROW)
            self.state = 516
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [85]:
                self.state = 514
                self.match(java_grammarParser.ID)
                pass
            elif token in [37]:
                self.state = 515
                self.newInstance()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 518
            self.match(java_grammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalExpression(self):
            return self.getTypedRuleContext(java_grammarParser.LogicalExpressionContext,0)


        def arithmeticExpression(self):
            return self.getTypedRuleContext(java_grammarParser.ArithmeticExpressionContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = java_grammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expression)
        try:
            self.state = 522
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 520
                self.logicalExpression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 521
                self.arithmeticExpression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalTerm(self):
            return self.getTypedRuleContext(java_grammarParser.LogicalTermContext,0)


        def logicalExpression(self):
            return self.getTypedRuleContext(java_grammarParser.LogicalExpressionContext,0)


        def logicalOperator(self):
            return self.getTypedRuleContext(java_grammarParser.LogicalOperatorContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_logicalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalExpression" ):
                listener.enterLogicalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalExpression" ):
                listener.exitLogicalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalExpression" ):
                return visitor.visitLogicalExpression(self)
            else:
                return visitor.visitChildren(self)



    def logicalExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = java_grammarParser.LogicalExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_logicalExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
            self.logicalTerm()
            self._ctx.stop = self._input.LT(-1)
            self.state = 533
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = java_grammarParser.LogicalExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalExpression)
                    self.state = 527
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 528
                    self.logicalOperator()
                    self.state = 529
                    self.logicalTerm() 
                self.state = 535
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LogicalTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def extendedIDwithThis(self):
            return self.getTypedRuleContext(java_grammarParser.ExtendedIDwithThisContext,0)


        def literal(self):
            return self.getTypedRuleContext(java_grammarParser.LiteralContext,0)


        def unaryLogicalExpression(self):
            return self.getTypedRuleContext(java_grammarParser.UnaryLogicalExpressionContext,0)


        def LPAREN(self):
            return self.getToken(java_grammarParser.LPAREN, 0)

        def logicalExpression(self):
            return self.getTypedRuleContext(java_grammarParser.LogicalExpressionContext,0)


        def RPAREN(self):
            return self.getToken(java_grammarParser.RPAREN, 0)

        def arithmeticExpression(self):
            return self.getTypedRuleContext(java_grammarParser.ArithmeticExpressionContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_logicalTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalTerm" ):
                listener.enterLogicalTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalTerm" ):
                listener.exitLogicalTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalTerm" ):
                return visitor.visitLogicalTerm(self)
            else:
                return visitor.visitChildren(self)




    def logicalTerm(self):

        localctx = java_grammarParser.LogicalTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_logicalTerm)
        try:
            self.state = 548
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 536
                self.extendedIDwithThis()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 537
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 538
                self.unaryLogicalExpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 539
                self.match(java_grammarParser.LPAREN)
                self.state = 540
                self.logicalExpression(0)
                self.state = 541
                self.match(java_grammarParser.RPAREN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 543
                self.match(java_grammarParser.LPAREN)
                self.state = 544
                self.arithmeticExpression(0)
                self.state = 545
                self.match(java_grammarParser.RPAREN)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 547
                self.arithmeticExpression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryLogicalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOGICAL_NOT(self):
            return self.getToken(java_grammarParser.LOGICAL_NOT, 0)

        def logicalTerm(self):
            return self.getTypedRuleContext(java_grammarParser.LogicalTermContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_unaryLogicalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryLogicalExpression" ):
                listener.enterUnaryLogicalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryLogicalExpression" ):
                listener.exitUnaryLogicalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryLogicalExpression" ):
                return visitor.visitUnaryLogicalExpression(self)
            else:
                return visitor.visitChildren(self)




    def unaryLogicalExpression(self):

        localctx = java_grammarParser.UnaryLogicalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_unaryLogicalExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self.match(java_grammarParser.LOGICAL_NOT)
            self.state = 551
            self.logicalTerm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOGICAL_OR(self):
            return self.getToken(java_grammarParser.LOGICAL_OR, 0)

        def LOGICAL_AND(self):
            return self.getToken(java_grammarParser.LOGICAL_AND, 0)

        def EQUAL(self):
            return self.getToken(java_grammarParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(java_grammarParser.NOT_EQUAL, 0)

        def GREATER_THAN(self):
            return self.getToken(java_grammarParser.GREATER_THAN, 0)

        def LESS_THAN(self):
            return self.getToken(java_grammarParser.LESS_THAN, 0)

        def LESS_THAN_OR_EQUAL(self):
            return self.getToken(java_grammarParser.LESS_THAN_OR_EQUAL, 0)

        def GREATER_THAN_OR_EQUAL(self):
            return self.getToken(java_grammarParser.GREATER_THAN_OR_EQUAL, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_logicalOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOperator" ):
                listener.enterLogicalOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOperator" ):
                listener.exitLogicalOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOperator" ):
                return visitor.visitLogicalOperator(self)
            else:
                return visitor.visitChildren(self)




    def logicalOperator(self):

        localctx = java_grammarParser.LogicalOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_logicalOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4593671619917905920) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmeticTerm(self):
            return self.getTypedRuleContext(java_grammarParser.ArithmeticTermContext,0)


        def arithmeticExpression(self):
            return self.getTypedRuleContext(java_grammarParser.ArithmeticExpressionContext,0)


        def arithmeticOperator(self):
            return self.getTypedRuleContext(java_grammarParser.ArithmeticOperatorContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_arithmeticExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticExpression" ):
                listener.enterArithmeticExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticExpression" ):
                listener.exitArithmeticExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticExpression" ):
                return visitor.visitArithmeticExpression(self)
            else:
                return visitor.visitChildren(self)



    def arithmeticExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = java_grammarParser.ArithmeticExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 100
        self.enterRecursionRule(localctx, 100, self.RULE_arithmeticExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            self.arithmeticTerm()
            self._ctx.stop = self._input.LT(-1)
            self.state = 564
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = java_grammarParser.ArithmeticExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmeticExpression)
                    self.state = 558
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 559
                    self.arithmeticOperator()
                    self.state = 560
                    self.arithmeticTerm() 
                self.state = 566
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArithmeticTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def extendedIDwithThis(self):
            return self.getTypedRuleContext(java_grammarParser.ExtendedIDwithThisContext,0)


        def literal(self):
            return self.getTypedRuleContext(java_grammarParser.LiteralContext,0)


        def unaryArithmeticExpression(self):
            return self.getTypedRuleContext(java_grammarParser.UnaryArithmeticExpressionContext,0)


        def LPAREN(self):
            return self.getToken(java_grammarParser.LPAREN, 0)

        def arithmeticExpression(self):
            return self.getTypedRuleContext(java_grammarParser.ArithmeticExpressionContext,0)


        def RPAREN(self):
            return self.getToken(java_grammarParser.RPAREN, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_arithmeticTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticTerm" ):
                listener.enterArithmeticTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticTerm" ):
                listener.exitArithmeticTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticTerm" ):
                return visitor.visitArithmeticTerm(self)
            else:
                return visitor.visitChildren(self)




    def arithmeticTerm(self):

        localctx = java_grammarParser.ArithmeticTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_arithmeticTerm)
        try:
            self.state = 574
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38, 85]:
                self.enterOuterAlt(localctx, 1)
                self.state = 567
                self.extendedIDwithThis()
                pass
            elif token in [30, 31, 32, 84, 86, 87]:
                self.enterOuterAlt(localctx, 2)
                self.state = 568
                self.literal()
                pass
            elif token in [43, 44]:
                self.enterOuterAlt(localctx, 3)
                self.state = 569
                self.unaryArithmeticExpression()
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 4)
                self.state = 570
                self.match(java_grammarParser.LPAREN)
                self.state = 571
                self.arithmeticExpression(0)
                self.state = 572
                self.match(java_grammarParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryArithmeticExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmeticTerm(self):
            return self.getTypedRuleContext(java_grammarParser.ArithmeticTermContext,0)


        def ADD(self):
            return self.getToken(java_grammarParser.ADD, 0)

        def SUB(self):
            return self.getToken(java_grammarParser.SUB, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_unaryArithmeticExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryArithmeticExpression" ):
                listener.enterUnaryArithmeticExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryArithmeticExpression" ):
                listener.exitUnaryArithmeticExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryArithmeticExpression" ):
                return visitor.visitUnaryArithmeticExpression(self)
            else:
                return visitor.visitChildren(self)




    def unaryArithmeticExpression(self):

        localctx = java_grammarParser.UnaryArithmeticExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_unaryArithmeticExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            _la = self._input.LA(1)
            if not(_la==43 or _la==44):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 577
            self.arithmeticTerm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(java_grammarParser.ADD, 0)

        def SUB(self):
            return self.getToken(java_grammarParser.SUB, 0)

        def MUL(self):
            return self.getToken(java_grammarParser.MUL, 0)

        def DIV(self):
            return self.getToken(java_grammarParser.DIV, 0)

        def MOD(self):
            return self.getToken(java_grammarParser.MOD, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_arithmeticOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticOperator" ):
                listener.enterArithmeticOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticOperator" ):
                listener.exitArithmeticOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticOperator" ):
                return visitor.visitArithmeticOperator(self)
            else:
                return visitor.visitChildren(self)




    def arithmeticOperator(self):

        localctx = java_grammarParser.ArithmeticOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_arithmeticOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 579
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 272678883688448) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def extendedIDwithThis(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(java_grammarParser.ExtendedIDwithThisContext)
            else:
                return self.getTypedRuleContext(java_grammarParser.ExtendedIDwithThisContext,i)


        def assignmentOperator(self):
            return self.getTypedRuleContext(java_grammarParser.AssignmentOperatorContext,0)


        def literal(self):
            return self.getTypedRuleContext(java_grammarParser.LiteralContext,0)


        def newInstance(self):
            return self.getTypedRuleContext(java_grammarParser.NewInstanceContext,0)


        def expression(self):
            return self.getTypedRuleContext(java_grammarParser.ExpressionContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(java_grammarParser.FunctionCallContext,0)


        def type_(self):
            return self.getTypedRuleContext(java_grammarParser.TypeContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = java_grammarParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_assignmentStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 582
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & 1023) != 0):
                self.state = 581
                self.type_()


            self.state = 584
            self.extendedIDwithThis()
            self.state = 585
            self.assignmentOperator()
            self.state = 591
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 586
                self.extendedIDwithThis()
                pass

            elif la_ == 2:
                self.state = 587
                self.literal()
                pass

            elif la_ == 3:
                self.state = 588
                self.newInstance()
                pass

            elif la_ == 4:
                self.state = 589
                self.expression()
                pass

            elif la_ == 5:
                self.state = 590
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(java_grammarParser.ASSIGN, 0)

        def ADD_ASSIGN(self):
            return self.getToken(java_grammarParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(java_grammarParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(java_grammarParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(java_grammarParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(java_grammarParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_assignmentOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentOperator" ):
                listener.enterAssignmentOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentOperator" ):
                listener.exitAssignmentOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentOperator" ):
                return visitor.visitAssignmentOperator(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOperator(self):

        localctx = java_grammarParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 593
            _la = self._input.LA(1)
            if not(((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 63) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_NUMBER(self):
            return self.getToken(java_grammarParser.INTEGER_NUMBER, 0)

        def FLOAT_NUMBER(self):
            return self.getToken(java_grammarParser.FLOAT_NUMBER, 0)

        def STRING(self):
            return self.getToken(java_grammarParser.STRING, 0)

        def TRUE(self):
            return self.getToken(java_grammarParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(java_grammarParser.FALSE, 0)

        def NULL(self):
            return self.getToken(java_grammarParser.NULL, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = java_grammarParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 595
            _la = self._input.LA(1)
            if not(((((_la - 30)) & ~0x3f) == 0 and ((1 << (_la - 30)) & 234187180623265799) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewInstanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(java_grammarParser.NEW, 0)

        def LPAREN(self):
            return self.getToken(java_grammarParser.LPAREN, 0)

        def formalParameters(self):
            return self.getTypedRuleContext(java_grammarParser.FormalParametersContext,0)


        def RPAREN(self):
            return self.getToken(java_grammarParser.RPAREN, 0)

        def ID(self):
            return self.getToken(java_grammarParser.ID, 0)

        def dataStructerDeclaration(self):
            return self.getTypedRuleContext(java_grammarParser.DataStructerDeclarationContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_newInstance

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewInstance" ):
                listener.enterNewInstance(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewInstance" ):
                listener.exitNewInstance(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewInstance" ):
                return visitor.visitNewInstance(self)
            else:
                return visitor.visitChildren(self)




    def newInstance(self):

        localctx = java_grammarParser.NewInstanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_newInstance)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 597
            self.match(java_grammarParser.NEW)
            self.state = 600
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [85]:
                self.state = 598
                self.match(java_grammarParser.ID)
                pass
            elif token in [1, 2, 3, 4]:
                self.state = 599
                self.dataStructerDeclaration()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 602
            self.match(java_grammarParser.LPAREN)
            self.state = 603
            self.formalParameters()
            self.state = 604
            self.match(java_grammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncrementStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def extendedIDwithThis(self):
            return self.getTypedRuleContext(java_grammarParser.ExtendedIDwithThisContext,0)


        def INCREMENT(self):
            return self.getToken(java_grammarParser.INCREMENT, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_incrementStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncrementStatement" ):
                listener.enterIncrementStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncrementStatement" ):
                listener.exitIncrementStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncrementStatement" ):
                return visitor.visitIncrementStatement(self)
            else:
                return visitor.visitChildren(self)




    def incrementStatement(self):

        localctx = java_grammarParser.IncrementStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_incrementStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 606
            self.extendedIDwithThis()
            self.state = 607
            self.match(java_grammarParser.INCREMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecrementStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def extendedIDwithThis(self):
            return self.getTypedRuleContext(java_grammarParser.ExtendedIDwithThisContext,0)


        def DECREMENT(self):
            return self.getToken(java_grammarParser.DECREMENT, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_decrementStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecrementStatement" ):
                listener.enterDecrementStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecrementStatement" ):
                listener.exitDecrementStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecrementStatement" ):
                return visitor.visitDecrementStatement(self)
            else:
                return visitor.visitChildren(self)




    def decrementStatement(self):

        localctx = java_grammarParser.DecrementStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_decrementStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 609
            self.extendedIDwithThis()
            self.state = 610
            self.match(java_grammarParser.DECREMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def extendedIDwithThis(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(java_grammarParser.ExtendedIDwithThisContext)
            else:
                return self.getTypedRuleContext(java_grammarParser.ExtendedIDwithThisContext,i)


        def LPAREN(self):
            return self.getToken(java_grammarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(java_grammarParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(java_grammarParser.COMMA)
            else:
                return self.getToken(java_grammarParser.COMMA, i)

        def getRuleIndex(self):
            return java_grammarParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = java_grammarParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612
            self.extendedIDwithThis()
            self.state = 613
            self.match(java_grammarParser.LPAREN)
            self.state = 615
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38 or _la==85:
                self.state = 614
                self.extendedIDwithThis()


            self.state = 621
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==74:
                self.state = 617
                self.match(java_grammarParser.COMMA)
                self.state = 618
                self.extendedIDwithThis()
                self.state = 623
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 624
            self.match(java_grammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dataType(self):
            return self.getTypedRuleContext(java_grammarParser.DataTypeContext,0)


        def VOID(self):
            return self.getToken(java_grammarParser.VOID, 0)

        def dataStructerDeclaration(self):
            return self.getTypedRuleContext(java_grammarParser.DataStructerDeclarationContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = java_grammarParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_type)
        try:
            self.state = 629
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [76, 77, 78, 79, 80, 81, 82, 83, 84]:
                self.enterOuterAlt(localctx, 1)
                self.state = 626
                self.dataType()
                pass
            elif token in [75]:
                self.enterOuterAlt(localctx, 2)
                self.state = 627
                self.match(java_grammarParser.VOID)
                pass
            elif token in [1, 2, 3, 4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 628
                self.dataStructerDeclaration()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(java_grammarParser.INT, 0)

        def FLOAT(self):
            return self.getToken(java_grammarParser.FLOAT, 0)

        def DOUBLE(self):
            return self.getToken(java_grammarParser.DOUBLE, 0)

        def LONG(self):
            return self.getToken(java_grammarParser.LONG, 0)

        def SHORT(self):
            return self.getToken(java_grammarParser.SHORT, 0)

        def BYTE(self):
            return self.getToken(java_grammarParser.BYTE, 0)

        def CHAR(self):
            return self.getToken(java_grammarParser.CHAR, 0)

        def BOOLEAN(self):
            return self.getToken(java_grammarParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(java_grammarParser.STRING, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_dataType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataType" ):
                listener.enterDataType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataType" ):
                listener.exitDataType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataType" ):
                return visitor.visitDataType(self)
            else:
                return visitor.visitChildren(self)




    def dataType(self):

        localctx = java_grammarParser.DataTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_dataType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 631
            _la = self._input.LA(1)
            if not(((((_la - 76)) & ~0x3f) == 0 and ((1 << (_la - 76)) & 511) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModifiersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def modifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(java_grammarParser.ModifierContext)
            else:
                return self.getTypedRuleContext(java_grammarParser.ModifierContext,i)


        def getRuleIndex(self):
            return java_grammarParser.RULE_modifiers

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModifiers" ):
                listener.enterModifiers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModifiers" ):
                listener.exitModifiers(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModifiers" ):
                return visitor.visitModifiers(self)
            else:
                return visitor.visitChildren(self)




    def modifiers(self):

        localctx = java_grammarParser.ModifiersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_modifiers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 634 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 633
                self.modifier()
                self.state = 636 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6160384) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUBLIC(self):
            return self.getToken(java_grammarParser.PUBLIC, 0)

        def PRIVATE(self):
            return self.getToken(java_grammarParser.PRIVATE, 0)

        def PROTECTED(self):
            return self.getToken(java_grammarParser.PROTECTED, 0)

        def STATIC(self):
            return self.getToken(java_grammarParser.STATIC, 0)

        def DEFAULT(self):
            return self.getToken(java_grammarParser.DEFAULT, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_modifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModifier" ):
                listener.enterModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModifier" ):
                listener.exitModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModifier" ):
                return visitor.visitModifier(self)
            else:
                return visitor.visitChildren(self)




    def modifier(self):

        localctx = java_grammarParser.ModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_modifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 638
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6160384) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassModifiersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(java_grammarParser.ClassModifierContext)
            else:
                return self.getTypedRuleContext(java_grammarParser.ClassModifierContext,i)


        def getRuleIndex(self):
            return java_grammarParser.RULE_classModifiers

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassModifiers" ):
                listener.enterClassModifiers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassModifiers" ):
                listener.exitClassModifiers(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassModifiers" ):
                return visitor.visitClassModifiers(self)
            else:
                return visitor.visitChildren(self)




    def classModifiers(self):

        localctx = java_grammarParser.ClassModifiersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_classModifiers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 641 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 640
                self.classModifier()
                self.state = 643 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==21 or _la==22):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABSTRACT(self):
            return self.getToken(java_grammarParser.ABSTRACT, 0)

        def DEFAULT(self):
            return self.getToken(java_grammarParser.DEFAULT, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_classModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassModifier" ):
                listener.enterClassModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassModifier" ):
                listener.exitClassModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassModifier" ):
                return visitor.visitClassModifier(self)
            else:
                return visitor.visitChildren(self)




    def classModifier(self):

        localctx = java_grammarParser.ClassModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_classModifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 645
            _la = self._input.LA(1)
            if not(_la==21 or _la==22):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataStructerDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dataStructers(self):
            return self.getTypedRuleContext(java_grammarParser.DataStructersContext,0)


        def LESS_THAN(self):
            return self.getToken(java_grammarParser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(java_grammarParser.GREATER_THAN, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(java_grammarParser.ID)
            else:
                return self.getToken(java_grammarParser.ID, i)

        def dataType(self):
            return self.getTypedRuleContext(java_grammarParser.DataTypeContext,0)


        def getRuleIndex(self):
            return java_grammarParser.RULE_dataStructerDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataStructerDeclaration" ):
                listener.enterDataStructerDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataStructerDeclaration" ):
                listener.exitDataStructerDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataStructerDeclaration" ):
                return visitor.visitDataStructerDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def dataStructerDeclaration(self):

        localctx = java_grammarParser.DataStructerDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_dataStructerDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 647
            self.dataStructers()
            self.state = 648
            self.match(java_grammarParser.LESS_THAN)
            self.state = 651
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [76, 77, 78, 79, 80, 81, 82, 83, 84]:
                self.state = 649
                self.dataType()
                pass
            elif token in [85]:
                self.state = 650
                self.match(java_grammarParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 653
            self.match(java_grammarParser.GREATER_THAN)
            self.state = 654
            self.match(java_grammarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataStructersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAYLIST(self):
            return self.getToken(java_grammarParser.ARRAYLIST, 0)

        def LINKEDLIST(self):
            return self.getToken(java_grammarParser.LINKEDLIST, 0)

        def HASHSET(self):
            return self.getToken(java_grammarParser.HASHSET, 0)

        def HASHMAP(self):
            return self.getToken(java_grammarParser.HASHMAP, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_dataStructers

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataStructers" ):
                listener.enterDataStructers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataStructers" ):
                listener.exitDataStructers(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataStructers" ):
                return visitor.visitDataStructers(self)
            else:
                return visitor.visitChildren(self)




    def dataStructers(self):

        localctx = java_grammarParser.DataStructersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_dataStructers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 656
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(java_grammarParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(java_grammarParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(java_grammarParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(java_grammarParser.SEMICOLON, 0)

        def PRINT(self):
            return self.getToken(java_grammarParser.PRINT, 0)

        def PRINTLN(self):
            return self.getToken(java_grammarParser.PRINTLN, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)




    def printStatement(self):

        localctx = java_grammarParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_printStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 658
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 659
            self.match(java_grammarParser.LPAREN)
            self.state = 660
            self.expression()
            self.state = 661
            self.match(java_grammarParser.RPAREN)
            self.state = 662
            self.match(java_grammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(java_grammarParser.TypeContext,0)


        def ID(self):
            return self.getToken(java_grammarParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(java_grammarParser.ASSIGN, 0)

        def NEW(self):
            return self.getToken(java_grammarParser.NEW, 0)

        def SCANNER(self):
            return self.getToken(java_grammarParser.SCANNER, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(java_grammarParser.LPAREN)
            else:
                return self.getToken(java_grammarParser.LPAREN, i)

        def expression(self):
            return self.getTypedRuleContext(java_grammarParser.ExpressionContext,0)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(java_grammarParser.RPAREN)
            else:
                return self.getToken(java_grammarParser.RPAREN, i)

        def DOT(self):
            return self.getToken(java_grammarParser.DOT, 0)

        def NEXT(self):
            return self.getToken(java_grammarParser.NEXT, 0)

        def SEMICOLON(self):
            return self.getToken(java_grammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_inputStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputStatement" ):
                listener.enterInputStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputStatement" ):
                listener.exitInputStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputStatement" ):
                return visitor.visitInputStatement(self)
            else:
                return visitor.visitChildren(self)




    def inputStatement(self):

        localctx = java_grammarParser.InputStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_inputStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 664
            self.type_()
            self.state = 665
            self.match(java_grammarParser.ID)
            self.state = 666
            self.match(java_grammarParser.ASSIGN)
            self.state = 667
            self.match(java_grammarParser.NEW)
            self.state = 668
            self.match(java_grammarParser.SCANNER)
            self.state = 669
            self.match(java_grammarParser.LPAREN)
            self.state = 670
            self.expression()
            self.state = 671
            self.match(java_grammarParser.RPAREN)
            self.state = 672
            self.match(java_grammarParser.DOT)
            self.state = 673
            self.match(java_grammarParser.NEXT)
            self.state = 674
            self.match(java_grammarParser.LPAREN)
            self.state = 675
            self.match(java_grammarParser.RPAREN)
            self.state = 676
            self.match(java_grammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExtendedIDwithThisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THIS(self):
            return self.getToken(java_grammarParser.THIS, 0)

        def extendedID(self):
            return self.getTypedRuleContext(java_grammarParser.ExtendedIDContext,0)


        def COMMA(self):
            return self.getToken(java_grammarParser.COMMA, 0)

        def getRuleIndex(self):
            return java_grammarParser.RULE_extendedIDwithThis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtendedIDwithThis" ):
                listener.enterExtendedIDwithThis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtendedIDwithThis" ):
                listener.exitExtendedIDwithThis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtendedIDwithThis" ):
                return visitor.visitExtendedIDwithThis(self)
            else:
                return visitor.visitChildren(self)




    def extendedIDwithThis(self):

        localctx = java_grammarParser.ExtendedIDwithThisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_extendedIDwithThis)
        self._la = 0 # Token type
        try:
            self.state = 684
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 678
                self.match(java_grammarParser.THIS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 681
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==38:
                    self.state = 679
                    self.match(java_grammarParser.THIS)
                    self.state = 680
                    self.match(java_grammarParser.COMMA)


                self.state = 683
                self.extendedID()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExtendedIDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(java_grammarParser.ID)
            else:
                return self.getToken(java_grammarParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(java_grammarParser.COMMA)
            else:
                return self.getToken(java_grammarParser.COMMA, i)

        def getRuleIndex(self):
            return java_grammarParser.RULE_extendedID

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtendedID" ):
                listener.enterExtendedID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtendedID" ):
                listener.exitExtendedID(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtendedID" ):
                return visitor.visitExtendedID(self)
            else:
                return visitor.visitChildren(self)




    def extendedID(self):

        localctx = java_grammarParser.ExtendedIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_extendedID)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 686
            self.match(java_grammarParser.ID)
            self.state = 691
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,63,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 687
                    self.match(java_grammarParser.COMMA)
                    self.state = 688
                    self.match(java_grammarParser.ID) 
                self.state = 693
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,63,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[46] = self.logicalExpression_sempred
        self._predicates[50] = self.arithmeticExpression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logicalExpression_sempred(self, localctx:LogicalExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def arithmeticExpression_sempred(self, localctx:ArithmeticExpressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




