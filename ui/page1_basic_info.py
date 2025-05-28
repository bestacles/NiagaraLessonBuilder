import customtkinter as ctk
from tkinter import Frame
from tkcalendar import DateEntry

TITLE_FONT = ("Arial", 22, "bold")
LABEL_FONT = ("Arial", 16, "bold")
INPUT_FONT = ("Arial", 14)

# Subjects for dropdown menu
SUBJECT_OPTIONS = [
    "Geography",
    "Gym",
    "Health",
    "History",
    "Language",
    "Math",
    "Music/Drama/Art",
    "Religion",
    "Science",
    "Social Studies",
    "STEAM",
]

class Page1:
    def __init__(self, master, data_store, next_callback, save_callback):
        self.master = master
        self.data_store = data_store
        self.next_callback = next_callback
        self.save_callback = save_callback
        self.build_ui()

    def build_ui(self):
        # Main container
        self.content_frame = ctk.CTkFrame(self.master, fg_color="#f0f0f0", corner_radius=10)
        self.content_frame.pack(padx=20, pady=20)

        # Group 1: Name, Subject dropdown, Topic, Time Estimate, Student Count
        fields = [
            ("Your Name", "name", "entry"),
            ("Subject of Lesson", "subject", "dropdown"),
            ("Topic", "topic", "entry"),
            ("Time Estimate (e.g., 40-50 min)", "time_estimate", "entry"),
            ("Number of Students", "student_count", "entry"),
        ]
        for label_text, key, widget_type in fields:
            container = ctk.CTkFrame(self.content_frame, fg_color="white", corner_radius=8)
            container.pack(fill="x", padx=20, pady=8)
            ctk.CTkLabel(container, text=label_text, font=LABEL_FONT).pack(anchor="w", padx=10, pady=(6,0))

            if widget_type == "dropdown":
                dropdown = ctk.CTkOptionMenu(
                    container,
                    values=SUBJECT_OPTIONS,
                    width=300
                )
                # Set previous value or default placeholder
                current = self.data_store.get(key, "Select Subject").strip()
                dropdown.set(current if current in SUBJECT_OPTIONS else "Select Subject")
                dropdown.pack(padx=10, pady=(4,10))
                setattr(self, f"{key}_dropdown", dropdown)
            else:
                entry = ctk.CTkEntry(container, placeholder_text=label_text, font=INPUT_FONT, width=300)
                entry.insert(0, self.data_store.get(key, "").strip())
                entry.pack(padx=10, pady=(4,10))
                setattr(self, f"{key}_entry", entry)

        # Grade & Date side-by-side
        duo_frame = ctk.CTkFrame(self.content_frame, fg_color="#f0f0f0")
        duo_frame.pack(fill="x", padx=20, pady=12)

        # Grade dropdown
        grade_frame = ctk.CTkFrame(duo_frame, fg_color="white", corner_radius=8)
        grade_frame.pack(side="left", expand=True, fill="both", padx=(0,10))
        ctk.CTkLabel(grade_frame, text="Select Grade", font=LABEL_FONT).pack(anchor="w", padx=10, pady=(6,0))
        self.grade_dropdown = ctk.CTkOptionMenu(
            grade_frame,
            values=[f"Grade {i}" for i in range(1, 9)],
            width=180
        )
        self.grade_dropdown.set(self.data_store.get("grade", "Select Grade").strip())
        self.grade_dropdown.pack(padx=10, pady=(4,10))

        # Date picker
        date_frame = ctk.CTkFrame(duo_frame, fg_color="white", corner_radius=8)
        date_frame.pack(side="left", expand=True, fill="both", padx=(10,0))
        ctk.CTkLabel(date_frame, text="Select Date", font=LABEL_FONT).pack(anchor="w", padx=10, pady=(6,0))
        picker_wrapper = ctk.CTkFrame(date_frame, fg_color="#e0e0e0", corner_radius=6)
        picker_wrapper.pack(padx=10, pady=(4,10))
        self.date_picker = DateEntry(
            picker_wrapper,
            font=INPUT_FONT,
            borderwidth=0,
            background="white",
            foreground="#333333",
            date_pattern="y-mm-dd",
            width=12
        )
        self.date_picker.pack(padx=6, pady=6)
        default_date = self.data_store.get("date", "").strip()
        if default_date:
            try:
                self.date_picker.set_date(default_date)
            except Exception:
                pass

    def save_and_continue(self):
        # Collect inputs
        new_data = {
            "name": self.name_entry.get().strip(),
            # Use dropdown value for subject
            "subject": self.subject_dropdown.get(),
            "topic": self.topic_entry.get().strip(),
            "time_estimate": self.time_estimate_entry.get().strip(),
            "student_count": self.student_count_entry.get().strip(),
            "grade": self.grade_dropdown.get(),
            "date": self.date_picker.get(),
        }
        self.data_store.update(new_data)
        self.save_callback()  # Centralized save
        print("[Page 1] Saved and sent to trigger_save:", self.data_store)
        self.next_callback()
