#include <stdlib.h>
#include <stdio.h>

int main () {

	int coins = 21;
	int input = 0;
	int counter = 1;
	int player = 0;
	
	while (coins > 0) {
		printf("The stack has %d coins.\n", coins);
		
		
		if (counter % 2 == 1) {
			printf("Player 1 takes: ");
			scanf("%d", &input);
			player = 1;
			while ((coins < input) && (coins <= 3)) {
				printf("There are only %d coins remaining for you to take.\n", coins);
				printf("Player 1 takes: ");
				scanf("%d", &input);
			}
			
		} else if (counter % 2 == 0) {
			printf("Player 2 takes: ");
			scanf("%d", &input);
			player = 2;
			while ((coins < input) && (coins <= 3)) {
				printf("There are only %d coins remaining for you to take.\n", coins);
				printf("Player 2 takes: ");
				scanf("%d", &input);
			}
		}
		
		while (input < 1 || input > 3) {
			printf("You can only take between 1 and 3 coins during each turn.\n");
			if (counter % 2 == 1) {
				printf("Player 1 takes: ");
				scanf("%d", &input);
				player = 1;
			} else if (counter % 2 == 0) {
				printf("Player 2 takes: ");
				scanf("%d", &input);
				player = 2;
			}
		
		}
		
		counter += 1;
		coins = coins - input;
		
	}
	if (coins < 0) {
		coins = 0;
	} 
	printf("The stack has %d coins.\n", coins);
	printf("Player %d wins!\n", player);



	return EXIT_SUCCESS;

}