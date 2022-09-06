from calendar import c
from delphifmx import *
from os.path import exists
import os
import csv
col_count = 3



class HelloForm(Form):
    global files
    files =[]
    for file in os.listdir("."):
        if file.endswith(".csv"):
            #print(os.path.join("/mydir", file))
            files.append(file)
    print(files)


    def __init__(self, owner):
        self.SetProps(Caption = "My To Do List", OnShow = self.__form_show, OnClose = self.__form_close)

        self.hello = Label(self)
        self.hello.SetProps(Parent = self, Text = "Next Do: ", Position = Position(PointF(20, 20)))

        self.edit = Edit(self)
        self.edit.SetProps(Parent = self, Position = Position(PointF(18,600)), Width = 600)

        self.clickme = Button(self)
        self.clickme.SetProps(Parent = self, Text = "Add", Position = Position(PointF(190, 18)), Width = 80, OnClick = self.__button_click)

        self.list = ListBox(self)
        self.list.SetProps(Parent = self, Position = Position(PointF(20, 60)), Width = 600, Columns= col_count, OnClick = self.__list_item_click)
        
        # I added this to populate a drop down list, ComboEdit
        self.file_list = ComboEdit(self)
        self.file_list.SetProps(Parent = self, Position = Position(PointF(400, 20)), Width = 300,OnChange = self.file_choice_click)
        for item in files:
            self.file_list.items.add(item)


    def __list_item_click(self, sender):
        if (self.list.itemindex > -1):
            self.list.items.delete(self.list.itemindex)

    def __form_show(self, sender):
        self.SetProps(Width = 1400, Height = 800)
        if exists("todo.txt"):
            self.list.items.loadfromfile("todo.txt")

    def __form_close(self, sender, action):
        self.list.items.savetofile("todo.txt")
        action = "caFree"

    def __button_click(self, sender):
        self.list.items.add(self.edit.text)
        self.edit.text = ""

    # need an on click event for file_list to
    def file_choice_click(self, sender):
        file_to_open = self.file_list.Text
        #print(file_to_open)
        csv_file = open(file_to_open, "r")
        csv_first = csv_file.readline()
        # figure out how many columns count the commas
        print(csv_first.count(','))
        csv_columns = csv_first.count(',') + 1
        # read in the csv file
        csv_parsed = self.get_file(csv_file.name,csv_columns)[0]
        print(csv_parsed)
        # open a list box with proper columns
        self.csv_lbox = ListBox(self)
        # set the width by the number of columns
        self.csv_lbox.SetProps(Parent = self, Position = Position(PointF(20, 300)), Width = 300 * csv_columns, Columns= csv_columns, OnClick = self.get_selected)
        # populate the list box 
        for index, item in enumerate(csv_parsed):
            for x in range(csv_columns):
                self.csv_lbox.items.add(item[x])   


        csv_file.close()

    def get_selected(self,sender):
        if self.csv_lbox.ItemIndex > -1:
            selection = self.csv_lbox.Items[self.csv_lbox.ItemIndex]
            #selection = self.csv_lbox(GetSelectedText)
            self.edit.Text= selection
            print(selection + ' = ' + str(self.csv_lbox.ItemIndex))
        

    # //////////// CSV FILE READER ///////////////
    def get_file(self, list_file, col_count):
        # now a more generic reader that can take any number of columns
        global row_count
        global file_error
        try:
            ''' call with file and get back list of lists'''
            with open(list_file) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                rowlist = []
                cvs_list = []
                line_count = 0
                for row in csv_reader:
                    if line_count > 0:
                        # avoids the header line
                        rowlist = [row[0]] # initalizes the list first item
                        if col_count > 1:
                            for x in range(1,col_count):
                                rowlist.append(row[x])
                            
                        cvs_list.append(rowlist)
                        # this is a 0 based list of lists
                        # access questions_list[q# - 1][column]
                    line_count += 1
                #print(f'Processed {line_count} lines.')
                row_count = line_count - 1
                # returns lists within lists acces via [list of items][items]
                return [cvs_list]
        except FileNotFoundError:
            print('file not found')
            # print message on screen
            file_error = True
# \\\\\\\\\\\\\\\\\\\\\\\\ CSV FILE READER \\\\\\\\\\\\\\\\\\\\\\\\\\\
    

def main():
    Application.Initialize()
    Application.Title = "Hello Delphi FMX"
    Application.MainForm = HelloForm(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()