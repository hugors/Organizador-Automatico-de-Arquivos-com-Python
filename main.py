import os
import shutil
from datetime import datetime
from collections import defaultdict
from tkinter import Tk, filedialog
from colorama import Fore, Style, init

init(autoreset=True)

class FileOrganizer:
    def __init__(self, directory):
        self.directory = directory
        self.extensions_map = defaultdict(list)
        self.create_default_extensions_map()
        self.history = []

    def create_default_extensions_map(self):
        self.extensions_map.update({
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
            'Videos': ['.mp4', '.mkv', '.mov', '.avi', '.wmv', '.flv'],
            'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx'],
            'Music': ['.mp3', '.wav', '.aac', '.flac'],
            'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
            'Code': ['.py', '.java', '.cpp', '.js', '.html', '.css'],
            'Others': []
        })

    def organize_by_extension(self):
        current_batch = []
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            if os.path.isfile(file_path):
                extension = os.path.splitext(filename)[1].lower()
                folder_name = self.get_folder_for_extension(extension)
                if folder_name:
                    new_path = self.move_file(file_path, folder_name)
                    current_batch.append((new_path, file_path))
        if current_batch:
            self.history.append(current_batch)

    def organize_by_date(self):
        current_batch = []
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            if os.path.isfile(file_path):
                created_at = datetime.fromtimestamp(os.path.getctime(file_path))
                folder_name = created_at.strftime('%Y-%m-%d')
                new_path = self.move_file(file_path, folder_name)
                current_batch.append((new_path, file_path))
        if current_batch:
            self.history.append(current_batch)

    def get_folder_for_extension(self, extension):
        for folder, extensions in self.extensions_map.items():
            if extension in extensions:
                return folder
        return 'Others'

    def move_file(self, file_path, folder_name):
        folder_path = os.path.join(self.directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        new_path = shutil.move(file_path, folder_path)
        print(Fore.GREEN + f"Moved {os.path.basename(file_path)} to {folder_path}")
        return new_path

    def undo_last_action(self):
        if not self.history:
            print(Fore.RED + "No actions to undo.")
            return
        last_batch = self.history.pop()
        folders_to_remove = set()
        for new_path, original_path in reversed(last_batch):
            shutil.move(new_path, original_path)
            print(Fore.YELLOW + f"Moved {os.path.basename(new_path)} back to {os.path.dirname(original_path)}")
            folders_to_remove.add(os.path.dirname(new_path))
        for folder in folders_to_remove:
            if os.path.exists(folder) and not os.listdir(folder):
                os.rmdir(folder)
                print(Fore.RED + f"Removed empty folder: {folder}")

    def interactive_menu(self):
        while True:
            print(Fore.CYAN + "\nFile Organizer - Choose an option:")
            print(Fore.CYAN + "1. Organização por Tipo de Arquivo")
            print(Fore.CYAN + "2. Organização por Data")
            print(Fore.CYAN + "3. Desfazer Última Ação")
            print(Fore.CYAN + "4. Sair")

            choice = input(Fore.YELLOW + "Enter your choice (1-4): ")

            if choice == '1':
                self.organize_by_extension()
            elif choice == '2':
                self.organize_by_date()
            elif choice == '3':
                self.undo_last_action()
            elif choice == '4':
                break
            else:
                print(Fore.RED + "Invalid choice, please try again.")

if __name__ == "__main__":
    root = Tk()
    root.withdraw()  # Hide the main Tkinter window
    directory = filedialog.askdirectory(title="Select Directory to Organize")
    if directory:
        organizer = FileOrganizer(directory)
        organizer.interactive_menu()
    else:
        print(Fore.RED + "No directory selected. Please try again.")