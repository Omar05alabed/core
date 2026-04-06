/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sa.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/04 16:41:55 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/06 13:04:01 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	ft_sa(s_stack **a)
{
	s_stack	*first;
	s_stack	*second;

	if (!a || !*a || !(*a)->next)
		return ;
	first = *a;
	second = (*a)->next;
	first->next = second->next;
	seconde->next = *a;
	*a = second;
	write(1, "sa\n", 3);
}
