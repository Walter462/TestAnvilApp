from ._anvil_designer import Form1Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    anvil.users.login_with_form()
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.text_box_1.text
    email = self.text_box_2.text
    feedback = self.text_box_3.text
    anvil.server.call('add_feedack', name, email, feedback)
    Notification('Feedback Submitted').show()
    self.clear_user_inputs_after_submit()
  
  def clear_user_inputs_after_submit(self):
    self.text_box_1.text =''
    self.text_box_2.text =''
    self.text_box_3.text =''