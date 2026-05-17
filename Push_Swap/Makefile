# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: user <user@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/13 00:00:00 by user              #+#    #+#              #
#    Updated: 2026/04/14 19:55:13 by domansou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = push_swap

CC = cc
CFLAGS = -Wall -Wextra -Werror
RM = rm -f

SRCS = adaptive.c assign_index.c bench.c bench_init.c chunk_sort.c disorder.c \
       free_stack.c ft_atoi.c ft_duplicate.c ft_issorted.c ft_new_node.c ft_pa.c \
       ft_parsing.c ft_pb.c ft_push.c ft_ra.c ft_rb.c ft_rr.c ft_rra.c ft_rrb.c \
       ft_rrr.c ft_sa.c ft_sb.c ft_ss.c is_number.c print_error.c radix_sort.c \
       simple_sort.c  stack_size.c main.c ft_print_char.c ft_print_dec.c \
       ft_printf.c ft_print_str.c str_comp.c ft_strcpy.c ft_print_float.c set_strategy.c \
       check_sorted.c handle_flags.c init_stack.c split_free.c  collect_tokens.c ft_split.c is_space.c

OBJS = $(SRCS:.c=.o)
HEADER = push_swap.h ft_printf.h

# ---------------------------- RULES -------------------------------- #

all: $(NAME)

$(NAME): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(NAME)

%.o: %.c $(HEADER)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(RM) $(OBJS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re
