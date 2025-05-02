#pragma once

#define MAX_LENGTH 20

struct employee_record {
    char *name;
    long ssn;
};

typedef struct employee_record EmployeeRecord;

void scanData(EmployeeRecord data[], int size);
void displayData(EmployeeRecord data[], int size);
void displayDataAt(EmployeeRecord data[], int i);