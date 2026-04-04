/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sa.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/04 16:41:55 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/04 17:02:03 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_sa(s_stack **a)
{
	s_stack	*first;
	s_stack	*seconde;

	if (!a || !*a || !(*a)->next)
		return ;
	first = *a;
	seconde = (*a)->next;
	first->next = seconde->next;
	seconde->next = *a;
	*a = seconde;
}
