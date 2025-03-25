#include <stdio.h>
#include <stdlib.h>
/*
Assignment  M2PA
File        prog3.c

Student:    Evagelos Petropoulos U75564437
Date:       3/24/25

Features:   This program will display a number of star symbols on a number of lines dictated first by the input of an integer
            value for nbStars of 1, 2, or 3, which will determine which path the program takes when putting stars on the amount
            of lines determined by lineID, which is also a user input of integer value.
Bugs:       If lineID is a negative integer, there is no output to the terminal.
*/

int main()
{
  
  int nbStars = 0;  //declare and initialize integer
  int lineID = 0;  //declare and initialize integer 

  /*ask user for number of stars on each line, and then the number of lines */
  printf("Enter a value for nbStars ");
  scanf("%d", &nbStars);

  printf("Enter a value for lineId ");
  scanf("%d", &lineID);
  if (nbStars < 1 || nbStars > 3) {
    /*statement catches if nbStars value input is outside of 1-3 range*/
    printf("Please input an integer value for nbStars of either 1, 2, or 3.\n");
  } else if(nbStars == 1) {
    /*loop for handling variable lineId*/
    for (int i = 1; i <= lineID; i++) {
      printf("#%d ", i);

      //declare and calculate the number of stars on each line if nbStars = 1
      int stars1 = nbStars * i;
      
      //loop for handling variable stars1
      for (int j = 1; j <= stars1; j++) {
        printf("*");
      }
      printf("\n"); //move to new line
    }
  } else if (nbStars == 2) {
    for (int i = 1; i <= lineID; i++) {
      printf("#%d ", i);

      //declare and calculate the number of stars on each line if nbStars = 2
      int stars2 = i * 2 - 1;

      //loop for handling stars2
      for (int j = 1; j <= stars2; j++) {
        printf("*");
      }
      printf("\n"); //move to new line
    }
  } else if (nbStars == 3) {
    for (int i = 1; i <= lineID; i++) {
      printf("#%d ", i);

      ///declare and calculate the number of stars on each line if nbStars = 2
      int stars3 = 1 + 3 * (i-1);

      //loop for handling stars3
      for (int j = 1; j <= stars3; j++) {
        printf("*");
      }
      printf("\n"); //move to new line
    } 
  } 
  return EXIT_SUCCESS;
}
 /*I came up with the formulas to calculate the number of stars that would appear on each line by first looking at each part
part of the table pertaining to a certain nbStars value by its lonesome.  After identifying the pattern,  I then wrote the
formula I believed would solve it and then fixing it up as I went or if I was very wrong in deducing it.  It took a little
bit of trial and error but after testing multiple lineID values for each nbStars value I believe I have figured it all out for
this exercise.
 */