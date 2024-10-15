#!/bin/bash

# Backup existing files (just in case)
sudo cp /usr/share/X11/xkb/symbols/us /usr/share/X11/xkb/symbols/us.bak
sudo cp /usr/share/X11/xkb/rules/evdev.xml /usr/share/X11/xkb/rules/evdev.xml.bak

# Add the custom variant to the symbols file (if it doesn't already exist)
if ! grep -q "xkb_symbols \"ahei\"" /usr/share/X11/xkb/symbols/us; then
    echo "Adding AHEI layout to the symbols file..."
    sudo bash -c 'cat << EOF >> /usr/share/X11/xkb/symbols/us

partial alphanumeric_keys
xkb_symbols "ahei" {

    name[Group1]= "English (AHEI)";

    key <TLDE> { [       grave,	asciitilde, dead_grave, dead_tilde	] };

    key <AE01> { [	    1,	exclam 		]	};
    key <AE02> { [	    2,	at		]	};
    key <AE03> { [	    3,	numbersign	]	};
    key <AE04> { [	    4,	dollar		]	};
    key <AE05> { [	    5,	percent		]	};
    key <AE06> { [	    6,	asciicircum, dead_circumflex, dead_circumflex ]	};
    key <AE07> { [	    7,	ampersand	]	};
    key <AE08> { [	    8,	asterisk	]	};
    key <AE09> { [	    9,	parenleft,  dead_grave]	};
    key <AE10> { [	    0,	parenright	]	};
    key <AE11> { [ bracketleft,	braceleft	]	};
    key <AE12> { [ bracketright, braceright,  dead_tilde] };

    key <AD01> { [   semicolon,	colon, dead_ogonek, dead_doubleacute ] };
    key <AD02> { [	    p,	P		]	};
    key <AD03> { [	    o,	O		]	};
    key <AD04> { [	    u,	U		]	};
    key <AD05> { [	    y,	Y		]	};
    key <AD06> { [	    q,	Q		]	};
    key <AD07> { [	    g,	G		]	};
    key <AD08> { [	    d,	D		]	};
    key <AD09> { [	    l,	L		]	};
    key <AD10> { [	    w,	W		]	};
    key <AD11> { [	slash,	question	]	};
    key <AD12> { [	equal,	plus		]	};

    key <AC01> { [	    a,	A 		]	};
    key <AC02> { [	    h,	H		]	};
    key <AC03> { [	    e,	E		]	};
    key <AC04> { [	    i,	I		]	};
    key <AC05> { [	comma,	less,   dead_cedilla, dead_caron	] };
    key <AC06> { [	    f,	F		]	};
    key <AC07> { [	    s,	S		]	};
    key <AC08> { [	    t,	T		]	};
    key <AC09> { [	    n,	N		]	};
    key <AC10> { [	    r,	R		]	};
    key <AC11> { [	minus,	underscore	]	};

    key <AB01> { [	    j,	J		]	};
    key <AB02> { [  apostrophe,	quotedbl, dead_acute, dead_diaeresis	] };
    key <AB03> { [	    k,	K		]	};
    key <AB04> { [      period,	greater, dead_abovedot, periodcentered	] };
    key <AB05> { [	    x,	X		]	};
    key <AB06> { [	    b,	B		]	};
    key <AB07> { [	    c,	C		]	};
    key <AB08> { [	    m,	M		]	};
    key <AB09> { [	    v,	V		]	};
    key <AB10> { [	    z,	Z		]	};

    key <BKSL> { [  backslash,  bar             ]       };
};
EOF'
else
    echo "AHEI layout already exists in the symbols file."
fi

# Check if xmlstarlet is installed
if ! command -v xmlstarlet &> /dev/null; then
    echo "xmlstarlet is not installed. Installing it now..."
    sudo apt-get install -y xmlstarlet
fi

# Add the variant entry to evdev.xml (if it doesn't already exist)
if ! grep -q "<description>English (AHEI)</description>" /usr/share/X11/xkb/rules/evdev.xml; then
    echo "Adding AHEI layout to evdev.xml..."

    # Insert the new variant into the correct layout section using xmlstarlet
    sudo xmlstarlet ed --inplace \
        -s '//layout[configItem/name="us"]/variantList' \
        -t elem -n variant -v "" \
        -s '//layout[configItem/name="us"]/variantList/variant[last()]' -t elem -n configItem -v "" \
        -s '//layout[configItem/name="us"]/variantList/variant[last()]/configItem' -t elem -n name -v "ahei" \
        -s '//layout[configItem/name="us"]/variantList/variant[last()]/configItem' -t elem -n description -v "English (AHEI)" \
        /usr/share/X11/xkb/rules/evdev.xml
else
    echo "AHEI layout already exists in evdev.xml."
fi

echo "AHEI layout installed successfully!"
