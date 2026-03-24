#include "include/raylib.h"
#include <string.h>

constexpr int COLS = 200;
constexpr int ROWS = 200;

int grid[ROWS][COLS] = {0};

int R[7][5] = {
    {1, 1, 1, 1, 0},
    {1, 0, 0, 0, 1},
    {1, 0, 0, 0, 1},
    {1, 1, 1, 1, 0},
    {1, 0, 1, 0, 0},
    {1, 0, 0, 1, 0},
    {1, 0, 0, 0, 1}
};

int Y[7][5] = {
    {1, 0, 0, 0, 1},
    {0, 1, 0, 1, 0},
    {0, 0, 1, 0, 0},
    {0, 0, 1, 0, 0},
    {0, 0, 1, 0, 0},
    {0, 0, 1, 0, 0},
    {0, 0, 1, 0, 0}
};

int U[7][5] = {
    {1, 0, 0, 0, 1},
    {1, 0, 0, 0, 1},
    {1, 0, 0, 0, 1},
    {1, 0, 0, 0, 1},
    {1, 0, 0, 0, 1},
    {1, 0, 0, 0, 1},
    {0, 1, 1, 1, 0}
};

void draw_char(int glyph[7][5], int ox, int oy) {
    for (int y = 0; y < 7; y++) {
        for (int x = 0; x < 5; x++){
            if (glyph[y][x]) grid[oy + y][ox + x] = 1;
        }
    }
}

int main() {
    InitWindow(COLS, ROWS, "Ryuru");

    int (*letters[5])[5] = {R, Y, U, R, U};
    for (int i = 0; i < 5; i++){
        draw_char(letters[i], 10 + i * 6, 10);
    }
    
    while (!WindowShouldClose())
    {
        BeginDrawing();
        ClearBackground(BLACK);

        for (int y = 0; y < ROWS; y++)
        {
            for (int x = 0; x < COLS; x++)
            {
                if (grid[y][x])
                    DrawPixel(x, y, WHITE);
            }
        }

        EndDrawing();
    }

    CloseWindow();
    return 0;
}
