// Nombre		: football.cpp
// Proposito	: Implementacion de un cubo de color
// Autor		: A. Harvey Pfoccori Quispe
// Compilacion	: gcc football.cpp -o football.exe -lGL -lglfw -lm
// Ejecucion	: ./football.exe

#include <GLFW/glfw3.h>
#include<math.h>

int main(int argc, const char* argv[]) {
    GLFWwindow* win;
    if (!glfwInit()) {
        return -1;
    }
        win = glfwCreateWindow(640, 480, "Ejemplo 4", NULL, NULL);
    if (!win)
    {
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(win);
    while (!glfwWindowShouldClose(win)) {
        glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        glBegin(GL_QUADS);
		{
			//glColor3f(0.039, 0.267, 0.035);
            glColor3f(0.02, 0.47, 0.35);
            glVertex2f(-0.92, 0.62);
            glVertex2f(0.92, 0.62);
            glVertex2f(0.92, -0.62);
            glVertex2f(-0.92, -0.62);
			
		}
        glEnd();

        glBegin(GL_LINE_LOOP);
        {
            glColor3f(1.0, 1.0, 1.0);
            glVertex2f(-0.9, 0.6);
            glVertex2f(0.9, 0.6);
            glVertex2f(0.9, -0.6);
            glVertex2f(-0.9, -0.6);
        }
        glEnd();
        glBegin(GL_LINE_LOOP);
        {
            glColor3f(1.0, 1.0, 1.0);
            glVertex2f(0.0, 0.6);
            glVertex2f(0.0, -0.6);
        }
        glEnd();
        glBegin(GL_LINE_LOOP);
        {
            glColor3f(1.0, 1.0, 1.0);
            glVertex2f(-0.9, 0.4);
            glVertex2f(-0.58, 0.4);
            glVertex2f(-0.58, -0.4);
            glVertex2f(-0.9, -0.4);
        }
        glEnd();
        glBegin(GL_LINE_LOOP);
        {
            glColor3f(1.0, 1.0, 1.0);
            glVertex2f(-0.9, 0.2);
            glVertex2f(-0.8, 0.2);
            glVertex2f(-0.8, -0.2);
            glVertex2f(-0.9, -0.2);
        }
        glEnd();
        glBegin(GL_LINE_LOOP);
        {
            glColor3f(1.0, 1.0, 1.0);
            glVertex2f(0.9, 0.4);
            glVertex2f(0.58, 0.4);
            glVertex2f(0.58, -0.4);
            glVertex2f(0.9, -0.4);
        }
        glEnd();
        glBegin(GL_LINE_LOOP);
        {
            glColor3f(1.0, 1.0, 1.0);
            glVertex2f(0.9, 0.2);
            glVertex2f(0.8, 0.2);
            glVertex2f(0.8, -0.2);
            glVertex2f(0.9, -0.2);
        }
        glEnd();

        glBegin(GL_LINE_LOOP);
        {
            float x, y;
            float pi = 3.141592653589;
            glColor3f(1.0, 1.0, 1.0);
            for(int i = 0; i < 360; i++) {
                x = 0.2* cos(pi * i / 180);
                y = 0.2 * sin(pi * i / 180);
                glVertex2f(x,y);
            }
        }
        glEnd();

        glBegin(GL_LINE_LOOP);
        {
            float x, y;
            float pi = 3.141592653589;
            glColor3f(1.0, 1.0, 1.0);
            for(int i = -73; i <= 73; i++) {
                x = 0.2* cos(pi * i / 180);
                y = 0.2* sin(pi * i / 180);
                glVertex2f(-0.64 + x,y);
            }
        }
        glEnd();

        glBegin(GL_LINE_LOOP);
        {
            float x, y;
            float pi = 3.141592653589;
            glColor3f(1.0, 1.0, 1.0);
            for(int i = 107; i <= 253; i++) {
                x = 0.2 * cos(pi * i / 180);
                y = 0.2 * sin(pi * i / 180);
                glVertex2f(0.64 + x,y);
            }
        }
        glEnd();

        glBegin(GL_POINTS);
        {
            glColor3f(1.0, 1.0, 1.0);
            glVertex2f(0.64, 0.0);
            glVertex2f(-0.64, 0.0);

        }
        glEnd();

        glfwSwapBuffers(win);
        glfwPollEvents();
    }
    glfwTerminate();
    return 0;
}
