import customtkinter as ctk

TITLE_FONT = ("Arial", 22, "bold")
LABEL_FONT = ("Arial", 16, "bold")
INPUT_FONT = ("Arial", 14)

class Page4:
    def __init__(self, master, data_store, next_callback, back_callback, save_callback):
        self.master = master
        self.data_store = data_store
        self.next_callback = next_callback
        self.back_callback = back_callback
        self.save_callback = save_callback
        self.build_ui()

    def build_ui(self):
        self.content_frame = ctk.CTkFrame(self.master, fg_color="#f0f0f0", corner_radius=10)
        self.content_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # A. Anticipatory Set / Opening
        self.anticipatory = self._create_card_textbox(
            title="A. Anticipatory Set / Opening:",
            key="anticipatory",
            initial=self.data_store.get("anticipatory", ""),
            height=180,
            description=(
                "Describe how you'll hook student interest or connect to prior knowledge.\n"
                "Enter each step or prompt on its own line; each line will appear as a bullet in the document.\n\n"
                "Example:\n"
                "- Ask students to brainstorm what they know about 24-hour time."
            )
        )

        # B. Mini Lesson (Direct Instruction)
        self.activity_1 = self._create_card_textbox(
            title="B. Mini Lesson (Direct Instruction):",
            key="activity_1",
            initial=self.data_store.get("activity_1", ""),
            height=250,
            description=(
                "Write out your instruction or modeling script step-by-step.\n"
                "Each line becomes a bullet in the document.\n\n"
                "Example:\n"
                "- Show the analog clock and explain how to read hours and minutes."
            )
        )

        # C1. Guided Practice
        self.activity_2 = self._create_card_textbox(
            title="C1. Activity #1 (Guided Practice):",
            key="activity_2",
            initial=self.data_store.get("activity_2", ""),
            height=250,
            description=(
                "Detail steps students follow with support.\n"
                "Enter each direction as a separate line.\n\n"
                "Example:\n"
                "- In pairs, students measure angles with protractors and discuss."
            )
        )

        # C2. Independent/Formal Assessment
        self.activity_3 = self._create_card_textbox(
            title="C2. Activity #2 (Independent/Formal Assessment):",
            key="activity_3",
            initial=self.data_store.get("activity_3", ""),
            height=250,
            description=(
                "Describe the assessment tasks and instructions verbatim.\n"
                "List each instruction on its own line.\n\n"
                "Example:\n"
                "- Complete the exit slip: measure three angles and label acute, right, or obtuse."
            )
        )

        # D. Technology Integration
        self.technology = self._create_card_textbox(
            title="D. Technology Integration:",
            key="technology",
            initial=self.data_store.get("technology", ""),
            height=150,
            description=(
                "Explain how technology supports the lesson.\n"
                "Enter each tool or step as a bullet.\n\n"
                "Example:\n"
                "- Use an interactive whiteboard timer to pace practice."
            )
        )

        # E. Unfinished Work / Homework
        self.unfinished = self._create_card_textbox(
            title="E. Unfinished Work / Homework:",
            key="unfinished",
            initial=self.data_store.get("unfinished", ""),
            height=150,
            description=(
                "Specify tasks students will finish later or practice at home.\n"
                "Each item on its own line will be bulleted.\n\n"
                "Example:\n"
                "- Finish the angle worksheet and review flashcards."
            )
        )

        # F. Alternative Plan
        self.alt_plan = self._create_card_textbox(
            title="F. Alternative Plan:",
            key="alt_plan",
            initial=self.data_store.get("alt_plan", ""),
            height=150,
            description=(
                "Describe backup steps in case of tech or time issues.\n"
                "List each contingency on a separate line.\n\n"
                "Example:\n"
                "- Prepare printed protractor cut-outs if software fails."
            )
        )

    def _create_card_textbox(self, title: str, key: str, initial: str, height: int, description: str = "") -> ctk.CTkTextbox:
        card = ctk.CTkFrame(self.content_frame, fg_color="white", corner_radius=8)
        card.pack(fill="both", padx=20, pady=12)

        ctk.CTkLabel(card, text=title, font=LABEL_FONT).pack(anchor="w", padx=10, pady=(10, 4))

        if description:
            ctk.CTkLabel(
                card,
                text=description,
                font=("Arial", 12, "italic"),
                text_color="gray",
                anchor="w",
                justify="left"
            ).pack(anchor="w", padx=12, pady=(0, 10), fill="x")

        box = ctk.CTkTextbox(card, height=height, font=INPUT_FONT, corner_radius=6)
        box.pack(fill="both", padx=10, pady=(0, 10))

        if initial and initial.strip():
            box.insert("1.0", initial.strip())

        setattr(self, f"_{key}_box", box)
        return box

    def save_and_continue(self):
        keys = ["anticipatory", "activity_1", "activity_2", "activity_3", "technology", "unfinished", "alt_plan"]
        for key in keys:
            box = getattr(self, f"_{key}_box")
            self.data_store[key] = box.get("1.0", "end").strip()

        self.save_callback()
        self.next_callback()

    def go_back(self):
        self.back_callback()
