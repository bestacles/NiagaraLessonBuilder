import customtkinter as ctk

TITLE_FONT = ("Arial", 22, "bold")
LABEL_FONT = ("Arial", 16, "bold")
INPUT_FONT = ("Arial", 14)

class Page3:
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

        self.student_materials = self._create_card_textbox(
            title="Student Materials:",
            key="student_materials",
            initial=self.data_store.get("student_materials", ""),
            height=100,
            description="List materials students will use (one item per line).\n\nExample:\n- Scissors\n- Glue stick\n- Chart paper"
        )

        self.teacher_materials = self._create_card_textbox(
            title="Teacher Materials:",
            key="teacher_materials",
            initial=self.data_store.get("teacher_materials", ""),
            height=100,
            description="List materials the teacher will prepare or use.\n\nExample:\n- Whiteboard markers\n- Assessment rubrics"
        )

        self.prior_knowledge = self._create_card_textbox(
            title="Prior Knowledge:",
            key="prior_knowledge",
            initial=self.data_store.get("prior_knowledge", ""),
            height=100,
            description="Write at least 2 things students should already understand.\n\nExample:\n- Students know what a map is.\n- Students can use cardinal directions."
        )

        self.prep_ahead = self._create_card_textbox(
            title="Need to Do Ahead of Time:",
            key="prep_ahead",
            initial=self.data_store.get("prep_ahead", ""),
            height=100,
            description="List tasks to be completed before the lesson.\n\nExample:\n- Print worksheets\n- Set up projector"
        )

    def _create_card_textbox(self, title: str, key: str, initial: str, height: int, description: str = "") -> ctk.CTkTextbox:
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

        # Textbox input
        box = ctk.CTkTextbox(card, height=height, font=INPUT_FONT, corner_radius=6)
        box.pack(fill="both", padx=10, pady=(0, 10))

        if initial and initial.strip():
            box.insert("1.0", initial.strip())
        return box

    def save_and_continue(self):
        self.data_store["student_materials"] = self.student_materials.get("1.0", "end").strip()
        self.data_store["teacher_materials"] = self.teacher_materials.get("1.0", "end").strip()
        self.data_store["prior_knowledge"] = self.prior_knowledge.get("1.0", "end").strip()
        self.data_store["prep_ahead"] = self.prep_ahead.get("1.0", "end").strip()
        self.save_callback()
        print("[Page 3] Saved and sent to trigger_save:", self.data_store)
        self.next_callback()

    def go_back(self):
        self.back_callback()
