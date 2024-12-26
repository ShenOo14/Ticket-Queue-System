
import tkinter as tk
from tkinter import messagebox

class TicketQueue:
    def __init__(self):
        self.queue = []
        self.tickets = {}
        self.count = 0

    def add_customer(self, *names): 
        for name in names:
            self.queue.append(name)
            self.count += 1

    def issue_all_tickets(self):
        while self.queue:
            name = self.queue.pop()
            self.tickets[self.count] = name

    def cancel_ticket(self, name):
        if name in self.queue:
            self.queue.remove(name)
            self.count -= 1
        else:
            raise ValueError(f"{name} is not in the queue.")

    def display_queue(self):
        return list(self.queue)

    def display_tickets(self):
        return self.tickets


class TicketQueueGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ticket Queue System")
        self.root.geometry("1920x1080")
        self.root.configure(bg="#f5f5f5")  # Light gray background
        self.queue_system = TicketQueue()

        
        self.title_label = tk.Label(
            self.root, text="Ticket reservation management", font=("Helvetica", 24, "bold"), bg="#f5f5f5", fg="#333333"
        )
        self.title_label.pack(pady=20)

        
        self.input_frame = tk.Frame(self.root, bg="#f5f5f5")
        self.input_frame.pack(pady=10)

        tk.Label(self.input_frame, text="Customer Name(s):", font=("Helvetica", 14), bg="#f5f5f5", fg="#555555").grid(
            row=0, column=0, padx=10, pady=10
        )
        self.name_entry = tk.Entry(self.input_frame, width=30, font=("Helvetica", 14))
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.add_button = tk.Button(
            self.input_frame,
            text="Add Customer(s)",
            command=self.add_customers,
            font=("Helvetica", 12),
            bg="#4caf50",
            fg="white",
            relief="raised",
            bd=2,
        )
        self.add_button.grid(row=0, column=2, padx=10, pady=10)

        
        self.buttons_frame = tk.Frame(self.root, bg="#f5f5f5")
        self.buttons_frame.pack(pady=20)

        self.issue_button = tk.Button(
            self.buttons_frame,
            text="Issue All Tickets",
            command=self.issue_all_tickets,
            font=("Helvetica", 12),
            bg="#2196f3",
            fg="white",
            relief="raised",
            bd=2,
        )
        self.issue_button.grid(row=0, column=0, padx=10, pady=10)

        self.cancel_button = tk.Button(
            self.buttons_frame,
            text="Cancel Ticket",
            command=self.cancel_ticket,
            font=("Helvetica", 12),
            bg="#f44336",
            fg="white",
            relief="raised",
            bd=2,
        )
        self.cancel_button.grid(row=0, column=1, padx=10, pady=10)

        
        self.display_frame = tk.Frame(self.root, bg="#f5f5f5")
        self.display_frame.pack(pady=20)

        self.queue_label = tk.Label(
            self.display_frame, text="Queue: []", font=("Helvetica", 14), bg="#f5f5f5", fg="#333333"
        )
        self.queue_label.pack()

        self.tickets_label = tk.Label(
            self.display_frame, text="Issued Tickets: {}", font=("Helvetica", 14), bg="#f5f5f5", fg="#333333"
        )
        self.tickets_label.pack()

    def update_display(self):
        self.queue_label.config(text=f"Queue: {self.queue_system.display_queue()}")
        self.tickets_label.config(text=f"Issued Tickets: {self.queue_system.display_tickets()}")

    def add_customers(self):
        names = self.name_entry.get().split(",")
        names = [name.strip() for name in names if name.strip()]
        if not names:
            messagebox.showerror("Input Error", "Please enter at least one name.")
            return
        self.queue_system.add_customer(*names)
        self.update_display()
        self.name_entry.delete(0, tk.END)

    def issue_all_tickets(self):
        if not self.queue_system.queue:
            messagebox.showinfo("No Customers", "No customers in the queue to issue tickets.")
            return
        self.queue_system.issue_all_tickets()
        self.update_display()

    def cancel_ticket(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("Input Error", "Please enter a name to cancel.")
            return
        try:
            self.queue_system.cancel_ticket(name)
            self.update_display()
        except ValueError as e:
            messagebox.showerror("Cancel Error", str(e))
        self.name_entry.delete(0, tk.END)



if __name__ == "__main__":
    root = tk.Tk()
    app = TicketQueueGUI(root)
    root.mainloop()


