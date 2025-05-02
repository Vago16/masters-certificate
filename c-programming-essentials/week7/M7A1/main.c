#include "a01.h"

#include <stdio.h>
#define NUMBER_RECORDS 5

int main () {
    EmployeeRecord mydata[NUMBER_RECORDS];

    scanData(mydata, NUMBER_RECORDS);

    displayData(mydata, NUMBER_RECORDS);


    int employee_num = 0;
    printf("Which employee do you want to display? ");
    scanf("%d", &employee_num);
    displayDataAt(mydata, employee_num);

}