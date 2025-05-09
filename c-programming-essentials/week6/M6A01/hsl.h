#include <stdbool.h>
#pragma once
int hsl_length ( char* s ) ;

bool hsl_compare ( char* s1 , char* s2 );

char * hsl_allocate ( int size ) ;

bool hsl_deallocate (char* s);

bool hsl_deallocate_cleanly(char** s);

char * hsl_clone ( char* s );

char* hsl_gather (char* s1 , char* s2 );

char* hsl_extract ( char* s1 , int start , int end );