// TODO - Implement your tests in this file using testlib functions

#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include "testlib.h"
#include "tools.h"

void test_example(){
    // Example test function for you to adapt
    struct dictionary * d = NULL;
    d = dictionary_build(-3);
    TEST("Building with negative size should return NULL", d==NULL);
}

void test_dictionary_build() {
    struct dictionary *d;

    //negative size
    d = dictionary_build(-5);
    TEST("Negative size returns NULL", d == NULL);

    //size of zero 
    d = dictionary_build(0);
    TEST("Zero size returns NULL", d == NULL);
}

void test_dictionary_add() {
    struct dictionary *d = NULL;
    int result;

    // Test 1: NULL dictionary
    result = dictionary_add(NULL, "hello", "bonjour");
    TEST("Add to NULL dictionary returns -1", result == -1);

    // Test 2: NULL english word
    d = dictionary_build(2);
    result = dictionary_add(d, NULL, "bonjour");
    TEST("Add with NULL English returns -3", result == -3);

    // Test 3: NULL foreign word
    result = dictionary_add(d, "hello", NULL);
    TEST("Add with NULL foreign returns -4", result == -4);

    // Test 4: Valid add
    result = dictionary_add(d, "hello", "bonjour");
    TEST("Add valid pair returns 0", result == 0);
    TEST("Word count should be 1", (*d).nbwords == 1);
   
    // Test 5: Add second valid pair
    result = dictionary_add(d, "goodbye", "au revoir");
    TEST("Second add returns 0", result == 0);
    TEST("Word count should be 2", (*d).nbwords == 2);

    // Test 6: Dictionary full
    result = dictionary_add(d, "thank you", "merci");
    TEST("Add when full returns -5", result == -5);

    dictionary_free(&d);
}
void test_dictionary_translate() {
    struct dictionary *d = dictionary_build(3);
        char *result;

        dictionary_add(d, "cat", "chat");
        dictionary_add(d, "dog", "chien");

        // Test 1: Translate English -> Foreign
        result = dictionary_translate(d, "cat", NULL);
        TEST("Translate 'cat' -> 'chat'", result != NULL && strcmp(result, "chat") == 0);
        free(result);

        // Test 2: Translate Foreign -> English
        result = dictionary_translate(d, NULL, "chien");
        TEST("Translate 'chien' -> 'dog'", result != NULL && strcmp(result, "dog") == 0);
        free(result); 
}

void runAllTests(){
     /* ROLE       Runs all the tests specified and displays results
     */

    // For instance, you would have the following line in our example;
    test_example();
    test_dictionary_build();
    test_dictionary_translate();
    test_dictionary_add();
}
