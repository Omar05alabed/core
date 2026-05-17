/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <omar.alabed@learner.42.tech>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/23 03:10:26 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/13 00:12:56 by domansou         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

static int	ft_handel_coversion(char specifier, va_list args, int fd)
{
	int	count;

	count = 0;
	if (specifier == 'c')
		count += ft_print_char(va_arg(args, int), fd);
	else if (specifier == 's')
		count += ft_print_str(va_arg(args, char *), fd);
	else if (specifier == 'd')
		count += ft_print_dec(va_arg(args, int), fd);
	if (specifier == 'f')
		count += ft_print_float(va_arg(args, double), fd);
	if (specifier == '%')
		count += ft_print_char('%', fd);
	return (count);
}

int	ft_printf(int fd, const char *format, ...)
{
	va_list	args;
	int		count;
	int		i;

	va_start(args, format);
	count = 0;
	i = 0;
	while (format[i])
	{
		if (format[i] == '%')
		{
			i++;
			if (format[i] == '.')
				count += ft_handel_coversion(format[i + 3], args, fd);
			else
				count += ft_handel_coversion(format[i], args, fd);
		}
		else
			count += ft_print_char(format[i], fd);
		i++;
	}
	va_end(args);
	return (count);
}
/*
#include <stdio.h>

int	main(void) {
	int count;

	count = ft_printf("Hello, %s", "World\n");

	count = ft_printf("Number: %d\n", 42);

	count = ft_printf("Character: %c\n", 'A');

	count = ft_printf("Hexadecimal: %x\n", 255);

	count = ft_printf("Percent: %%\n");

	count = ft_printf("Pointer: %p\n", (void*)main);
  printf("omar %s", "alabed\n");

	return (0);
}*/
