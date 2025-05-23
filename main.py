from D import Recarga
from D import Validador

def main():
    #? Inicializa las variables de la clase Recarga
    recarga = Recarga("2023-10-01", "123456", "TERMINAL1", "LOTE1", "2023-10-01", "12:00:00", "TARJETA1", "AUTORIZACION1", "REFERENCIA1", 100.0, 120.0, 20.0, "MARCA1")
    print(recarga)
    
    #? Inicializa las variables de la clase Validador
    validador = Validador("2023-10-01", "123456", "TERMINAL1", "LOTE1", "2023-10-01", "12:00:00", "TARJETA1", "AUTORIZACION1", "REFERENCIA1", 100.0, 120.0, "MARCA1")
    print(validador)
if __name__ == "__main__":
    main()
    #? Llama a la función main