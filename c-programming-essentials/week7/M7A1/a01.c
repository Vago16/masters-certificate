#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

#include "a01.h"

void scanData ( EmployeeRecord data[], int size ) {
    for(int i = 0; i < size; i ++) {
        printf("\tInformation about employee %d:\n", i);
        printf("\t\tFull name = ");
        scanf("%19s", data[i].name);        //or fgets(data[i].name, MAX_LENGTH, stdin);
        getchar();
        printf("\t\tSSN = ");
        scanf("%ld", &data[i].ssn);
        getchar();
    }
}

void displayData(EmployeeRecord data[], int size) {
    for(int i = 0; i < size; i ++) {
        displayDataAt(data, i);
    }
}

void displayDataAt(EmployeeRecord data[], int i) {
    printf("Employee #%d: name = %s, ssn = %ld\n", i, data[i].name, data[i].ssn);
}