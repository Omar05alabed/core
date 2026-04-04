/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sb.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/04 17:02:17 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/04 17:15:11 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_sb(s_stack **b)
{
	s_stack	first;
	s_stack	second;

	if (!b || !*b || !(*b)->next)
		return ;
	first = *b;
	second = (*b)->next;
	first->next = second->next;
	second->next = *b;
	*b = second;
}
