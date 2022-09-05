from tkinter import Tk, simpledialog, messagebox

def read_from_file():
    with open('capital_data.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            country, city = line.split('.')
            the_world[country] = city     # the_world = {India:"New Delhi", China:"Beijing", .........}

def write_to_file(country_name, city_name):
    with open('capital_data.txt', 'a') as file:
        file.write('\n' + country_name + '.' + city_name)
        print('Ask the Expert – Capital Cities of the World')

root = Tk()         #Calls the TK inter window
root.withdraw()  # hides the blank tkinterface
the_world = {}   # initialising the empty dictionary the_world

read_from_file()   # calling the function to read the capital_data.txt file





while True:
    query_country = simpledialog.askstring('Country', 'Type the name of a country:')     # Italy
    #We are taking input from the user (Country name)
    if query_country in the_world:
        result = the_world[query_country]       
        messagebox.showinfo('Answer', 'The capital city of ' + query_country + ' is ' + result + '!')
    else:
        new_city = simpledialog.askstring('Teach me', 'I don\'t know! ' + 'What is the capital city of ' + query_country + '?')
        the_world[query_country] = new_city
        write_to_file(query_country, new_city)

root.mainloop()

