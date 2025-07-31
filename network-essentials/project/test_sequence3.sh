#!/bin/bash
#ChatGpt(version GPT-4.1)was used to convert the bash test files into .sh files able to executed by a Linux/Unix system
#I first asked the model "Can you make these batch files into .sh files executable by a mac?" followed by giving it the project instructions,
#and then asking it to replace the ./udpMsgSend function with the netcat function since udpMsgSend is not native to Mac.
#Link-----
#     https://chatgpt.com/c/688abd23-2b98-800e-b768-f38a0f0efaa5
echo "REM Test sequence #3 for CNT 5008 project"

curl http://127.0.0.1:8080/test.html

echo -n "Mickey" | nc -u -w1 127.0.0.1 1100
echo "Waiting for 0 seconds, press CTRL+C to quit ..."
sleep 2

echo -n "Minnie" | nc -u -w1 127.0.0.1 1200
echo "Waiting for 0 seconds, press CTRL+C to quit ..."
sleep 6

echo -n "Goofy" | nc -u -w1 127.0.0.1 1300
echo "Waiting for 0 seconds, press CTRL+C to quit ..."
sleep 2

curl http://127.0.0.1:8080/test.html

read -p "Press Enter to continue..."