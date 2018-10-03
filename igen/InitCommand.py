# coding=utf-8

from Pasteboard import pasteboard_write
from Model import InitModel
from Command import Command

class InitCommand(Command):

	def __init__(self, model_text):
		super(InitCommand, self).__init__()
		self.model_text = model_text

	@classmethod
	def description(cls):
		return "Create init method for struct model"

	@classmethod
	def name(cls):
		return "init"
		
	def create_init(self):
		# try:
		output = InitModel(self.model_text).create_init()
		pasteboard_write(output)
		print("Text has been copied to clipboard.")
		# except:
		# 	print("Invalid model text in clipboard.")




