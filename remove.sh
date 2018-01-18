#!/bin/bash

if [[ $(ufs ls) =~ "midi.py" ]]; then # check if midi.py is already on the micro:bit
	ufs rm midi.py
	echo "Removed midi.py"
fi
