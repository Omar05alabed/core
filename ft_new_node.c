/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_new_node.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/04 14:39:34 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/04 14:52:13 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

s_stack	*new_node(int value)
{
	s_stack	*node;

	node = malloc(sizeof s_stack);
	if (!node)
		return (NULL);
	node->value = value;
	node->index = 0;
	node->next = NULL;
	return (node);
}
