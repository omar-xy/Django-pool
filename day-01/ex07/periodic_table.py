import sys
def fwrite(filename, content):
    with open(filename, 'a') as f:
        f.write(content + '\n')

def HTMLify(items):
    # Each element must be in a ’box’ of a HTML table
    fwrite("periodic_table.html", "<!DOCTYPE html>")
    fwrite("periodic_table.html", "<html lang=\"en\">")
    fwrite("periodic_table.html", "<head>")
    fwrite("periodic_table.html", "<meta charset=\"UTF-8\">")
    fwrite("periodic_table.html", "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
    fwrite("periodic_table.html", "<link rel=\"stylesheet\" href=\"periodic_table.css\">")
    fwrite("periodic_table.html", "</head>")
    fwrite("periodic_table.html", "<body>")
    fwrite("periodic_table.html", "<div class=\"container\">")  # Add a container div
    for key, value in items.items():
        numstr = "No" + value[1].split(':')[1]
        small = (value[2].split(':')[1]).strip()
        molar = value[3].split(':')[1]
        electrons = value[4].split(':')[1] + " electrons"
        fwrite("periodic_table.html", "<div class=\"box\">")  # Add a box div
        fwrite("periodic_table.html", "<table>")
        fwrite("periodic_table.html", " <tr>")
        fwrite("periodic_table.html", "     <td>")
        fwrite("periodic_table.html", f"           <h4>{key}</h4>")
        fwrite("periodic_table.html", "            <ul>")
        fwrite("periodic_table.html", f"               <li>{numstr}</li>")
        fwrite("periodic_table.html", f"               <li>{small}</li>")
        fwrite("periodic_table.html", f"               <li>{molar}</li>")
        fwrite("periodic_table.html", f"               <li>{electrons}</li>")
        fwrite("periodic_table.html", "            </ul>")
        fwrite("periodic_table.html", "      </td>")
        fwrite("periodic_table.html", "</tr>")
        fwrite("periodic_table.html", "</table>")
        fwrite("periodic_table.html", "</div>")  # Close the box div
    fwrite("periodic_table.html", "</div>")  # Close the container div
    fwrite("periodic_table.html", "</body>")
    fwrite("periodic_table.html", "</html>")


if __name__ == "__main__":
    file = open("periodic_table.txt", "r")
    elements = file.read()
    elements = elements.split('\n')
    ListElements = list(map(str, elements))
    d = {}
    values = []
    for i in range(len(ListElements)):
        elem1 = ListElements[i].split('=')[0]
        split_elements = ListElements[i].split('=')
        if len(split_elements) > 1:
            values = split_elements[1].split(',')
        d[elem1] = values
    HTMLify(d)
    
