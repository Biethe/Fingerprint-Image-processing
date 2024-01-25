import os
from tkinter import filedialog
import numpy as np
import customtkinter
from tkinter import *
from PIL import Image as Im
from tkdocviewer import *
from image import Image
from starter2 import Starter_2
from starter3 import Starter_3

from main_course_1 import Main_Course_1
from main_course_1_reconstruction import Main_Course_1_Reconstruction

import sys
sys.path.append("main_course_5") #to access modules in main_course_5
from main_course_5 import Image_registration_tools

class Starter_4_Window(customtkinter.CTkToplevel):
    # Create a window for starter 4
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Starter 4')
        self.geometry("650x500")
        self.resizable(True, True)
        self.state('normal')
        self.configure(bg="black")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)   
        self.rowconfigure(2, weight=1)  
        self.rowconfigure(3, weight=1) 
        self.rowconfigure(4, weight=1)    
        self.label = customtkinter.CTkLabel(self, 
                                            text="Here, you are about to either dilate or erode the binary version of an image." +
                                            "\n You first need to select your image:",
                                            fg_color="transparent", font=('Calibri', 14, 'bold'))
        self.label.grid(row=0, column=0, sticky=E)
        self.button = customtkinter.CTkButton(self, text='Select file', width=120, height=40, 
                                                font=('Cambria', 16), command=self.open_file_dialog)
        self.button.grid(row=1, column=0)

        self.combobox1 = customtkinter.CTkComboBox(self, values=["Square", "Horizontal Rectangle", "Vertical Rectangle"],
                                            command=self.struct_element_shape)
        self.combobox1.set("Square")
        self.combobox1.grid(row=2, column=0)

        self.combobox2 = customtkinter.CTkComboBox(self, values=['Dilation', 'Erosion'], 
                                                   command=self.operation_select)
        self.combobox2.set('Dilation')
        self.combobox2.grid(row=3, column=0)

        self.combobox3 = customtkinter.CTkComboBox(self, values=["3", "4", "5", "6", "7"],
                                            command=self.struct_element_size)
        self.combobox3.set("3")
        self.combobox3.grid(row=4, column=0)
        
    def open_file_dialog(self):
        global filename
        filename = filedialog.askopenfilename()
    
    def struct_element_shape(self, choice):
        global shape
        shape = choice
    
    def operation_select(self, choice):
        global operation
        operation = choice

    def struct_element_size(self, choice):
        img = Image(filename)
        global size
        size = choice
        threshold = img.compute_threshold()
        img.binarize(threshold)
        if operation == 'Erosion':
            img.erosion(shape, int(size))
            img.display()
        if operation  == 'Dilation':
            img.dilation(shape, int(size))
            img.display()
            
            
