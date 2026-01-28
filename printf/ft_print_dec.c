/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_dec.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <omar.alabed@learner.42.tech>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/21 20:14:07 by oalabed           #+#    #+#             */
/*   Updated: 2026/01/23 02:13:42 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "ft_printf.h"

int	ft_print_dec(int n)
{
	int		count;
	long	num;

	count = 0;
	num = n;
	if (n < 0)
	{
		count += ft_print_char('-');
		num = -num;
	}
	if (num >= 10)
		count += ft_print_dec(num / 10);
	count += ft_print_char(num % 10 + '0');
	return (count);
}
/*
int main()
{
	ft_print_dec(0);
	ft_print_char('\n');
	ft_print_dec(-7);
	ft_print_char('\n');
	ft_print_dec(5);
	ft_print_char('\n');
	ft_print_dec(999);
	ft_print_char('\n');
        ft_print_dec(-2147483648);
	return (0);
	
}*/
