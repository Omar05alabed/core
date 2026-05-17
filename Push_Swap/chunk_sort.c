/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   chunk_sort.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/12 14:31:20 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/12 17:56:51 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/* ******************************static  int     chunk_size(int  size)

{

		int i;


		i=1;

		while(i*i < size)

				i++;

		return(i);

}


void	sort_medium_chunk(t_stack **a,
		t******************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   chunk_sort.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/08 15:18:15 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/12 13:11:34 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	max_index(t_stack *s)
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

static int	pos_index(t_stack *s, int idx)
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

static void	push_chunks(t_stack **a, t_stack **b, int chunk, t_bench *bench)
{
	int	i;

	i = 0;
	while (*a)
	{
		if ((*a)->index <= i)
		{
			ft_pb(a, b, bench);
			ft_rb(b, bench);
			i++;
		}
		else if ((*a)->index <= i + chunk)
		{
			ft_pb(a, b, bench);
			i++;
		}
		else
			ft_ra(a, bench);
	}
}

static void	pull_max(t_stack **a, t_stack **b, t_bench *bench)
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
				ft_rb(b, bench);
		else
			while (pos++ < size)
				ft_rrb(b, bench);
		ft_pa(a, b, bench);
	}
}

void	sort_medium_chunk(t_stack **a, t_stack **b, t_bench *bench)
{
	int	size;
	int	chunk;
	int	i;

	if (!a || !*a)
		return ;
	size = stack_size(*a);
	i = 1;
	while (i * i < size)
		i++;
	chunk = i;
	push_chunks(a, b, chunk, bench);
	pull_max(a, b, bench);
}
