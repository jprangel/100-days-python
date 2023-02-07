
MODEL_LETTER_FILE ="Input/Letters/starting_letter.txt"
NAMES_FILE = "Input/Names/invited_names.txt"
OUTPUT_PATH = "Output/ReadyToSend/"
PLACEHOLDER = "[name]"

# Trick to get the current path
def get_root_path():
    root_path = __file__
    root_path = root_path.strip('main.py')
    return root_path
    
root_path = get_root_path()

with open(f"{root_path}{NAMES_FILE}", mode="r") as names_list:
    for name in names_list:
        name = name.strip()
        with open(f"{root_path}{MODEL_LETTER_FILE}", mode="r") as model_letter:
            letter = model_letter.read()
            msg = letter.replace(PLACEHOLDER, name)
            FILENAME = "invite_letter_" + name + ".txt"
            with open(f"{root_path}{OUTPUT_PATH}{FILENAME}", mode='w') as invite_letter:
                invite_letter.write(msg)
