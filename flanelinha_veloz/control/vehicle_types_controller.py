from datetime import timedelta, datetime

from flanelinha_veloz.entity.veiculo import Veiculo
from flanelinha_veloz.exceptions.durationValueNotValidException import \
    DurationValueNotValidException
from flanelinha_veloz.exceptions.missingDataException import \
    MissingDataException
from flanelinha_veloz.exceptions.priceValueNotValidException import \
    PriceValueNotValidException
from flanelinha_veloz.exceptions.vehicleTypesAlreadyExistsInTheSystemException import \
    VehicleTypesAlreadyExistsInTheSystemException
from flanelinha_veloz.persistence.vehicleTypesDAO import VehicleTypesDAO
from flanelinha_veloz.view.vehicle_types_boundary import VehicleTypesBoundary


class VehicleTypesController:
    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__boundary = VehicleTypesBoundary()
        self.__vehicle_types_dao = VehicleTypesDAO()
        self.__codigo = 0

    def open_screen(self):
        try:
            action_options = {
                None: self.__system_controller.shutdown,
                0: self.return_menu_manager,
                1: self.open_create_vehicle_type_screen,
                2: self.open_read_vehicle_type_screen,
                3: self.open_menu_update_vehicle_type_screen,
                4: self.open_menu_delete_vehicle_type_screen
            }
            while True:
                option_number = self.__boundary.open_options()
                selected_function = action_options[option_number]
                selected_function()
        except Exception as e:
            self.__boundary.show_message(str(e))

    def return_menu_manager(self):
        self.__system_controller.menu_controller.open_menu_manager()

    def open_read_vehicle_type_screen(self):
        while True:
            try:
                all_vehicle_types = self.get_x_in_table('all')
                if all_vehicle_types == []:
                    self.__boundary.show_message(
                        'Sem tipo de veículos cadastrados, cadastre algum!')
                    break
                else:
                    values = self.__boundary.read_vehicle_types_screen(
                        all_vehicle_types)
                    acao = values['acao']
                    if acao is None:
                        self.__system_controller.shutdown()
                    else:
                        break
            except ValueError:
                self.__boundary.show_message(
                    'Existem campos em branco, confira!', 'red')
            except Exception as e:
                self.__boundary.show_message(str(e))

    def open_menu_update_vehicle_type_screen(self):
        while True:
            try:
                all_vehicle_types = self.get_x_in_table('cod_name')
                if all_vehicle_types == []:
                    self.__boundary.show_message(
                        'Sem tipos de veículos cadastrados, cadastre algum!')
                    break
                else:
                    values = self.__boundary.menu_update_vehicle_types_screen(
                        all_vehicle_types)
                    acao = values['acao']
                    if acao == VehicleTypesBoundary.UPDATE:
                        try:
                            codigo_para_atualizacao = int(
                                values['valores']['codigo'])
                            vehicle_type = self.search_for_vehicle_types_by_codigo(
                                codigo_para_atualizacao)
                            if vehicle_type != None:
                                self.open_update_vehicle_type_screen(
                                    vehicle_type, codigo_para_atualizacao)
                            else:
                                raise Exception
                        except Exception:
                            self.__boundary.show_message(
                                'Esse código não existe na base!')
                            self.open_menu_update_vehicle_type_screen()
                    elif acao is None:
                        self.__system_controller.shutdown()
                    else:
                        break
            except ValueError:
                self.__boundary.show_message(
                    'Valores em branco, favor conferir.', 'red')
            except Exception as e:
                self.__boundary.show_message(str(e))

    def open_update_vehicle_type_screen(self, vehicle_type,
                                        codigo_para_atualizacao):
        while True:
            try:
                values = self.__boundary.update_vehicle_types_screen(
                    vehicle_type)
                acoes = values['acao']
                if acoes == VehicleTypesBoundary.SUBMIT:
                    valor_atualicao = values['valores']
                    for value in valor_atualicao:
                        if valor_atualicao[value] is None or valor_atualicao[
                            value] == '':
                            raise MissingDataException
                    codigo = codigo_para_atualizacao
                    preco = valor_atualicao['preco']
                    duracao = valor_atualicao['duracao']
                    try:
                        preco = float(preco)
                    except Exception:
                        raise PriceValueNotValidException
                    try:
                        duracao = datetime.strptime(duracao, "%H:%M")
                    except Exception:
                        raise DurationValueNotValidException
                    duracao = timedelta(hours=duracao.hour,
                                        minutes=duracao.minute)
                    nome = valor_atualicao['nome']
                    obj = Veiculo(codigo, duracao, nome, preco)
                    self.vehicle_types_registration(obj)
                    self.__boundary.show_message(
                        'Atualização do tipo de veículo concluído!', 'green')
                    self.open_screen()
                elif acoes is None:
                    self.__system_controller.shutdown()
                else:
                    break
            except ValueError:
                self.__boundary.show_message(
                    'Na atualização, existem campos em branco, confira!',
                    'red')
            except Exception as e:
                self.__boundary.show_message(str(e))

    def open_menu_delete_vehicle_type_screen(self):
        while True:
            try:
                all_vehicle_types = self.get_x_in_table('cod_name')
                if all_vehicle_types == []:
                    self.__boundary.show_message(
                        'Sem tipo de veículos cadastrados, cadastre algum!')
                    break
                else:
                    values = self.__boundary.menu_delete_vehicle_types_screen(
                        all_vehicle_types)
                    acao = values['acao']
                    if acao == VehicleTypesBoundary.DELETE:
                        try:
                            codigo_para_atualizacao = int(
                                values['valores']['codigo'])
                            vehicle_type = self.search_for_vehicle_types_by_codigo(
                                codigo_para_atualizacao)
                            if vehicle_type != None:
                                self.vehicle_types_delete(vehicle_type)
                                self.__boundary.show_message(
                                    'Tipo de veículo deletado com sucesso!',
                                    'green')
                                self.open_screen()
                            else:
                                raise Exception
                        except Exception:
                            self.__boundary.show_message(
                                'Esse código não existe na base!')
                            self.open_menu_delete_vehicle_type_screen()
                    elif acao is None:
                        self.__system_controller.shutdown()
                    else:
                        break
            except ValueError:
                self.__boundary.show_message(
                    'Valores em branco, favor conferir.', 'red')
            except Exception as e:
                self.__boundary.show_message(str(e))

    def open_create_vehicle_type_screen(self):
        while True:
            try:
                values = self.__boundary.registration_vehicle_types_screen()
                acao = values['acao']
                if acao == VehicleTypesBoundary.SUBMIT:
                    valores = values['valores']
                    for value in valores:
                        if valores[value] is None or valores[value] == '':
                            raise MissingDataException
                    preco = valores['preco']
                    duracao = valores['duracao']
                    try:
                        preco = float(preco)
                    except Exception:
                        raise PriceValueNotValidException
                    try:
                        duracao = datetime.strptime(duracao, "%H:%M")
                    except Exception:
                        raise DurationValueNotValidException
                    duracao = timedelta(hours=duracao.hour,
                                        minutes=duracao.minute)
                    nome = valores['nome']
                    self.validate_name(nome)
                    codigo = self.update_total_code()
                    obj = Veiculo(codigo, duracao, nome, preco)
                    self.vehicle_types_registration(obj)
                    self.update_total_code()
                    self.__boundary.show_message(
                        'Cadastramento do tipo de veículo concluído!', 'green')
                    break
                elif acao is None:
                    self.__system_controller.shutdown()
                else:
                    break
            except ValueError:
                self.__boundary.show_message(
                    'Existem campos em branco, confira!', 'red')
            except Exception as e:
                self.__boundary.show_message(str(e))

    def validate_name(self, text):
        for vehicle_type in self.__vehicle_types_dao.get_all():
            name = str(vehicle_type.nome)
            if name == text:
                raise VehicleTypesAlreadyExistsInTheSystemException

    def vehicle_types_registration(self, vehicle_types: Veiculo):
        if vehicle_types is not None and \
                isinstance(vehicle_types, Veiculo) and \
                vehicle_types not in self.__vehicle_types_dao.get_all():
            self.__vehicle_types_dao.add(vehicle_types)

    def vehicle_types_delete(self, vehicle_types: Veiculo):
        if vehicle_types is not None and \
                isinstance(vehicle_types, Veiculo) and \
                vehicle_types in self.__vehicle_types_dao.get_all():
            self.__vehicle_types_dao.remove(vehicle_types.codigo)

    def search_for_vehicle_types_by_codigo(self, codigo: int):
        try:
            return self.__vehicle_types_dao.get(codigo)
        except KeyError:
            self.__boundary.show_message('Nenhum tipo de veículo encontrado!',
                                         'red')

    def search_for_vehicle_types_by_name(self, name: str):
        try:
            vehicle_type = None
            for vehicle_types in self.__vehicle_types_dao.get_all():
                if vehicle_types.nome == name:
                    vehicle_type = vehicle_types
            if vehicle_type is None:
                raise Exception
            else:
                return vehicle_type
        except KeyError:
            self.__boundary.show_message('Nenhum tipo de veículo encontrado!',
                                         'red')

    def get_x_in_table(self, qtd):
        data = []
        if qtd == 'all':
            for vehicle_type in self.__vehicle_types_dao.get_all():
                duracao = str(vehicle_type.duracao)[:-3]
                data.append([vehicle_type.codigo, vehicle_type.nome,
                             vehicle_type.preco, duracao])
        elif qtd == 'cod_name':
            for vehicle_type in self.__vehicle_types_dao.get_all():
                data.append([vehicle_type.codigo, vehicle_type.nome])
        elif qtd == 'cod':
            for vehicle_type in self.__vehicle_types_dao.get_all():
                data.append(vehicle_type.codigo)
        return data

    def update_total_code(self):
        return_of_all = self.get_x_in_table('all')
        if return_of_all == []:
            self.__codigo = 0
        else:
            last = return_of_all[-1]
            code = last[0]
            self.__codigo = code + 1
        return self.__codigo
