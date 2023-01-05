#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
  // make sure they CLI properly
  if (argc != 2)
    {
    printf("Usage: ./caesar key\n");
    return 1;
  }

  // we need a Key thats not a String
  for (int i = 0; i < strlen(argv[1]); i++)
    {

    if (isalpha(argv[1][i]))
        {
      printf("Usage: ./caesar key\n");
      return 1;
    }
  }

  string text = get_string("plaintext: ");
  printf("ciphertext: ");
  int key = atoi(argv[1]) % 26;

  // loop over the word
  for (int i = 0, length = strlen(text); i < length; i++)
    {

    // checking word consists of alphanumerics
    if (isalnum(text[i]))
        {

      // if lowercase
      if (islower(text[i]))
            {
        printf("%c", (((text[i] + key) - 97) % 26 + 97));
      }
      // if uppercase
      else
            {
        printf("%c", (((text[i] + key) - 65) % 26 + 65));
      }
    }
    // print whatever is not to be ciphered
    else
        {
      printf("%c", text[i]);
    }
  }
  printf("\n");
}
