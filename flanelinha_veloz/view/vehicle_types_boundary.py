import venv
import PySimpleGUI as sg
from flanelinha_veloz.entity.veiculo import Veiculo

from flanelinha_veloz.view.abstract_boundary import AbstractBoundary


class vehicleTypesBoundary(AbstractBoundary):
    CANCEL = 0
    SUBMIT = 1
    DELETE = 2
    UPDATE = 3
    TEXT_SIZE = 20
    INPUT_SIZE = 70

    def open_options(self):
        layout = [
            [sg.Button('Adicionar', key=1, size=vehicleTypesBoundary.TEXT_SIZE)],
            [sg.Button('Listar', key=2, size=vehicleTypesBoundary.TEXT_SIZE)],
            [sg.Button('Alterar', key=3, size=vehicleTypesBoundary.TEXT_SIZE)],
            [sg.Button('Excluir', key=4, size=vehicleTypesBoundary.TEXT_SIZE)],
            [sg.Cancel('Voltar', key=vehicleTypesBoundary.CANCEL, size=vehicleTypesBoundary.TEXT_SIZE)]
        ]

        window = sg.Window('Flanelinha Veloz - Tipos de Veículos',
                           size=(900, 550),
                           element_justification='c',
                           resizable=True,
                           margins=(150, 150)) \
            .Layout(layout)
        button, values = window.Read()
        window.close()
        return button

    def registration_vehicle_types_screen(self):
        layout = [
            [sg.Text('Nome: * ', size=vehicleTypesBoundary.TEXT_SIZE),
             sg.In(key='nome', size=vehicleTypesBoundary.INPUT_SIZE)],
            [sg.Text('Preço: * ', size=vehicleTypesBoundary.TEXT_SIZE),
             sg.In(key='preco', size=vehicleTypesBoundary.INPUT_SIZE)],
            [sg.Text('Duração: * (hh:mm) ', size=vehicleTypesBoundary.TEXT_SIZE),
             sg.In(key='duracao', size=vehicleTypesBoundary.INPUT_SIZE)],
            [sg.Cancel('Voltar', key=vehicleTypesBoundary.CANCEL),
             sg.Submit('Cadastrar', key=vehicleTypesBoundary.SUBMIT)]
        ]
        window = sg.Window('Flanelinha Veloz - Cadastro Tipos de Veículo',
                           size=(900, 550),
                           element_justification='c',
                           resizable=True,
                           margins=(200, 200)) \
            .Layout(layout)
        button, values = window.Read()
        window.close()
        return {
            'acao': button,
            'valores': values
        }
    
    def read_vehicle_types_screen(self, vehicle_type):
        layout = [
            [sg.Table(values=vehicle_type,
                       headings=['Código', 'Nome', 'Preço', 'Duração'],
                       max_col_width=25,
                       auto_size_columns=True,
                       justification='center',
                       expand_y=True,
                       expand_x=True,
                       vertical_scroll_only=True)],
            [sg.Cancel('Voltar', key=vehicleTypesBoundary.CANCEL)]
        ]
        window = sg.Window('Flanelinha Veloz - Cadastro Tipos de Veículo',
                           size=(900, 550),
                           element_justification='c',
                           resizable=True,
                           margins=(50, 50)) \
            .Layout(layout)
        button, values = window.Read()
        window.close()
        return {
            'acao': button,
            'valores': values
        }
