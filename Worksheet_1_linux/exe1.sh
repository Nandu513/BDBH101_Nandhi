#!/bin/bash

#checking for all the executable files in the current directory using for loop
for file in *
do 	
	#check whether it is a file or not 
	if [ -f $file ];then
		#check whether it is executable or not
		if [ -x $file ]; then
			#print complete file details with ls -l
			ls -l $file
		else 
			echo "$file is not a executable file"
		fi
	else
		#else print it is not a file 
		echo "$file is not a file"
	fi
done
		
