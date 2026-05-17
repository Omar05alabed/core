/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   bench.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/12 14:34:46 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/15 01:28:25 by domansou         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	bench(double disorder, t_bench *benchb)
{
	ft_printf(2, "[bench] disorder: ");
	ft_print_float(disorder * 100, 2);
	ft_printf(2, "%%\n");
	ft_printf(2, "[bench] strategy: %s /", benchb->strategy);
	ft_printf(2, "%s \n", benchb->complexity);
	ft_printf(2, "[bench] total_ops: %d\n", benchb->total_obs);
	ft_printf(2, "[bench] sa: %d sb: %d ss: %d pa: %d pb: %d\n", benchb->sa,
		benchb->sb, benchb->ss, benchb->pa, benchb->pb);
	ft_printf(2, "[bench] ra: %d rb: %d rr: %d rra: %d rrb: %d rrr: %d\n",
		benchb->ra, benchb->rb, benchb->rr, benchb->rra, benchb->rrb,
		benchb->rrr);
}
