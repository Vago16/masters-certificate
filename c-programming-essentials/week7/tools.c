// TODO - Implement the functions in this file

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "tools.h"

struct dictionary *dictionary_build(int size){
	if (size <= 0){
        return NULL;
    }

    struct dictionary *dict = malloc(sizeof(struct dictionary));
    if (!dict){
        return NULL;
    }

    (*dict).data = malloc(sizeof(struct wordPair *) * size);
    
    if ((*dict).data){
        free(dict);
        return NULL;
    }

    (*dict).nbwords = 0;
    (*dict).size = size;

    return dict;

}

int dictionary_add(struct dictionary* d, const char * const english, const char * const foreign){

    if (d == NULL || d->data == NULL){
        return -1;
    }

    struct wordPair *new_pair = malloc(sizeof(struct wordPair));

    if (new_pair == NULL) {
        return -2;
    }

    if (english == NULL){
        return -3;
    }

    if (foreign == NULL){
        return -4;
    }

    if (d->nbwords >= d->size){
        return -5;
    }

    (*new_pair).englishWord = strdup(english);
    (*new_pair).foreignWord = strdup(foreign);

    if ((*new_pair).englishWord == NULL || (*new_pair).foreignWord == NULL) {
        //free mem if strdup failed
        free((*new_pair).englishWord);
        free((*new_pair).foreignWord);
        free(new_pair);
        return -6;
    }

    (*d).data[(*d).nbwords] = new_pair;
    (*d).nbwords++;

    return 0;
}

int dictionary_free(struct dictionary ** p){

    if (p == NULL || *p == NULL) {
        return -1;
    }

    struct dictionary *dict = *p;

    if ((*dict).data != NULL) {
        for (int i = 0; i < (*dict).nbwords; i++){

            if ((*dict).data[i]){
                free((*((*dict).data[i])).englishWord);
                free((*((*dict).data[i])).foreignWord);
                free((*dict).data[i]);
            }
        }
        free((*dict).data);
    }
    free(*p);
    *p = NULL;
    return 0;
}

char* dictionary_translate(struct dictionary* d, const char* const english_word,const char* const foreign_word){
    if (d == NULL || (*d).data == NULL) {
        return NULL;
    }

    if ((english_word == NULL && foreign_word == NULL) ||
        (english_word != NULL && foreign_word != NULL)) {
        return NULL;
    }

    for (int i = 0; i < (*d).nbwords; i++) {
        struct wordPair *pair = (*d).data[i];

        if (english_word != NULL && strcmp((*pair).englishWord, english_word) == 0) {
            return strdup((*pair).foreignWord);
        }

        if (foreign_word != NULL && strcmp((*pair).foreignWord, foreign_word) == 0) {
            return strdup((*pair).englishWord);
        }
    }

    return NULL;
}
