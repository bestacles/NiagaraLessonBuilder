import customtkinter as ctk

TITLE_FONT = ("Arial", 22, "bold")
LABEL_FONT = ("Arial", 16, "bold")
INPUT_FONT = ("Arial", 14)

class Page5:
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

        self.struggle_1 = self._create_card_textbox(
            title="Struggling Students – Accommodation 1:",
            key="struggle_1",
            initial=self.data_store.get("struggle_1", ""),
            height=120,
            description="Provide one support strategy to help students who need more guidance. Leave empty if not applicable. \n\nExample: Offer graphic organizers for writing responses."
        )
        self.struggle_2 = self._create_card_textbox(
            title="Struggling Students – Accommodation 2:",
            key="struggle_2",
            initial=self.data_store.get("struggle_2", ""),
            height=120,
            description="List an additional support that helps reinforce learning. Leave empty if not applicable.\n\nExample: Use visual aids or manipulatives."
        )

        self.ell_1 = self._create_card_textbox(
            title="Language Learners – Accommodation 1:",
            key="ell_1",
            initial=self.data_store.get("ell_1", ""),
            height=120,
            description="Support language needs and build vocabulary. Leave empty if not applicable. \n\nExample: Pair with a peer for structured conversations."
        )
        self.ell_2 = self._create_card_textbox(
            title="Language Learners – Accommodation 2:",
            key="ell_2",
            initial=self.data_store.get("ell_2", ""),
            height=120,
            description="Provide sentence frames or visuals to support comprehension. Leave empty if not applicable.\n\nExample: I can help by..."
        )

        self.gifted_1 = self._create_card_textbox(
            title="Gifted & Talented Students – Accommodation 1:",
            key="gifted_1",
            initial=self.data_store.get("gifted_1", ""),
            height=120,
            description="Add challenge or complexity to keep advanced learners engaged. Leave empty if not applicable. \n\nExample: Encourage students to design their own experiment."
        )
        self.gifted_2 = self._create_card_textbox(
            title="Gifted & Talented Students – Accommodation 2:",
            key="gifted_2",
            initial=self.data_store.get("gifted_2", ""),
            height=120,
            description="Provide opportunities for leadership, research, or independent exploration. Leave empty if not applicable."
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
            "struggle_1": self.struggle_1.get("1.0", "end").strip(),
            "struggle_2": self.struggle_2.get("1.0", "end").strip(),
            "ell_1": self.ell_1.get("1.0", "end").strip(),
            "ell_2": self.ell_2.get("1.0", "end").strip(),
            "gifted_1": self.gifted_1.get("1.0", "end").strip(),
            "gifted_2": self.gifted_2.get("1.0", "end").strip(),
        })
        self.save_callback()
        print("[Page 5] Saved and sent to trigger_save:", self.data_store)
        self.next_callback()

    def go_back(self):
        self.back_callback()
