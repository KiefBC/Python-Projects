#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int grade_avg(int letter, int words, int sentences)
{
  // Calculate the average number of letters per 100 words
  float l = (float) letter / (float) words * 100;
  // Calculate the average number of sentences per 100 words
  float s = (float) sentences / (float) words * 100;
  // Calculate the grade average
  float index = 0.0588 * l - 0.296 * s - 15.8;

  if (index < 1)
    {
    printf("Before Grade 1");
  }
    else if (index >= 16)
    {
    printf("Grade 16+");
  }
    else
    {
    printf("Grade %.0f", index);
  }
  printf("\n");
  return 0;

}

int count_letters(string text)
{
  int letter = 0;
  int words = 1;
  int sentences = 0;
  for (int i = 0; text[i] != '\0'; i++)
    {
    // count letters
    if (isalpha(text[i]))
        {
      letter++;
    }
    // count words
    else if (isspace(text[i]))
        {
      words++;
    }
    // count sentences
    else if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
      sentences++;
    }
  }
  printf("%i letters\n%i words\n%i sentences\n", letter, words, sentences);
  grade_avg(letter, words, sentences);
  return 0;
}


int main(void)
{
  //prompt the user
  string text = get_string("Text: ");
  // printf("%s\n", text);
  count_letters(text);


}#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int grade_avg(int letter, int words, int sentences)
{
  // Calculate the average number of letters per 100 words
  float l = (float) letter / (float) words * 100;
  // Calculate the average number of sentences per 100 words
  float s = (float) sentences / (float) words * 100;
  // Calculate the grade average
  float index = 0.0588 * l - 0.296 * s - 15.8;

  if (index < 1)
    {
    printf("Before Grade 1");
  }
    else if (index >= 16)
    {
    printf("Grade 16+");
  }
    else
    {
    printf("Grade %.0f", index);
  }
  printf("\n");
  return 0;

}

int count_letters(string text)
{
  int letter = 0;
  int words = 1;
  int sentences = 0;
  for (int i = 0; text[i] != '\0'; i++)
    {
    // count letters
    if (isalpha(text[i]))
        {
      letter++;
    }
    // count words
    else if (isspace(text[i]))
        {
      words++;
    }
    // count sentences
    else if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
      sentences++;
    }
  }
  printf("%i letters\n%i words\n%i sentences\n", letter, words, sentences);
  grade_avg(letter, words, sentences);
  return 0;
}


int main(void)
{
  //prompt the user
  string text = get_string("Text: ");
  // printf("%s\n", text);
  count_letters(text);


}