class Starter_1_Window(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Starter 1')
        self.geometry("750x650")
        self.resizable(True, True)
        self.configure(bg="black")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        self.rowconfigure(8, weight=1)
        self.rowconfigure(9, weight=1)
        self.rowconfigure(10, weight=1)
        self.rowconfigure(11, weight=1)
        self.rowconfigure(12, weight=1)
        self.rowconfigure(13, weight=1)

        # Variables to store user inputs
        self.selected_file = ""
        self.create_rectangle_var = BooleanVar(value=False)
        self.top_left_x = IntVar()
        self.top_left_y = IntVar()
        self.dimension_x = IntVar()
        self.dimension_y = IntVar()
        self.rectangle_color = StringVar(value="black")
        self.axis_symmetry_var = BooleanVar(value=False)
        self.axis_symmetry_choice = StringVar(value="along X axis")
        self.diagonal_symmetry_var = BooleanVar(value=False)
        self.diagonal_symmetry_choice = StringVar(value="diagonal")

        # Label at the top
        self.label = customtkinter.CTkLabel(self, text="Perform Rectangle and Symmetry Operations on a Fingerprint Image",
                              fg_color="transparent", font=('Calibri', 14, 'bold'))
        self.label.grid(row=0, column=0, sticky='w', padx=10, pady=10)

        # Select file button
        self.button = customtkinter.CTkButton(self, text='Select File', width=120, height=40,
                                font=('Cambria', 16), command=self.open_file_dialog)
        self.button.grid(row=1, column=0, pady=(0, 10))

        # Display selected file name
        self.selected_file_label = customtkinter.CTkLabel(self, text="Selected File: None", font=('Calibri', 12))
        self.selected_file_label.grid(row=2, column=0, sticky='w', padx=10)

        # Checkbox for creating a rectangle
        self.create_rectangle_checkbox = customtkinter.CTkCheckBox(self, text="Create a Rectangle", variable=self.create_rectangle_var,
                                                                  command=self.toggle_rectangle_entries)
        self.create_rectangle_checkbox.grid(row=3, column=0, sticky='w', padx=10)

        # Entries for rectangle dimensions
        self.top_left_label = customtkinter.CTkLabel(self, text="Top Left Corner Coordinates:", font=('Calibri', 12))
        self.top_left_label.grid(row=4, column=0, sticky='w', padx=10)
        self.top_left_entry_x = customtkinter.CTkEntry(self, font=('Calibri', 12), state="disabled")
        self.top_left_entry_x.grid(row=5, column=0, padx=10, pady=(0, 10))
        self.top_left_entry_y = customtkinter.CTkEntry(self, font=('Calibri', 12), state="disabled")
        self.top_left_entry_y.grid(row=6, column=0, padx=10, pady=(0, 10))

        self.dimension_label = customtkinter.CTkLabel(self, text="Rectangle Dimensions (width, height):", font=('Calibri', 12))
        self.dimension_label.grid(row=7, column=0, sticky='w', padx=10)
        self.dimension_entry_x = customtkinter.CTkEntry(self, font=('Calibri', 12), state="disabled")
        self.dimension_entry_x.grid(row=8, column=0, padx=10, pady=(0, 10))
        self.dimension_entry_y = customtkinter.CTkEntry(self, font=('Calibri', 12), state="disabled")
        self.dimension_entry_y.grid(row=9, column=0, padx=10, pady=(0, 10))

        # Combobox for rectangle color
        self.rectangle_color_label = customtkinter.CTkLabel(self, text="Rectangle Color:", font=('Calibri', 12))
        self.rectangle_color_label.grid(row=10, column=0, sticky='w', padx=10)
        self.rectangle_color_combo = customtkinter.CTkComboBox(self, values=["black", "white"], state="disabled")
        self.rectangle_color_combo.grid(row=11, column=0, padx=10, pady=(0, 10))

        # Checkbox for axis symmetry
        self.axis_symmetry_checkbox = customtkinter.CTkCheckBox(self, text="Axis Symmetry", variable=self.axis_symmetry_var,
                                                                command=self.toggle_axis_symmetry_combobox)
        self.axis_symmetry_checkbox.grid(row=12, column=0, sticky='w', padx=10)

        # Combobox for axis symmetry choice
        self.axis_symmetry_label = customtkinter.CTkLabel(self, text="Axis Symmetry Choice:", font=('Calibri', 12))
        self.axis_symmetry_label.grid(row=13, column=0, sticky='w', padx=10)
        self.axis_symmetry_entry = customtkinter.CTkComboBox(self, values=["along Horizontal axis", "along Vertical axis"], state="disabled")
        self.axis_symmetry_entry.grid(row=14, column=0, padx=10, pady=(0, 10))

        # Checkbox for diagonal symmetry
        self.diagonal_symmetry_checkbox = customtkinter.CTkCheckBox(self, text="Diagonal Symmetry", variable=self.diagonal_symmetry_var,
                                                                    command=self.toggle_diagonal_symmetry_combobox)
        self.diagonal_symmetry_checkbox.grid(row=15, column=0, sticky='w', padx=10)

        # Combobox for diagonal symmetry choice
        self.diagonal_symmetry_label = customtkinter.CTkLabel(self, text="Diagonal Symmetry Choice:", font=('Calibri', 12))
        self.diagonal_symmetry_label.grid(row=16, column=0, sticky='w', padx=10)
        self.diagonal_symmetry_entry = customtkinter.CTkComboBox(self, values=["diagonal", "anti-diagonal"], state="disabled")
        self.diagonal_symmetry_entry.grid(row=17, column=0, padx=10, pady=(0, 10))

        # Transform button
        self.transform_button = customtkinter.CTkButton(self, text='Transform', width=120, height=40,
                                          font=('Cambria', 16), command=self.transform_image)
        self.transform_button.grid(row=18, column=0, pady=(10, 0))

    def open_file_dialog(self):
        self.selected_file = filedialog.askopenfilename()
        if self.selected_file != "":
            # Create an instance of the Image class with the selected file
            img = Image(self.selected_file)
            # Update the label with the file name and size
            self.selected_file_label.configure(text=f"Selected File: {self.selected_file} \n" \
                                                    f"(Size: {img.n}x{img.m})")

    def toggle_rectangle_entries(self):
        state = "normal" if self.create_rectangle_var.get() else "disabled"
        self.top_left_entry_x.configure(state=state)
        self.top_left_entry_y.configure(state=state)
        self.dimension_entry_x.configure(state=state)
        self.dimension_entry_y.configure(state=state)
        self.rectangle_color_combo.configure(state=state)

    def toggle_axis_symmetry_combobox(self):
        state = "normal" if self.axis_symmetry_var.get() else "disabled"
        self.axis_symmetry_entry.configure(state=state)

    def toggle_diagonal_symmetry_combobox(self):
        state = "normal" if self.diagonal_symmetry_var.get() else "disabled"
        self.diagonal_symmetry_entry.configure(state=state)

    def transform_image(self):
        # Create an instance of the Image class with the selected file
        img = Image(self.selected_file)

        # Check if rectangle needs to be created
        if self.create_rectangle_var.get():
            top_left_x = int(self.top_left_entry_x.get())
            top_left_y = int(self.top_left_entry_y.get())
            dimension_x = int(self.dimension_entry_x.get())
            dimension_y = int(self.dimension_entry_y.get())
            rectangle_color = str(self.rectangle_color_combo.get())
            img.create_rectangle((top_left_x, top_left_y), dimension_x, dimension_y, rectangle_color)

        # Check if axis symmetry needs to be applied
        if self.axis_symmetry_var.get():
            axis_symmetry = str(self.axis_symmetry_entry.get())
            if axis_symmetry == "along Horizontal axis":
                img.symmetry()
            else:
                img.symmetry(axis=1)

        # Check if diagonal symmetry needs to be applied
        if self.diagonal_symmetry_var.get():
            diagonal_symmetry = str(self.diagonal_symmetry_entry.get())
            if diagonal_symmetry == "diagonal":
                img.symmetry_diagonal(axis=1)
            else:
                img.symmetry_diagonal()

        # Display the transformed image
        img.display()

            
            
class Starter_2_Window(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Starter 2')
        self.geometry("750x500")
        self.resizable(True, True)
        self.configure(bg="black")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        
        # Variables to store user inputs
        self.selected_file = ""
        self.rotation_angle = DoubleVar()
        self.center_x = IntVar()
        self.center_y = IntVar()
        self.translation_x = IntVar()
        self.translation_y = IntVar()
        self.data_conservation_var = BooleanVar(value=False)
        self.inverse_order_var = BooleanVar(value=False)

        # Label at the top
        self.label = customtkinter.CTkLabel(self, text="Perform Rotation-Translation on a Fingerprint Image",
                              fg_color="transparent", font=('Calibri', 14, 'bold'))
        self.label.grid(row=0, column=0, sticky='w', padx=10, pady=10)

        # Select file button
        self.button = customtkinter.CTkButton(self, text='Select File', width=120, height=40,
                                font=('Cambria', 16), command=self.open_file_dialog)
        self.button.grid(row=1, column=0, pady=(0, 10))

        # Display selected file name
        self.selected_file_label = customtkinter.CTkLabel(self, text="Selected File: None", font=('Calibri', 12))
        self.selected_file_label.grid(row=2, column=0, sticky='w', padx=10)

        # Rotation angle entry
        self.angle_label = customtkinter.CTkLabel(self, text="Enter Rotation Angle (degrees):", font=('Calibri', 12))
        self.angle_label.grid(row=3, column=0, sticky='w', padx=10)
        self.angle_entry = customtkinter.CTkEntry(self, font=('Calibri', 12))
        self.angle_entry.grid(row=4, column=0, padx=10, pady=(0, 10))

        # Center of rotation entry
        self.center_label = customtkinter.CTkLabel(self, text="Enter Center of Rotation (x, y):", font=('Calibri', 12))
        self.center_label.grid(row=5, column=0, sticky='w', padx=10)
        self.center_entry_x = customtkinter.CTkEntry(self, font=('Calibri', 12))
        self.center_entry_x.grid(row=6, column=0, padx=10, pady=(0, 10))
        self.center_entry_y = customtkinter.CTkEntry(self, font=('Calibri', 12))
        self.center_entry_y.grid(row=7, column=0, padx=10, pady=(0, 10))

        # Translation entry
        self.translation_label = customtkinter.CTkLabel(self, text="Enter Translation (x, y):", font=('Calibri', 12))
        self.translation_label.grid(row=8, column=0, sticky='w', padx=10)
        self.translation_entry_x = customtkinter.CTkEntry(self, font=('Calibri', 12))
        self.translation_entry_x.grid(row=9, column=0, padx=10, pady=(0, 10))
        self.translation_entry_y = customtkinter.CTkEntry(self, font=('Calibri', 12))
        self.translation_entry_y.grid(row=10, column=0, padx=10, pady=(0, 10))

        # Checkboxes
        self.data_conservation_checkbox = customtkinter.CTkCheckBox(self, text="Data Conservation", variable=self.data_conservation_var)
        self.data_conservation_checkbox.grid(row=11, column=0, sticky='w', padx=10)
        self.inverse_order_checkbox = customtkinter.CTkCheckBox(self, text="Inverse Rotation and Translation Order", variable=self.inverse_order_var)
        self.inverse_order_checkbox.grid(row=12, column=0, sticky='w', padx=10)

        # Transform button
        self.transform_button = customtkinter.CTkButton(self, text='Transform', width=120, height=40,
                                          font=('Cambria', 16), command=self.transform_image)
        self.transform_button.grid(row=13, column=0, pady=(10, 0))

    def open_file_dialog(self):
        self.selected_file = filedialog.askopenfilename()
        if self.selected_file != "":
            # Create an instance of the Image class with the selected file
            img = Image(self.selected_file)
            # Update the label with the file name and size
            self.selected_file_label.configure(text=f"Selected File: {self.selected_file} \n" \
                                                    f"(Size: {img.n}x{img.m})")

    def transform_image(self):
        # Retrieve user inputs
        rotation_angle = float(self.angle_entry.get())
        center_x = int(self.center_entry_x.get())
        center_y = int(self.center_entry_y.get())
        translation_x = int(self.translation_entry_x.get())
        translation_y = int(self.translation_entry_y.get())
        data_conservation = self.data_conservation_var.get()
        inverse_order = self.inverse_order_var.get()

        # Create an instance of the Image class with the selected file
        img = Image(self.selected_file)

        # Perform rotation-translation operation
        img.rotate_translate(rotation_angle, (center_x, center_y), (translation_x, translation_y),
                             data_conservation, inverse_order)

        # Display the transformed image
        img.display()
        
        
class Main_1_Simulation_Window(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Main Course 1 Simulation')
        self.geometry("650x500")
        self.resizable(True, True)
        self.configure(bg="black")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        
        # Variables to store user inputs
        self.selected_file = ""
        self.center_x = IntVar()
        self.center_y = IntVar()
        self.apply_all_transformations_var = BooleanVar(value=False)

        # Explanation text
        explanation_text = "Perform an operation of simulation of low pressure on any fingerprint."
        self.explanation_label = customtkinter.CTkLabel(self, text=explanation_text, fg_color="transparent", font=('Calibri', 14, 'bold'))
        self.explanation_label.grid(row=0, column=0, sticky='w', padx=10, pady=10)

        # Select file button
        self.button = customtkinter.CTkButton(self, text='Select File', width=120, height=40,
                                font=('Cambria', 16), command=self.open_file_dialog)
        self.button.grid(row=1, column=0, pady=(0, 10))

        # Display selected file name and size
        self.selected_file_label = customtkinter.CTkLabel(self, text="Selected File: None", font=('Calibri', 12))
        self.selected_file_label.grid(row=2, column=0, sticky='w', padx=10)

        # Center coordinates entries
        self.center_label = customtkinter.CTkLabel(self, text="Enter Center of Low Pressure (x, y):", font=('Calibri', 12))
        self.center_label.grid(row=3, column=0, sticky='w', padx=10)
        self.center_entry_x = customtkinter.CTkEntry(self, font=('Calibri', 12))
        self.center_entry_x.grid(row=4, column=0, padx=10, pady=(0, 10))
        self.center_entry_y = customtkinter.CTkEntry(self, font=('Calibri', 12))
        self.center_entry_y.grid(row=5, column=0, padx=10, pady=(0, 10))

        # Checkbox for applying all transformations
        self.apply_all_transformations_checkbox = customtkinter.CTkCheckBox(self, text="Apply All Transformations", variable=self.apply_all_transformations_var)
        self.apply_all_transformations_checkbox.grid(row=6, column=0, sticky='w', padx=10)

        # Reminder text about rotating the image
        reminder_text = "Note: You might want to rotate the image before applying this kind of transformation,\n" \
                        "so the vertical axis of the fingerprint aligns with the vertical axis of the image."
        self.reminder_label = customtkinter.CTkLabel(self, text=reminder_text, fg_color="transparent", font=('Calibri', 10))
        self.reminder_label.grid(row=7, column=0, sticky='w', padx=10, pady=(0, 10))

        # Transform button
        self.transform_button = customtkinter.CTkButton(self, text='Transform', width=120, height=40,
                                          font=('Cambria', 16), command=self.transform_image)
        self.transform_button.grid(row=8, column=0, pady=(10, 0))

    def open_file_dialog(self):
        self.selected_file = filedialog.askopenfilename()
        if self.selected_file != "":
            # Create an instance of the Image class with the selected file
            img = Image(self.selected_file)
            # Update the label with the file name and size
            self.selected_file_label.configure(text=f"Selected File: {self.selected_file} \n" \
                                                    f"(Size: {img.n}x{img.m})")

    def transform_image(self):
        # Retrieve user inputs
        center_x = int(self.center_entry_x.get())
        center_y = int(self.center_entry_y.get())
        apply_all_transformations = self.apply_all_transformations_var.get()

        # Create an instance of the Image class with the selected file
        img = Image(self.selected_file)

        # Perform low-pressure simulation
        low_pressure_img = Main_Course_1.simulate_low_pressure(img, center_x, center_y, Main_Course_1.c5)

        # Apply additional transformations if requested
        if apply_all_transformations:
            low_pressure_img.binarize(low_pressure_img.compute_threshold())
            low_pressure_img.dilation("Horizontal Rectangle", 3)
            low_pressure_img.blur(3)

        # Display the transformed image
        low_pressure_img.display()
        
        
class Main_1_Restauration_Window(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Main Course 1 Restauration')
        self.geometry("650x500")
        self.resizable(True, True)
        self.configure(bg="black")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        self.rowconfigure(8, weight=1)
        
        # Variables to store user inputs
        self.selected_file = ""
        self.top_left_x = IntVar()
        self.top_left_y = IntVar()
        self.dimension_x = IntVar()
        self.dimension_y = IntVar()
        self.number_patches = IntVar()
        self.patch_size = IntVar()

        # Explanation text
        explanation_text = "Perform an operation of restoration of a specific part of any fingerprint."
        self.explanation_label = customtkinter.CTkLabel(self, text=explanation_text, fg_color="transparent", font=('Calibri', 14, 'bold'))
        self.explanation_label.grid(row=0, column=0, sticky='w', padx=10, pady=10)

        # Select file button
        self.button = customtkinter.CTkButton(self, text='Select File', width=120, height=40,
                                font=('Cambria', 16), command=self.open_file_dialog)
        self.button.grid(row=1, column=0, pady=(0, 10))

        # Display selected file name and size
        self.selected_file_label = customtkinter.CTkLabel(self, text="Selected File: None", font=('Calibri', 12))
        self.selected_file_label.grid(row=2, column=0, sticky='w', padx=10)

        # Top-left corner coordinates entries
        self.top_left_label = customtkinter.CTkLabel(self, text="Top Left Corner Coordinates of Restoration Rectangle:", font=('Calibri', 12))
        self.top_left_label.grid(row=3, column=0, sticky='w', padx=10)
        self.top_left_entry_x = customtkinter.CTkEntry(self, font=('Calibri', 12))
        self.top_left_entry_x.grid(row=4, column=0, padx=10, pady=(0, 10))
        self.top_left_entry_y = customtkinter.CTkEntry(self, font=('Calibri', 12))
        self.top_left_entry_y.grid(row=5, column=0, padx=10, pady=(0, 10))

        # Rectangle dimensions entries
        self.dimension_label_x = customtkinter.CTkLabel(self, text="Vertical Dimension of the Rectangle:", font=('Calibri', 12))
        self.dimension_label_x.grid(row=6, column=0, sticky='w', padx=10)
        self.dimension_entry_x = customtkinter.CTkEntry(self, font=('Calibri', 12))
        self.dimension_entry_x.grid(row=7, column=0, padx=10, pady=(0, 10))
        self.dimension_label_y = customtkinter.CTkLabel(self, text="Horizontal Dimension of the Rectangle:", font=('Calibri', 12))
        self.dimension_label_y.grid(row=8, column=0, sticky='w', padx=10)
        self.dimension_entry_y = customtkinter.CTkEntry(self, font=('Calibri', 12))
        self.dimension_entry_y.grid(row=9, column=0, padx=10, pady=(0, 10))

        # Number of patches entry
        self.patches_label = customtkinter.CTkLabel(self, text="Number of Patches:", font=('Calibri', 12))
        self.patches_label.grid(row=11, column=0, sticky='w', padx=10)
        self.number_patches_entry = customtkinter.CTkEntry(self, font=('Calibri', 12))
        self.number_patches_entry.grid(row=12, column=0, padx=10, pady=(0, 10))

        # Patch size entry
        self.patch_size_label = customtkinter.CTkLabel(self, text="Patch Size (odd number >= 3):", font=('Calibri', 12))
        self.patch_size_label.grid(row=13, column=0, sticky='w', padx=10)
        self.patch_size_entry = customtkinter.CTkEntry(self, font=('Calibri', 12))
        self.patch_size_entry.grid(row=14, column=0, padx=10, pady=(0, 10))

        # Transform button
        self.transform_button = customtkinter.CTkButton(self, text='Transform', width=120, height=40,
                                          font=('Cambria', 16), command=self.transform_image)
        self.transform_button.grid(row=15, column=0, pady=(10, 0))

    def open_file_dialog(self):
        self.selected_file = filedialog.askopenfilename()
        if self.selected_file != "":
            # Create an instance of the Image class with the selected file
            img = Image(self.selected_file)
            # Update the label with the file name and size
            self.selected_file_label.configure(text=f"Selected File: {self.selected_file} \n" \
                                                    f"(Size: {img.n}x{img.m})")

    def transform_image(self):
        # Retrieve user inputs
        top_left_x = int(self.top_left_entry_x.get())
        top_left_y = int(self.top_left_entry_y.get())
        dimension_x = int(self.dimension_entry_x.get())
        dimension_y = int(self.dimension_entry_y.get())
        number_patches = int(self.number_patches_entry.get())
        patch_size = int(self.patch_size_entry.get())

        # Create an instance of the Image class with the selected file
        img = Image(self.selected_file)
        
        # Open the weak finger image
        img2 = Image("images/weak_finger.png")

        # Create a binary mask with the specified rectangle
        mask = np.full((img.n, img.m), False)
        mask[top_left_x : top_left_x + dimension_x, top_left_y : top_left_y + dimension_y] = True

        # Crop the image into several patches
        patches = img2.crop_patches(number_patches, patch_size)

        # Apply the restoration algorithm onto the image
        img = Main_Course_1_Reconstruction.restauration(img, patches, mask, patch_size)

        # Display the transformed image, with the rectangle in which the restauration has been performed
        img.display(point=(top_left_x, top_left_y), rectangle=((top_left_x, top_left_y), (dimension_x, dimension_y)))

class Main_Course_5_Window(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Starter 2')
        self.geometry("750x500")
        self.resizable(True, True)
        self.configure(bg="black")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        
        # Variables to store user inputs
        self.selected_file = ""
        self.rotation_angle = DoubleVar()
        self.center_x = IntVar()
        self.center_y = IntVar()
        self.translation_x = IntVar()
        self.translation_y = IntVar()
        self.data_conservation_var = BooleanVar(value=False)
        self.inverse_order_var = BooleanVar(value=False)

        # Label at the top
        self.label = customtkinter.CTkLabel(self, text="Perform Rotation-Translation on a Fingerprint Image",
                              fg_color="transparent", font=('Calibri', 14, 'bold'))
        self.label.grid(row=0, column=0, sticky='w', padx=10, pady=10)

        # Select file button
        self.button = customtkinter.CTkButton(self, text='Select File', width=120, height=40,
                                font=('Cambria', 16), command=self.open_file_dialog)
        self.button.grid(row=1, column=0, pady=(0, 10))

        # Display selected file name
        self.selected_file_label = customtkinter.CTkLabel(self, text="Selected File: None", font=('Calibri', 12))
        self.selected_file_label.grid(row=2, column=0, sticky='w', padx=10)

        # Rotation angle entry
        self.angle_label = customtkinter.CTkLabel(self, text="Enter Rotation Angle (degrees):", font=('Calibri', 12))
        self.angle_label.grid(row=3, column=0, sticky='w', padx=10)
        self.angle_entry = customtkinter.CTkEntry(self, font=('Calibri', 12))
        self.angle_entry.grid(row=4, column=0, padx=10, pady=(0, 10))

        # Center of rotation entry
        self.center_label = customtkinter.CTkLabel(self, text="Enter Center of Rotation (x, y):", font=('Calibri', 12))
        self.center_label.grid(row=5, column=0, sticky='w', padx=10)
        self.center_entry_x = customtkinter.CTkEntry(self, font=('Calibri', 12))
        self.center_entry_x.grid(row=6, column=0, padx=10, pady=(0, 10))
        self.center_entry_y = customtkinter.CTkEntry(self, font=('Calibri', 12))
        self.center_entry_y.grid(row=7, column=0, padx=10, pady=(0, 10))

        # Translation entry
        self.translation_label = customtkinter.CTkLabel(self, text="Enter Translation (x, y):", font=('Calibri', 12))
        self.translation_label.grid(row=8, column=0, sticky='w', padx=10)
        self.translation_entry_x = customtkinter.CTkEntry(self, font=('Calibri', 12))
        self.translation_entry_x.grid(row=9, column=0, padx=10, pady=(0, 10))
        self.translation_entry_y = customtkinter.CTkEntry(self, font=('Calibri', 12))
        self.translation_entry_y.grid(row=10, column=0, padx=10, pady=(0, 10))

        # Checkboxes
        self.data_conservation_checkbox = customtkinter.CTkCheckBox(self, text="Data Conservation", variable=self.data_conservation_var)
        self.data_conservation_checkbox.grid(row=11, column=0, sticky='w', padx=10)
        self.inverse_order_checkbox = customtkinter.CTkCheckBox(self, text="Inverse Rotation and Translation Order", variable=self.inverse_order_var)
        self.inverse_order_checkbox.grid(row=12, column=0, sticky='w', padx=10)

        # Transform button
        self.transform_button = customtkinter.CTkButton(self, text='Transform', width=120, height=40,
                                          font=('Cambria', 16), command=self.transform_image)
        self.transform_button.grid(row=13, column=0, pady=(10, 0))

    def open_file_dialog(self):
        self.selected_file = filedialog.askopenfilename()
        if self.selected_file != "":
            # Create an instance of the Image class with the selected file
            img = Image(self.selected_file)
            # Update the label with the file name and size
            self.selected_file_label.configure(text=f"Selected File: {self.selected_file} \n" \
                                                    f"(Size: {img.n}x{img.m})")

    def transform_image(self):
        # Retrieve user inputs
        rotation_angle = float(self.angle_entry.get())
        center_x = int(self.center_entry_x.get())
        center_y = int(self.center_entry_y.get())
        translation_x = int(self.translation_entry_x.get())
        translation_y = int(self.translation_entry_y.get())
        data_conservation = self.data_conservation_var.get()
        inverse_order = self.inverse_order_var.get()

        # Create an instance of the Image class with the selected file
        img = Image(self.selected_file)

        # Perform rotation-translation operation
        img.rotate_translate(rotation_angle, (center_x, center_y), (translation_x, translation_y),
                             data_conservation, inverse_order)

        # Display the transformed image
        img.display()
        


        
class SecondWindow(customtkinter.CTkToplevel):
    #Build a new window for section selection
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Section Selection')
        self.geometry("250x150")
        self.resizable(False, False)
        self.state('normal')
        self.configure(bg="black")
        # Reconfigure our rows and columns for grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.label = customtkinter.CTkLabel(self, 
                                            text="Pick the section you want \n to have a snippet of:",
                                            fg_color="transparent", font=('Calibri', 16, 'bold'))
        self.label.grid(column=0, row=0)
        #Create a list of the different sections we have worked on so far
        self.combobox = customtkinter.CTkComboBox(self, values=["Starter 1", "Starter 2", "Starter 3",
                                                          "Starter 4", "Starter 5", "Main Course 1 (Simulation)", "Main Course 1 (Restauration)", "Main course 5"],
                                            command=self.combobox_callback)
        self.combobox.set("Starter 1")
        self.combobox.grid(row=1, column=0)

    #This function creates the command that should be executed whenever a section is selected
    # To be updated
    def combobox_callback(self, choice):
        if choice == "Starter 1":
            self.toplevel_window = None
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = Starter_1_Window(self)  # create window if its None or destroyed
            else:
                self.toplevel_window.focus()
        if choice == "Starter 2":
            self.toplevel_window = None
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = Starter_2_Window(self)  # create window if its None or destroyed
            else:
                self.toplevel_window.focus()
        if choice == "Starter 3":
            os.system('starter3.py')
        if choice == "Starter 4":
            self.toplevel_window = None
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = Starter_4_Window(self)  # create window if its None or destroyed
            else:
                self.toplevel_window.focus()
        if choice == "Starter 5":
            os.system('starter5.py')
        if choice == "Main Course 1 (Simulation)":
            self.toplevel_window = None
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = Main_1_Simulation_Window(self)  # create window if its None or destroyed
            else:
                self.toplevel_window.focus()
        if choice == "Main Course 1 (Restauration)":
            self.toplevel_window = None
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = Main_1_Restauration_Window(self)  # create window if its None or destroyed
            else:
                self.toplevel_window.focus()
        if choice == "Main course 5":
            self.toplevel_window = None
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = Main_Course_5_Window(self)  # create window if its None or destroyed
            else:
                self.toplevel_window.focus()


class App(customtkinter.CTk):
    #Creates the home window
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("{0}x{1}+0+0".format(1100, 700))
        self.title('Fingerprint Image Processing')
        # self.iconbitmap('unfpa_logo.ico')
        self.resizable(False, False)
        self.state('normal')
        self.configure(bg="black")
        # Reconfigure our rows and columns for grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        image_1 = customtkinter.CTkImage(light_image=Im.open("images/uga.png"),
                                        dark_image=Im.open("images/uga.png"),
                                        size=(250, 100))
        self.label_img_1 = customtkinter.CTkLabel(self, image=image_1, text = "")
        self.label_img_1.grid(row=0, column=1)

        self.label_1 = customtkinter.CTkLabel(self, text="Fingerprint Digital Processing", fg_color="transparent",
                                    font=('Helvetica', 30, 'bold'))
        self.label_1.grid(row=1, column=1, sticky=N)

        image_2 = customtkinter.CTkImage(light_image=Im.open("images/fingerprint.png"),
                                        dark_image=Im.open("images/fingerprint.png"),
                                        size=(100, 40))
        self.label_img_2 = customtkinter.CTkLabel(self, image=image_2, text = "")
        self.label_img_2.grid(row=1, column=1)

        self.label_2 = customtkinter.CTkLabel(self, text="With Bierhoff, Sabin, Sacha and Vincent", fg_color="transparent",
                                    font=('Comic Sans MS', 30, 'italic'))
        self.label_2.grid(row=2, column=1, sticky=N)

        self.button_1 = customtkinter.CTkButton(self, text='Start', width=120, height=40, font=('Cambria', 16), command=self.open_toplevel)
        self.button_1.grid(row=2, column=1)

        self.toplevel_window = None


    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = SecondWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()




app = App()
app.mainloop()