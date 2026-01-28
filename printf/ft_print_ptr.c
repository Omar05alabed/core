/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_ptr.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <omar.alabed@learner.42.tech>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/22 16:55:42 by oalabed           #+#    #+#             */
/*   Updated: 2026/01/28 04:42:55 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_print_ptr(void *ptr)
{
	int				count;
	unsigned long	addr;

	count = 0;
	addr = (unsigned long)ptr;
	if (!ptr)
		ft_print_str("(nil)");
	count += ft_print_str("0x");
	count += ft_print_hex(addr, 'x');
	return (0);
}
/*
int	main(void)
{
	int n = 10;
	char c = 'A';

	ft_print_ptr(&n);
	ft_print_char('\n');
	ft_print_ptr(&c);
}*/
