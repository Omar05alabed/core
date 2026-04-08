/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   chunk_sort.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/08 15:18:15 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/08 15:18:24 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	max_index(s_stack *s)
{
	int	max;

	if (!s)
		return (-1);
	max = s->index;
	while (s)
	{
		if (s->index > max)
			max = s->index;
		s = s->next;
	}
	return (max);
}

static int	pos_index(s_stack *s, int idx)
{
	int	pos;

	pos = 0;
	while (s)
	{
		if (s->index == idx)
			return (pos);
		pos++;
		s = s->next;
	}
	return (-1);
}

static void	push_chunks(s_stack **a, s_stack **b, int chunk)
{
	int	i;

	i = 0;
	while (*a)
	{
		if ((*a)->index <= i)
		{
			ft_pb(a, b);
			ft_rb(b);
			i++;
		}
		else if ((*a)->index <= i + chunk)
		{
			ft_pb(a, b);
			i++;
		}
		else
			ft_ra(a);
	}
}

static void	pull_max(s_stack **a, s_stack **b)
{
	int	max;
	int	pos;
	int	size;

	while (*b)
	{
		max = max_index(*b);
		pos = pos_index(*b, max);
		size = stack_size(*b);
		if (pos <= size / 2)
			while (pos-- > 0)
				ft_rb(b);
		else
			while (pos++ < size)
				ft_rrb(b);
		ft_pa(a, b);
	}
}

void	sort_medium_chunk(s_stack **a, s_stack **b)
{
	int	size;
	int	chunk;

	if (!a || !*a)
		return ;
	size = stack_size(*a);
	chunk = (size <= 100) * 15 + (size > 100) * 35;
	push_chunks(a, b, chunk);
	pull_max(a, b);
}
