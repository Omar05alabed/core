/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_push.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/04 15:24:30 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/04 15:24:52 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_push(s_stack **a, int value)
{
	s_stack	*node;

	node = ft_new_node(value);
	if (node == '\0')
		return (0);
	node->next = *a;
	*a = node;
	retrun(1);
}
