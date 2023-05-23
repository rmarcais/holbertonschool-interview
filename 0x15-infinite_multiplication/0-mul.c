#include "holberton.h"
#include <stdio.h>
/**
 * is_digit - checks if a character is a digit
 * @c: the character to check
 *
 * Return: 1 if c is a digit, 0 otherwise.
 */
int is_digit(char c)
{
	if (c >= '0' && c <= '9')
		return (1);
	return (0);
}

/**
 * _strlen - returns the length of a string
 * @s: the string
 *
 * Return: the length of s.
 */
int _strlen(char *s)
{
	int count = 0;

	while (*s++)
	{
		count++;
	}

	return (count);
}

/**
 * is_number - checks if a string represents a number
 * @s: the string to check
 *
 * Return: 1 if s represents a number, 0 otherwise.
 */
int is_number(char *s)
{
	while (*s)
		if (is_digit(*s++) == 0)
			return (0);

	return (1);
}

/**
 * print_message - prints a string
 * @message: message to print
 *
 * Return: Nothing.
 */
void print_message(char *message)
{
	while (*message)
		_putchar(*message++);
	_putchar('\n');
}

/**
 * _memset_with_zero - copies the string 0 to all the characters of s
 * @s: the string to initialize
 * @len: the length of the string
 *
 * Return: Nothing.
 */
void _memset_with_zero(char *s, int len)
{
	int i;

	for (i = 0; i < len; i++)
	{
		s[i] = '0';
	}
}

/**
 * main - multiplies two numbers and prints the result
 * @first: first number
 * @second: second number
 * @len_first: length of the first number
 * @len_second: length of the second number
 * Return: Nothing.
 */
void multiply(char *first, char *second, int len_first, int len_second)
{
	int carry, sum, index1 = 0, index2 = 0, n1, n2, i, j;
	char *result;

	result = malloc((len_first + len_second + 1) * sizeof(char));
	if (!result)
		return;
	_memset_with_zero(result, len_first + len_second);
	for (i = len_first - 1; i >= 0; i--)
	{
		carry = 0;
		n1 = first[i] - 48;
		index2 = 0;
		for (j = len_second - 1; j >= 0; j--)
		{
			n2 = second[j] - 48;
			sum = n1 * n2 + (result[index1 + index2] - 48) + carry;
			carry = sum / 10;
			result[index1 + index2] = sum % 10 + 48;
			index2++;
		}
		if (carry > 0)
			result[index1 + index2] += carry;
		index1++;
	}
	i = _strlen(result) - 1;

	while (i >= 0 && result[i] == '0')
		i--;
	if (i == -1)
	{
		print_message("0");
		return;
	}
	while (i >= 0)
	{
		_putchar(result[i]);
		i--;
	}
	_putchar('\n');
	free(result);
}

/**
 * main - main entry point
 * @argc: counts number of arguments
 * @argv: array of pointers
 * Return: Always 0.
 */
int main(int argc, char *argv[])
{
	int len1, len2;

	if (argc != 3 || !is_number(argv[1]) || !is_number(argv[2]))
	{
		print_message("Error");
		exit(98);
	}
	len1 = _strlen(argv[1]);
	len2 = _strlen(argv[2]);
	if (len1 == 0 || len2 == 0)
	{
		print_message("0");
		return (0);
	}

	multiply(argv[1], argv[2], len1, len2);

	return (0);
}
