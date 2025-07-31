#!/bin/bash
echo "=== Test Sequence #3 ==="

curl http://127.0.0.1:8080/test.html

echo -n "Mickey" | nc -u -w1 127.0.0.1 1100
sleep 2

echo -n "Minnie" | nc -u -w1 127.0.0.1 1200
sleep 6

echo -n "Goofy" | nc -u -w1 127.0.0.1 1300
sleep 2

curl http://127.0.0.1:8080/test.html

read -p "Press Enter to continue..."