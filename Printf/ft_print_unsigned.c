/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_unsigned.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <omar.alabed@learner.42.tech>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/22 02:21:49 by oalabed           #+#    #+#             */
/*   Updated: 2026/02/28 02:35:13 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_print_unsigned(unsigned int n)
{
	unsigned int	count;

	count = 0;
	if (n >= 10)
		count += ft_print_unsigned(n / 10);
	count += ft_print_char(n % 10 + '0');
	return (count);
}

/*int main()
{
	ft_print_unsigned(1);
	ft_print_char('\n');
	ft_print_unsigned(15);
	ft_print_char('\n');
	ft_print_unsigned(4294967295);
	ft_print_char('\n');
}*/
