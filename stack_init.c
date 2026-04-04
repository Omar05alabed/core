/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_init.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/04 15:11:56 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/04 17:29:48 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
s_stack	*stack_init(int *arr, int size)
{
	s_stack	*stack;
	int		z;

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
