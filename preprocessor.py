import os


class HTMLPreprocessor:
    def __init__(self, warnings: bool = True, pretty: bool = True, input_dir: str = "preprocessor", output_dir: str = "templates") -> None:
        self.input_dir = input_dir
        self.output_dir = output_dir

        self.warnings = warnings
        self.pretty = pretty

        self.indent_tags = ["html", "head", "body", "div", "script", "style", "form"]
        self.indent_spaces = 4

        self.prefix = "sh:["
        self.suffix = "]"

        self.shared = {}

    def process_to_str(self, template_name: str, levels: int = -1) -> str:
        for filename in os.listdir(f"{self.input_dir}/shared"):
            with open(f"{self.input_dir}/shared/{filename}", "r") as f:
                self.shared[filename.split(".")[0]] = f.read()

        with open(f"{self.input_dir}/templates/{template_name}", "r") as f:
            html = f.read()

            if levels == -1:
                count = 0
                while self.prefix in html and self.suffix in html:
                    if self.warnings and count % 1000 == 999:
                        print("[PREPROCESSOR WARNING] possible circularly dependant components")
                    
                    for k, v in self.shared.items():
                        html = html.replace(self.prefix + k + self.suffix, v)
                    
                    count += 1

            else:
                for _ in range(levels):
                    for k, v in self.shared.items():
                        html = html.replace(self.prefix + k + self.suffix, v)
        
        if self.pretty:
            pretty_html = ""
            prev_tag = ""
            indent_counter = 0

            for i, line in enumerate(html.split("\n")):
                tag = line.strip().removeprefix("<").removeprefix("<").split(">")[0].split(" ")[0] if line.strip().startswith("<") else ""
                
                if line.count(tag) == 2 and line.count("<") >= 2 and line.count(">") >= 2 and line.count("/") >= 1:
                    tag = ""

                if prev_tag in self.indent_tags:
                    indent_counter += 1
                
                elif tag in [f"/{tag}" for tag in self.indent_tags]:
                    indent_counter -= 1

                pretty_html += (self.indent_spaces * " ") * indent_counter + line.strip() + "\n"
                
                prev_tag = tag

            return pretty_html
        
        return html

    
    def process_to_files(self, levels: int = -1):
        for filename in os.listdir(f"{self.input_dir}/shared"):
            with open(f"{self.input_dir}/shared/{filename}", "r") as f:
                self.shared[filename.split(".")[0]] = f.read()

        for filename in os.listdir(f"{self.input_dir}/templates"):
            with open(f"{self.input_dir}/templates/{filename}", "r") as f:
                html = f.read()

                if levels == -1:
                    count = 0
                    while self.prefix in html and self.suffix in html:
                        if self.warnings and count % 1000 == 999:
                            print("[PREPROCESSOR WARNING] possible circularly dependant components")
                        
                        for k, v in self.shared.items():
                            html = html.replace(self.prefix + k + self.suffix, v)
                        
                        count += 1

                else:
                    for _ in range(levels):
                        for k, v in self.shared.items():
                            html = html.replace(self.prefix + k + self.suffix, v)
                
                with open(f"{self.output_dir}/{filename}", "w") as f2:
                    f2.seek(0)
                    f2.truncate(0)

                    if self.pretty:
                        pretty_html = ""
                        prev_tag = ""
                        indent_counter = 0

                        for i, line in enumerate(html.split("\n")):
                            tag = line.strip().removeprefix("<").removeprefix("<").split(">")[0].split(" ")[0] if line.strip().startswith("<") else ""
                            
                            if line.count(tag) == 2 and line.count("<") >= 2 and line.count(">") >= 2 and line.count("/") >= 1:
                                tag = ""

                            if prev_tag in self.indent_tags:
                                indent_counter += 1
                            
                            elif tag in [f"/{tag}" for tag in self.indent_tags]:
                                indent_counter -= 1

                            pretty_html += (self.indent_spaces * " ") * indent_counter + line.strip() + "\n"
                            
                            prev_tag = tag

                    f2.write(pretty_html if self.pretty else html)