// TODO - Implement the functions in this file

#include <stdlib.h>
#include <ctype.h>

void word_reverse( char* str ){
    /* 	ROLE        Reverses the order of the character in the string. Does
                    not modify the end of string marker '\0'.
        PARAMETERS  str - the string to reverse
    */
    char *end = str;

    //move the end variable to the last character before \0, '' is for space in memory
    while (*end != '\0') {
        end += 1;
    }
    
    //moves end back to just before \0
    end -= 1;

    //swap style loop to switch characters
    while (str < end) {
        char temporary = *str;
        *str = *end;
        *end = temporary;
        
        //increment/decrement str and end resepectively to get through the string
        str += 1;
        end -= 1;
    }
}

int is_separator( char data ){
    /* ROLE         Tests if the character passed as parameter is a separator;
                    i.e. something different than a letter or digit.
       RETURNS      1 - if data is a separator
                    0 - otherwise
       PARAMETERS   data - the character to test
    */

    return ( !isalnum(data) );
}

int words_initialize( char* str, char* words[], int maxwords ){
    /* 	ROLE        Parses the string str and identify each word in it.
                    Words are separated by any character which makes the
                    is_separator function returns true.
                    The address of the first character of each word in
                    the string str, is stored as a pointer in the array words.
                    When we find the end of the word we just added in the string
                    str, we modify it so that the next character becomes '\0'.
                    We are not able to handle more than maxwords words
                    and subsequent ones will be ignored.
                    Our function will return the number of words it found
                    which also indicates how many of the maxwords elements in
                    the array words are meaningful.

		RETURNS     the number of words identified in the string input.
		PARAMETERS  input    - string in which we will identify words
                    words    - an array of pointer on strings which will be the
                               words we have identified
                    maxwords - the size of the words array of pointers
    */
   int word_count = 0;
   int i = 0;

   while (str[i] != '\0' && word_count < maxwords) {

    
   }


}


void word_handle_marker(char* str){  // WORKING FUNCTION - JUST DOCUMENT :)  - GIFT
     /* ROLE         Replaces the end of string marker '\0' by a space ' '
        PARAMETERS   str - the string to modify
     */

     while(*str){ str++; }
     *str = ' ';
}


void words_modify(char* str){

     const int MAXWORDS = 256;
     char* allwords[MAXWORDS];
     int i;
     int nbwords;

     /* initialize all pointers in allwords to NULL */
     for(i=0; i < MAXWORDS ; i++)
              allwords[i] = NULL;

    nbwords = words_initialize(str, allwords, MAXWORDS);
    for(i=0 ; i < nbwords ; i++){
            word_reverse(allwords[i]);
    }

    for(i=0 ; i < (nbwords-1) ; i++){
            word_handle_marker(allwords[i]);
    }
}
