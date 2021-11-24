# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# JWray,11.22.21,Modified code to complete assignment 06
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name_str = "ToDoFile.txt"  # The name of the data file
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data separated into elements of a dictionary {Task,Priority}
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection
task_str = "" # stores task that is either going to be added or deleted
priority_str = "" # stores priority that is either going to be added or deleted

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds new item to list of dictionary rows

               :param task: (string) with name of task:
               :param priority: (string) with priority of task
               :param list_of_rows: (list) you want to append the new data to:
               :return: (list) of dictionary rows
               """
        row = {'Task': task, 'Priority': priority}
        list_of_rows.append(row)
        print('Your task has been added!\n')
        return list_of_rows

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Adds new item to list of dictionary rows

              :param task: (string) with name of task:
              :param list_of_rows: (list) you want to remove the task from:
              :return: (list) of dictionary rows
              """
        found = False
        for row in list_of_rows:
            if task.lower() in row['Task'].lower():
                list_of_rows.remove(row)
                print('\n"' + task + '" has been removed from your task list.\n')
                found = True
        if not found:
            print('\n"' + task + '" was NOT found on your task list\n')
        return list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Adds new item to list of dictionary rows

              :param file_name: (string) with name of file:
              :param list_of_rows: (list) you want to write to a file:
              :return: (list) of dictionary rows
                      """
        file = open(file_name, 'w')
        for row in list_of_rows:
            file.write(row['Task'] + ', ' + row['Priority'] + '\n')
        file.close()
        print('Data has been saved!\n')
        return list_of_rows


# Presentation (Input/Output)  -------------------------------------------- #


class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display:
        :return: nothing
        """
        print("******* The current tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_task_and_priority():
        """ Collects user input for saving a new task item to the list

                :param none
                :return: task: (string) name of task to add
                :return: priority: (string) priority level of task
                """
        # get task and priority to be added to the list
        task = input('Please enter task: ')
        priority = input('Please assign priority level ["high", "medium", or "low"]: ')
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """ Collects user input for task to be removed from the list

               :param none
               :return: task: (string) name of task to add
               """
        # get name of task user wants to remove
        task = input('\nWhat task would you like to remove: ')
        return task


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(file_name_str, table_lst)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.output_current_tasks_in_list(table_lst)  # Show current data in the list/table
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':  # Add a new Task
        # call function to get user input
        task_str, priority_str = IO.input_new_task_and_priority()
        # call function to save the new task to the current list
        Processor.add_data_to_list(task_str.strip(), priority_str.strip(), table_lst)
        continue  # to show the menu

    elif choice_str == '2':  # Remove an existing Task
        # get task to be removed
        task_str = IO.input_task_to_remove()
        # call function to remove the task from the list
        Processor.remove_data_from_list(task_str, table_lst)
        continue  # to show the menu

    elif choice_str == '3':  # Save Data to File
        # call function to save the current list to a file
        Processor.write_data_to_file(file_name_str, table_lst)
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program
        print("Goodbye!")
        break  # and Exit
