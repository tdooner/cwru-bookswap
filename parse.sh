######
# Pass in via argument 1 a file, sorted by ISBN, with the following columns:
#   ISBN, Purchase Price, Seller 1, Seller 1's Offer, Seller 2, Seller 2's Offer
#
# Call this: ./parse.sh file.txt
#
# Btw, this is not the right tool for this job, but I want to do this
#  anyhow.
######

IFS=$'\n'
for line in $(cat $1); do
	ISBN=`echo $line | cut -d " " -f 1`
	PRICE=`echo $line | cut -d " " -f 2`
	PRICE2=`echo $line | cut -d " " -f 4` #Seller 1's Offer
	if [ $PRICE == "0.00" ]
	then
		PERCENT1="0.00"
	else
		PERCENT1=`echo $PRICE2/$PRICE | bc -l`
	fi
	
	PRICE3=`echo $line | cut -d " " -f 6` #Seller 2's Offer
	if [ $PRICE == "0.00" ]
	then
		PERCENT2="0.00"
	else
		PERCENT2=`echo $PRICE3/$PRICE | bc -l`
	fi

	HASOUTPUTISBN="0"
	if [ `echo $PERCENT1">1" | bc` == "1" ] 
	then
		if [ $HASOUTPUTISBN == "0" ]
		then
			echo -n $ISBN" "
			HASOUTPUTISBN="1"
		fi
		echo -n $PERCENT1" "
	fi

	if [ `echo $PERCENT2">1" | bc` == "1" ] 
	then
		if [ $HASOUTPUTISBN == "0" ] 
		then
			# I don't know how this could be true here if PERCENT2 is always 
			# less than PERCENT1... but...
			echo -n $ISBN" "
			HASOUTPUTISBN="1"
		fi
		echo -n $PERCENT2" "
	fi
	if [ $HASOUTPUTISBN == "1" ]
	then
		echo ""
	fi
done
