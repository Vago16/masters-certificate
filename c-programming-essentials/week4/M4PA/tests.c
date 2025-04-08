// TODO - Implement your tests in this file using testlib functions

#include <stdlib.h>
#include "tools.h"
#include "testlib.h"

//test_sort() tests are to check if just the function matrixSort works
//test_is_sorted() tests are to check if the function isMatrixSorted works too

void example_test(){
    // Example test function
    int matrix[NB_ROWS][NB_COLS] = {{1 , 2 , 3 , 4 ,  5},
                                    {6 , 7 , 8 , 9 , 10},
                                    {11, 12, 13, 14, 15} };
    TEST("Already sorted matrix", isMatrixSorted(matrix) == 1);
}

void test_sort_1(){
    // Example test function
    int matrix[NB_ROWS][NB_COLS] = {{1 , 2 , 5 , 4 ,  3},
                                    {6 , 7 , 8 , 9 , 10},
                                    {11, 12, 13, 14, 15} };
    matrixSort(matrix);
    TEST("test_sort_1",isMatrixSorted(matrix));
}

void test_is_sorted_1(){
    // tests if second dimension is working properly, should FAIL
    int matrix[NB_ROWS][NB_COLS] = {{6 , 7 , 8 , 9 , 10},
                                    {1 , 2 , 3 , 4 ,  5},
                                    {11, 12, 13, 14, 15} };
    TEST("test_is_sorted_1",isMatrixSorted(matrix));
}

void test_is_sorted_2(){
    // tests with negative numbers, sorted wrong in both columns and rows, should FAIL
    int matrix[NB_ROWS][NB_COLS] = {{-1, -2, -3, -4, -5},
                                    {-6, -7, -8, -9, -10},
                                    {-11, -12, -13, -14, -15} };
    TEST("test_is_sorted_2",isMatrixSorted(matrix));
}

void test_is_sorted_3(){
    // tests with negative numbers, sorted in rows but not in columns, should FAIL
    int matrix[NB_ROWS][NB_COLS] = {{-5, -4, -3, -2, -1},
                                    {-10, -9, -8, -7, -6},
                                    {-15, -14, -13, -12, -11} };
    TEST("test_sort_3",isMatrixSorted(matrix));
}

void test_is_sorted_4(){
    // tests with negative numbers, sorted both in columns and rows
    int matrix[NB_ROWS][NB_COLS] = {{-15, -14, -13, -12, -11},
                                    {-10, -9, -8, -7, -6},
                                    {-5, -4, -3, -2, -1} };
    TEST("test_is_sorted_4",isMatrixSorted(matrix));
}

void test_sort_2(){
    // tests with negative numbers, sorted both in columns and rows, but for matrixSort this time too
    int matrix[NB_ROWS][NB_COLS] = {{-15, -14, -13, -12, -11},
                                    {-10, -9, -8, -7, -6},
                                    {-5, -4, -3, -2, -1} };
    matrixSort(matrix);
    TEST("test_sort_2",isMatrixSorted(matrix));
}

void test_is_sorted_5(){
    // tests with duplicate numbers and out of order, should FAIL
    int matrix[NB_ROWS][NB_COLS] = {{1, 2, 5, 2, 3},
                                    {11, 11, 13, 15, 15},
                                    {6, 7, 8, 6, 10} };
    TEST("test_is_sorted_5",isMatrixSorted(matrix));
}

void test_sort_3(){
    // tests matrixSort with duplicate numbers
    int matrix[NB_ROWS][NB_COLS] = {{1, 2, 5, 2, 3},
                                    {11, 11, 13, 15, 15},
                                    {6, 7, 8, 6, 10} };
    matrixSort(matrix);
    TEST("test_sort_3",isMatrixSorted(matrix));
}

void test_sort_4(){
    // tests matrixSort with all equal numbers
    int matrix[NB_ROWS][NB_COLS] = {{7, 7, 7, 7, 7},
                                    {7, 7, 7, 7, 7},
                                    {7, 7, 7, 7, 7} };
    matrixSort(matrix);
    TEST("test_sort_4",isMatrixSorted(matrix));
}

void test_sort_5(){
    // tests an already sorted 2D array,like example_test(), but with larger values
    int matrix[NB_ROWS][NB_COLS] = {{10 , 20, 30, 40, 50},
                                    {60, 70, 80, 90, 100},
                                    {1000, 2000, 3000, 4000, 5000} };
    matrixSort(matrix);
    TEST("test_sort_5",isMatrixSorted(matrix));
}


void runAllTests(){
    // This is how you would use the above test functions
    example_test();
    test_sort_1();
    test_is_sorted_1();
    test_is_sorted_2();
    test_is_sorted_3();
    test_is_sorted_4();
    test_sort_2();
    test_is_sorted_5();
    test_sort_3();
    test_sort_4();
    test_sort_5();
}
