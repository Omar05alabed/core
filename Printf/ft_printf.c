/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <omar.alabed@learner.42.tech>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/23 03:10:26 by oalabed           #+#    #+#             */
/*   Updated: 2026/02/28 02:32:10 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "ft_printf.h"

static	int	ft_handel_coversion(char specifier, va_list args)
{
	int	count;

	count = 0;
	if (specifier == 'c')
		count += ft_print_char(va_arg(args, int));
	else if (specifier == 's')
		count += ft_print_str(va_arg(args, char *));
	else if (specifier == '%')
		count += ft_print_percent();
	else if (specifier == 'd' || specifier == 'i')
		count += ft_print_dec(va_arg(args, long));
	else if (specifier == 'u')
		count += ft_print_unsigned(va_arg(args, unsigned int));
	else if (specifier == 'X' || specifier == 'x')
		count += ft_print_hex(va_arg(args, unsigned int), specifier);
	else if (specifier == 'p')
		count += ft_print_ptr(va_arg(args, void *));
	return (count);
}

int	ft_printf(const char *format, ...)
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
			count += ft_handel_coversion(format[i], args);
		}
		else
			count += ft_print_char(format[i]);
		i++;
	}
	va_end(args);
	return (count);
}
/*
#include <stdio.h>

int main() {
    int count;

    count = ft_printf("Hello, %s", "World\n");
    
    count = ft_printf("Number: %d\n", 42);
    
    count = ft_printf("Character: %c\n", 'A');
   
    count = ft_printf("Hexadecimal: %x\n", 255);
   
    count = ft_printf("Percent: %%\n");
    
    count = ft_printf("Pointer: %p\n", (void*)main);
  printf("omar %s", "alabed\n");

    return 0;
}*/
