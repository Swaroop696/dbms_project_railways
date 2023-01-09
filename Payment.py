import tkinter as tk


def submit_payment():
    # Get the payment amount from the entry field
    payment_amount = amount_entry.get()

    # Validate the payment amount
    try:
        payment_amount = float(payment_amount)
        if payment_amount <= 0:
            raise ValueError
    except ValueError:
        message_label.config(text="Please enter a valid payment amount.")
        return

    # Get the selected payment method
    payment_method = payment_method_variable.get()

    # Submit the payment
    message_label.config(text=f"Payment of ${payment_amount} submitted using {payment_method}.")


# Create the window
window = tk.Tk()
window.title("Payment Page")

# Create a label for the payment amount
amount_label = tk.Label(text="Payment Amount:")
amount_label.pack()

# Create an entry field for the payment amount
amount_entry = tk.Entry()
amount_entry.pack()

# Create a label and option menu for the payment method
payment_method_label = tk.Label(text="Payment Method:")
payment_method_label.pack()

payment_method_variable = tk.StringVar(window)
payment_method_variable.set("Credit Card")  # default value
payment_method_optionmenu = tk.OptionMenu(window, payment_method_variable, "Credit Card", "PayPal")
payment_method_optionmenu.pack()

# Create a button to submit the payment
submit_button = tk.Button(text="Submit Payment", command=submit_payment)
submit_button.pack()

# Create a label to display a message
message_label = tk.Label(text="")
message_label.pack()

# Run the main loop to display the window
window.mainloop()
