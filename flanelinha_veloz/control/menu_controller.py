from flanelinha_veloz.view.menu_boundary import MenuBoundary


class MenuController:

    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__menu_screen = MenuBoundary()

    def see_client_profile(self):
        self.__system_controller.client_controller.open_menu_client()

    def see_schedule_service_screen(self):
        self.__system_controller.client_controller.open_schedule_service_screen()

    def see_employees_profile(self):
        self.__system_controller.employees_controller.open_profile_employees_screen()

    def see_vehicle_types(self):
        self.__system_controller.vehicle_types_controller.open_screen()

    def see_types_of_services(self):
        self.__system_controller.types_of_services_controller.open_screen()

    def see_establishment_operation(self):
        self.__system_controller.establishment_operation_controller.open_screen()

    def see_car_spot(self):
        self.__system_controller.car_spot_controller.open_screen()

    def see_next_day_report(self):
        self.__system_controller.next_day_report_controller.open_screen()

    def open_menu_client(self):
        try:
            action_options = {
                None: self.__system_controller.shutdown,
                MenuBoundary.SHUTDOWN: self.__system_controller.shutdown,
                MenuBoundary.OPEN_PROFILE: self.see_client_profile,
                MenuBoundary.SCHEDULE_SERVICE: self.see_schedule_service_screen
            }
            while True:
                option_number = self.__menu_screen.open_menu_client()
                selected_function = action_options[option_number]
                selected_function()
        except Exception as e:
            self.__menu_screen.show_message(str(e))

    def open_menu_manager(self):
        try:
            action_options = {
                None: self.__system_controller.shutdown,
                0: self.__system_controller.shutdown,
                1: self.see_employees_profile,
                2: self.see_vehicle_types,
                3: self.see_types_of_services,
                4: self.see_car_spot,
                5: self.see_establishment_operation,
                6: self.see_next_day_report
            }
            while True:
                option_number = self.__menu_screen.open_menu_manager()
                selected_function = action_options[option_number]
                selected_function()
        except Exception as e:
            self.__menu_screen.show_message(str(e))

    def open_menu_employer(self):
        try:
            action_options = {
                None: self.__system_controller.shutdown,
                0: self.__system_controller.shutdown,
                1: self.see_employees_profile,
            }
            while True:
                option_number = self.__menu_screen.open_menu_employer()
                selected_function = action_options[option_number]
                selected_function()
        except Exception as e:
            self.__menu_screen.show_message(str(e))
