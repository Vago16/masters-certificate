#include <stdio.h>
#include <stdlib.h>
/*
Assignment  M2PA
File        prog2.c

Student:    Evagelos Petropoulos U75564437
Date:       3/24/25

Features:   Program takes in first an input value(integer) for the number of stars(nbStars) that will appear on each line, take
            the input value(integer) for the number of lines(nbLines) that will have stars, and then output it to the terminal.
Bugs:       Entering in a non integer value for variable nbStars causes the program to skip waiting for an input for variable
            nbLines and ends the program with no output to terminal, and entering in a non integer value for variable Nblines
            causes the program to terminate with no output to terminal.
*/

int main()
{
  
  int nbStars = 0;  //declare and initialize integer
  int nbLines = 0;  //declare and initialize integer 

  /*ask user for number of stars on each line, and then the number of lines */
  printf("Enter a value for nbStars\t");
  scanf("%d", &nbStars);

  printf("Enter a value for nbLines\t");
  scanf("%d", &nbLines);

  /*loop for handling variable nbLines*/
  for (int i = 1; i <= nbLines; i++) {
    printf("#%d", i);

    //loop for handling variable nbStars, which prints the value associated with it on each line
    //for readability, I use variable j in here as the counter instead of i again
    for (int j = 1; j <= nbStars; j++) {
      printf("*");
    }
    
    printf("\n");   //move to new line
  }
  

  return EXIT_SUCCESS;
}
