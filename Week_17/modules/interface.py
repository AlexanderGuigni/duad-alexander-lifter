import PySimpleGUI as sg
from actions import convert_list_of_lists, filter_by_date, format_list_to_money, get_today_date, get_first_day_current_month_date,sort_list_of_list


class Interface:

    def __init__(self,data):
        self.__data = data
        


    def open_main_window(self):
        movement_data = convert_list_of_lists(self.__data.movements_data)
        movement_data[1] = format_list_to_money(movement_data[1])

        current_date = get_today_date()
        start_date = get_first_day_current_month_date()

        filtered_movement_data = filter_by_date(movement_data[1], start_date, current_date)

        layout = [
            [sg.Button(key = "-BUTTON_ADD_CAT-", button_text = "Add Category"), sg.Button(key = "-BUTTON_ADD_MOV_EXP-",button_text = "Add Expense"),sg.Button(key = "-BUTTON_ADD_MOV_INC-",button_text = "Add Income")],
            [sg.Text(text ="Filter"), sg.Input(key = "-DATE_FROM-",default_text=start_date,size = (15, 1),readonly= True),sg.CalendarButton(button_text="#",format=("%d-%m-%Y")), sg.Input(key = "-DATE_TO-",default_text=current_date, size = (15, 1), readonly= True), sg.CalendarButton(button_text="#",format=("%d-%m-%Y")), sg.Button(key = "-BUTON_FILTER-",button_text ="Apply Filters")],
            [sg.Text("Movements")],
            [sg.Table(key = "-TABLE_MOVMENTS-",values= sort_list_of_list(filtered_movement_data), headings= movement_data[0], auto_size_columns=True, display_row_numbers= False, justification='left', size= (170,18), vertical_scroll_only= True, max_col_width=40)],
        ]

        window = sg.Window("Finance Manager", layout)

        while True:
            event, values = window.read()
        
            if event == "-BUTTON_ADD_CAT-":
                self.open_add_category_window()
                self.__data.save_csv(False)
            if event == "-BUTTON_ADD_MOV_EXP-":
                self.open_add_movement_window()
                self.__data.save_csv()
                self.filter_movents_grid(window)
            if event == "-BUTTON_ADD_MOV_INC-":
                self.open_add_movement_window(False)
                self.__data.save_csv()
                self.filter_movents_grid(window)
            if event == "-BUTON_FILTER-":
                self.filter_movents_grid(window)
            if event == sg.WINDOW_CLOSED:
                break
        window.close()

    def filter_movents_grid(self, window):
        movement_data = convert_list_of_lists(self.__data.movements_data)
        movement_data[1] = format_list_to_money(movement_data[1])
        from_date = window["-DATE_FROM-"].get()
        to_date = window["-DATE_TO-"].get()
        filtered_movement_data = filter_by_date(movement_data[1], from_date, to_date)
        window["-TABLE_MOVMENTS-"].update(values= sort_list_of_list(sort_list_of_list(filtered_movement_data)))

    def open_add_category_window(self):

        layout = [
            [sg.Text(text = "Category Name"),sg.Input(key = "-CATEGORY_NAME-",size = (15, 1), enable_events= True)],
            [sg.Text(text = "Category Type"),sg.Radio(key = "-CAT_TYPE_EXP-",group_id = "CAT_TYPE", text= "Expense",default= True),sg.Radio(key = "-CAT_TYPE_INC-",group_id = "CAT_TYPE", text= "Income")],
            [sg.Button(key = "-BUTTON_CAT_ADD-", button_text = "Add")]
        ]

        window = sg.Window(title= "Add Category", layout= layout, modal= True)

        while True:
            event, values = window.read()

            if event == "-CATEGORY_NAME-":
                window["-CATEGORY_NAME-"].update(background_color = "white")
            
            if event == "-BUTTON_CAT_ADD-":
                category_name = window["-CATEGORY_NAME-"].get()
                if category_name != "":
                    category_type = "Expense" if window["-CAT_TYPE_EXP-"].get() else "Income"
                    self.__data.add_category(category_name,category_type)
                    break
                else:
                    window["-CATEGORY_NAME-"].update(background_color = "red")
            if event == sg.WINDOW_CLOSED:
                break
        window.close()

    def open_add_movement_window(self,isExpense = True):
        
        if isExpense:
            category_data_filtered_by_type = list(filter(lambda x: x["Type"] == "Expense", self.__data.category_data))
        else:
            category_data_filtered_by_type = list(filter(lambda x: x["Type"] == "Income", self.__data.category_data))

        category_data = list(map(lambda x: x[1],convert_list_of_lists(category_data_filtered_by_type)[1]))

        if category_data == []:
                error_visible = True
        else:
                error_visible = False

        layout = [
            [sg.Text(text = "There are no categories available.",key= "-NO_CAT_ERR_MESSAGE-",visible= error_visible,background_color= "red", text_color= "white")],
            [sg.Text(text = "Category *"),sg.Combo(key = "-CATEGORY_NAME-",readonly = True, values= category_data, size = (15, 1),enable_events = True),sg.Text(text = "Type"),sg.Input(key = "-CAT_TYPE-", size = (15, 1),readonly = True)],
            [sg.Text(text = "Description *"),sg.Input(key = "-DESCRIP-", size = (38, 1),enable_events = True)],
            [sg.Text(text = "Amount *"),sg.Input(key = "-AMOUNT-", size = (15, 1), enable_events = True), sg.Text(text = "Date"),sg.Input(key = "-DATE-", size = (15, 1),readonly = True,default_text= get_today_date()),sg.CalendarButton(button_text="#",format=("%d-%m-%Y"))],
            [sg.Button(key = "-BUTTON_CAT_ADD-", button_text = "Add",disabled= error_visible)]
        ]

        window = sg.Window(title= "Add Movement", layout=layout, modal= True)

        while True:
            event, values = window.read()

            if event == "-CATEGORY_NAME-":
                category_type = list(filter(lambda x: x["Category"] == window["-CATEGORY_NAME-"].get(), category_data_filtered_by_type))[0]["Type"]
                window["-CATEGORY_NAME-"].update(background_color = "white")
                window["-CAT_TYPE-"].update(value = category_type )

            if event == "-DESCRIP-":
                window["-DESCRIP-"].update(background_color = "white")

            if event == "-AMOUNT-":
                window["-AMOUNT-"].update(background_color = "white")
                amount = window["-AMOUNT-"].get()
                try:
                    amount = float(amount)
                except Exception as ex:
                    amount = amount[0 :len(amount)-1]
                    window["-AMOUNT-"].update(value = amount)

            if event == "-BUTTON_CAT_ADD-":
                category_name = window["-CATEGORY_NAME-"].get()
                category_type = window["-CAT_TYPE-"].get()
                description = window["-DESCRIP-"].get()
                amount = window["-AMOUNT-"].get()
                date = window["-DATE-"].get()
                if(category_name != "" and amount != "" and description != ""):
                    self.__data.add_movement(category_name,category_type,amount,description,date)
                    break
                else:
                    if category_name == "":
                        window["-CATEGORY_NAME-"].update(background_color = "red")
                    if amount == "":
                        window["-AMOUNT-"].update(background_color = "red")
                    if description == "":
                        window["-DESCRIP-"].update(background_color = "red")
            if event == sg.WINDOW_CLOSED:
                break
        window.close()

