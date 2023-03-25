# Import gspread to allow manipulation of google sheets data
import gspread

# Enables access to gspread functionality for associated google account upon authentication
gc = gspread.oauth()

# Open google sheet named Workout Plan
sh = gc.open("Workout Plan")
worksheet_1 = sh.worksheet("Pull")
worksheet_2 = sh.worksheet("Push")
worksheet_3 = sh.worksheet("ATG")
worksheet_4 = sh.worksheet("Active Rest")

# get_all_values used to retrieve data from google sheet
res = worksheet_1.get_all_values() # list of lists
print(res)
print(len(res))

values_list = worksheet_1.row_values(1)
print(values_list)
values_list = worksheet_1.col_values(1)
print(values_list)

print(worksheet_1.row_count, worksheet_1.col_count)
print(worksheet_1.get('A1'))
print(worksheet_1.get('A1:C1'))

# INSERT UPDATE

user = ["Susan", "28", "Sydney"]
worksheet_1.insert_row(user, 20)
worksheet_1.insert_row(user, 16) #same with column
worksheet_1.append_row(user)
#worksheet_1.update_cell(1, 2, value)

# DELETE
#worksheet.delete_rows(1)
#worksheet.delete_columns(1)