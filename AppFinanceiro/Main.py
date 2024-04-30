from AppFinanceiro import AppFinanceiro
from Utils import receberOpcMenu
import Menu
import Crud

def main():
    app = AppFinanceiro()  
    conta = None  
    while True:
        Menu.exibirMenu()
        opc_menu = receberOpcMenu()
        if opc_menu == 1:
            conta = Crud.adicionarConta(conta, app)
            continue
        if opc_menu == 2:
            Crud.adicionarReceita(app, conta)
            continue
        if opc_menu == 3:
            Crud.adicionarDespesa(app, conta)
            continue
        if opc_menu == 4:
            Crud.extratoReceitas(conta, app)
            continue
        if opc_menu == 5:
            Crud.extratoDespesas(conta, app)
            continue
        if opc_menu == 6:
            Crud.extratoDespesaOrdenada(conta, app)
            continue
        print('Encerrando o programa!')
        return

if __name__ == "__main__":
    main()
