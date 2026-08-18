#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# PyEngine Architect M3 - Dynamic Refactored Module
# ------------------------------------------------------------------

            if "if __name__" in line and "__main__" in line:
                in_main_block = True

            # Dinamik Kategorizasyon
            if constant_pattern.match(line):
                modules["config"].append(line)
            elif in_main_block:
                modules["main"].append(line)
            elif any(
                ui_kw in line
                for ui_kw in [
                    "ctk.",
                    "tk.",
                    "QtWidgets",
                    "QMainWindow",
                    "Button",
                    "Label",
                    "Frame",
                ]
            ):
                modules["gui"].append(line)
            elif line.startswith("class "):
                modules["models"].append(line)
            elif line.startswith("def "):
                modules["utils"].append(line)
            else:
                if not in_main_block:
                    modules["utils"].append(line)

        if not modules["main"]:
            modules["main"].append(
                "if __name__ == '__main__':\n    print('PyEngine Architect App Running!')"
            )

        return modules, requirements


if __name__ == "__main__":
    app = PyEngineArchitectM3()
    app.mainloop()