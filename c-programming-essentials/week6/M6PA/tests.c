// TODO - Implement your tests in this file using testlib functions

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "tools.h"
#include "testlib.h"

void test_single_word1(){
    // Example of test function
    char *translation = NULL;
    translation = taurahize_word("qwer");
    TEST("Testing 4 letter word", strcmp(translation, "Aoke") == 0);
    free(translation);
}

void test_single_word2(){
    // Example of test function
    char *translation = NULL;
    translation = taurahize_word("qwertyuiopoiuytr");
    TEST("Testing 16 letter word", strcmp(translation, "#@%") == 0);
    free(translation);
}

void test_single_word3(){
    // Example of test function
    char *translation = NULL;
    translation = taurahize_word("");
    TEST("Testing 0 letter word", strcmp(translation, "") == 0);
    free(translation);
}

void test_multiple_words1(){
    // Example of test function
    char *translation = NULL;
    translation = taurahize_phrase("qwer asdf tyui");
    TEST("Testing 3 words", strcmp(translation, "Aoke Aoke Aoke") == 0);
    free(translation);
}

void test_multiple_words2(){
    // Example of test function
    char *translation = NULL;
    translation = taurahize_phrase("qwer\t asdf\t tyui");
    TEST("Testing 3 words with tabs", strcmp(translation, "Aoke Aoke Aoke") == 0);
    free(translation);
}

void runAllTests(){
    // this is how you would use the tests examples above;
    test_single_word1();
    test_single_word2();
    test_single_word3();
    test_multiple_words1();
    test_multiple_words2();
}
