#include <stdio.h>
#include <stdlib.h>

/*An exercise in conceptualizing pointers.*/

int main ()
    {
    printf("1.\n"); ////////////
    int array[5] = {0,1,2,3,4};

    for(int i =0; i < 5; i++) {
        printf("Array index %d is %d   ", i + 1, array[i]);
    }

    printf("\n");
    
    printf("2.\n"); ////////////
    int *p1, **p2;
    printf("Trying to print the variable pointers p1 or p2 leads to a segmentation fault as they are not yet declared with a non-NULL value.\n");
    //printf("Pointer *p1's value is %d\n", *p1);       //leads to segmentation fault cause not declared with a non-NULL value, causing segmentation fault
    //printf("Pointer **p2's value is %d\n", **p2);     //leads to segmentation fault cause not declared with a non-NULL value, causing segmentation fault
    
    printf("3.\n"); ////////////
    int * parray[2] = { NULL , NULL };    // printf("Pointer *parrays's value is %d\n", *parray);*/ 
    /*attempting to printf this pointer would lead to dereferencing a NULL pointer and getting the first value of the array, 
    which is NULL and would liekly lead to segmentation fault */
    for(int i =0; i < 2; i++) {
        printf("parray index %d is %d   ", i + 1, parray[i]);
    }
    printf("\n");

    printf("4.\n"); ///////////
    p1= & array[2] ;        //p1 now points to array[2]

    printf("Pointer *p1's value is %d\n", *p1); 
    printf("p1's memory address is %d\n", p1);       //will print out warning when compiling and print out memory address

    printf("5.\n"); ///////////
    *p1 = 20 ;      //3rd index(array[2] value of the array is now 20)

    printf("Pointer *p1's value is %d\n", *p1); 
    printf("p1's memory address is %d\n", p1);   //same memory value as prior

    for(int i =0; i < 5; i++) {
        printf("Array index %d is %d   ", i + 1, array[i]);
    }

    printf("\n");

    printf("6.\n"); ///////////
    p2 = & p1 ;

    printf("Pointer *p1's value is %d\n", *p1); 
    printf("p1's memory address is %d\n", p1);
    printf("Pointer **p2's value is %d\n", **p2);       //now pointing at whatever value p1 is pointing at
    printf("Pointer *p2's value is a memory address which is %d\n", *p2);     //since it is pointing at a pointer, its value is a memory address
    printf("p2's memory address is %d\n", p2);      //unique memory address

    printf("7.\n"); ///////////
    ** p2 = 30 ;        //whatever value the pointer that p2 is pointing at should be 30, in this case array[2]

    printf("Pointer *p1's value is %d\n", *p1); //30
    printf("p1's memory address is %d\n", p1);
    printf("Pointer **p2's value is %d\n", **p2);  //30
    printf("Pointer *p2's value is a memory address which is %d\n", *p2);   
    printf("p2's memory address is %d\n", p2);
    for(int i =0; i < 5; i++) {
        printf("Array index %d is %d   ", i + 1, array[i]);
    }
    printf("\n");

    printf("8.\n"); ///////////
    //*p2 = NULL;
    printf("The expression \"*p2 = NULL\" leads to a segmentation fault.\n");

    printf("9.\n"); ///////////
    parray[0] = & array[0];     //since parray is an array of pointers, it is now pointing at array[0]

    printf("Memory address of parray[0] is %d\n", parray[0]);
    printf("Dereferencing parray[0] gets the value %d\n", *parray[0]);      //value at where it is pointing, array[0]
    printf("Value of array[0] is now %d\n",array[0]);

    printf("10.\n"); ///////////
    parray[1] = & **p2; // parray[1] now points at **p2, which points at *p1, which points at array[2]

    printf("Memory address of parray[1] is %d\n", parray[1]);
    printf("Dereferencing parray[1] gets the value %d\n", *parray[1]);      //value at where it is pointing, **p2
    printf("Pointer *p1's value is %d\n", *p1); //30
    printf("p1's memory address is %d\n", p1);
    printf("Pointer **p2's value is %d\n", **p2);  //30
    printf("Pointer *p2's value is a memory address which is %d\n", *p2);   //points at p1's memory address
    printf("p2's memory address is %d\n", p2);

    for(int i =0; i < 5; i++) {
        printf("Array index %d is %d   ", i + 1, array[i]);
    }
    printf("\n");

    printf("11.\n"); ///////////
    *parray[0] = 30 ;

    printf("Memory address of parray[0] is %d\n", parray[0]);
    printf("Dereferencing parray[0] gets the value %d\n", *parray[0]);      //value at where it is pointing, array[0]
    printf("Value of array[0] is now %d\n",array[0]);       //30
    printf("\n");

    printf("12.\n"); ///////////
    *parray[1] = 300;

    printf("Memory address of parray[1] is %d\n", parray[1]);
    printf("Dereferencing parray[1] gets the value %d\n", *parray[1]);      //value at where it is pointing, **p2
    printf("Pointer *p1's value is %d\n", *p1); //300
    printf("p1's memory address is %d\n", p1);
    printf("Pointer **p2's value is %d\n", **p2);  //300
    printf("Pointer *p2's value is a memory address which is %d\n", *p2);   //points at p1's memory address
    printf("p2's memory address is %d\n", p2);

    printf("\nFinal look at Array\n");

    for(int i =0; i < 5; i++) {
        printf("Array index %d is %d   ", i + 1, array[i]);
    }

    printf("\nFinal look at parray\n");

    for(int i =0; i < 2; i++) {
        printf("parray index %d is %d   ", i + 1, parray[i]);
    }
    printf("\n");
    return EXIT_SUCCESS;
    }

    