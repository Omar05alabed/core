/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_parsing.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <oalabed@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/04 14:21:25 by oalabed           #+#    #+#             */
/*   Updated: 2026/04/04 14:36:44 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	*ft_parsing(int argc, char **argv)
{
	int		*arr;
	int		i;
	long	num;

	arr = malloc(sizeof(int) * argc - 1);
	if (!arr)
		return (0);
	i = 1;
	while (i < argc)
	{
		is_number(argv[i]);
		num = ft_atoi(argv[i]);
		if (num < int_Min || num > int_max)
			print_erorr();
		arr[i - 1] = num;
		i++;
	}
	ft_duplicate(arr, argc - 1);
	return (arr);
}
