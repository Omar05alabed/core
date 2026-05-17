/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rra.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/06 13:28:48 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/08 15:42:34 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_rra(t_stack **a, t_bench *bench)
{
	t_stack	*last;
	t_stack	*second_last;

	if (!a || !*a || !(*a)->next)
		return ;
	second_last = *a;
	while (second_last->next->next)
		second_last = second_last->next;
	last = second_last->next;
	last->next = *a;
	*a = last;
	second_last->next = NULL;
	write(1, "rra\n", 4);
	if (bench)
	{
		bench->total_obs++;
		bench->rra++;
	}
}
