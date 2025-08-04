
class Fuck:
    def __init__(self, input_path: str, output_path: str):
        self.input_path: str = input_path
        self.output_path: str = output_path
        self.valid_characters: list[str] = ['<', '>', '+', '-', '.', ',', '[', ']']

    def characters_gen(self):
        with open(self.input_path, 'r') as input_file:
            read = input_file.read(1)

            while read:
                yield read
                read = input_file.read(1)

    def sanitize(self) -> None:
        file_gen = self.characters_gen()
        sanitized: list[str] = []

        for character in file_gen:
            if character not in self.valid_characters:
                continue
            else:
                sanitized.append(character)

        with open(self.output_path, 'w') as output_file:
            output_file.write(''.join(sanitized))

def main():
    fobj: Fuck = Fuck(input_path=".\\bf helloworld.txt", output_path=".\\sanitized.txt")

    fobj.sanitize()

if __name__ == "__main__":
    main()