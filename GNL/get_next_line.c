/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: oalabed <omar.alabed@learner.42.tech>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/19 03:01:36 by oalabed           #+#    #+#             */
/*   Updated: 2026/03/01 01:20:06 by oalabed          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static char	*read_file(int fd, char *buffer)
{
	char	*tmp;
	ssize_t	bytes;
	char	*joined;

	if (!buffer)
		buffer = ft_strdup("");
	tmp = malloc(BUFFER_SIZE + 1);
	if (!tmp)
		return (NULL);
	bytes = read(fd, tmp, BUFFER_SIZE);
	while (bytes > 0)
	{
		tmp[bytes] = '\0';
		joined = ft_strjoin(buffer, tmp);
		free(buffer);
		buffer = joined;
		if (ft_strchr(buffer, '\n'))
			break ;
		bytes = read(fd, tmp, BUFFER_SIZE);
	}
	free(tmp);
	if (bytes < 0)
		return (free(buffer), NULL);
	return (buffer);
}

static char	*extract_line(char *buffer)
{
	size_t	i;

	i = 0;
	if (!buffer || !buffer[i])
		return (NULL);
	while (buffer[i] && buffer[i] != '\n')
		i++;
	if (buffer[i] == '\n')
		i++;
	return (ft_substr(buffer, 0, i));
}

static char	*clean_buffer(char *buffer)
{
	size_t	i;
	char	*new_buffer;

	i = 0;
	while (buffer[i] && buffer[i] != '\n')
		i++;
	if (!buffer[i])
	{
		free(buffer);
		return (NULL);
	}
	new_buffer = ft_substr(buffer, i + 1, ft_strlen(buffer) - i);
	free(buffer);
	return (new_buffer);
}

char	*get_next_line(int fd)
{
	static char	*buffer;
	char		*line;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	buffer = read_file(fd, buffer);
	if (!buffer)
		return (NULL);
	line = extract_line(buffer);
	buffer = clean_buffer(buffer);
	return (line);
}
