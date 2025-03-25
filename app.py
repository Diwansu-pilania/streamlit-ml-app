from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import datetime

class Form1(Form1Template):
  
    def __init__(self, **properties):
        self.init_components(**properties)
        print(dir(self))  # Debugging: Check available attributes

    def prediction_click(self, **event_args):
        """Called when the prediction button is clicked"""
        try:
            # Collect all inputs
            input_fields = {
                "State": self.state.text.strip(),
                "Location": self.location.text.strip(),
                "Agency": self.agency.text.strip(),
                "Type": self.type.text.strip(),
                "SO2": self.so2.text.strip(),
                "RSPM": self.rspm.text.strip(),
                "SPM": self.spm.text.strip(),
                "PM2.5": self.pm2_5.text.strip(),
                "Year": self.year.text.strip(),
                "Month": self.month.text.strip(),
                "Day": self.day.text.strip()
            }

            # Debugging: Print input values
            print("Raw Inputs:", input_fields)

            # Check for missing values
            for field, value in input_fields.items():
                if not value:
                    self.predicted_no2.text = f"Missing value: {field}. Please fill in all fields."
                    self.predicted_no2.visible = True
                    return
            
            # Convert numeric fields safely
            try:
                so2 = float(input_fields["SO2"])
                rspm = float(input_fields["RSPM"])
                spm = float(input_fields["SPM"])
                pm2_5 = float(input_fields["PM2.5"])
                year = int(input_fields["Year"])
                month = int(input_fields["Month"])
                day = int(input_fields["Day"])
            except ValueError as ve:
                self.predicted_no2.text = f"Invalid number format: {ve}"
                self.predicted_no2.visible = True
                return

            # Format date
            date = datetime.date(year, month, day).isoformat()

            # Call server function
            no2 = anvil.server.call('predict_no2',
                                    input_fields["State"],
                                    input_fields["Location"],
                                    input_fields["Agency"],
                                    input_fields["Type"],
                                    so2, rspm, spm, pm2_5, date)

            # Display result
            self.predicted_no2.text = f"Predicted NO2 Level: {no2}" if no2 is not None else "Prediction failed."
            self.predicted_no2.visible = True

        except Exception as e:
            self.predicted_no2.text = f"Error: {str(e)}"
            self.predicted_no2.visible = True
