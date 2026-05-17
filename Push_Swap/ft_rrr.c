/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rrr.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/06 13:59:57 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/12 14:54:59 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_rrr(t_stack **a, t_stack **b, t_bench *bench)
{
	ft_rra(a, bench);
	ft_rrb(b, bench);
	if (bench)
	{
		bench->total_obs++;
		bench->rrr++;
	}
	write(1, "rrr\n", 3);
}
