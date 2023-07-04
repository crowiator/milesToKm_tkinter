import tkinter


#window
window = tkinter.Tk()
window.title("Miles to km")
window.minsize(width=200, height=100)

# ENtry component for number
input = tkinter.Entry(width=10)
input.grid(row=0, column=1)

# Miles label
miles_label = tkinter.Label(text="Miles", font=("Arial", 15, "bold"))
miles_label.grid(row=0, column=2)

# Label for text
text_label = tkinter.Label(text="is equal to ", font=("Arial", 15, "bold"))
text_label.grid(row=1, column=0)

# Label for result
result_label = tkinter.Label(text="0", font=("Arial", 15, "bold"))
result_label.grid(row=1, column=1)

# Label for km
km_label = tkinter.Label(text="Km", font=("Arial", 15, "bold"))
km_label.grid(row=1, column=2)


def miles_to_km():
    miles = float(input.get())
    km = 1.60934 * miles
    result_label.config(text=str(km))

#Button
button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)

window.mainloop()