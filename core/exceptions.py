from json.decoder import JSONDecodeError

class SettingsFileNotFoundError(FileNotFoundError):
	pass

class SettingNotFoundError(KeyError):
	def __init__(self, key, *args: object) -> None:
		self.key = key
		super().__init__(*args)

class ValueEmptyError(ValueError):
	def __init__(self, keys, *args: object) -> None:
		self.keys = keys
		super().__init__(*args)

class FileNotJsonError(Exception):
	pass