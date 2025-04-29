#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#include "hsl.h"

int hsl_length ( char* s ) {
    if (s == NULL){
        return 0;
    }
    int count = 0;
    while(s[count] != '\0'){
        count++;
    }

    return count;
}

bool hsl_compare ( char* s1 , char* s2 ) {
    int size1 = hsl_length(s1);
    int size2 = hsl_length(s2);

    if (size1 != size2){
        return false;
    }
    for(int i = 0; i < size1; i++){
        if (s1[i] != s2[i]){
            return false;
        }
    }
    return true;
}

char * hsl_allocate ( int size ){
    return (char*)malloc(sizeof(char) * size + 1);
}

bool hsl_deallocate (char* s){
    if (!s) {
        return false;
    }
    free(s);
    return true;
}

bool hsl_deallocate_cleanly(char** s){
    if (*s == NULL) {
        return false;
    }
    free(*s);
    *s = NULL;
    return true;
}

char * hsl_clone ( char* s ){
    if (!s) {
        return NULL;
    }

    int len = hsl_length(s);
    char * temp = hsl_allocate(len);
    char *start = temp;
    while(*s) *temp++ = *s++; {
        *temp = '\0';
    }
    

    return start;
}

char* hsl_gather (char* s1 , char* s2 ){
    return NULL;
}

char* hsl_extract ( char* s1 , int start , int end ){
    return NULL;
}
