#include <stdio.h>
#include <stdlib.h>
/*
We	are	going	to	re-work	the	program	you	wrote	in	102-A04	but	this	time	we’ll	use	nested	ternary	conditional	
operators	instead	of	nested	if	statements.	
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
   (A < B) ? (
        (B < C) ? (
            (C < D) ? (
                printf("A(%d) < B(%d) < C(%d) < D(%d)", A, B, C, D)
            ) : (
                printf("A(%d) < B(%d) < C(%d) > D(%d)", A, B, C, D)
            )
        ) : (
            (C < D) ? (
                printf("A(%d) < B(%d) > C(%d) < D(%d)", A, B, C, D)
            ) : (
                printf("A(%d) < B(%d) > C(%d) > D(%d)", A, B, C, D)
            )
        ) 
    ) : (
        (B < C) ? (
            (C < D) ? (
                printf("A(%d) > B(%d) < C(%d) < D(%d)", A, B, C, D)
             ) : (
                printf("A(%d) > B(%d) < C(%d) > D(%d)", A, B, C, D)
            )
        ) : (
            (C < D) ? (
                printf("A(%d) > B(%d) > C(%d) < D(%d)", A, B, C, D)
            ) : (
                printf("A(%d) > B(%d) > C(%d) > D(%d)", A, B, C, D)
            )
        )            
    );

    printf("\n");
    return EXIT_SUCCESS;
}