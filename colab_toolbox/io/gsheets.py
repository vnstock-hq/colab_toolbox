import gspread
import pandas as pd
from typing import Union
from google.colab import auth
from google.auth import default
from gspread_dataframe import set_with_dataframe
from gspread.exceptions import WorksheetNotFound

class GSheets:
    def __init__(self, url: str):
        self.sheet_id = url.split('/')[5]
        self.gc = self._authenticate()

    def _authenticate(self):
        auth.authenticate_user()
        creds, _ = default()
        gc = gspread.authorize(creds)
        return gc
    
    def read (self, sheet_name: Union[str, None] = None) -> pd.DataFrame:
        # Open the Google Sheets file by key
        workbook = self.gc.open_by_key(self.sheet_id)
        
        # If sheet_name is provided, open that specific sheet, otherwise open the first sheet
        if sheet_name:
            try:
                sheet = workbook.worksheet(sheet_name)
            except WorksheetNotFound:
                raise ValueError(f"Sheet '{sheet_name}' not found in the Google Sheets file.")
        else:
            sheet = workbook.sheet1
        
        # Read the sheet into a pandas DataFrame
        data = sheet.get_all_values()
        df = pd.DataFrame.from_records(data)
        return df

    def write(self, df: pd.DataFrame, sheet_name: Union[str, None] = None):
        # Open the Google Sheets file by key
        workbook = self.gc.open_by_key(self.sheet_id)
        
        # If sheet_name is provided, open that specific sheet, otherwise open the first sheet
        if sheet_name:
            try:
                sheet = workbook.worksheet(sheet_name)
            except WorksheetNotFound:
                # Create a new sheet if the specified sheet_name does not exist
                sheet = workbook.add_worksheet(title=sheet_name, rows=df.shape[0]+10, cols=df.shape[1]+10)
        else:
            sheet = workbook.sheet1
        
        # Clear the existing content of the sheet
        sheet.clear()
        
        # Write the DataFrame to the sheet
        set_with_dataframe(sheet, df)