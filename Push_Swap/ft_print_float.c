/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_float.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: domansou <domansou@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/12 23:10:27 by domansou          #+#    #+#             */
/*   Updated: 2026/04/13 00:14:10 by domansou         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	print_fraction(double fraction, int fd)
{
	int	count;
	int	i;
	int	digit;

	count = 0;
	i = 0;
	while (i < 2)
	{
		fraction *= 10;
		digit = (int)fraction;
		count += ft_print_char(digit + '0', fd);
		fraction -= digit;
		i++;
	}
	return (count);
}

int	ft_print_float(double n, int fd)
{
	long	int_part;
	double	fraction;
	int		count;

	count = 0;
	if (n < 0)
	{
		count += ft_print_char('-', fd);
		n = -n;
	}
	int_part = (long)n;
	count += ft_print_dec(int_part, fd);
	count += ft_print_char('.', fd);
	fraction = n - int_part;
	count += print_fraction(fraction, fd);
	return (count);
}
