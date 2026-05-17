/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_str.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <omar.alabed@learner.42.tech>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/20 23:41:28 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/12 14:10:06 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include <unistd.h>

int	ft_print_str(char *s, int fd)
{
	int	i;

	i = 0;
	if (!s)
		return (ft_print_str("(null)", fd));
	while (s[i])
	{
		write(fd, &s[i], 1);
		i++;
	}
	return (i);
}
/*
int	main(void)
{
	int count;

	// Test 1: Normal string
	count = ft_print_str("Hello, World!");
	write(1, "\n", 1);

	// Test 2: Empty string
	count = ft_print_str("");
	write(1, " (empty string printed)\n", 24);

	// Test 3: NULL pointer
	count = ft_print_str(NULL);
	write(1, "\n", 1);

	// Test 4: String with special characters
	count = ft_print_str("Tab:\there\nNewline above");
	write(1, "\n", 1);

	return (0);
}*/
