/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ss.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/04 17:11:18 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/12 14:54:27 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	ft_ss(t_stack **a, t_stack **b, t_bench *bench)
{
	ft_sa(a, bench);
	ft_sb(b, bench);
	if (bench)
	{
		bench->total_obs++;
		bench->ss++;
	}
	write(1, "ss\n", 3);
}
