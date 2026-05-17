/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   collect_tokens.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: domansou <domansou@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/14 17:41:11 by domansou          #+#    #+#             */
/*   Updated: 2026/04/14 20:42:36 by domansou         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

static int	count_words(char *s)
{
	int	i;
	int	count;

	i = 0;
	count = 0;
	while (s[i])
	{
		while (s[i] && is_space(s[i]))
			i++;
		if (s[i])
		{
			count++;
			while (s[i] && !is_space(s[i]))
				i++;
		}
	}
	return (count);
}

static int	count_total_tokens(int argc, char **argv, int start)
{
	int	total;

	total = 0;
	while (start < argc)
	{
		total += count_words(argv[start]);
		start++;
	}
	return (total);
}

static int	append_tokens(char **all, char **tmp, int k)
{
	int	j;

	j = 0;
	while (tmp[j])
	{
		all[k] = tmp[j];
		k++;
		j++;
	}
	free(tmp);
	return (k);
}

static void	free_partial(char **arr, int size)
{
	int	i;

	i = 0;
	while (i < size)
	{
		free(arr[i]);
		i++;
	}
	free(arr);
}

char	**collect_tokens(int argc, char **argv, int start)
{
	char	**all;
	char	**tmp;
	int		total;
	int		k;

	total = count_total_tokens(argc, argv, start);
	if (total == 0)
		return (NULL);
	all = malloc(sizeof(char *) * (total + 1));
	if (!all)
		return (NULL);
	k = 0;
	while (start < argc)
	{
		tmp = split_whitespace(argv[start]);
		if (!tmp)
			return (free_partial(all, k), NULL);
		k = append_tokens(all, tmp, k);
		start++;
	}
	all[k] = NULL;
	return (all);
}
