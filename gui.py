#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# PyEngine Architect M3 - Dynamic Refactored Module
# ------------------------------------------------------------------

    class CTkDnD(ctk.CTk, TkinterDnD.DnDWrapper):
    CTkDnD = ctk.CTk
        ctk.set_appearance_mode("dark")
        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        title_label = ctk.CTkLabel(
            font=ctk.CTkFont(family="Roboto", size=28, weight="bold"),
        subtitle_label = ctk.CTkLabel(
            font=ctk.CTkFont(family="Roboto", size=13),
        # Drag & Drop Zone Frame (Material 3 Expressive Card Style)
        self.drop_frame = ctk.CTkFrame(
        self.drop_icon = ctk.CTkLabel(
            font=ctk.CTkFont(size=42),
        self.drop_label = ctk.CTkLabel(
            font=ctk.CTkFont(size=15, weight="bold"),
        or_label = ctk.CTkLabel(
            font=ctk.CTkFont(size=11),
        self.select_btn = ctk.CTkButton(
            font=ctk.CTkFont(size=13, weight="bold"),
        self.progress_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.progress_status_label = ctk.CTkLabel(
            font=ctk.CTkFont(size=12, weight="bold"),
        self.progress_bar = ctk.CTkProgressBar(
        log_frame = ctk.CTkFrame(
        log_title = ctk.CTkLabel(
            font=ctk.CTkFont(size=11, weight="bold"),
        self.log_textbox = ctk.CTkTextbox(
            font=ctk.CTkFont(family="Consolas", size=12),