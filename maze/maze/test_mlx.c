#include "mlx.h"

int main(void)
{
    void *mlx;
    void *window;

    mlx = mlx_init();
    window = mlx_new_window(mlx, 800, 600, "My Maze");

    mlx_loop(mlx);

    return (0);
}
