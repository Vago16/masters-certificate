# COT5008 - Project for CNT 5008 for Summer 2025: Knocking on Ports

**Evagelos Petropoulos**

## Project Structure

project/
├-- screenshots/
| └-- screenshots of weblite_knock.c executable and output of test sequences
├-- test-scripts/
| └--test_sequence1 through test_sequence5 included in folder
├-- tests/
│-- readMe.MD
│-- test.html
│-- weblite_knock.c
│-- weblite.c(code is imported in weblite_knock.c)

## How to run tests

1. In a bash shell, neavigate to project directory.
   `$ cd project`

2. Compile weblite_knock.c.
   `$ gcc weblite_knock.c -o weblite_knock`

3. Run the executable weblite_knock, it will now be ready and waiting for a test sequence.
   `$ ./weblite_knock`

4. In a seperate bash shell, navigate to test-scripts directory.
   `$ cd test-scripts`

5. Run the provided command depending on which test sequence you wish to check.
   `$ chmod +x test_sequence1.sh   # test_sequence1 is used as example, can be any of them`

6. To execute the test sequence, use the bash command in front of the file name.
   `$ bash test_sequence1.sh      # test_sequence1 is used as example, can be any of them`

7. After the test sequence is done running, go back into the bash shell weblite_knock is running and press CTRL+C to quit the program, and then the process can be repeated.
   `^C`

## Expected Output from weblite_knock for test_sequence1.sh

`UserName:project UserName$ ./weblite_knock`
`Waiting for knock sequence...`
`Knock sequence received`
`>>>weblite_knock is running on port 8080<<<`
`Sending file 'test.html'`
