/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   assaign_index.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/06 14:20:57 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/06 14:35:05 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	assign_index(s_stack **a)
{
	s_stack	*current;
	s_stack	*compare;
	int		index;

	current = *a;
	while (current)
	{
		index = 0;
		compare = *a;
		while (compare)
		{
			if (compare->value < current->value)
				index++;
			compare = compare->next;
		}
		current->index = index;
		current = current->next;
	}
}
