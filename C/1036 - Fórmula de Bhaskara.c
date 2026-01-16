#include <stdio.h>
#include <math.h>

int main() {
    double A, B, C, x1, x2, delta;

    scanf("%lf %lf %lf", &A, &B, &C);

    delta = B*B - 4*A*C;

    if (delta < 0 || A == 0) {
        printf("Impossivel calcular\n");
    } else {
        x1 = (-B + sqrt(delta)) / (2*A);
        x2 = (-B - sqrt(delta)) / (2*A);

        printf("R1 = %.5lf\n", x1);
        printf("R2 = %.5lf\n", x2);
    }

    return 0;
}
