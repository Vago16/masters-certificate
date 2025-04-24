#include <stdio.h>
#include <stdlib.h>

int main () {
    int myarray[3] = {1,2,3};
    printf("Step 1\n");
    for(int i =0; i < 3; i++) {
        printf("Array index %d  memory address is %p   ", i, &myarray[i]);
    }
    printf("\n");

    printf("myarray memory address is %p\n", myarray);
    printf("\n");

    printf("Step 2\n");
    printf("\tFirst address\t = %p\n", &myarray[0]);
    printf("\tSecond address\t = %p\n", &myarray[1]);
    printf("\tDifference\t = %ld\n", &myarray[1] - &myarray[0]);        //1 int unit is 4
    printf("\n");

    printf("Step 3\n");
    int * p = &myarray[2];

    printf("\t(p-1)\t = %p\n", p - 1);
    printf("\t(p-2)\t = %p\n", p - 2);
    printf("\t(p-3)\t = %p\n", p - 3);
    printf("\n");
    
    *p = myarray[0];
    printf("%p\n", p);
    printf("%d\n", *p);
    for(int i =0; i < 3; i++) {
        printf("\tIteration #%d\tp = %p, *p = %d\n", i, p++, i + 1);
    }
}