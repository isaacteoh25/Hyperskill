PREFIX = "- "
TEXT_PROMPT = f"{PREFIX}Text: "
LABEL_PROMPT = f"{PREFIX}Label: "
LEVEL_PROMPT = f"{PREFIX}Level: "
URL_PROMPT = f"{PREFIX}URL: "
ROW_PROMPT = f"{PREFIX}Number of rows: "


class MarkDown:
    NEW_LINE = '\n'

    def __init__(self):
        self.all_commands = {'plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list',
                             'new-line', '!help'}
        self.result_text = ""

    def header(self, level_, text_):
        self.result_text += f"{'#' * level_} {text_}{self.NEW_LINE}"

    def link(self, label_, url_):
        self.result_text += f"[{label_}]({url_})"

    def plain(self, text_):
        self.result_text += f"{text_}"

    def bold(self, text_):
        self.result_text += f"**{text_}**"

    def italic(self, text_):
        self.result_text += f"*{text_}*"

    def inline_code(self, text_):
        self.result_text += f"`{text_}`"

    def new_line(self):
        self.result_text += f"{self.NEW_LINE}"

    def output(self):
        print(self.result_text)


    def ordered(self, row_):
        for i in range(1, row_ + 1):
            # rowo.append(input(f"- Row #{i}:"))
            a = input(f"- Row #{i}:")
            self.result_text += f"{i}. {a}\n"
    def unordered(self, row_):
        for i in range(1, row_ + 1):
            # rowo.append(input(f"- Row #{i}:"))
            a = input(f"- Row #{i}:")
            self.result_text += f"* {a}\n"

    def save(self):
        name_file = open('output.md', 'w', encoding='utf-8')
        name_file.writelines(self.result_text)
        name_file.close()


markdown = MarkDown()
rowo = []
while (user_input := input("- Choose a formatter: ")) != '!done':
    if user_input not in markdown.all_commands:
        print("Unknown formatting type or command. Please try again")
        continue
    elif user_input == '!help':
        print("Available MarkDown: plain bold italic header link inline-code ordered-list unordered-list new-line\nSpecial "
              "commands: !help !done")
        continue
    else:
        if user_input == 'header':
            while (level := input(LEVEL_PROMPT)) not in '123456':
                print("The level should be within the range of 1 to 6")
            markdown.header(int(level), input(TEXT_PROMPT))
        elif user_input == 'plain':
            markdown.plain(input(TEXT_PROMPT))
        elif user_input == 'bold':
            markdown.bold(input(TEXT_PROMPT))
        elif user_input == 'italic':
            markdown.italic(input(TEXT_PROMPT))
        elif user_input == 'inline-code':
            markdown.inline_code(input(TEXT_PROMPT))
        elif user_input == 'link':
            markdown.link(input(LABEL_PROMPT), input(URL_PROMPT))
        elif user_input == 'new-line':
            markdown.new_line()
        elif user_input == "ordered-list":
            while (level := int(input(ROW_PROMPT))) <= 0:
                print("The number of rows should be greater than zero")
            markdown.ordered(level)
        elif user_input == "unordered-list":
            while (level := int(input(ROW_PROMPT))) <= 0:
                print("The number of rows should be greater than zero")
            markdown.unordered(level)
    markdown.output()
markdown.save()
