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

/*COPY OF Prog4.c*/

int adjust_roll(int roll);  //Takes the value representing dice roll as parameter
int payoff (int R1, int R2, int R3); // Takes the 3 values representing dice rolls as parameters

int main() {
    int R1 = 1; 
    int R2 = 1; 
    int R3 = 1;
    
    for (int R1 = 1; R1 <= 6; R1++) {
        for (int R2 = 1; R2 <= 6; R2++) {
            for (int R3 = 1; R3 <= 6; R3++) { 
                
                payoff(R1, R2, R3);
            }
        }
    }

    return EXIT_SUCCESS; 
}


//changed repeating if...else to a function to increase efficency
int adjust_roll(int roll) {
    if (roll == 1 || roll == 2) {
        return 1;
    } else if (roll == 3 || roll == 4) {
        return 2;
    } else if (roll == 5 || roll == 6) {
        return 3;
    } return 0; // default to prvent warning
}

int payoff (int R1, int R2, int R3) {
    int adj_R1 = adjust_roll(R1);
    int adj_R2 = adjust_roll(R2);
    int adj_R3 = adjust_roll(R3);

    int result = adj_R1;    //declare and initialize payoff to whatever value adj_R1 holds at first

    if (adj_R2 < adj_R1) {
        result += adj_R2;
        if (adj_R3 < adj_R2) {
            result += 2 * adj_R3;
        } else if (adj_R3 < adj_R1) {
            result += adj_R3;
        }
    } else if (adj_R3 < adj_R1) {
        result += adj_R3;
    }
    // Display the results
    printf("%d %d %d payoff is %d\n", adj_R1, adj_R2, adj_R3, result); 
    return result;
}
