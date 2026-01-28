/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_str.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <omar.alabed@learner.42.tech>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/20 23:41:28 by oalabed           #+#    #+#             */
/*   Updated: 2026/01/20 23:41:31 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include "ft_printf.h"

int	ft_print_str(char	*s)
{
	int	i;

	i = 0;
	if (!s)
		return (ft_print_str("(null)"));
	while (s[i])
	{
		write(1, &s[i], 1);
		i++;
	}
	return (i);
}
/*
int main(void)
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
    
    return 0;
}*/
