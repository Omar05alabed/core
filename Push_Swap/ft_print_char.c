/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_char.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <omar.alabed@learner.42.tech>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/09 14:05:13 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/12 13:24:09 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_print_char(char c, int fd)
{
	write(fd, &c, 1);
	return (1);
}
/*
int	main(void)
{
	ft_print_char('S');
	ft_print_char('\n');
}*/
