import customtkinter as ctk

TITLE_FONT = ("Arial", 22, "bold")
LABEL_FONT = ("Arial", 16, "bold")
INPUT_FONT = ("Arial", 14)

class Page2:
    def __init__(self, master, data_store, next_callback, back_callback, save_callback):
        self.master = master
        self.data_store = data_store
        self.next_callback = next_callback
        self.back_callback = back_callback
        self.save_callback = save_callback
        self.build_ui()

    def build_ui(self):
        # Main container
        self.content_frame = ctk.CTkFrame(self.master, fg_color="#f0f0f0", corner_radius=10)
        self.content_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Student Learning Objectives
        self.objectives = self._create_list_textbox(
            title="Student Learning Objectives (SLOs):",
            key="learning_objectives",
            height=120,
            description=(
                "Use action verbs to define what students will learn.\n"
                "Write each objective on its own line.\n\n"
                "Example:\n"
                "By the end of this lesson, students will be able to identify and classify angles (acute, right, and obtuse) by examining everyday objects and images, demonstrating their understanding verbally and on a worksheet with at least 80% accuracy."
            )
        )

        # “I can…” Statements
        self.icans = self._create_list_textbox(
            title="“I can…” Statements:",
            key="i_can_statements",
            height=120,
            description=(
                "Write from the student’s perspective using measurable language.\n"
                "List each statement on a new line.\n\n"
                "Example:\n"
                "I can describe my community.\n"
                "I can explain what a rural area is."
            )
        )

        # Curriculum Expectations
        self.curriculum = self._create_list_textbox(
            title="Ontario Curriculum Expectations:",
            key="curriculum_expectations",
            height=120,
            description=(
                "Paste curriculum expectations from the Ontario Curriculum here.\n"
                "Write each expectation on a separate line.\n\n"
                "Example:\n"
                "B1.1: Identify key characteristics of urban and rural communities."
            )
        )

    def _create_list_textbox(self, title: str, key: str, height: int = 100, description: str = ""):
        card = ctk.CTkFrame(self.content_frame, fg_color="white", corner_radius=8)
        card.pack(fill="both", padx=20, pady=12)

        # Title
        ctk.CTkLabel(card, text=title, font=LABEL_FONT).pack(anchor="w", padx=10, pady=(10, 4))

        # Description
        if description:
            ctk.CTkLabel(
                card,
                text=description,
                font=("Arial", 12, "italic"),
                text_color="gray",
                anchor="w",
                justify="left"
            ).pack(anchor="w", padx=12, pady=(0, 10), fill="x")

        # Textbox
        box = ctk.CTkTextbox(card, height=height, font=INPUT_FONT, corner_radius=6)
        box.pack(fill="both", padx=10, pady=(0, 10))

        # Load saved text
        initial = self.data_store.get(key, "").strip()
        if initial:
            box.insert("1.0", initial)

        return box

    def save_and_continue(self):
        self.data_store["learning_objectives"] = self.objectives.get("1.0", "end-1c")
        self.data_store["i_can_statements"] = self.icans.get("1.0", "end-1c")
        self.data_store["curriculum_expectations"] = self.curriculum.get("1.0", "end-1c")
        self.save_callback()
        print("[Page 2] Saved and sent to trigger_save:", self.data_store)
        self.next_callback()

    def go_back(self):
        self.back_callback()
