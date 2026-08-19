#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# PyEngine Architect M3 - Dynamic Refactored Module
# ------------------------------------------------------------------

import os
import re
import sys
import threading
import time
from tkinter import filedialog, messagebox

import customtkinter as ctk

# TkinterDnD2 entegrasyonu (Sürükle - Bırak desteği)
try:
    from tkinterdnd2 import DND_FILES, TkinterDnD


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.TkdndVersion = TkinterDnD._tkdnd_version(self)

except ImportError:



    def __init__(self):
        super().__init__()

        # --- Material 3 Expressive Koyu Tema Renk Paleti ---
        self.M3_BG = "#131318"  # Surface Container Lowest
        self.M3_SURFACE = "#1C1B20"  # Surface Container
        self.M3_SURFACE_HIGH = "#2B2930"  # Surface Container High
        self.M3_PRIMARY = "#D0BCFF"  # Primary Accent (Expressive Purple)
        self.M3_ON_PRIMARY = "#381E72"
        self.M3_SECONDARY = "#CCC2DC"  # Secondary Accent
        self.M3_TEXT = "#E6E1E5"  # On Surface Text
        self.M3_SUBTEXT = "#938F99"  # Outline / Subtext

        # --- Pencere Ayarları ---
        self.title("PyEngine Architect - Material 3 Expressive")
        self.geometry("720x620")
        self.resizable(False, False)

        self.configure(fg_color=self.M3_BG)

        self.selected_file_path = None
        self.is_processing = False

        self._build_ui()

    def _build_ui(self):
        # Header / Title Area
        header_frame.pack(padx=32, pady=(28, 12), fill="x")

            header_frame,
            text="⚡ PyEngine Architect",
            text_color=self.M3_PRIMARY,
        )
        title_label.pack(anchor="w")

            header_frame,
            text="Material 3 Expressive Otomatik Kod Parçalayıcı Engine",
            text_color=self.M3_SUBTEXT,
        )
        subtitle_label.pack(anchor="w", pady=(2, 0))

            self,
            fg_color=self.M3_SURFACE_HIGH,
            corner_radius=28,  # Extra rounded corners for M3 Expressive
            border_width=0,
        )
        self.drop_frame.pack(padx=32, pady=12, fill="x", ipady=20)

            self.drop_frame,
            text="📁",
            text_color=self.M3_PRIMARY,
        )
        self.drop_icon.pack(pady=(12, 4))

            self.drop_frame,
            text="Dosyayı buraya bırakın veya seçin",
            text_color=self.M3_TEXT,
        )
        self.drop_label.pack()

            self.drop_frame,
            text="Yüklendiği an otomatik olarak analiz edip parçalayacaktır",
            text_color=self.M3_SUBTEXT,
        )
        or_label.pack(pady=(2, 10))

            self.drop_frame,
            text="Dosya Seç",
            command=self.browse_file,
            fg_color=self.M3_PRIMARY,
            text_color=self.M3_ON_PRIMARY,
            hover_color=self.M3_SECONDARY,
            corner_radius=20,
        )
        self.select_btn.pack(pady=(0, 10))

        if hasattr(self, "drop_target_register"):
            self.drop_frame.drop_target_register(DND_FILES)
            self.drop_frame.dnd_bind("<<Drop>>", self.on_file_drop)

        # Progress / Indicator Zone
        self.progress_frame.pack(padx=32, pady=(4, 4), fill="x")

            self.progress_frame,
            text="",
            text_color=self.M3_PRIMARY,
        )

            self.progress_frame,
            orientation="horizontal",
            mode="indeterminate",
            height=6,
            corner_radius=3,
            progress_color=self.M3_PRIMARY,
            fg_color=self.M3_SURFACE,
        )

        # Log & Output Area
            self, fg_color=self.M3_SURFACE, corner_radius=20
        )
        log_frame.pack(padx=32, pady=12, fill="both", expand=True)

            log_frame,
            text="ANALİZ VE DÖNÜŞÜM LOGLARI",
            text_color=self.M3_SUBTEXT,
        )
        log_title.pack(anchor="w", padx=16, pady=(10, 4))

            log_frame,
            fg_color=self.M3_BG,
            text_color=self.M3_TEXT,
            corner_radius=12,
        )
        self.log_textbox.pack(
            padx=16, pady=(0, 16), fill="both", expand=True
        )

        self.log("PyEngine Architect M3 Hazır. Dosya bırakıldığında otomatik başlayacaktır...")

    def log(self, text):
        self.log_textbox.insert("end", f"> {text}\n")
        self.log_textbox.see("end")

    def browse_file(self):
        if self.is_processing:
            return
        file_path = filedialog.askopenfilename(
            filetypes=[("Python Files", "*.py *.pyw")]
        )
        if file_path:
            self.on_file_selected(file_path)

    def on_file_drop(self, event):
        if self.is_processing:
            return
        file_path = event.data.strip("{}")
        if file_path.endswith((".py", ".pyw")):
            self.on_file_selected(file_path)
        else:
            messagebox.showerror(
                "Hata", "Lütfen geçerli bir .py veya .pyw dosyası bırakın!"
            )

    def on_file_selected(self, path):
        """Dosya seçildiği/bırakıldığı an OTOMATİK çalışır."""
        self.selected_file_path = path
        filename = os.path.basename(path)
        self.drop_label.configure(
            text=f"İşleniyor: {filename}", text_color=self.M3_PRIMARY
        )
        self.log(f"Dosya algılandı: {filename}")

        # Otomatik işlemi başlat
        threading.Thread(target=self.process_refactoring, daemon=True).start()

    def show_loading_ui(self, is_loading, text=""):
        if is_loading:
            self.is_processing = True
            self.select_btn.configure(state="disabled")
            self.progress_status_label.configure(text=text)
            self.progress_status_label.pack(anchor="w", pady=(0, 4))
            self.progress_bar.pack(fill="x")
            self.progress_bar.start()
        else:
            self.is_processing = False
            self.progress_bar.stop()
            self.progress_bar.pack_forget()
            self.progress_status_label.pack_forget()
            self.select_btn.configure(state="normal")

    def process_refactoring(self):
        try:
            self.show_loading_ui(True, "⚡ Kod Yapısı İçeriğe Göre Analiz Ediliyor...")
            time.sleep(0.6)

            with open(
                self.selected_file_path, "r", encoding="utf-8", errors="ignore"
            ) as f:
                content = f.read()

            source_filename = os.path.basename(self.selected_file_path)
            base_name = os.path.splitext(source_filename)[0]

            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            if not os.path.exists(desktop_path):
                desktop_path = os.path.join(os.path.expanduser("~"), "Masaüstü")

            target_dir = os.path.join(desktop_path, f"{base_name}_architect_build")
            os.makedirs(target_dir, exist_ok=True)

            self.show_loading_ui(True, "🧠 Koda Göre Dinamik Modüller Oluşturuluyor...")
            time.sleep(0.5)

            # Akıllı Kod Bölme Mantığı
            modules, requirements = self._smart_split_code(content)

            gpl_header = (
                "#!/usr/bin/env python3\n"
                "# -*- coding: utf-8 -*-\n"
                "# ------------------------------------------------------------------\n"
                "# PyEngine Architect M3 - Dynamic Refactored Module\n"
                "# ------------------------------------------------------------------\n\n"
            )

            # Oluşturulan dinamik modülleri kaydet
            for mod_name, mod_lines in modules.items():
                if mod_lines:
                    file_path = os.path.join(target_dir, f"{mod_name}.py")
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(gpl_header + "\n".join(mod_lines))
                    self.log(f" [✓] {mod_name}.py oluşturuldu ({len(mod_lines)} satır).")

            # Requirements oluştur
            req_content = (
                "\n".join(sorted(list(requirements)))
                if requirements
                else "# Harici bağımlılık tespit edilmedi."
            )
            with open(
                os.path.join(target_dir, "requirements.txt"),
                "w",
                encoding="utf-8",
            ) as f:
                f.write(req_content)
            self.log(" [✓] requirements.txt oluşturuldu.")

            self.show_loading_ui(False)
            self.drop_label.configure(
                text="Dosyayı buraya bırakın veya seçin", text_color=self.M3_TEXT
            )
            self.log(f"\n✨ İşlem Bitti! Modüller Masaüstünde: {target_dir}")

            messagebox.showinfo(
                "Tamamlandı",
                f"Kod içeriğine göre dinamik olarak bölündü!\n\nKlasör: {target_dir}",
            )

        except Exception as e:
            self.show_loading_ui(False)
            self.log(f"⚠️ Hata: {str(e)}")
            messagebox.showerror("Hata", str(e))

    def _smart_split_code(self, source_code):
        """Kodu ezbere değil, içeriğindeki ifadelere göre dinamik modüllere böler."""
        lines = source_code.splitlines()

        modules = {
            "config": [],
            "gui": [],
            "models": [],
            "utils": [],
            "main": [],
        }

        requirements = set()
        import_pattern = re.compile(r"^\s*(?:import|from)\s+([a-zA-Z0-9_]+)")
        constant_pattern = re.compile(r"^[A-Z0-9_]{2,}\s*=")

        std_libs = {
            "os", "sys", "re", "math", "time", "datetime", "json", "random",
            "tkinter", "threading", "subprocess", "pathlib", "collections"
        }

        in_main_block = False

        for line in lines:
            # Bağımlılık Tespiti
            imp_match = import_pattern.match(line)
            if imp_match:
                mod_name = imp_match.group(1)
                if mod_name not in std_libs:
                    requirements.add(mod_name)
