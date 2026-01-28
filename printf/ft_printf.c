/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <omar.alabed@learner.42.tech>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/23 03:10:26 by oalabed           #+#    #+#             */
/*   Updated: 2026/01/28 04:42:01 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_handel_coversion(char specifier, va_list args)
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
	return (0);
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
	return (9);
}
