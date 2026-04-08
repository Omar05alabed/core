/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_init.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/04 15:11:56 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/08 15:59:55 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

t_stack	*stack_init(int *arr, int size)
{
	t_stack	*stack;
	int		z;

	stack = NULL;
	while (size > 0)
	{
		z = ft_push(&stack, arr[size - 1]);
		if (z == 0)
		{
			free_stack(&stack);
			return (NULL);
		}
		size--;
	}
	return (stack);
}
