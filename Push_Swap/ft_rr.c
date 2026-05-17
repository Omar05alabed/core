/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rr.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/04 17:54:54 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/12 14:54:43 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	ft_rr(t_stack **a, t_stack **b, t_bench *bench)
{
	ft_ra(a, bench);
	ft_rb(b, bench);
	if (bench)
	{
		bench->total_obs++;
		bench->rr++;
	}
	write(1, "rr\n", 3);
}
