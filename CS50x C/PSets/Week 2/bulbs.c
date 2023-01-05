#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Function to print a dark or light emoji depending on the value of the bit
void print_bulb(int bit)
{
  if (bit == 0)
    {
    // Dark emoji
    printf("\U000026AB");
  }
    else if (bit == 1)
    {
    // Light emoji
    printf("\U0001F7E1");
  }
}

int main(void)
{
  // Read a string from the user using the CS50 library
  string s = get_string("Enter a string: ");

  // Iterate over each character in the string
  for (int i = 0; i < strlen(s); i++)
    {
    // Iterate over each bit in the character, starting with the most significant bit
    for (int j = 7; j >= 0; j--)
        {
      // Convert the character to binary >> shifting to the right and print the result using the print_bulb() function
      print_bulb((s[i] >> j) & 1);
    }
    printf("\n"); // Print a new line after processing each character
  }
}