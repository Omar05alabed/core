/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   simple_sort.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/06 14:43:17 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/06 15:17:21 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	get_min_pos(s_stack *stack)
{
	int	min;
	int	pos;
	int	i;

	min = stack->value;
	pos = 0;
	i = 0;
	while (stack)
	{
		if (stack->value < min)
		{
			min = stack->value;
			pos = i;
		}
		i++;
		stack = stack->next;
	}
	return (pos);
}

void	simple_sort(s_stack **a, s_stack **b)
{
	int	size;
	int	pos;

	size = stack_size(a);
	while (size > 0)
	{
		pos = get_min_pos(*a);
		if (pos <= size / 2)
		{
			while (pos > 0)
			{
				ft_ra(a);
				pos--;
			}
		}
		else
		{
			while (pos++ < size)
				ft_rra(a);
		}
		ft_pb(a, b);
		size--;
	}
	while (*b)
		ft_pa(a, b);
}
