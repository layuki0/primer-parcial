#include <iostream>

int main() {
    std::cout << "Bienvenido al juego más simple!\n";
    std::cout << "Adivina el número (entre 1 y 5): ";
    int numero_secreto = 3;
    int intento;
    std::cin >> intento;

    if (intento == numero_secreto) {
        std::cout << "¡Correcto! Ganaste.\n";
    } else {
        std::cout << "Incorrecto. El número era " << numero_secreto << ".\n";
    }
    return 0;
}
