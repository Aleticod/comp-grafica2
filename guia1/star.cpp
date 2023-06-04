// Nombre		: star.cpp
// Proposito	: Implementacion de un cubo de color
// Autor		: A. Harvey Pfoccori Quispe
// Compilacion	: gcc star.cpp -o star.exe -lGL -lglfw
// Ejecucion	: ./star.exe

#include <GLFW/glfw3.h>
int main(int argc, const char* argv[]) {
    GLFWwindow* win;
    if (!glfwInit()) {
        return -1;
    }
        win = glfwCreateWindow(640, 480, "Ejemplo 3", NULL, NULL);
    if (!win)
    {
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(win);
    while (!glfwWindowShouldClose(win)) {
        glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);
        glBegin(GL_LINE_LOOP);
        {
            glColor3f(1.0, 0.0, 0.0);
            glVertex2f(0.5, 0.5);
            glVertex2f(0.1, 0.1);
            glVertex2f(0.3, 0.7);
            glVertex2f(0.5, 0.1);
            glVertex2f(0.1, 0.5);
        }
    glEnd();
    glfwSwapBuffers(win);
    glfwPollEvents();
    }
    glfwTerminate();
    return 0;
}
