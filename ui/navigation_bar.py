import customtkinter as ctk
from datetime import datetime

class NavBar:
    def __init__(
        self,
        master,
        on_back=None,
        on_next=None,
        on_save=None,
        on_import=None,
        on_export=None,
        show_back=True,
        show_next=True
    ):
        self.master = master
        self.on_back = on_back
        self.on_next = on_next
        self.on_save = on_save
        self.on_import = on_import
        self.on_export = on_export

        self.frame = ctk.CTkFrame(master)
        button_padding = {"padx": 12, "pady": 5}

        # Back Button
        if show_back and self.on_back:
            self.back_btn = ctk.CTkButton(
                self.frame,
                text="← Back",
                font=("Arial", 14, "bold"),
                command=self.handle_back
            )
            self.back_btn.pack(side="left", **button_padding)

        # Save Button
        if self.on_save:
            self.save_btn = ctk.CTkButton(
                self.frame,
                text="💾 Save Draft",
                font=("Arial", 14, "bold"),
                command=self.handle_save
            )
            self.save_btn.pack(side="left", **button_padding)

        # Import Button
        if self.on_import:
            self.import_btn = ctk.CTkButton(
                self.frame,
                text="📂 Load Draft",
                font=("Arial", 14, "bold"),
                command=self.handle_import
            )
            self.import_btn.pack(side="left", **button_padding)

        # Export Button
        if self.on_export:
            self.export_btn = ctk.CTkButton(
                self.frame,
                text="📤 Export",
                font=("Arial", 14, "bold"),
                command=self.handle_export
            )
            self.export_btn.pack(side="left", **button_padding)

        # Next Button
        if show_next and self.on_next:
            self.next_btn = ctk.CTkButton(
                self.frame,
                text="Next →",
                font=("Arial", 14, "bold"),
                command=self.handle_next
            )
            self.next_btn.pack(side="right", **button_padding)

        # Status Label
        self.status_label = ctk.CTkLabel(
            self.frame,
            text="",
            font=("Arial", 12, "bold"),
            text_color="gray"
        )
        self.status_label.pack(side="bottom", pady=(5, 0))

    def handle_save(self):
        if self.on_save:
            self.on_save()
            now = datetime.now().strftime("%H:%M:%S")
            self.status_label.configure(text=f"Last saved: {now}")

    def handle_import(self):
        if self.on_import:
            self.on_import()
            now = datetime.now().strftime("%H:%M:%S")
            self.status_label.configure(text=f"Draft loaded: {now}")

    def handle_export(self):
        if self.on_export:
            self.on_export()
            now = datetime.now().strftime("%H:%M:%S")
            self.status_label.configure(text=f"Exported: {now}")

    def handle_next(self):
        if self.on_next:
            self.on_next()

    def handle_back(self):
        if self.on_back:
            self.on_back()
