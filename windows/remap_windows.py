import re

"""
Make ctrl keys work correctly by remapping the VK_ values in the klc file.
Insert the original specification from the file as `klc_spec` below, and the script
will print an updated version.
"""

klc_spec = """02	1		0	1	0021	-1	-1	00a1		// DIGIT ONE, EXCLAMATION MARK, <none>, <none>, INVERTED EXCLAMATION MARK
03	2		0	2	0022	-1	0040	-1		// DIGIT TWO, QUOTATION MARK, <none>, COMMERCIAL AT, <none>
04	3		0	3	0023	-1	00a3	-1		// DIGIT THREE, NUMBER SIGN, <none>, POUND SIGN, <none>
05	4		0	4	00a4	-1	0024	-1		// DIGIT FOUR, CURRENCY SIGN, <none>, DOLLAR SIGN, <none>
06	5		0	5	0025	-1	20ac	-1		// DIGIT FIVE, PERCENT SIGN, <none>, EURO SIGN, <none>
07	6		0	6	0026	-1	-1	-1		// DIGIT SIX, AMPERSAND, <none>, <none>, <none>
08	7		0	7	002f	-1	007b	-1		// DIGIT SEVEN, SOLIDUS, <none>, LEFT CURLY BRACKET, <none>
09	8		0	8	0028	-1	005b	-1		// DIGIT EIGHT, LEFT PARENTHESIS, <none>, LEFT SQUARE BRACKET, <none>
0a	9		0	9	0029	-1	005d	-1		// DIGIT NINE, RIGHT PARENTHESIS, <none>, RIGHT SQUARE BRACKET, <none>
0b	0		0	0	003d	-1	007d	-1		// DIGIT ZERO, EQUALS SIGN, <none>, RIGHT CURLY BRACKET, <none>
0c	OEM_PLUS	0	002b	003f	-1	005c	00bf		// PLUS SIGN, QUESTION MARK, <none>, REVERSE SOLIDUS, INVERTED QUESTION MARK
0d	OEM_4		0	00b4@	0060@	-1	-1	-1		// ACUTE ACCENT, GRAVE ACCENT, <none>, <none>, <none>
10	Q		1	00e5	00c5	-1	-1	-1		// LATIN SMALL LETTER A WITH RING ABOVE, LATIN CAPITAL LETTER A WITH RING ABOVE, <none>, <none>, <none>
11	W		1	p	P	-1	-1	-1		// LATIN SMALL LETTER P, LATIN CAPITAL LETTER P, <none>, <none>, <none>
12	E		1	o	O	-1	-1	-1		// LATIN SMALL LETTER O, LATIN CAPITAL LETTER O, <none>, <none>, <none>
13	R		1	u	U	-1	00fc	00dc		// LATIN SMALL LETTER U, LATIN CAPITAL LETTER U, <none>, LATIN SMALL LETTER U WITH DIAERESIS, LATIN CAPITAL LETTER U WITH DIAERESIS
14	T		1	y	Y	-1	-1	-1		// LATIN SMALL LETTER Y, LATIN CAPITAL LETTER Y, <none>, <none>, <none>
15	Y		1	q	Q	-1	-1	-1		// LATIN SMALL LETTER Q, LATIN CAPITAL LETTER Q, <none>, <none>, <none>
16	U		1	g	G	-1	-1	-1		// LATIN SMALL LETTER G, LATIN CAPITAL LETTER G, <none>, <none>, <none>
17	I		1	d	D	-1	-1	-1		// LATIN SMALL LETTER D, LATIN CAPITAL LETTER D, <none>, <none>, <none>
18	O		1	l	L	-1	-1	-1		// LATIN SMALL LETTER L, LATIN CAPITAL LETTER L, <none>, <none>, <none>
19	P		1	w	W	-1	-1	-1		// LATIN SMALL LETTER W, LATIN CAPITAL LETTER W, <none>, <none>, <none>
1a	OEM_6		0	0027	002a	001b	-1	-1		// APOSTROPHE, ASTERISK, ESCAPE, <none>, <none>
1b	OEM_1		0	00a8@	005e@	001d	007e@	-1		// DIAERESIS, CIRCUMFLEX ACCENT, INFORMATION SEPARATOR THREE, TILDE, <none>
1e	A		1	a	A	-1	-1	-1		// LATIN SMALL LETTER A, LATIN CAPITAL LETTER A, <none>, <none>, <none>
1f	S		1	h	H	-1	-1	-1		// LATIN SMALL LETTER H, LATIN CAPITAL LETTER H, <none>, <none>, <none>
20	D		1	e	E	-1	20ac	-1		// LATIN SMALL LETTER E, LATIN CAPITAL LETTER E, <none>, EURO SIGN, <none>
21	F		1	i	I	-1	-1	-1		// LATIN SMALL LETTER I, LATIN CAPITAL LETTER I, <none>, <none>, <none>
22	G		0	002c	003b	-1	-1	-1		// COMMA, SEMICOLON, <none>, <none>, <none>
23	H		1	f	F	-1	-1	-1		// LATIN SMALL LETTER F, LATIN CAPITAL LETTER F, <none>, <none>, <none>
24	J		1	s	S	-1	00df	-1		// LATIN SMALL LETTER S, LATIN CAPITAL LETTER S, <none>, LATIN SMALL LETTER SHARP S (German), <none>
25	K		1	t	T	-1	-1	-1		// LATIN SMALL LETTER T, LATIN CAPITAL LETTER T, <none>, <none>, <none>
26	L		1	n	N	-1	00f1	00d1		// LATIN SMALL LETTER N, LATIN CAPITAL LETTER N, <none>, LATIN SMALL LETTER N WITH TILDE, LATIN CAPITAL LETTER N WITH TILDE
27	OEM_3		1	r	R	-1	-1	-1		// LATIN SMALL LETTER R, LATIN CAPITAL LETTER R, <none>, <none>, <none>
28	OEM_7		0	002d	005f	-1	-1	-1		// HYPHEN-MINUS, LOW LINE, <none>, <none>, <none>
29	OEM_5		0	00a7	00bd	001c	-1	-1		// SECTION SIGN, VULGAR FRACTION ONE HALF, INFORMATION SEPARATOR FOUR, <none>, <none>
2b	OEM_2		0	003c	003e	-1	007c	-1		// LESS-THAN SIGN, GREATER-THAN SIGN, <none>, VERTICAL LINE, <none>
2c	Z		1	j	J	-1	-1	-1		// LATIN SMALL LETTER J, LATIN CAPITAL LETTER J, <none>, <none>, <none>
2d	X		1	00e4	00c4	-1	00e6	00c6		// LATIN SMALL LETTER A WITH DIAERESIS, LATIN CAPITAL LETTER A WITH DIAERESIS, <none>, LATIN SMALL LETTER AE (ash) *, LATIN CAPITAL LETTER AE (ash) *
2e	C		1	k	K	-1	-1	-1		// LATIN SMALL LETTER K, LATIN CAPITAL LETTER K, <none>, <none>, <none>
2f	V		0	002e	003a	-1	-1	-1		// FULL STOP, COLON, <none>, <none>, <none>
30	B		1	x	X	-1	-1	-1		// LATIN SMALL LETTER X, LATIN CAPITAL LETTER X, <none>, <none>, <none>
31	N		1	b	B	-1	-1	-1		// LATIN SMALL LETTER B, LATIN CAPITAL LETTER B, <none>, <none>, <none>
32	M		1	c	C	-1	00e7	00c7		// LATIN SMALL LETTER C, LATIN CAPITAL LETTER C, <none>, LATIN SMALL LETTER C WITH CEDILLA, LATIN CAPITAL LETTER C WITH CEDILLA
33	OEM_COMMA	1	m	M	-1	00b5	-1		// LATIN SMALL LETTER M, LATIN CAPITAL LETTER M, <none>, MICRO SIGN, <none>
34	OEM_PERIOD	1	v	V	-1	-1	-1		// LATIN SMALL LETTER V, LATIN CAPITAL LETTER V, <none>, <none>, <none>
35	OEM_MINUS	1	z	Z	-1	-1	-1		// LATIN SMALL LETTER Z, LATIN CAPITAL LETTER Z, <none>, <none>, <none>
39	SPACE		0	0020	0020	0020	-1	-1		// SPACE, SPACE, SPACE, <none>, <none>
56	OEM_102	5	00f6	00d6	001c	00f8	00d8		// LATIN SMALL LETTER O WITH DIAERESIS, LATIN CAPITAL LETTER O WITH DIAERESIS, INFORMATION SEPARATOR FOUR, LATIN SMALL LETTER O WITH STROKE, LATIN CAPITAL LETTER O WITH STROKE
53	DECIMAL	0	002c	002c	-1	-1	-1		// COMMA, COMMA, , , """

lines = klc_spec.split("\n")
values = []
for line in lines:
    parts = re.split(r"\t+", line)
    values.append(parts)


def find_vk_line(letter, values):
    for line_num in range(len(values)):
        vk = values[line_num][1]
        if vk == letter:
            return line_num
    return None


for line_num in range(len(values)):
    vk = values[line_num][1]
    letter = values[line_num][4]
    if vk != letter:
        vk_line = find_vk_line(letter, values)
        if vk_line != None:
            values[line_num][1], values[vk_line][1] = (
                values[vk_line][1],
                values[line_num][1],
            )

result = "\n".join(["\t".join(line_values) for line_values in values])
print(result)
