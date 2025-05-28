import customtkinter as ctk
from tkinter import filedialog

TITLE_FONT = ("Arial", 22, "bold")
LABEL_FONT = ("Arial", 16, "bold")
INPUT_FONT = ("Arial", 14)

class Page8:
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

        # File upload section
        card = ctk.CTkFrame(self.content_frame, fg_color="white", corner_radius=8)
        card.pack(fill="both", padx=20, pady=12)

        ctk.CTkLabel(card, text="Appendix – Upload Files (Optional):", font=LABEL_FONT).pack(anchor="w", padx=10, pady=(10, 4))
        ctk.CTkLabel(
            card,
            text="Attach any worksheets, handouts, assessments, or visuals referenced in your plan.",
            font=("Arial", 12, "italic"),
            text_color="gray",
            anchor="w",
            justify="left"
        ).pack(anchor="w", padx=12, pady=(0, 10), fill="x")

        upload_btn = ctk.CTkButton(card, text="Choose Files...", command=self.pick_files, width=200)
        upload_btn.pack(padx=10, pady=(0, 4))

        self.files_list = ctk.CTkTextbox(card, height=80, corner_radius=6, font=INPUT_FONT)
        self.files_list.configure(state="disabled")
        self.files_list.pack(fill="both", padx=10, pady=(0, 10))

        paths = self.data_store.get("appendix_files", [])
        if paths:
            self._update_files_list(paths)

        # Optional: Appendix text/descriptions
        self.appendix_text = self._create_card_textbox(
            title="Appendix Descriptions (Optional):",
            key="appendix_text",
            initial=self.data_store.get("appendix_text", ""),
            height=100,
            description=(
                "Provide any notes, captions, or instructions related to your uploaded appendix files.\n"
                "Example:\n"
                "Worksheet 1: Steps for guided practice."
            )
        )

        # APA References section
        self.apa_references = self._create_card_textbox(
            title="APA References:",
            key="apa_references",
            initial=self.data_store.get("apa_references", ""),
            height=100,
            description=(
                "List sources used in lesson development. Follow APA formatting.\n\n"
                "Example:\n"
                "Ontario Ministry of Education. (2023). The Ontario Curriculum..."
            )
        )

    def pick_files(self):
        paths = filedialog.askopenfilenames()
        if paths:
            self.data_store["appendix_files"] = list(paths)
            self._update_files_list(paths)
            self.save_callback()

    def _update_files_list(self, paths):
        self.files_list.configure(state="normal")
        self.files_list.delete("1.0", "end")
        for p in paths:
            self.files_list.insert("end", p + "\n")
        self.files_list.configure(state="disabled")

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

        box = ctk.CTkTextbox(card, height=height, corner_radius=6, font=INPUT_FONT)
        box.pack(fill="both", padx=10, pady=(0, 10))

        if initial and initial.strip():
            box.insert("1.0", initial.strip())
        setattr(self, f"_{key}_box", box)
        return box

    def save_and_continue(self):
        # Save appendix text, APA references and persist uploads
        txt = getattr(self, "_appendix_text_box").get("1.0", "end").strip()
        self.data_store["appendix_text"] = txt
        refs = getattr(self, "_apa_references_box").get("1.0", "end").strip()
        self.data_store["apa_references"] = refs
        self.save_callback()
        print("[Page 8] Saved and sent to trigger_save:", self.data_store)
        self.next_callback()

    def go_back(self):
        self.back_callback()