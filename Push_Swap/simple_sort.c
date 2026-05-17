/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   simple_sort.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/06 14:43:17 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/12 17:53:47 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	get_min_pos(t_stack *stack)
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

void	simple_sort(t_stack **a, t_stack **b, t_bench *bench)
{
	int	size;
	int	pos;

	size = stack_size(*a);
	while (size > 0)
	{
		pos = get_min_pos(*a);
		if (pos <= size / 2)
		{
			while (pos > 0)
			{
				ft_ra(a, bench);
				pos--;
			}
		}
		else
		{
			while (pos++ < size)
				ft_rra(a, bench);
		}
		ft_pb(a, b, bench);
		size--;
	}
	while (*b)
		ft_pa(a, b, bench);
}
