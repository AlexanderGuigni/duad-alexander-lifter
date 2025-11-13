from datetime import date, timedelta, datetime

def convert_string_to_date(string_date):
    return datetime.strptime(string_date, "%d-%m-%Y").date()
    

def format_to_money(amount, currency):
    return (currency + "{:,.2f}").format(float(amount))


def get_today_date():
    return date.today().strftime("%d-%m-%Y")


def get_first_day_current_month_date():
    current_date = convert_string_to_date(get_today_date())
    current_day = int(current_date.strftime("%d"))
    return (date.today() - timedelta(days=current_day-1)).strftime("%d-%m-%Y")

def sort_list_of_list(my_list):
    return list(sorted(my_list, key= lambda x: (convert_string_to_date(x[5]),x[0]), reverse= True))

def compare_dates(initial_date,final_date):
    if not isinstance(initial_date, date):
        initial_date = convert_string_to_date(initial_date)
    if not isinstance(final_date, date):
        final_date = convert_string_to_date(final_date)
    return True if initial_date >= final_date else False