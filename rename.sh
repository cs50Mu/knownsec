#!/bin/bash


ls test/ | while read f
do
	mv "test/$f" "test/${f/.txt/}.exe"
done
