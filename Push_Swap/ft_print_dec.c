/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_dec.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <omar.alabed@learner.42.tech>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/21 20:14:07 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/12 17:00:20 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

int	ft_print_dec(int n, int fd)
{
	int		count;
	long	num;

	count = 0;
	num = n;
	if (n < 0)
	{
		count += ft_print_char('-', fd);
		num = -num;
	}
	if (num >= 10)
		count += ft_print_dec(num / 10, fd);
	count += ft_print_char(num % 10 + '0', fd);
	return (count);
}
/*
int	main(void)
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
