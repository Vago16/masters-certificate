// TODO - Implement your tests in this file using testlib functions

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "tools.h"
#include "testlib.h"

void test_single_word(){
    // Example of test function
    char *translation = NULL;
    translation = taurahize_word("qwer");
    TEST("Testing 4 letter word", strcmp(translation, "Aoke") == 0);
    free(translation);
}

void test_multiple_words(){
    // Example of test function
    char *translation = NULL;
    translation = taurahize_word("qwer asdf tyui");
    TEST("Testing 3 words", strcmp(translation, "Aoke Aoke Aoke") == 0);
    free(translation);
}

void runAllTests(){
    // this is how you would use the tests examples above;
    // test_single_word();
    // test_multiple_words();
}
