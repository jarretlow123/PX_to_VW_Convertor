# PX to VW Convertor (Python)

This Python script could converts pixel (px) values in specify CSS files to viewport width (vw) units based on a specified screen width.

## Usage

1. **Install Required Packages**

   Ensure you have Python installed. Additionally, the script uses the `json` and `re` modules, which are part of the Python standard library.

2. **Configure 'config.json'**

   Modify the `config.json` file with the necessary parameters:
   ```json
   {
       "screen_width": 1920,  // Replace with your screen width
       "files": [
           "file1.css",
           "file2.css",
           "file3.css"
           // Add more CSS files to convert
       ]
   }

## To use this

run the code below 
```
python px_to_vw_converter.py
```

## Contributors

- Low Kah Xuan (https://github.com/jarretlow123)
