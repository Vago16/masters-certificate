#include <stdio.h>
#include <stdlib.h>
/*
Assignment  M2PA
File        prog4.c

Student:    Evagelos Petropoulos U75564437
Date:       3/24/25

Features:   This program takes in three inputs(R1, R2, and R3) which represent dice rolls, each with integer values
            ranging from 1 to 6.  It then computes a score based on the rolls and returns them to the terminal.
Bugs:       If a non in integer value is entered for one of the input variables, then the program will stop asking for the
            rest of the imput and tell you in two separate print statements at least one roll is outside of the acceptable range
*/

int main()
{
    int R1, R2, R3; //declare and initialize integers for the rolls

    printf("You will be entering in values for three dice rolls, please enter in a value from 1 to 6.\n");

    printf("What is the value of the first roll(R1)? ");
    scanf("%d", &R1);

    printf("What is the value of the second roll(R2)? ");
    scanf("%d", &R2);

    printf("What is the value of the third roll(R3)? ");
    scanf("%d", &R3);

    if (R1 == 1 || R1 == 2 ) {
        R1 = 1;
    } else if (R1 == 3 || R1 == 4) {
        R1 = 2;
    } else if (R1 == 5 || R1 == 6) {
        R1 = 3;
    } else {
        printf("R1's value is outside of the acceptable range.\n");
    }

    if (R2 == 1 || R2 == 2 ) {
        R2 = 1;
    } else if (R2 == 3 || R2 == 4) {
        R2 = 2;
    } else if (R2 == 5 || R2 == 6) {
        R2 = 3;
    } else {
        printf("R2's value is outside of the acceptable range.\n");
    }

    if (R3 == 1 || R3 == 2 ) {
        R3 = 1;
    } else if (R3 == 3 || R3 == 4) {
        R3 = 2;
    } else if (R3 == 5 || R3== 6) {
        R3 = 3;
    } else {
        printf("R3's value is outside of the acceptable range.\n");
    }

    if (R1 < 1 || R1 > 6 || R2 < 1 || R2 > 6 || R3 < 1 || R3 > 6) {
        printf("You have entered a value that is outside of the acceptable range of at least one of the rolls.\n");
    } else {
        int payoff = R1;    //seclare and initialize payoff to whatever value R1 holds at first

        if (R2 < R1) {
            payoff += R2;

            if (R3 < R2) {
                payoff += 2 * R3;
            } else if (R3 < R1) {
                payoff += R3;
            }
        } else if (R3 < R1) {
            payoff += R3;
        }

        printf("%d\n", payoff);
    } 
    

    return EXIT_SUCCESS;
}
