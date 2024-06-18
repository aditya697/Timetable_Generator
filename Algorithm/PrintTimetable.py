# from Data import df_timetable
# from tabulate import tabulate
#
# headers = ["8.20-9.10", "9.10-10.00", "10.00-10.50", "11.00-11.50", "11.50-12.40", "12.40-1.30", "1.30-2.20",
#            "2.30-3.20", "3.20-4.10", "4.10-5.00"]
#
# print(df_timetable)
#
# days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
#
# for entries in df_timetable:
#     tt1 = []
#     semester = entries['semester']
#     batch = entries['batch']
#     print("Timetable for " + semester + " " + batch)
#     sorted_days = sorted(entries['data'], key=lambda x: days_order.index(x[0]))
#     for entry in sorted_days:
#         row = []
#         for s in entry:
#             row.append(s)
#         tt1.append(row)
#     print(tabulate(tt1, headers=[f'{semester}/{batch}'] + headers))


# PrintTimetable.py

from Data import df_timetable
from bs4 import BeautifulSoup
from tabulate import tabulate
import pandas as pd
import re


headers = ["8.20-9.10", "9.10-10.00", "10.00-10.50", "11.00-11.50", "11.50-12.40", "12.40-1.30", "1.30-2.20",
               "2.30-3.20", "3.20-4.10", "4.10-5.00"]

days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


def generate_timetable_html():
    timetable_html = ''
    i = 1  # Counter for applying different borders

    values_to_clear = ['FL12', 'N5', 'EL14', 'B12', 'B11', 'M4', 'E14', 'N4', 'CL11', 'DL11', 'A12', 'F11', 'M3', 'F13', 'D14', 'DL13', 'N3', 'BL12', 'A11', 'E11', 'C14', 'AL14', 'D13', 'EL11', 'DL14', 'M1', 'AL13', 'D12', 'BL11', 'AL12', 'E13', 'M2', 'FL11', 'A14', 'CL12', 'B14', 'B13', 'C11', 'E12', 'EL13', 'F12', 'C13', 'N1', 'AL11', 'BL14', 'D11', 'EL12','BL13','DL12']

    for entries in df_timetable:
        semester = entries['semester']
        batch = entries['batch']
        timetable_html += '<div style="text-align: center; margin: 20px auto;">'  # Center the entire box
        timetable_html += '<div style="display: inline-block;">'  # Center the timetable
        timetable_html += '<table style="border-collapse: collapse; text-align: center; font-size: 14px; width: 100%;">'
        timetable_html += f"<tr><th style='border: 1px solid black; text-align: left; font-weight: bold;'>{semester} {batch}</th>" + \
                          ''.join([f"<th style='border: 1px solid black; width: 10%;'>{header}</th>" for header in headers]) + \
                          "</tr>"
        sorted_days = sorted(entries['data'], key=lambda x: days_order.index(x[0]))
        for day_info in sorted_days:
            day, *slots = day_info
            row = ""
            for slot in slots:
                if slot in values_to_clear:
                    row += "<td style='border: 1px solid black; width: 10%;'></td>"  # Empty cell
                else:
                    row += f"<td style='border: 1px solid black; width: 10%;'>{slot}</td>"
            # Making days bold
            timetable_html += f"<tr><td style='border: 1px solid black; text-align: left; font-weight: bold;'>{day}</td>{row}</tr>"
        timetable_html += '</table></div></div>'
        i += 1

    return timetable_html


def generate_excel(timetable_html):
    soup = BeautifulSoup(timetable_html, 'html.parser')

    timetable_df_list = []

    # Find all tables within the HTML
    tables = soup.find_all('table')

    for table in tables:
        # Extract the semester and batch from the table header
        header = table.find('th').text.strip()
        semester, batch = header.split()

        # Extract table data
        rows = table.find_all('tr')[1:]  # Skip the header row
        data = []
        for row in rows:
            cells = row.find_all(['th', 'td'])
            day = cells[0].text.strip()
            slots = [cell.text.strip() for cell in cells[1:]]
            data.append([day] + slots)

        # Create DataFrame
        df = pd.DataFrame(data, columns=[f"{semester} {batch}", "8.20-9.10", "9.10-10.00", "10.00-10.50", "11.00-11.50", "11.50-12.40", "12.40-1.30", "1.30-2.20", "2.30-3.20", "3.20-4.10", "4.10-5.00"])

        # Append to the timetable_df_list
        timetable_df_list.append((f"Timetable for {semester} {batch}", df))

    # Exporting to Excel
    with pd.ExcelWriter("timetables.xlsx") as writer:
        for name, df in timetable_df_list:
            df_styled = df.style.applymap(lambda x: 'border: 1px solid black;').set_properties(**{'font-size': '14px'})
            df_styled.to_excel(writer, sheet_name=name, index=False)


if __name__ == "__main__":
    timetable_html = generate_timetable_html()
    print(timetable_html)
    generate_excel(timetable_html)
