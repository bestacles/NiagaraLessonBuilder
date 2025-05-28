# ui/page9_review.py

import customtkinter as ctk

TITLE_FONT = ("Arial", 22, "bold")
LABEL_FONT = ("Arial", 16, "bold")
DESC_FONT = ("Arial", 12, "italic")

# Define the display order and friendly names for preview
PREVIEW_FIELDS = [
    ("name", "Name"),
    ("date", "Date"),
    ("subject", "Subject of Lesson"),
    ("grade", "Grade Level"),
    ("topic", "Topic"),
    ("time_estimate", "Time Estimate"),
]
MULTILINE_FIELDS = [
    ("learning_objectives", "Student Learning Objectives"),
    ("i_can_statements", "I can… Statements"),
    ("curriculum_expectations", "Curriculum Expectations"),
    ("student_materials", "Student Materials"),
    ("teacher_materials", "Teacher Materials"),
    ("prior_knowledge", "Prior Knowledge"),
    ("prep_ahead", "Need to Do Ahead of Time"),
    ("anticipatory", "Anticipatory Set / Opening"),
    ("mini_lesson", "Mini Lesson"),
    ("activity_1", "Activity #1"),
    ("activity_2", "Activity #2"),
    ("activity_3", "Activity #3"),
    ("technology", "Technology Integration"),
    ("unfinished", "Unfinished Work / Homework"),
    ("alt_plan", "Alternative Plan"),
    ("struggle_1", "Struggling Students – Accom. 1"),
    ("struggle_2", "Struggling Students – Accom. 2"),
    ("ell_1", "Language Learners – Accom. 1"),
    ("ell_2", "Language Learners – Accom. 2"),
    ("gifted_1", "Gifted & Talented – Accom. 1"),
    ("gifted_2", "Gifted & Talented – Accom. 2"),
    ("closure", "Closure"),
    ("formal_assessment", "Formal Assessment"),
    ("informal_assessment", "Informal Assessment"),
    ("apa_references", "APA References"),
]

class Page9:
    def __init__(self, master, data_store, next_callback, back_callback, save_callback):
        self.master = master
        self.data_store = data_store
        self.next_callback = next_callback
        self.back_callback = back_callback
        self.save_callback = save_callback
        self.build_ui()

    def build_ui(self):
        self.content_frame = ctk.CTkFrame(
            self.master, fg_color="#f0f0f0", corner_radius=10
        )
        self.content_frame.pack(padx=20, pady=20, fill="both", expand=True)

        card = ctk.CTkFrame(self.content_frame, fg_color="white", corner_radius=8)
        card.pack(fill="both", padx=20, pady=12)

        # Title
        ctk.CTkLabel(
            card,
            text="Review & Export",
            font=TITLE_FONT
        ).pack(anchor="center", pady=(12, 6))

        # Description
        ctk.CTkLabel(
            card,
            text=(
                "Look over your draft below. If everything looks good, "
                "click Export to save your lesson plan."
            ),
            font=DESC_FONT,
            text_color="gray",
            anchor="w",
            justify="left"
        ).pack(anchor="w", padx=12, pady=(0, 12), fill="x")

        # Preview textbox
        summary = ctk.CTkTextbox(
            card,
            height=600,
            corner_radius=6,
            font=("Arial", 12),
            wrap="word"
        )
        summary.pack(fill="both", padx=10, pady=(0, 10))

        # Populate preview
        summary.configure(state="normal")
        # Single-line fields
        for key, label in PREVIEW_FIELDS:
            val = self.data_store.get(key, "")
            summary.insert("end", f"{label}: {val}\n")
        summary.insert("end", "\n")
        # Multiline fields
        for key, label in MULTILINE_FIELDS:
            val = self.data_store.get(key, "").strip()
            summary.insert("end", f"{label}:\n",
                           )
            if val:
                for line in val.splitlines():
                    summary.insert("end", f"    {line}\n")
            else:
                summary.insert("end", "    (no entry)\n")
            summary.insert("end", "\n")
        summary.configure(state="disabled")

    def save_and_continue(self):
        self.save_callback()
        self.next_callback()

    def go_back(self):
        self.back_callback()