# this script finds unique animals in the "animals.csv" file and returns a sorted list

# loop over files
for file in "$@" 
do
	echo "Unique species in $file:"
	# extract species
	cut -d , -f 2 $file | sort | uniq 
done


