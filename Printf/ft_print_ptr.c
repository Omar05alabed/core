/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_ptr.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <omar.alabed@learner.42.tech>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/22 16:55:42 by oalabed           #+#    #+#             */
/*   Updated: 2026/02/28 03:04:29 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_print_ptr(void *ptr)
{
	int					count;
	unsigned long long	a;

	count = 0;
	if (!ptr)
	{
		write(1, "(nil)", 5);
		count = 5;
		return (count);
	}
	a = (unsigned long long)ptr;
	count += ft_print_str("0x");
	count += ft_print_hex(a, 'x');
	return (count);
}
/*
int	main(void)
{
	int n = 10;
	char c = 'A';

	ft_print_ptr(&n);
	ft_print_char('\n');
	ft_print_ptr(&c);
	return (0);
}*/
