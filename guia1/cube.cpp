// Nombre		: cube.cpp
// Proposito	: Implementacion de un cubo de color
// Autor		: A. Harvey Pfoccori Quispe
// Compilacion	: gcc cube.cpp -o cube.exe -lGL -lglfw
// Ejecucion	: ./cube.exe

#include <GLFW/glfw3.h>

int main(int argc, const char* argv[]) {
    GLFWwindow* win;

    if (!glfwInit()) {
		return -1;
	}

    win = glfwCreateWindow(640, 480, "Ejemplo 2", NULL, NULL);
	if (!win) {
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(win);

    while (!glfwWindowShouldClose(win)) {
        glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        glBegin(GL_QUADS);
		{
			// Arista - Cyan
			glColor3f(0.0, 1.0, 1.0);
			glVertex2f(0.0, 0.7);

			// Arista - Verde
			glColor3f(0.0, 1.0, 0.0);
			glVertex2f(0.5, 0.7);

			// Arista - Amarilla
			glColor3f(1.0, 1.0, 0.0);
			glVertex2f(0.6, 0.5);

			// Arista- Blanco
			glColor3f(1.0, 1.0, 1.0);
			glVertex2f(0.1, 0.5);
		}

		glBegin(GL_QUADS);
		{
			// Cara izquierda - Cyan
			glColor3f(0.0, 1.0, 1.0);
			glVertex2f(0.0, 0.7);

			// Arista- Blanco
			glColor3f(1.0, 1.0, 1.0);
			glVertex2f(0.1, 0.5);

			// Arista - Magenta
			glColor3f(1.0, 0.0, 1.0);
			glVertex2f(0.1, 0.0);

			// Arista - Azul
			glColor3f(0.0, 0.0, 1.0);
			glVertex2f(0.0, 0.2);
			
		}

		glBegin(GL_QUADS);
		{
			// Cara izquierda - Blanco
			glColor3f(1.0, 1.0, 1.0);
			glVertex2f(0.1, 0.5);

			// Arista- Amarillo
			glColor3f(1.0, 1.0, 0.0);
			glVertex2f(0.6, 0.5);

			// Arista - Rojo
			glColor3f(1.0, 0.0, 0.0);
			glVertex2f(0.6, 0.0);

			// Arista - Magenta
			glColor3f(1.0, 0.0, 1.0);
			glVertex2f(0.1, 0.0);
			
		}

		glEnd();

		glfwSwapBuffers(win);
		glfwPollEvents();
    }

    glfwTerminate();
    return 0;
}
