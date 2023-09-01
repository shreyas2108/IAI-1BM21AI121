#include <stdio.h>

int main() {
    int x; 
    

    int favorable_outcomes = 0;
    int total_outcomes = 0;

    for (int die1 = 1; die1 <= 6; die1++) {
        for (int die2 = 1; die2 <= 6; die2++) {
            if (die1 != die2 && die1 + die2 == 6){
                favorable_outcomes++;
            }
            total_outcomes++;
        }
    }

   
    int gcd = 1;
    for (int i = 1; i <= favorable_outcomes; i++) {
        if (favorable_outcomes % i == 0 && total_outcomes % i == 0) {
            gcd = i;
        }
    }
    favorable_outcomes /= gcd;
    total_outcomes /= gcd;

    printf("%d/%d\n", favorable_outcomes, total_outcomes);

    return 0;
}
