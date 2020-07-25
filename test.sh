#!/bin/bash

directory=`pwd`
echo "$directory \b/$0"
read -p "ENter your NAme: " name
read -p "Number of Directories to Create: " n

a=0

until [ $a -eq $n ]
do
	cd
	cd Desktop
	a=`expr $a + 1`
	mkdir $name$a
done

echo "DOne ! Go & take a look of Desktop :D"
