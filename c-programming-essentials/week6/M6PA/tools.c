// TODO - Implement the functions in this file

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "tools.h"

char *strdup (const char *s) {
    char *d = (char *)(malloc (strlen (s) + 1)); /* Space for length plus nul */
    if (d == NULL) return NULL;                  /* No memory                 */
    strcpy (d,s);                                /* Copy the characters       */
    return d;                                    /* Return the new string     */
}

char* taurahize_word(const char * const word){
    return strdup(word);  // Useless right now, modify it
}


char* taurahize_phrase(const char* const phrase){
     return strdup(phrase);  // Useless right now, modify it
}
