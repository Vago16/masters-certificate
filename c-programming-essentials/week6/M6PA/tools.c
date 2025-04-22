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
    char *translation_table[] = {"", "A", "Ba", "Aki", "Aoke", "Aehok", "Aloaki", "Ishnelo",
                            "Akiticha", "Echeyakee", "Awakahnahe", "Aloakihshne", "Awakeekieloh",
                            "Ishnehawahalo", "Awakeeahmenalo", "Ishnehalohporah"};

    size_t len = strlen(word);
    if (len > 15) {
        return strdup("#@%");
    } else {
        return strdup(translation_table[len]); 
    } 
    
}


char* taurahize_phrase(const char* const phrase){
    size_t len = strlen(phrase);
    char *working_copy = strdup(phrase);

    char *translation = (char *)malloc(len + 1);
    
    if (!translation) {
        free(working_copy);
        return NULL;
    }

    translation[0] = '\0';  //initialize

    char *word = strtok(working_copy, " \t"); 

    while (word != NULL) {
        char *translated_word = taurahize_word(word);
        if (!translated_word) break;

        strcat(translation, translated_word);
        free(translated_word);

        word = strtok(NULL, " \t");

        if (word != NULL){
            strcat(translation, " ");
        }
    }
    free(working_copy);
    return translation;
}
