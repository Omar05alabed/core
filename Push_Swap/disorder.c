/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   disorder.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/08 14:09:58 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/12 11:20:06 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

double	compute_disorder(t_stack *a)
{
	t_stack	*i;
	t_stack	*j;
	int		mistake;
	int		total;

	if (!a)
		return (0.0);
	i = a;
	mistake = 0;
	total = 0;
	while (i->next != NULL)
	{
		j = i->next;
		while (j != NULL)
		{
			total = total + 1;
			if (i->value > j->value)
				mistake++;
			j = j->next;
		}
		i = i->next;
	}
	if (total == 0)
		return (0);
	return ((double)mistake / total);
}
