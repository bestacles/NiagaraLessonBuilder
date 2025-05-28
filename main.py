# main.py (with enhanced Help modal behavior)
import json
import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
from ui.page1_basic_info import Page1
from ui.page2_learning_outcomes import Page2
from ui.page3_preparation import Page3
from ui.page4_body_lesson import Page4
from ui.page5_accommodations import Page5
from ui.page6_closure import Page6
from ui.page7_assessment import Page7
from ui.page8_appendix import Page8
from ui.page9_review import Page9
from ui.navigation_bar import NavBar
from document_generator import LessonPlanDocGenerator

SAVE_FILE = "lesson_draft.json"

ctk.set_appearance_mode("System")  # use system theme

class LessonPlanApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Niagara Lesson Plan Builder")
        self.geometry("1440x960")
        self._in_navigation = False

        # Load existing draft if present
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, 'r') as f:
                    self.lesson_data = json.load(f)
                print("📂 Draft loaded successfully.")
            except Exception as e:
                messagebox.showerror("Load Error", f"Could not load draft: {e}")
                self.lesson_data = {}
        else:
            print("🟡 No draft found — starting fresh.")
            self.lesson_data = {}

        self.total_pages = 9
        self.current_page = 1
        self.page_titles = {
            1: ("Step 1 of 9", "Basic Information"),
            2: ("Step 2 of 9", "Learning Outcomes"),
            3: ("Step 3 of 9", "Preparation"),
            4: ("Step 4 of 9", "Body of the Lesson"),
            5: ("Step 5 of 9", "Accommodations"),
            6: ("Step 6 of 9", "Closure"),
            7: ("Step 7 of 9", "Assessment"),
            8: ("Step 8 of 9", "Appendix & References"),
            9: ("Step 9 of 9", "Review & Export"),
        }

        # Top bar
        self.top_bar = ctk.CTkFrame(self)
        self.top_bar.pack(padx=20, pady=(20, 0), fill="x")
        self.step_label = ctk.CTkLabel(self.top_bar, font=("Arial", 18, "bold"))
        self.step_label.pack(side="left", padx=10, pady=10)
        self.page_title_label = ctk.CTkLabel(self.top_bar, font=("Arial", 16, "bold"))
        self.page_title_label.pack(side="left", padx=10)
        # Help button
        help_btn = ctk.CTkButton(
            self.top_bar,
            text="❔",
            width=30,
            height=30,
            font=("Arial", 14, "bold"),
            command=self.show_help
        )
        help_btn.pack(side="right", padx=10, pady=10)

        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(self, height=10)
        self.progress_bar.pack(fill="x", padx=20)

        # Navigation bar
        self.nav_bar = NavBar(
            master=self,
            on_back=self.safe_previous_page,
            on_next=self.safe_next_page,
            on_save=self.save_draft_as,
            on_import=self.import_draft,
            on_export=self.export_plan,
        )
        self.nav_bar.frame.pack(padx=20, pady=(10, 0), fill="x")

        # Scrollable area
        self.canvas = ctk.CTkCanvas(self, borderwidth=0, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True, padx=20, pady=(10, 20))
        self.scroll_frame = ctk.CTkFrame(self.canvas)
        self.scroll_frame.grid_columnconfigure(0, weight=1)
        self.scroll_window = self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(self.scroll_window, width=e.width))
        self.v_scroll = ctk.CTkScrollbar(self, orientation="vertical", command=self.canvas.yview)
        self.v_scroll.place(relx=1.0, rely=0, relheight=1.0, anchor="ne")
        self.canvas.configure(yscrollcommand=self.v_scroll.set)
        self.scroll_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        # Initialize pages
        self.pages = {}
        frame1 = ctk.CTkFrame(self.scroll_frame)
        page1 = Page1(frame1, self.lesson_data, self.safe_next_page, self.trigger_save)
        self.pages[1] = (frame1, page1)
        for idx, cls in {2: Page2, 3: Page3, 4: Page4, 5: Page5, 6: Page6, 7: Page7, 8: Page8, 9: Page9}.items():
            frm = ctk.CTkFrame(self.scroll_frame)
            inst = cls(frm, self.lesson_data, self.safe_next_page, self.safe_previous_page, self.trigger_save)
            self.pages[idx] = (frm, inst)
        for frm, _ in self.pages.values():
            frm.pack_forget()
        self.show_page(self.current_page)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def show_page(self, num):
        for frm, _ in self.pages.values():
            frm.pack_forget()
        frm, _ = self.pages[num]
        frm.pack(fill="both", expand=True)
        step, title = self.page_titles[num]
        self.step_label.configure(text=step)
        self.page_title_label.configure(text=title)
        self.progress_bar.set(num / self.total_pages)
        self.canvas.yview_moveto(0)

    def safe_next_page(self):
        if getattr(self, '_in_navigation', False): return
        self._in_navigation = True
        frm, inst = self.pages[self.current_page]
        if hasattr(inst, 'save_and_continue'): inst.save_and_continue()
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.show_page(self.current_page)
        self._in_navigation = False

    def safe_previous_page(self):
        if getattr(self, '_in_navigation', False): return
        self._in_navigation = True
        frm, inst = self.pages[self.current_page]
        if hasattr(inst, 'save_and_continue'): inst.save_and_continue()
        if self.current_page > 1:
            self.current_page -= 1
            self.show_page(self.current_page)
        self._in_navigation = False

    def save_draft(self):
        """Auto-save to default path without dialog."""
        try:
            with open(SAVE_FILE, 'w') as f:
                json.dump(self.lesson_data, f, indent=4)
            print("💾 Draft auto-saved")
        except Exception as e:
            print("❌ Auto-save failed:", e)

    def save_draft_as(self):
        """Prompts Save As for draft JSON file."""
        path = filedialog.asksaveasfilename(defaultextension='.json', filetypes=[('JSON','*.json')], initialfile=SAVE_FILE)
        if not path: return
        try:
            with open(path, 'w') as f:
                json.dump(self.lesson_data, f, indent=4)
            print("💾 Draft saved to", path)
        except Exception as e:
            messagebox.showerror("Save Error", f"Could not save draft: {e}")

    def import_draft(self):
        path = filedialog.askopenfilename(filetypes=[('JSON','*.json')])
        if not path: return
        try:
            with open(path, 'r') as f:
                self.lesson_data = json.load(f)
            print("📂 Draft imported from", path)
            self.show_page(1)
        except Exception as e:
            messagebox.showerror("Load Error", f"Could not import draft: {e}")

    def trigger_save(self):
        self.save_draft()

    def export_plan(self):
        """Save As dialog for Word export."""
        self.save_draft()
        date = self.lesson_data.get('date','')
        subj = self.lesson_data.get('subject','').replace(' ','_')
        default = f"Lesson_{date}_{subj}.docx"
        path = filedialog.asksaveasfilename(defaultextension='.docx', filetypes=[('Word','*.docx')], initialfile=default)
        if not path: return
        try:
            LessonPlanDocGenerator(self.lesson_data).generate_docx(path)
            print("✅ Exported to", path)
        except Exception as e:
            messagebox.showerror("Export Error", f"Could not export: {e}")

    def show_help(self):
        """Display a modal Help & Tips window."""
        help_win = ctk.CTkToplevel(self)
        help_win.title("Help & Tips")
        help_win.transient(self)
        help_win.grab_set()
        help_win.geometry("500x550")
        frm = ctk.CTkFrame(help_win, fg_color="#f0f0f0")
        frm.pack(fill="both", expand=True, padx=20, pady=20)

        # Key Tips
        header = ctk.CTkLabel(frm, text="Key Tips:", font=("Arial", 14, "bold"))
        header.pack(anchor="w", pady=(0,5))
        tips = [
            "Enter each bullet or step on its own line.",
            "Indent sub‑bullets by pressing space ↑↑ (double-space) at start of line.",
            "Blank sections auto‑omit from export.",
        ]
        for tip in tips:
            lbl = ctk.CTkLabel(frm, text=f"• {tip}", font=("Arial", 12))
            lbl.pack(anchor="w", padx=(20,0))

        # Features
        feat_h = ctk.CTkLabel(frm, text="Features:", font=("Arial", 14, "bold"))
        feat_h.pack(anchor="w", pady=(10,5))
        feats = [
            "Auto‑save when navigating pages.",
            "Save As & Import Draft functionality.",
            "Export to Word (.docx) with formatted bullets.",
            "Appendix file uploads & APA refs.",
        ]
        for fitem in feats:
            lbl = ctk.CTkLabel(frm, text=f"• {fitem}", font=("Arial", 12))
            lbl.pack(anchor="w", padx=(20,0))

        # Usage
        use_h = ctk.CTkLabel(frm, text="Usage:", font=("Arial", 14, "bold"))
        use_h.pack(anchor="w", pady=(10,5))
        usage = [
            "Complete each section with Next/Back.",
            "Use Save Draft to name a JSON file.",
            "Use Import Draft to reload an existing draft.",
            "Click Export to generate the final .docx.",
            "Access this help anytime via the ❔ button.",
        ]
        for idx, u in enumerate(usage, start=1):
            lbl = ctk.CTkLabel(frm, text=f"{idx}. {u}", font=("Arial", 12))
            lbl.pack(anchor="w", padx=(20,0))

        ok_btn = ctk.CTkButton(frm, text="OK", width=80, command=help_win.destroy)
        ok_btn.pack(side="bottom", pady=(20,0))

if __name__ == "__main__":
    app = LessonPlanApp()
    app.mainloop()