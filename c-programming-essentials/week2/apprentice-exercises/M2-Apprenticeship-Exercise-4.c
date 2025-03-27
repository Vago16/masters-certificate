# include <stdlib.h>
# include <stdio.h>
# include <stdbool.h>

int main() {
    int g = 0;
    int grade = 0;
    int sum = 0;

    do {
        do {
            printf("Enter grade #%d  ", g + 1);
            scanf("%d", &grade);

            if (grade == -1) break;
            if (grade > 100 || grade < 0) {
                printf("Enter in grades between 0 and 100 only.\n");
                printf("-1 to quit.\n");
            } else {break;}

        } while(true);

        if (grade == -1) {break;}
        else{
            sum += grade;
            g++;
        }

    } while (true);

    printf("Average of grades is %.2f", (double)sum / g);

    printf("\n");
    return EXIT_SUCCESS;
}
