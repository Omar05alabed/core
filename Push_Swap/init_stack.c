/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init_stack.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: domansou <domansou@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/14 07:26:57 by domansou          #+#    #+#             */
/*   Updated: 2026/04/15 01:31:29 by domansou         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

static void	build_stack(t_stack **a, int *arr, int size)
{
	int	i;

	i = 0;
	while (i < size)
	{
		ft_push(a, arr[i]);
		i++;
	}
	assign_index(a);
}

void	init_stack(int argc, char **argv, int start, t_stack **a)
{
	char	**tokens;
	int		*arr;
	int		size;

	tokens = collect_tokens(argc, argv, start);
	if (!tokens)
		print_error();
	arr = to_int_array(tokens, &size);
	if (!arr || ft_duplicate(arr, size))
	{
		free_split(tokens);
		print_error();
	}
	build_stack(a, arr, size);
	free(arr);
	free_split(tokens);
}
