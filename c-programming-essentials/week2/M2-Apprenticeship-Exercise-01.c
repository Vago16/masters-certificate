#include <stdio.h>

/*
Write a program which prompts the user for 4 integers values to be stored in variables A , B , C and D. You will
then display 3 messages on the screen (each by executing a printf statement) which will state the result of the
comparison of the variables two by two.
*/

int main() {
    //initialize variables
    int A = 0;  
    int B = 0;
    int C = 0;
    int D = 0;

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
    
    //if..else statements to compare variables and print comparison of them
    if (A == B) {
        printf("A(%d) is equal to B(%d)", A, B);
    } else if (A > B) {
        printf("A(%d) is > than B(%d)", A, B);
    } else { 
        printf("A(%d) is < than B(%d)", A, B);
    }
    printf("\n");

    if (B == C) {
        printf("B(%d) is equal to C(%d)", B, C);
    } else if (B > C) {
        printf("B(%d) is > than C(%d)", B, C);
    } else { 
        printf("B(%d) is < than C(%d)", B, C);
    }
    printf("\n");

    if (C == D) {
        printf("C(%d) is equal to D(%d)", C, D);
    } else if (C > D) {
        printf("C(%d) is > than D(%d)", C, D);
    } else { 
        printf("C(%d) is < than D(%d)", C, D);
    }
    printf("\n");
}
