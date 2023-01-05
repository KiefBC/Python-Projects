#include <cs50.h>
#include <stdio.h>

int main(void)
{
  long long cardNum;
  do
{
    cardNum = get_long_long("Enter Card number: ");
  }
while (cardNum < 1);
  long long tempCC;
  int remNum, sum = 0, sum1 = 0, counter = 1, currentNum, total;
  tempCC = cardNum;
  do
{
    currentNum = tempCC % 10;
    if (counter % 2 == 0)
    {
      currentNum = currentNum * 2;
      if (currentNum > 9)
        {
        currentNum = currentNum - 9;
      }
      sum += currentNum;
    }
    else
    {
      sum1 += currentNum;
    }
    counter++;
    tempCC = tempCC / 10;
  }
while (tempCC > 0);
  total = sum + sum1;
  if (total % 10 == 0)
{
    tempCC = cardNum;
    do
    {
      tempCC = tempCC / 10;
    }
    while (tempCC < 10 || tempCC > 100);

    if (((counter - 1) == 15) && (tempCC == 34 || tempCC == 37))
    {
      printf("AMEX\n");
    }
    else if (((counter - 1) == 16) && (tempCC >= 51 && tempCC <= 55))
    {
      printf("MASTERCARD\n");
    }
    else if ((((counter - 1) == 13) || ((counter - 1) == 16)) && (tempCC / 10 == 4))
    {
      printf("VISA\n");
    }
    else
    {
      printf("INVALID\n");
    }
  }
 else
 {
    printf("INVALID\n");
  }
}