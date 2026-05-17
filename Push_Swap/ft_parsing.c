/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_parsing.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/04 14:21:25 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/14 20:27:49 by domansou         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

static int	count_tokens(char **tokens)
{
	int	i;

	i = 0;
	while (tokens[i])
		i++;
	return (i);
}

int	*to_int_array(char **tokens, int *size)
{
	int		*arr;
	long	value;
	int		i;

	if (!tokens || !size)
		return (NULL);
	*size = count_tokens(tokens);
	arr = (int *)malloc(sizeof(int) * (*size));
	if (!arr)
		return (NULL);
	i = 0;
	while (i < *size)
	{
		if (!is_number(tokens[i]))
			return (free(arr), NULL);
		value = ft_atoi(tokens[i]);
		if (value < INT_MIN || value > INT_MAX)
			return (free(arr), NULL);
		arr[i] = (int)value;
		i++;
	}
	return (arr);
}
