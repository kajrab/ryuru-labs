#include "raylib.h"

int main() {
    InitWindow(400, 400, "pixel");

    while (!WindowShouldClose()) {
        BeginDrawing();
        ClearBackground(BLACK);

        DrawPixel(200, 200, (Color){255, 0, 0, 255});

        EndDrawing();
    }

    CloseWindow();
}
