import Tkinter as tk
from validate_email import validate_email
import phonenumbers
from PIL import Image, ImageTk 

# Define country codes
country_codes = {
    "United States": "US",
    "India": "IN",
    "United Kingdom": "GB",
    "Canada": "CA",
    "Australia": "AU",
    "France": "FR",
    "Germany": "DE",
    "China": "CN",
    "Japan": "JP",
    "Mexico": "MX",
    "Brazil": "BR",
    "South Africa": "ZA",
    "Russia": "RU",
    "Italy": "IT",
    "Spain": "ES"
}

# Tkinter GUI with Security Analysis Features
root = tk.Tk()
root.title("ValiCOm")
root.geometry("340x230")  # Adjusted size for a compact look
root.configure(bg="white")

# Main Interface
start_frame = tk.Frame(root, bg="white")
start_frame.pack(fill="both", expand=True)

# Title and Menu Buttons Frame for Center Alignment
title_frame = tk.Frame(start_frame, bg="white")
title_frame.pack(expand=True)

# Title Label
tk.Label(title_frame, text="ValiCom", font=("Helvetica", 24, "bold"), fg="black", bg="white").pack()

# Load the image and resize it
image = Image.open("ValiCom_logo1.png")
image = image.resize((50, 50), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(image)


    # Display the image
tk.Label(title_frame, image=icon, bg="white").pack(pady=10)

tk.Label(title_frame, text="Choose Analysis Type", font=("Helvetica", 12, "bold"), fg="black", bg="white").pack(pady=5)

# Button Frame for Centered Buttons
button_frame = tk.Frame(title_frame, bg="white")
button_frame.pack(pady=10)

# Button functions to navigate
def show_email_input():
    start_frame.pack_forget()
    phone_input_frame.pack_forget()
    email_input_frame.pack(fill="both", expand=True)

def show_phone_input():
    start_frame.pack_forget()
    email_input_frame.pack_forget()
    phone_input_frame.pack(fill="both", expand=True)

def show_analysis():
    email_input_frame.pack_forget()
    phone_input_frame.pack_forget()
    analysis_frame.pack(fill="both", expand=True)

def go_back():
    email_input_frame.pack_forget()
    phone_input_frame.pack_forget()
    analysis_frame.pack_forget()
    start_frame.pack(fill="both", expand=True)

# Main Menu Buttons
tk.Button(button_frame, text="Email Analysis", font=("Helvetica", 14), command=show_email_input, width=15, height=2, bg="#4CAF50", fg="black").grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Phone Analysis", font=("Helvetica", 14), command=show_phone_input, width=15, height=2, bg="#4CAF50", fg="black").grid(row=0, column=1, padx=10)

# Email Input Frame
email_input_frame = tk.Frame(root, bg="white")
content_frame_email = tk.Frame(email_input_frame, bg="white")
content_frame_email.pack(expand=True)

# Back Button in Email Input Frame
tk.Button(content_frame_email, text="Back", font=("Helvetica", 10), command=go_back, bg="#f44336", fg="black").pack(anchor="nw", padx=5, pady=5)

tk.Label(content_frame_email, text="Enter Emails (comma-separated):", font=("Helvetica", 12), fg="black", bg="white").pack(pady=5)
email_text = tk.Text(content_frame_email, height=5, width=40, font=("Helvetica", 10), bd=1, relief="solid", wrap="word")
email_text.pack(padx=10, pady=5)

# Analyze Emails and Go to Phone Analysis Button
tk.Button(content_frame_email, text="Analyze Emails", font=("Helvetica", 12), command=lambda: analyze_emails(email_text.get("1.0", "end-1c")), bg="#4CAF50", fg="black").pack(pady=5)
tk.Button(content_frame_email, text="Switch to Phone Analysis", font=("Helvetica", 10), command=show_phone_input, bg="#2196F3", fg="black").pack(pady=5)

# Phone Input Frame
phone_input_frame = tk.Frame(root, bg="white")
content_frame_phone = tk.Frame(phone_input_frame, bg="white")
content_frame_phone.pack(expand=True)

# Back Button in Phone Input Frame
tk.Button(content_frame_phone, text="Back", font=("Helvetica", 10), command=go_back, bg="#f44336", fg="black").pack(anchor="nw", padx=5, pady=5)

# Dropdown menu with "Select Country" as the default option
country_var = tk.StringVar(root)
country_var.set("Select Country")
country_menu = tk.OptionMenu(content_frame_phone, country_var, "Select Country", *sorted(country_codes.keys()))
country_menu.config(font=("Helvetica", 10))
country_menu.pack(padx=10, pady=(10, 5))

tk.Label(content_frame_phone, text="Enter Phone Numbers (comma-separated):", font=("Helvetica", 12), fg="black", bg="white").pack(pady=5)
phone_text = tk.Text(content_frame_phone, height=5, width=40, font=("Helvetica", 10), bd=1, relief="solid", wrap="word")
phone_text.pack(padx=10, pady=5)

# Analyze Phones and Go to Email Analysis Button
tk.Button(content_frame_phone, text="Analyze Phones", font=("Helvetica", 12), command=lambda: analyze_phone_numbers(phone_text.get("1.0", "end-1c").split(","), country_var.get()), bg="#4CAF50", fg="black").pack(pady=5)
tk.Button(content_frame_phone, text="Switch to Email Analysis", font=("Helvetica", 10), command=show_email_input, bg="#2196F3", fg="black").pack(pady=5)

# Analysis Frame
analysis_frame = tk.Frame(root, bg="white")
content_frame_analysis = tk.Frame(analysis_frame, bg="white")
content_frame_analysis.pack(expand=True)

tk.Label(content_frame_analysis, text="Analysis Results:", font=("Helvetica", 12), fg="black", bg="white").pack(pady=10)
result_output = tk.Text(content_frame_analysis, height=8, width=40, font=("Helvetica", 10), bd=1, relief="solid", wrap="word")
result_output.pack(padx=10, pady=5)

# Back Button on Analysis Page
tk.Button(content_frame_analysis, text="Back", font=("Helvetica", 10), command=go_back, bg="#f44336", fg="black").pack(anchor="nw", padx=5, pady=5)

# Helper function to perform email analysis and display results
def analyze_emails(emails):
    emails = emails.split(",")
    results = []
    for email in emails:
        is_valid = validate_email(email.strip(), verify=True)
        results.append("{} - Valid: {}".format(email.strip(), is_valid))
    display_analysis_results(results)
    show_analysis()

# Helper function to perform phone analysis and display results
def analyze_phone_numbers(numbers, country_name):
    country_code = country_codes.get(country_name, "US")
    results = []
    for number in numbers:
        number = number.strip()
        try:
            parsed_number = phonenumbers.parse(number, country_code)
            is_valid = phonenumbers.is_valid_number(parsed_number)
            results.append("{} - Valid: {}".format(number, is_valid))
        except phonenumbers.NumberParseException:
            results.append("{} - Invalid format".format(number))
    display_analysis_results(results)
    show_analysis()

# Function to display results in the analysis frame
def display_analysis_results(results):
    result_output.delete("1.0", tk.END)
    result_output.insert(tk.END, "\n".join(results) + "\n")

# Run the application
root.mainloop()
