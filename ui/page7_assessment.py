import customtkinter as ctk

TITLE_FONT = ("Arial", 22, "bold")
LABEL_FONT = ("Arial", 16, "bold")
INPUT_FONT = ("Arial", 14)

class Page7:
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

        self.formal = self._create_card_textbox(
            title="Formal Assessment:",
            key="formal_assessment",
            initial=self.data_store.get("formal_assessment", ""),
            height=120,
            description="Describe any summative assessment and its purpose.\n\nExample:\nStudents complete a quiz or submit a final project based on the learning outcomes."
        )

        self.informal = self._create_card_textbox(
            title="Informal Assessment:",
            key="informal_assessment",
            initial=self.data_store.get("informal_assessment", ""),
            height=120,
            description="Describe how you'll monitor any learning during the lesson.\n\nExample:\nObserve group discussions or check exit slips for understanding."
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

        return box

    def save_and_continue(self):
        self.data_store.update({
            "formal_assessment": self.formal.get("1.0", "end").strip(),
            "informal_assessment": self.informal.get("1.0", "end").strip(),
        })
        self.save_callback()
        print("[Page 7] Saved and sent to trigger_save:", self.data_store)
        self.next_callback()

    def go_back(self):
        self.back_callback()
