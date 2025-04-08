// TODO - Implement the functions in this file

#include <stdlib.h>
#include "tools.h"

/*
Assignment  M4PA
File        M4PA.c

Student:    Evagelos Petropoulos U75564437
Date:       4/7/25

Features:   This program implements 2 functions that are meant to work on 2 dimensional arrays.  isMatrixSorted checks
            if the matrix is sorted and matrixSort sorts the matrix. 
Bugs:       No known bugs
*/

int isMatrixSorted( int data[NB_ROWS][NB_COLS] ){
    int total_elements = NB_ROWS * NB_COLS; //size of array

    for (int i = 0; i < total_elements - 1; i++) {
        int current = data[i / NB_COLS][i % NB_COLS];   //first index is referencing row, second index is referencingcolumn
        int next = data[(i + 1) / NB_COLS][(i + 1) % NB_COLS];      //next elements in row and column, respectively
        if (current > next) {
            return 0;
        }
    }
    return 1;
}

void matrixSort( int data[NB_ROWS][NB_COLS]){
    int i, j;       //initialize loop variables
    int total_elements = NB_ROWS * NB_COLS; //size of array

    for (i = 0; i < total_elements - 1; i++) {

        for (j = i + 1; j < total_elements; j++) {
            int iRow = i / NB_COLS;     //variables for outer loop row and column
            int iCol = i % NB_COLS;
            int jRow = j / NB_COLS;     //variables for inner loop row and column
            int jCol = j % NB_COLS;

            if (data[iRow][iCol] > data[jRow][jCol]) {
                int temp = data[iRow][iCol];        //temporarary variable to hold data to swap
                data[iRow][iCol] = data[jRow][jCol];
                data[jRow][jCol] = temp;
            }
        }
    }
}
