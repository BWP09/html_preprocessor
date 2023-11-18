import os, bs4


class HTMLPreprocessor:
    def __init__(self, pretty: bool = True, input_dir: str = "preprocessor", output_dir: str = "templates") -> None:
        self.input_dir = input_dir
        self.output_dir = output_dir

        self.pretty = pretty

        self.shared = {}
    
    def process_html(self, levels: int = 1):
        for filename in os.listdir(f"{self.input_dir}/shared"):
            with open(f"{self.input_dir}/shared/{filename}", "r") as f:
                self.shared[filename.split(".")[0]] = f.read()
        
        for filename in os.listdir(f"{self.input_dir}/templates"):
            with open(f"{self.input_dir}/templates/{filename}", "r") as f:
                html = f.read()

                for _ in range(levels):
                    for k, v in self.shared.items():
                        html = html.replace("|sh:" + k + "|", v)
                
                with open(f"{self.output_dir}/{filename}", "w") as f2:
                    f2.seek(0)
                    f2.truncate(0)

                    if self.pretty:
                        pretty_html = ""
                        prev_tag = ""
                        indent_counter = 0

                        for i, line in enumerate(html.split("\n")):
                            tag = line.strip().removeprefix("<").removeprefix("<").split(">")[0].split(" ")[0]
                            
                            if prev_tag in ["html", "head", "body", "div", "p"]:
                                indent_counter += 1
                                print(f"{i}:{indent_counter}:{tag}")
                            
                            elif prev_tag in ["/html", "/head", "/body", "/div", "/p"]:
                                indent_counter -= 1
                                print(f"{i}:{indent_counter}:{tag}")

                            pretty_html += (4 * " ") * indent_counter + line.strip() + "\n"
                            
                            prev_tag = tag

                    f2.write(pretty_html if self.pretty else html)