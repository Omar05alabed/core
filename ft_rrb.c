/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rrb.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/06 13:58:13 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/06 14:02:38 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	ft_rrb(s_stack **b)
{
	s_stack	*last;
	s_stack	*second_last;

	if (!b || !*b || !(*b)->next)
		return ;
	second_last = *b;
	while (second_last->next->next)
		second_last = second_last->next;
	last = second_last->next;
	last->next = *b;
	*b = last;
	second_last->next = NULL;
	write(1, "rrb\n", 4);
}
