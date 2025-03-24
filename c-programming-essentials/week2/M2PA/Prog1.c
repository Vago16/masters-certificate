#include <stdio.h>
#include <stdlib.h>
/*
Assignment  M2PA
File        prog1.c

Student:    Evagelos Petropoulos U75564437
Date:       3/23/25

Features:   Program takes in an input from the user for the variable NbStars and will continue requesting a value(integer)
            until the input value is between 1-3 inclusive. Then, the program will do the same for the variable Nblines but this time
            for the range 1-9 inclusive.
Bugs:       The do... while loops infinitely loop if they attempt to scan an input that is a non-integer
*/

int main()
{
  int nbStars = 0;  //declare and initialize integer, this will store a value that is betweeen 1 and 3 inclusive
  int nbLines = 0;  //declare and initialize integer before user input, this will store a value that is in the range of 1 ro 9 inclusive


  //Handling variable nbStars - we keep reading until it’s in range (1-3 inclusive)
  do {
    printf("Enter a value for NbStars\t");
    scanf("%d", &nbStars);
    printf("\n");
  } while (nbStars < 1 || nbStars > 3);

  //Handling variable nbStars - we keep reading until it’s in range (1-9 inclusive)
  do {
    printf("Enter a value for NbLines\t");
    scanf("%d", &nbLines);
    printf("\n");
  } while (nbLines < 1 || nbLines > 9);

  return EXIT_SUCCESS;
}
