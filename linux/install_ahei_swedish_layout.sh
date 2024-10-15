#!/bin/bash

# Backup existing files (just in case)
sudo cp /usr/share/X11/xkb/symbols/se /usr/share/X11/xkb/symbols/se.bak
sudo cp /usr/share/X11/xkb/rules/evdev.xml /usr/share/X11/xkb/rules/evdev.xml.bak

# Add the custom variant to the symbols file (if it doesn't already exist)
if ! grep -q "xkb_symbols \"ahei\"" /usr/share/X11/xkb/symbols/se; then
    echo "Adding AHEI layout to the symbols file..."
    sudo bash -c 'cat << EOF >> /usr/share/X11/xkb/symbols/se

partial alphanumeric_keys
xkb_symbols "ahei_swedish" {

   include "se(basic)"

   name[Group1]="Swedish (AHEI)";

   key <AD01> { [ aring, Aring, braceleft ] };
   key <AD02> { [ p, P, braceright ] };
   key <AD03> { [ o, O, parenleft ] };
   key <AD04> { [ u, U ] };
   key <AD05> { [ y, Y ] };
   key <AD06> { [ q, Q ] };
   key <AD07> { [ g, G ] };
   key <AD08> { [ d, D ] };
   key <AD09> { [ l, L ] };
   key <AD10> { [ w, W ] };
   key <AD11> { [ apostrophe, asterisk ] };

   key <AC01> { [ a, A ] };
   key <AC02> { [ h, H ] };
   key <AC03> { [ e, E, parenright ] };
   key <AC04> { [ i, I ] };
   key <AC05> { [ comma, semicolon, bracketleft ] };
   key <AC06> { [ f, F ] };
   key <AC07> { [ s, S, ssharp, U1E9E ] };
   key <AC08> { [ t, T ] };
   key <AC09> { [ n, N ] };
   key <AC10> { [ r, R ] };
   key <AC11> { [ minus, underscore ] };
   key <BKSL> { [ less, greater, bar ] };

   key <LSGT> { [ odiaeresis, Odiaeresis ] };
   key <AB01> { [ j, J ] };
   key <AB02> { [ adiaeresis, Adiaeresis ] };
   key <AB03> { [ k, K ] };
   key <AB04> { [ period, colon, bracketright ] };
   key <AB05> { [ x, X ] };
   key <AB06> { [ b, B ] };
   key <AB07> { [ c, C ] };
   key <AB08> { [ m, M ] };
   key <AB09> { [ v, V ] };
   key <AB10> { [ z, Z ] };
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
if ! grep -q "<description>Swedish (AHEI)</description>" /usr/share/X11/xkb/rules/evdev.xml; then
    echo "Adding AHEI layout to evdev.xml..."

    # Insert the new variant into the correct layout section using xmlstarlet
    sudo xmlstarlet ed --inplace \
        -s '//layout[configItem/name="se"]/variantList' \
        -t elem -n variant -v "" \
        -s '//layout[configItem/name="se"]/variantList/variant[last()]' -t elem -n configItem -v "" \
        -s '//layout[configItem/name="se"]/variantList/variant[last()]/configItem' -t elem -n name -v "ahei_swedish" \
        -s '//layout[configItem/name="se"]/variantList/variant[last()]/configItem' -t elem -n description -v "Swedish (AHEI)" \
        /usr/share/X11/xkb/rules/evdev.xml
else
    echo "AHEI layout already exists in evdev.xml."
fi

echo "Swedish AHEI layout installed successfully!"
