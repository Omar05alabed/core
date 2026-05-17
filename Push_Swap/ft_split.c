/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: domansou <domansou@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/14 07:09:50 by domansou          #+#    #+#             */
/*   Updated: 2026/04/14 20:44:27 by domansou         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	count_words(const char *s)
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

static char	*extract_word(const char *s, int start, int end)
{
	char	*word;
	int		i;

	word = malloc(sizeof(char) * (end - start + 1));
	if (!word)
		return (NULL);
	i = 0;
	while (start < end)
		word[i++] = s[start++];
	word[i] = '\0';
	return (word);
}

static int	fill_split(const char *s, char **res, int *j)
{
	int	i;
	int	start;

	i = 0;
	while (s[i])
	{
		while (s[i] && is_space(s[i]))
			i++;
		start = i;
		while (s[i] && !is_space(s[i]))
			i++;
		if (i > start)
		{
			res[*j] = extract_word(s, start, i);
			if (!res[*j])
				return (0);
			(*j)++;
		}
	}
	return (1);
}

char	**split_whitespace(const char *s)
{
	char	**res;
	int		words;
	int		j;

	words = count_words(s);
	res = malloc(sizeof(char *) * (words + 1));
	if (!res)
		return (NULL);
	j = 0;
	if (!fill_split(s, res, &j))
		return (free_split(res), NULL);
	res[j] = NULL;
	return (res);
}
