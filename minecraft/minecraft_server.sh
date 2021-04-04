#usr/bin/bash

while :
do
	echo [$(date +"%T")] "Loading Server..."
	cd /opt/minecraft &&
	 sudo java -Xms2048M -Xmx2048M -jar /opt/minecraft/forge-1.16.4.jar nogui
	echo [$(date +"%T")] "Restarting!"
done
