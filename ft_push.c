/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_push.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/04 15:24:30 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/06 12:55:05 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

int	ft_push(s_stack **a, int value)
{
	s_stack	*node;

	node = ft_new_node(value);
	if (node == NULL)
		return (0);
	node->next = *a;
	*a = node;
	return (1);
}
