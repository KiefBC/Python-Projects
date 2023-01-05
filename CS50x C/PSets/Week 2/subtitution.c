#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    // check for correct number of command line arguments
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    // get the key
    string key = argv[1];

    // check that the key is 26 characters long
    if (strlen(key) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    // check that the key only contains lowercase letters
    for (int i = 0; i < 26; i++)
    {
        if (!isalpha(key[i]))
        {
            printf("Key must only contain letters.\n");
            return 1;
        }
    }

    // create an array to store the mapping from plaintext to ciphertext
    char mapping[26];

    // initialize the mapping array
    for (int i = 0; i < 26; i++)
    {
        char c = tolower(key[i]);

        // check for duplicates in the key
        for (int j = 0; j < i; j++)
        {
            if (c == mapping[j])
            {
                printf("Key must not contain duplicate characters.\n");
                return 1;
            }
        }

        mapping[i] = c;
    }

    // get the plaintext
    string plaintext = get_string("plaintext: ");
    int n = strlen(plaintext);

    // create an array to store the ciphertext
    char ciphertext[n + 1];

    // encrypt the plaintext
    for (int i = 0; i < n; i++)
    {
        char c = plaintext[i];

        // preserve case
        if (isupper(c))
        {
            ciphertext[i] = toupper(mapping[c - 'A']);
        }
        else if (islower(c))
        {
            ciphertext[i] = tolower(mapping[c - 'a']);
        }
        else
        {
            ciphertext[i] = c;
        }
    }

    // add null terminator to the ciphertext array
    ciphertext[n] = '\0';

    // print the ciphertext
    printf("ciphertext: %s\n", ciphertext);

    return 0;
}
