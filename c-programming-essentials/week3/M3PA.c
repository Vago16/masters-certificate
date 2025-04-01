#include <stdio.h>
#include <stdlib.h>
/*
Assignment  M3PA
File        M3PA.c

Student:    Evagelos Petropoulos U75564437
Date:       3/31/25

Features:   This program uses 3 nested recursive loops to calculate the payoff of the dice game specified in Prog4.c.
Bugs:       No known bugs
*/

int payoff (int R1, int R2, int R3); // Takes the 3 values representing dice rolls as parameters
void loopR1(int startR1, int endR1, int startR2, int endR2, int startR3, int endR3);  //starts the recursive loops and holds start and end values
void loopR2(int R1, int startR2, int endR2, int startR3, int endR3);
void loopR3(int R1, int R2, int startR3, int endR3);

int main() {
    //starting and ending values for each dice roll
    int start = 1;
    int end = 3;
    loopR1(start, end, start, end, start, end);

    return EXIT_SUCCESS; 
}

int payoff (int R1, int R2, int R3) {

    int result = R1;    //declare and initialize payoff to whatever value R1 holds at first

    if (R2 < R1) {
        result += R2;
        if (R3 < R2) {
            result += 2 * R3;
        } else if (R3 < R1) {
            result += R3;
        }
    } else if (R3 < R1) {
        result += R3;
    }
    // Display the results
    printf("%d %d %d payoff is %d\n", R1, R2, R3, result); 
    return result;
}

void loopR1(int startR1, int endR1, int startR2, int endR2, int startR3, int endR3) {
    //base case
    if (startR1 > endR1) {
        return;
    }
    loopR2(startR1, startR2, endR2, startR3, endR3);

    // Recursive call for the next value of R1
    loopR1(startR1 + 1, endR1, startR2, endR2, startR3, endR3);
}

void loopR2(int R1, int startR2, int endR2, int startR3, int endR3) {
    //base case
    if (startR2 > endR2) {
        return;
    }

    loopR3(R1, startR2, startR3, endR3);

    // Recursive call for the next value of R2
    loopR2(R1, startR2 + 1, endR2, startR3, endR3);
}

void loopR3(int R1, int R2, int startR3, int endR3) {
    //base case
    if (startR3 > endR3) {
        return;
    }
    
    //calculate payoff
    payoff(R1, R2, startR3);
    
    // Recursive call for the next value of R3
    loopR3(R1, R2, startR3 + 1, endR3);
}