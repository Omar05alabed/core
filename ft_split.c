/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <omar.alabed@learner.42.tech>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/25 01:01:26 by oalabed           #+#    #+#             */
/*   Updated: 2025/12/28 04:19:39 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdlib.h>

static int count_words(char const *s, char c)
{
    int count;

    count = 0;
    while (*s)
    {
        while (*s == c)
            s++;
        if (*s)
            count++;
        while (*s && *s != c)
            s++;
    }
    return (count);
}

static char *word_dup(char const *s, char c)
{
    char *word;
    int i;
    int len;

    len = 0;
    while (s[len] && s[len] != c)
        len++;
    word = (char *)malloc(sizeof(char) * (len + 1));
    if (!word)
        return (NULL);
    i = 0;
    while (i < len)
    {
        word[i] = s[i];
        i++;
    }
    word[i] = '\0';
    return (word);
}

static void free_all(char **arr, int i)
{
    while (i >= 0)
        free(arr[i--]);
    free(arr);
}

char **ft_split(char const *s, char c)
{
    char **result;
    int i;

    if (!s)
        return (NULL);
    result = (char **)malloc(sizeof(char *) * (count_words(s, c) + 1));
    if (!result)
        return (NULL);
    i = 0;
    while (*s)
    {
        while (*s == c)
            s++;
        if (*s)
        {
            result[i] = word_dup(s, c);
            if (!result[i])
                return (free_all(result, i - 1), NULL);
            i++;
            while (*s && *s != c)
                s++;
        }
    }
    result[i] = NULL;
    return (result);
}
