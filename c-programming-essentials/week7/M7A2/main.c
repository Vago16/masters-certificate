#include "a02.h"

#include <stdio.h>
#include <stdlib.h>


int main () {
    printf("How many employees do you wish to handle? ");
    int num_records = 5;
    scanf("%d", &num_records);
    getchar();

    EmployeeRecord * mydata = NULL;
    mydata = (EmployeeRecord*)malloc(num_records * sizeof(EmployeeRecord));

    scanData(mydata, num_records);

    displayData(mydata, num_records);


    int employee_num = 0;
    printf("Which employee do you want to display? ");
    scanf("%d", &employee_num);
    displayDataAt(mydata, employee_num);


    for(int i = 0; i < num_records; i ++) {
        free(mydata[i].name);
    }

    free(mydata);
}