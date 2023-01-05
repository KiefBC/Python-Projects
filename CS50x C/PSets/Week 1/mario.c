#include <cs50.h>
#include <stdio.h>

int main(void)
{
  int n;

  // Get height of pyramid
  while (true)
    {
    n = get_int("Height: ");
    if (n >= 1 && n < 9)
        {
      break;
    }
  }

  int row, col, space, n1 = n, n2 = n;

  // Print pyramid
  for (row = 1; row <= n1; row++)
    {

    // left Side
    for (space = n2 - row; space > 0; space--)
        {
      printf(" ");
    }

    // Left Side Spacing
    for (col = 1; col <= row; col++)
        {
      printf("#");
    }

    // Gap between left and Right side
    printf("  ");

    // Right Side
    for (col = 1; col <= row; col++)
        {
      printf("#");
    }

    // new line
    printf("\n");
  }
}