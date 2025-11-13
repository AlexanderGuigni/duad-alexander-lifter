import PySimpleGUI as sg
from actions import  get_today_date, get_first_day_current_month_date,sort_list_of_list,compare_dates
from finance_manager import FinanceManager

class Interface:

    def open_main_window(self):
        finance_manager = FinanceManager()

        current_date = get_today_date()
        start_date = get_first_day_current_month_date()
        filtered_movement_data = finance_manager.filter_by_date(start_date, current_date)

        layout = [
            [sg.Button(key = "-BUTTON_ADD_CAT-", button_text = "Add Category"), sg.Button(key = "-BUTTON_ADD_MOV_EXP-",button_text = "Add Expense"),sg.Button(key = "-BUTTON_ADD_MOV_INC-",button_text = "Add Income")],
            [sg.Text(text ="Filter"), sg.Input(key = "-DATE_FROM-",default_text=start_date,size = (13, 1),readonly= True),sg.CalendarButton(button_text="#",format=("%d-%m-%Y")), sg.Input(key = "-DATE_TO-",default_text=current_date, size = (13, 1), readonly= True), sg.CalendarButton(button_text="#",format=("%d-%m-%Y")), sg.Button(key = "-BUTTON_FILTER-",button_text ="Apply Filters"), sg.Text(text = "Start date must be later than the end date",key= "-FILTER_DATES_ERR_MESSAGE-",visible= False,background_color= "red", text_color= "white")],
            [sg.Text("Movements")],
            [sg.Table(key = "-TABLE_MOVMENTS-",values= sort_list_of_list(FinanceManager.convert_to_list_of_lists(filtered_movement_data)), headings= finance_manager.movements_headers, auto_size_columns=True, display_row_numbers= False, justification='left', size= (170,18), vertical_scroll_only= True, max_col_width=40)],
        ]

        window = sg.Window("Finance Manager", layout)

        while True:
            event, values = window.read()
            if event == "-BUTTON_ADD_CAT-":
                self.open_add_category_window(finance_manager= finance_manager)
            if event == "-BUTTON_ADD_MOV_EXP-":
                self.open_add_movement_window(finance_manager= finance_manager)
                window["-BUTTON_FILTER-"].click()
            if event == "-BUTTON_ADD_MOV_INC-":
                self.open_add_movement_window(False, finance_manager= finance_manager)
                window["-BUTTON_FILTER-"].click()
            if event == "-BUTTON_FILTER-":
                self.filter_movents_grid(window, finance_manager)
            if event == sg.WINDOW_CLOSED:
                break
        window.close()

    def filter_movents_grid(self, window, finance_manager = FinanceManager()):
        from_date = window["-DATE_FROM-"].get()
        to_date = window["-DATE_TO-"].get()
        filtered_movement_data = finance_manager.filter_by_date(from_date, to_date)
        if compare_dates(from_date, to_date):
            window["-FILTER_DATES_ERR_MESSAGE-"].update(visible = False)
            window["-TABLE_MOVMENTS-"].update(values= sort_list_of_list(FinanceManager.convert_to_list_of_lists(filtered_movement_data)))
        else:
            window["-FILTER_DATES_ERR_MESSAGE-"].update(visible = True)


    def open_add_category_window(self, finance_manager = FinanceManager()):
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
                if category_name.strip() != "":
                    category_type = "Expense" if window["-CAT_TYPE_EXP-"].get() else "Income"
                    finance_manager.add_category(category_name,category_type)
                    break
                else:
                    window["-CATEGORY_NAME-"].update(background_color = "red")
            if event == sg.WINDOW_CLOSED:
                break
        window.close()

    def open_add_movement_window(self,isExpense = True, finance_manager = FinanceManager()):
        
        if isExpense:
            category_data_filtered_by_type = FinanceManager.convert_to_list_of_lists(finance_manager.get_expenses_categories(),False)
        else:
            category_data_filtered_by_type = FinanceManager.convert_to_list_of_lists(finance_manager.get_income_categories(),False)

        category_data = list(map(lambda x: x[1], category_data_filtered_by_type))

        category_type = "Expense" if isExpense else "Income"

        if category_data == []:
                error_visible = True
        else:
                error_visible = False

        layout = [
            [sg.Text(text = "There are no categories available.",key= "-NO_CAT_ERR_MESSAGE-",visible= error_visible,background_color= "red", text_color= "white")],
            [sg.Text(text = "Category *"),sg.Combo(key = "-CATEGORY_NAME-",readonly = True, values= category_data, size = (15, 1),enable_events = True),sg.Text(text = "Type"),sg.Input(key = "-CAT_TYPE-", size = (15, 1),readonly = True, default_text= category_type)],
            [sg.Text(text = "Description *"),sg.Input(key = "-DESCRIP-", size = (38, 1),enable_events = True)],
            [sg.Text(text = "Amount *"),sg.Input(key = "-AMOUNT-", size = (15, 1), enable_events = True), sg.Text(text = "Date"),sg.Input(key = "-DATE-", size = (15, 1),readonly = True,default_text= get_today_date(),enable_events = True),sg.CalendarButton(key="-DATE_CAL-",button_text="#",format=("%d-%m-%Y"))],
            [sg.Button(key = "-BUTTON_CAT_ADD-", button_text = "Add",disabled= error_visible)]
        ]

        window = sg.Window(title= "Add Movement", layout=layout, modal= True)

        while True:
            event, values = window.read()
            if event == "-CATEGORY_NAME-":
                window["-CATEGORY_NAME-"].update(background_color = "white")
            if event == "-DESCRIP-":
                window["-DESCRIP-"].update(background_color = "white")
            if event == "-DATE-":
                window["-DATE_CAL-"].update(button_color = ("white", "midnightblue"))
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
                description = window["-DESCRIP-"].get()
                amount = window["-AMOUNT-"].get()
                date = window["-DATE-"].get()
                date_isvalid = compare_dates(date, get_today_date())
                if(category_name != "" and amount != "" and description != "" and date_isvalid):
                    finance_manager.add_movement(category_name,amount,description,date)
                    break
                else:
                    if category_name.strip() == "":
                        window["-CATEGORY_NAME-"].update(background_color = "red")
                    if amount.strip() == "":
                        window["-AMOUNT-"].update(background_color = "red")
                    if description.strip() == "":
                        window["-DESCRIP-"].update(background_color = "red")
                    if not date_isvalid:
                        print("here")
                        window["-DATE_CAL-"].update(button_color = ("white", "red"))
            if event == sg.WINDOW_CLOSED:
                break
        window.close()

