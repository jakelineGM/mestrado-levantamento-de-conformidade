#include <stdio.h>
#include <math.h>

double raiz(double x, double x0, double e) {
  if (fabs(x - x0 * x0) <= e) {
    return x0;
  } else {
  double novo_x0 = (x0 + x / x0) / 2.0;
  return raiz(x, novo_x0, e);
  }
}

int main(void) {
  int N;
  scanf("%d", &N);
  for (int i = 0; i < N; i++) {
    int z;
    double z0, e;
    scanf("%d %lf %lf", &z, &z0, &e);
    double resultado = raiz((double)z, z0, e);
    printf("%.5f\n", resultado);
  }
return 0;
}