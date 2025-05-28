import customtkinter as ctk

TITLE_FONT = ("Arial", 22, "bold")
LABEL_FONT = ("Arial", 16, "bold")
INPUT_FONT = ("Arial", 14)

class Page6:
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

        self.closure = self._create_card_textbox(
            title="Closure:",
            key="closure",
            initial=self.data_store.get("closure", ""),
            height=250,
            description="Briefly describe the review or wrap-up activity.\n\nExample:\nStudents share one new thing they learned or complete a short exit ticket."
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

        box = ctk.CTkTextbox(card, height=height, font=INPUT_FONT, corner_radius=6)
        box.pack(fill="both", padx=10, pady=(0, 10))

        if initial and initial.strip():
            box.insert("1.0", initial.strip())

        return box

    def save_and_continue(self):
        self.data_store["closure"] = self.closure.get("1.0", "end").strip()
        self.save_callback()
        print("[Page 6] Saved and sent to trigger_save:", self.data_store)
        self.next_callback()

    def go_back(self):
        self.back_callback()
