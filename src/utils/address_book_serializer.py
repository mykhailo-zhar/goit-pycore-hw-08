import pickle
from pathlib import Path

from src.address_book import AddressBook


class AddressBookSerializer:
    def __init__(self, file_path: str):
        """
        Initialize the address book serializer.

        Args:
            file_path (str): The path to the file to serialize the address book to.

        Raises:
            FileNotFoundError: If the file path is not a file or does not exist.
        """
        self.file_path = Path(file_path)
        if self.file_path.is_dir():
            raise FileNotFoundError(f"Path {self.file_path} must not be a directory")

    def serialize(self, address_book: AddressBook) -> None:
        """
        Serialize the address book to the file.

        Args:
            address_book (AddressBook): The address book to serialize.

        Returns:
            str: The serialized address book.
        """
        with open(self.file_path, "wb") as f:
            pickle.dump(address_book, f)

    def deserialize(self) -> AddressBook:
        """
        Deserialize the address book from the file.

        Returns:
            AddressBook: The deserialized address book.
        """
        with open(self.file_path, "rb") as f:
            return pickle.load(f)
