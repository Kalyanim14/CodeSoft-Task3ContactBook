import tkinter as tk
from tkinter import messagebox
import re

# Initialize the contact list as a dictionary
contacts = {}

# Function to add a new contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()
    
    if name and phone:
        contacts[name] = {'Phone': phone, 'Email': email if email else None, 'Address': address if address else None}
        update_contact_list()
        clear_entries()
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showwarning("Input Error", "Name and Phone are required fields.")

# Function to view the contact list
def update_contact_list():
    listbox.delete(0, tk.END)
    for name, details in contacts.items():
        contact_info = f"{name} - {details['Phone']}"
        if details['Email']:
            contact_info += f" - {details['Email']}"
        if details['Address']:
            contact_info += f" - {details['Address']}"
        listbox.insert(tk.END, contact_info)

# Function to search contacts
def search_contact():
    search_term = entry_search.get().lower()
    if search_term:
        listbox.delete(0, tk.END)
        pattern = re.compile(search_term)
        for name, details in contacts.items():
            contact_info = f"{name} - {details['Phone']}"
            if details['Email']:
                contact_info += f" - {details['Email']}"
            if details['Address']:
                contact_info += f" - {details['Address']}"
            # Search for any sequence matching the search term
            if pattern.search(contact_info.lower()):
                listbox.insert(tk.END, contact_info)
    else:
        update_contact_list()

# Function to update contact information
def update_contact():
    selected = listbox.curselection()
    if selected:
        selected_index = selected[0]
        selected_name = listbox.get(selected_index).split(" - ")[0]
        phone = entry_phone.get()
        email = entry_email.get()
        address = entry_address.get()
        
        if phone:
            contacts[selected_name] = {'Phone': phone, 'Email': email if email else None, 'Address': address if address else None}
            update_contact_list()
            clear_entries()
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showwarning("Input Error", "Phone is required to update contact.")
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to update.")

# Function to delete a contact
def delete_contact():
    selected = listbox.curselection()
    if selected:
        selected_index = selected[0]
        selected_name = listbox.get(selected_index).split(" - ")[0]
        del contacts[selected_name]
        update_contact_list()
        clear_entries()
        messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")

# Function to populate the fields with the selected contact's details for update
def select_contact(event):
    selected = listbox.curselection()
    if selected:
        selected_index = selected[0]
        selected_name = listbox.get(selected_index).split(" - ")[0]
        contact = contacts[selected_name]
        
        entry_name.delete(0, tk.END)
        entry_name.insert(0, selected_name)
        
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, contact['Phone'])
        
        entry_email.delete(0, tk.END)
        entry_email.insert(0, contact.get('Email', ''))
        
        entry_address.delete(0, tk.END)
        entry_address.insert(0, contact.get('Address', ''))

# Function to clear entry fields
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_search.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Contact Book")
root.geometry("800x700")
root.config(bg="AliceBlue")  # Set the background color to AliceBlue

# Title
title = tk.Label(root, text="Contact Book", font=("Helvetica", 18), bg="AliceBlue")
title.pack(pady=20)

# Frame for contact details
frame = tk.Frame(root, bg="AliceBlue")
frame.pack(pady=10)

# Name Entry
label_name = tk.Label(frame, text="Name:", font=("Arial", 12), bg="AliceBlue")
label_name.grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame, font=("Arial", 12), width=40)
entry_name.grid(row=0, column=1, padx=5, pady=5)

# Phone Entry
label_phone = tk.Label(frame, text="Phone:", font=("Arial", 12), bg="AliceBlue")
label_phone.grid(row=1, column=0, padx=5, pady=5)
entry_phone = tk.Entry(frame, font=("Arial", 12), width=40)
entry_phone.grid(row=1, column=1, padx=5, pady=5)

# Email Entry (optional)
label_email = tk.Label(frame, text="Email (optional):", font=("Arial", 12), bg="AliceBlue")
label_email.grid(row=2, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame, font=("Arial", 12), width=40)
entry_email.grid(row=2, column=1, padx=5, pady=5)

# Address Entry (optional)
label_address = tk.Label(frame, text="Address (optional):", font=("Arial", 12), bg="AliceBlue")
label_address.grid(row=3, column=0, padx=5, pady=5)
entry_address = tk.Entry(frame, font=("Arial", 12), width=40)
entry_address.grid(row=3, column=1, padx=5, pady=5)

# Button to Add Contact
add_button = tk.Button(frame, text="Add Contact", font=("Arial", 12), command=add_contact, bg="AliceBlue")
add_button.grid(row=4, column=0, columnspan=2, pady=10)

# Search Section
search_frame = tk.Frame(root, bg="AliceBlue")
search_frame.pack(pady=10)

# Search Entry
label_search = tk.Label(search_frame, text="Search by Name, Phone, Email or Address:", font=("Arial", 12), bg="AliceBlue")
label_search.grid(row=0, column=0, padx=5, pady=5)
entry_search = tk.Entry(search_frame, font=("Arial", 12), width=40)
entry_search.grid(row=0, column=1, padx=5, pady=5)

# Search Button
search_button = tk.Button(search_frame, text="Search", font=("Arial", 12), command=search_contact, bg="AliceBlue")
search_button.grid(row=0, column=2, padx=5, pady=5)

# Listbox to display contacts
listbox_frame = tk.Frame(root, bg="AliceBlue")
listbox_frame.pack(pady=10)

listbox = tk.Listbox(listbox_frame, font=("Arial", 12), width=50, height=10)
listbox.pack(pady=10)

# Bind listbox to select contact for update
listbox.bind("<<ListboxSelect>>", select_contact)

# Button to update selected contact
update_button = tk.Button(root, text="Update Contact", font=("Arial", 12), command=update_contact, bg="AliceBlue")
update_button.pack(pady=5)

# Button to delete selected contact
delete_button = tk.Button(root, text="Delete Contact", font=("Arial", 12), command=delete_contact, bg="AliceBlue")
delete_button.pack(pady=5)

# Button to clear entries
clear_button = tk.Button(root, text="Clear Entries", font=("Arial", 12), command=clear_entries, bg="AliceBlue")
clear_button.pack(pady=5)

# Run the application
root.mainloop()
