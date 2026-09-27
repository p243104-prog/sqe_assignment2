```python
"""
Shared helper for sales and purchase dialogs.
"""

import tkinter as tk
from tkinter import ttk, messagebox


class TransactionDialog:
    """Base helper for common transaction dialog functionality."""

    def __init__(
        self,
        parent,
        controller,
        product_controller,
        auth_controller,
        callback=None
    ):
        self.controller = controller
        self.product_controller = product_controller
        self.auth_controller = auth_controller
        self.callback = callback

        self.dialog = tk.Toplevel(parent)
        self.dialog.transient(parent)
        self.dialog.grab_set()

    def setup_product_combo(
        self,
        parent_frame,
        include_stock=False
    ):
        """Create and configure the product selection combobox."""

        self.product_var = tk.StringVar()

        products = self.product_controller.get_all_products()

        if include_stock:
            product_values = [
                f"{p['product_id']} - {p['product_name']} "
                f"(Stock: {p['quantity_in_stock']})"
                for p in products
            ]
        else:
            product_values = [
                f"{p['product_id']} - {p['product_name']}"
                for p in products
            ]

        self.product_combo = ttk.Combobox(
            parent_frame,
            textvariable=self.product_var,
            values=product_values,
            width=45,
            state='readonly'
        )

        self.product_combo.grid(
            row=0,
            column=1,
            pady=5
        )

        if product_values:
            self.product_combo.current(0)

        self.product_combo.bind(
            '<<ComboboxSelected>>',
            self.on_product_selected
        )

    def get_selected_product(self):
        """Return the currently selected product."""

        product_str = self.product_var.get()

        if not product_str:
            return None

        product_id = int(product_str.split(' - ')[0])

        return self.product_controller.get_product(product_id)

    def finish_save(self, success, result, success_message):
        """Handle the common result of saving a transaction."""

        if success:
            messagebox.showinfo("Success", success_message)
            self.dialog.destroy()

            if self.callback:
                self.callback()
        else:
            messagebox.showerror("Error", result)
```
