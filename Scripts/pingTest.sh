prevDate=0
prevMinute=0

#while true
#do
#	time=$(date +'%T')
#	currDate=$(date +'%d%m%Y')
#	echo $time
#	touch 'test.txt'
#	printf "TESTING" >> 'test.txt'
#	printf $time'\n' >> ${currDate}.txt
#	sleep 100000000
#done

while true
do
	currDate=$(date +'%d%m%Y')
	currMinute=$(date +'%M')
	if [ $prevDate -ge $currDate ];
	then
		echo "Same date";
		#We want to try pinging every minute so..
		#If it's the same minute, do nothing.
		#Else, do a ping test
		if [ $prevMinute -ge $currMinute ];
		then
			echo "Same Minute: "$(date +'%T')
		else
			echo "Different Minute: "$(date +'%T')
			time=$(date +'%T')
			#Ping Google Every Second Until it becomes available
			count=0
			while true;
			do
				ping -W 1 -c 1 '8.8.8.8'
				if [ $? -eq 0 ];
				then
					echo "ping succeed";
					break
				else
					echo "ping fail";
					count=$((count+1))
					sleep 1;
				fi
			done
			#If we pinged google and it succeeded the 1st time, then print OK
			#Else, print FAIL and how many seconds the internet was down for
			if [ $count -eq 0 ];
			then
				printf $time' - OK\n' >> ${currDate}.txt
			else
				awk 'NR==3 {printf $time" - FAIL - DOWNTIME: "$count" - LINK: "$3"00%"" - NOISE: "$4"\n"}''' /proc/net/wireless
				#printf $time' - FAIL - DOWNTIME: '$count'\n' >> ${currDate}.txt
			fi
		fi
	else
		echo "Different date";
		touch ${currDate}.txt
	fi
	prevDate=$currDate
	prevMinute=$currMinute
	echo "----------------------------------SLEEP---------------------------------";
	sleep 10
done