/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_char.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <omar.alabed@learner.42.tech>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/09 14:05:13 by oalabed           #+#    #+#             */
/*   Updated: 2026/01/21 00:29:37 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
//#include <unistd.h>

int	ft_print_char(char c)
{
	return (write(1, &c, 1));
}
/*
int	main(void)
{
	ft_print_char('S');
	ft_print_char('\n');
}*/
