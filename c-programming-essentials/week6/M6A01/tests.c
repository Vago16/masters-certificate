#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#include "hsl.h"

int main () {
    char *s0 = NULL;
    char *s1 = "";
    char *s2 = "hello there";
    printf("String [%s] is %d characters long.\n", s0, hsl_length(s0));
    printf("String [%s] is %d characters long.\n", s1, hsl_length(s1));
    printf("String [%s] is %d characters long.\n", s2, hsl_length(s2));

    char *s3 = "hello there";
    char *s4 = "heLLo there";
    char *s5 = "hello";
    printf("Strings [%s] and [%s] are %s",
        s2, s3, hsl_compare(s2,s3)? "identical.\n" : "different.\n" );
    printf("Strings [%s] and [%s] are %s",
        s0, s0, hsl_compare(s0,s0)? "identical.\n" : "different.\n" );
    printf("Strings [%s] and [%s] are %s",
        s1, s1, hsl_compare(s1,s1)? "identical.\n" : "different.\n" );
    printf("Strings [%s] and [%s] are %s",
        s3, s4, hsl_compare(s3,s4)? "identical.\n" : "different.\n" );
    printf("Strings [%s] and [%s] are %s",
        s3, s5, hsl_compare(s3,s5)? "identical.\n" : "different.\n" );

    char *s6 = hsl_allocate(hsl_length(s5));
    printf("Deallocating s6: %s.\n", hsl_deallocate(s6) ? "success" : "issue");
    s6 = NULL;
    printf("Deallocating s6 when void: %s.\n", hsl_deallocate(s6) ? "success" : "issue");

    s6 = hsl_allocate(hsl_length(s5));
    printf("Cleanly Deallocating s6: %s ----> %p.\n", hsl_deallocate_cleanly(&s6) ? "success" : "issue", s6);

    char*s7 = hsl_clone(s5);
    printf("Clone of [%s] is [%s]\n", s5, s7);
    
    return EXIT_SUCCESS;
}