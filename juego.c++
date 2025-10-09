#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>

using namespace std;

const int FILAS = 8;
const int COLUMNAS = 8;
const int MINAS = 10;

struct Celda {
    bool mina = false;
    bool descubierta = false;
    int minasCerca = 0;
};

void mostrarTablero(const vector<vector<Celda>>& tablero, bool mostrarMinas = false) {
    cout << "   ";
    for (int c = 0; c < COLUMNAS; ++c) cout << c << " ";
    cout << endl;
    for (int f = 0; f < FILAS; ++f) {
        cout << f << " |";
        for (int c = 0; c < COLUMNAS; ++c) {
            if (tablero[f][c].descubierta) {
                if (tablero[f][c].mina) cout << "*|";
                else cout << tablero[f][c].minasCerca << "|";
            } else if (mostrarMinas && tablero[f][c].mina) {
                cout << "*|";
            } else {
                cout << " |";
            }
        }
        cout << endl;
    }
}

void colocarMinas(vector<vector<Celda>>& tablero) {
    int colocadas = 0;
    while (colocadas < MINAS) {
        int f = rand() % FILAS;
        int c = rand() % COLUMNAS;
        if (!tablero[f][c].mina) {
            tablero[f][c].mina = true;
            colocadas++;
        }
    }
}

void contarMinasCerca(vector<vector<Celda>>& tablero) {
    for (int f = 0; f < FILAS; ++f) {
        for (int c = 0; c < COLUMNAS; ++c) {
            if (tablero[f][c].mina) continue;
            int cuenta = 0;
            for (int df = -1; df <= 1; ++df) {
                for (int dc = -1; dc <= 1; ++dc) {
                    int nf = f + df, nc = c + dc;
                    if (nf >= 0 && nf < FILAS && nc >= 0 && nc < COLUMNAS && tablero[nf][nc].mina)
                        cuenta++;
                }
            }
            tablero[f][c].minasCerca = cuenta;
        }
    }
}

void descubrir(vector<vector<Celda>>& tablero, int f, int c) {
    if (f < 0 || f >= FILAS || c < 0 || c >= COLUMNAS || tablero[f][c].descubierta)
        return;
    tablero[f][c].descubierta = true;
    if (tablero[f][c].minasCerca == 0 && !tablero[f][c].mina) {
        for (int df = -1; df <= 1; ++df)
            for (int dc = -1; dc <= 1; ++dc)
                if (df != 0 || dc != 0)
                    descubrir(tablero, f + df, c + dc);
    }
}

bool haGanado(const vector<vector<Celda>>& tablero) {
    for (int f = 0; f < FILAS; ++f)
        for (int c = 0; c < COLUMNAS; ++c)
            if (!tablero[f][c].mina && !tablero[f][c].descubierta)
                return false;
    return true;
}

int main() {
    srand(time(0));
    vector<vector<Celda>> tablero(FILAS, vector<Celda>(COLUMNAS));
    colocarMinas(tablero);
    contarMinasCerca(tablero);

    bool juegoTerminado = false;
    while (!juegoTerminado) {
        mostrarTablero(tablero);
        int f, c;
        cout << "Introduce fila y columna (ejemplo: 3 4): ";
        cin >> f >> c;
        if (f < 0 || f >= FILAS || c < 0 || c >= COLUMNAS) {
            cout << "Posición inválida.\n";
            continue;
        }
        if (tablero[f][c].mina) {
            cout << "¡Has perdido!\n";
            mostrarTablero(tablero, true);
            juegoTerminado = true;
        } else {
            descubrir(tablero, f, c);
            if (haGanado(tablero)) {
                cout << "¡Has ganado!\n";
                mostrarTablero(tablero, true);
                juegoTerminado = true;
            }
        }
    }
    return 0;
}