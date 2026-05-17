/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   radix_sort.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/08 13:57:18 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/08 15:50:11 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	radix_sort(t_stack **a, t_stack **b, t_bench *bench)
{
	int	i;
	int	size;
	int	j;
	int	max_bits;

	size = stack_size(*a);
	i = 0;
	max_bits = 0;
	while ((size >> max_bits) != 0)
		max_bits++;
	while (i < max_bits)
	{
		j = 0;
		while (j < size)
		{
			if (((*a)->index >> i) & 1)
				ft_ra(a, bench);
			else
				ft_pb(a, b, bench);
			j++;
		}
		while (*b != NULL)
			ft_pa(a, b, bench);
		i++;
	}
}
