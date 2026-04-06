/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_parsing.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/04 14:21:25 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/06 12:51:40 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

int	*ft_parsing(int argc, char **argv)
{
	int		*arr;
	int		i;
	long	num;

	arr = malloc(sizeof(int) * (argc - 1));
	if (!arr)
		return (NULL);
	i = 1;
	while (i < argc)
	{
		is_number(argv[i]);
		num = ft_atoi(argv[i]);
		if (num < INT_MIN || num > INT_MAX)
			print_error();
		arr[i - 1] = num;
		i++;
	}
	ft_duplicate(arr, argc - 1);
	return (arr);
}
