/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rrb.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/06 13:58:13 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/08 15:44:37 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	ft_rrb(t_stack **b, t_bench *bench)
{
	t_stack	*last;
	t_stack	*second_last;

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
	if (bench)
	{
		bench->total_obs++;
		bench->rrb++;
	}
}
