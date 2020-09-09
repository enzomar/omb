#!/bin/bash


function ccurl {
	echo -n "> $1 => "
	echo $(curl -s -o /dev/null -w "%{http_code}" $1)
}

function ccurlk {
	echo -n "> $1 (insecure) => "
	echo $(curl -s -k -o /dev/null -w "%{http_code}" $1)
}

phase=$(sh tools/get_phase.sh)
echo "PHASE:"$phase

if [ $phase = "dev" ]; then    	
	ccurl "http://0.0.0.0:5050"
	ccurl "http://0.0.0.0:8000"
fi


if [ $phase = "uat" ]; then    	
	ccurl "http://0.0.0.0:3000"
	ccurl "http://0.0.0.0:3030"
	ccurlk "https://0.0.0.0:3443"
fi


if [ $phase = "prd" ]; then    	
	ccurl "http://0.0.0.0:80"
	ccurl "https://0.0.0.0:443"
fi

