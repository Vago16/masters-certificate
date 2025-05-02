#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

#include "a02.h"

void scanData ( EmployeeRecord data[], int size ) {
    for(int i = 0; i < size; i ++) {
        printf("\tInformation about employee %d:\n", i);
        printf("\t\tFull name = ");
        char buffer[MAX_LENGTH];
        scanf("%19s", buffer);        //or fgets(data[i].name, MAX_LENGTH, stdin);
        getchar();

        int length = strlen(buffer);
        data[i].name = (char*)malloc(sizeof(char) * (length+1));
        strcpy(data[i].name, buffer);

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