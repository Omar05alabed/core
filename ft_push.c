/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_push.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/04 15:24:30 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/08 15:50:58 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

int	ft_push(t_stack **a, int value)
{
	t_stack	*node;

	node = ft_new_node(value);
	if (node == NULL)
		return (0);
	node->next = *a;
	*a = node;
	return (1);
}
