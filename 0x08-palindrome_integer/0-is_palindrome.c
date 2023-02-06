#include "palindrome.h"
#include <stdio.h>

/**
 * is_palindrome - Checks wether or not a given
 * unsigned integer is a palindrome
 *
 * @n: The number to check
 *
 * Return: 1 if n is a palindrome, and 0 otherwise
 */
int is_palindrome(unsigned long n)
{
	unsigned long int n_copy = n, n_reverse = 0;

	while (n_copy > 0)
	{
		n_reverse = n_reverse * 10 + n_copy % 10;
		n_copy /= 10;
	}

	if (n == n_reverse)
		return (1);
	return (0);
}
