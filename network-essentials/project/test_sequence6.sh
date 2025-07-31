#!/bin/bash
# Test sequence #6 for CNT 5008 project

curl http://127.0.0.1:8080/test.html

echo -n "Mickey" | nc -u 127.0.0.1 1100
echo "Waiting for 0 seconds, press CTRL+C to quit ..."
sleep 2

echo -n "Minnie" | nc -u 127.0.0.1 1200
echo "Waiting for 0 seconds, press CTRL+C to quit ..."
sleep 2

echo -n "Goofy" | nc -u 127.0.0.1 1300
echo "Waiting for 0 seconds, press CTRL+C to quit ..."
sleep 2

curl http://127.0.0.1:8080/test.html

echo -n "Donald" | nc -u 127.0.0.1 1400
echo "Waiting for 0 seconds, press CTRL+C to quit ..."
sleep 2

curl http://127.0.0.1:8080/test.html

echo -n "Mickey" | nc -u 127.0.0.1 1100
echo "Waiting for 0 seconds, press CTRL+C to quit ..."
sleep 2

echo -n "Minnie" | nc -u 127.0.0.1 1200
echo "Waiting for 0 seconds, press CTRL+C to quit ..."
sleep 2

echo -n "Goofy" | nc -u 127.0.0.1 1300
echo "Waiting for 0 seconds, press CTRL+C to quit ..."
sleep 2

curl http://127.0.0.1:8080/test.html
