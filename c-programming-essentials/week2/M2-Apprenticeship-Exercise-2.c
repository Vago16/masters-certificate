#include <stdio.h>
#include <stdlib.h>
/*
We are going to re-work the program you wrote in 102-A03 to obtain the same result but differently. We now
want you to write a program using nested conditional statements. The key is that instead of using a different
printf to display the three comparison messages (cf. 102-A03), you will now have to display a unique message
with a single printf. Of course, there will be many of those printf statements throughout the code each of
them corresponding to one of the possibilities (e.g., A < B > C < D).
*/

int main() {
    //initialize variables
    int A, B, C, D;

    //Take user input for variables to be compared
    printf("What is the value for A? ");
    scanf("%d", &A);
    
    printf("What is the value for B? ");
    scanf("%d", &B);
    
    printf("What is the value for C? ");
    scanf("%d", &C);
    
    printf("What is the value for D? ");
    scanf("%d", &D);
    
    printf("Here are the comparisons I can make;\n");
    
    //nested if..else statements to compare variables and print comparison of all the variables
    if (A < B)
        if (B < C) 
            if (C < D)  {
                printf("A(%d) < B(%d) < C(%d) < D(%d)", A, B, C, D); 
            } else {
                printf("A(%d) < B(%d) < C(%d) > D(%d)", A, B, C, D); }
        else {
            if (C < D)  {
                printf("A(%d) < B(%d) > C(%d) < D(%d)", A, B, C, D); 
            } else {
                printf("A(%d) < B(%d) > C(%d) > D(%d)", A, B, C, D); }
        }
    else {
        if (B < C) 
            if (C < D)  {
                printf("A(%d) > B(%d) < C(%d) < D(%d)", A, B, C, D); 
            } else {
                printf("A(%d) > B(%d) < C(%d) > D(%d)", A, B, C, D); }
        else {
            if (C < D)  {
                printf("A(%d) > B(%d) > C(%d) < D(%d)", A, B, C, D); 
            } else {
                printf("A(%d) > B(%d) > C(%d) > D(%d)", A, B, C, D); }
        }
    }

    printf("\n");
    return EXIT_SUCCESS;
}

