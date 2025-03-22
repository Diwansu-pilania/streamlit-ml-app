from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Debugging: Print available attributes
        print(dir(self)) 

        # Any code you write here will run before the form opens.

    def prediction_click(self, **event_args):
        """This method is called when the button is clicked"""
        try:
            # Call the server function to get the prediction
            no2 = anvil.server.call('predict_no2',
                                     self.state.text,
                                     self.location.text,
                                     self.type.text,
                                     self.so2.text,  # Convert to float
                                     self.rspm.text,  # Convert to float
                                     self.spm.text,    
                                     self.pm2_5.text, # Convert to float
                                     self.year.text,
                                     self.month.text,
                                     self.day.text
                                    )
            if no2 is not None:
                self.predicted_no2.text = f"Predicted NO2 Level: {no2}"
                self.predicted_no2.visible = True
            else:
                self.predicted_no2.text = "Prediction failed."
                self.predicted_no2.visible = True
        except Exception as e:
            self.predicted_no2.text = f"Error: {str(e)}"
            self.predicted_no2.visible = True
